"""Read the reviewed Fusion assembly and export its tessellation for the viewer."""
import json
from mcp_client import FusionMCPClient

SCRIPT = r'''
import adsk.core as C, adsk.fusion as F, json
def run(context):
 app=C.Application.get(); d=F.Design.cast(app.activeProduct)
 expected=json.load(open(r'C:\thyristor\deliverables\Reviewed_Verification.json'))
 occurrences=list(d.rootComponent.occurrences)
 actual=[{'name':o.component.name,'bodies':o.component.bRepBodies.count} for o in occurrences]
 assert actual==expected['components'], 'Open the reviewed assembled model before exporting'
 result={'source':'Reviewed Fusion assembly','units':'mm','components':[]}
 for o in occurrences:
  comp={'name':o.component.name,'vertices':[],'normals':[],'indices':[],'bodies':o.component.bRepBodies.count}
  for body in o.component.bRepBodies:
   calc=body.meshManager.createMeshCalculator()
   calc.surfaceTolerance=0.005
   mesh=calc.calculate()
   offset=len(comp['vertices'])//3
   for p in mesh.nodeCoordinates:
    p.transformBy(o.transform2)
    comp['vertices'].extend([round(p.x*10,5),round(p.y*10,5),round(p.z*10,5)])
   for n in mesh.normalVectors:
    n.transformBy(o.transform2)
    comp['normals'].extend([round(n.x,6),round(n.y,6),round(n.z,6)])
   comp['indices'].extend([i+offset for i in mesh.nodeIndices])
  result['components'].append(comp)
 path=r'C:\thyristor\deliverables\reviewed_viewer_mesh.json'
 with open(path,'w') as f: json.dump(result,f,separators=(',',':'))
 print(json.dumps({'path':path,'components':len(actual),'bodies':sum(c['bodies'] for c in actual)}))
'''

if __name__ == '__main__':
    print(json.dumps(FusionMCPClient().execute_script(SCRIPT, read_only=True)))
