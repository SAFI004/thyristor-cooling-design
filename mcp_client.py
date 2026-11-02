"""
Direct MCP Client for Autodesk Fusion 360 on port 27182
"""
import socket
import json

MCP_HOST = '127.0.0.1'
MCP_PORT = 27182

class FusionMCPClient:
    def __init__(self):
        self.session_id = None
        self.req_id = 0
        self.initialize()

    def _raw_post(self, payload, is_notification=False):
        s = socket.socket()
        s.connect((MCP_HOST, MCP_PORT))
        body = json.dumps(payload)
        headers = [
            'POST /mcp HTTP/1.1',
            f'Host: {MCP_HOST}:{MCP_PORT}',
            'Content-Type: application/json',
            f'Content-Length: {len(body)}',
            'Connection: close'
        ]
        if self.session_id:
            headers.append(f'MCP-Session-Id: {self.session_id}')
        req = '\r\n'.join(headers) + '\r\n\r\n' + body
        s.sendall(req.encode('utf-8'))
        s.settimeout(60.0) # CAD operations might take a few seconds
        resp = b''
        while True:
            try:
                chunk = s.recv(8192)
                if not chunk:
                    break
                resp += chunk
            except:
                break
        s.close()
        parts = resp.split(b'\r\n\r\n', 1)
        for line in parts[0].decode('utf-8', errors='replace').split('\r\n'):
            if line.lower().startswith('mcp-session-id:'):
                self.session_id = line.split(':', 1)[1].strip()
        if len(parts) > 1 and parts[1].strip():
            try:
                return json.loads(parts[1].decode('utf-8', errors='replace'))
            except Exception as e:
                return {'raw': parts[1].decode('utf-8', errors='replace')}
        return None

    def request(self, method, params=None):
        self.req_id += 1
        payload = {
            'jsonrpc': '2.0',
            'id': self.req_id,
            'method': method,
            'params': params or {}
        }
        return self._raw_post(payload)

    def notify(self, method, params=None):
        payload = {
            'jsonrpc': '2.0',
            'method': method,
            'params': params or {}
        }
        return self._raw_post(payload, is_notification=True)

    def initialize(self):
        res = self.request('initialize', {
            'protocolVersion': '2024-11-05',
            'capabilities': {'tools': {}},
            'clientInfo': {'name': 'antigravity-fusion-bridge', 'version': '1.0'}
        })
        self.notify('notifications/initialized')
        return res

    def call_tool(self, tool_name, arguments):
        return self.request('tools/call', {
            'name': tool_name,
            'arguments': arguments
        })

    def execute_script(self, script_str, read_only=False):
        return self.call_tool('fusion_mcp_execute', {
            'featureType': 'script',
            'object': {
                'script': script_str,
                'readOnly': read_only
            }
        })

    def take_screenshot(self, direction="iso-top-right", width=1200, height=900):
        return self.call_tool('fusion_mcp_read', {
            'queryType': 'screenshot',
            'direction': direction,
            'width': width,
            'height': height,
            'transparentBackground': False,
            'antiAliasing': True
        })

if __name__ == '__main__':
    client = FusionMCPClient()
    print("Connected to Fusion MCP Server! Session:", client.session_id)
