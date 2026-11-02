"""Build the 360-degree viewer from the reviewed Fusion mesh export.
Run export_reviewed_viewer_mesh.py first when the CAD assembly changes.
"""
import json
import os
from pathlib import Path

OUTPUT_DIR = str(Path(__file__).resolve().parent / "deliverables")
source = json.loads((Path(OUTPUT_DIR) / "reviewed_viewer_mesh.json").read_text())
components_data = {}
for index, comp in enumerate(source["components"]):
    number = int(comp["name"][:2])
    color = {2: "#b54132", 5: "#2980b9" if "Inlet" in comp["name"] else "#e74c3c",
             6: "#5dade2", 7: "#d9743c", 8: "#26282c", 9: "#d6b245", 10: "#d6b245"}.get(number, "#cad4dc")
    dz = -18 if number == 2 else -38 if number in (3, 13) else -58 if number == 15 else 38 if number in (7, 8, 9, 10, 11) else 14 if number == 6 else 24 if number in (4, 5, 12) else 0
    comp.update(colors=color, metalness=0.1 if number in (2, 6, 8) else 0.7,
                roughness=0.7 if number in (2, 6, 8) else 0.32,
                explode_vector=[30 if number == 14 else 0, 0, dz])
    components_data[f"part_{index}"] = comp

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liquid Mini-Channel Cold Plate for Thyristor Cooling</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: #0d121d;
            color: #e2e8f0;
            overflow: hidden;
            width: 100vw;
            height: 100vh;
        }}
        #canvas-container {{
            width: 100%;
            height: 100%;
            position: absolute;
            top: 0;
            left: 0;
        }}
        .header-panel {{
            position: absolute;
            top: 20px;
            left: 20px;
            background: rgba(15, 23, 42, 0.88);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 16px 20px;
            border-radius: 12px;
            max-width: 440px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            z-index: 10;
        }}
        .header-panel h1 {{
            font-size: 15px;
            font-weight: 700;
            color: #38bdf8;
            letter-spacing: -0.01em;
            margin-bottom: 4px;
            text-transform: uppercase;
        }}
        .header-panel p {{
            font-size: 12px;
            color: #94a3b8;
            line-height: 1.4;
        }}
        .badge {{
            display: inline-block;
            background: rgba(56, 189, 248, 0.15);
            color: #38bdf8;
            border: 1px solid rgba(56, 189, 248, 0.3);
            font-size: 10px;
            font-weight: 600;
            padding: 2px 8px;
            border-radius: 9999px;
            margin-top: 6px;
        }}
        .controls-panel {{
            position: absolute;
            bottom: 24px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(15, 23, 42, 0.9);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 14px 24px;
            border-radius: 16px;
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
            justify-content: center;
            width: max-content;
            max-width: calc(100vw - 32px);
            box-shadow: 0 12px 35px rgba(0,0,0,0.6);
            z-index: 10;
        }}
        .control-group {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .control-label {{
            font-size: 12px;
            font-weight: 600;
            color: #cbd5e1;
            white-space: nowrap;
        }}
        input[type="range"] {{
            -webkit-appearance: none;
            width: 150px;
            height: 6px;
            background: #334155;
            border-radius: 3px;
            outline: none;
        }}
        input[type="range"]::-webkit-slider-thumb {{
            -webkit-appearance: none;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: #38bdf8;
            cursor: pointer;
            box-shadow: 0 0 8px rgba(56, 189, 248, 0.6);
        }}
        .btn {{
            background: #1e293b;
            color: #f1f5f9;
            border: 1px solid rgba(255,255,255,0.1);
            padding: 7px 14px;
            font-size: 12px;
            font-weight: 500;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .btn:hover {{
            background: #334155;
            border-color: #38bdf8;
            color: #38bdf8;
        }}
        .btn.active {{
            background: rgba(56, 189, 248, 0.2);
            border-color: #38bdf8;
            color: #38bdf8;
        }}
        .parts-panel {{
            position: absolute;
            top: 20px;
            right: 20px;
            background: rgba(15, 23, 42, 0.88);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 16px;
            border-radius: 12px;
            width: 320px;
            max-height: calc(100vh - 170px);
            overflow-y: auto;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            z-index: 10;
        }}
        .parts-title {{
            font-size: 13px;
            font-weight: 700;
            color: #f8fafc;
            margin-bottom: 12px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            padding-bottom: 6px;
            display: flex;
            justify-content: space-between;
        }}
        .part-item {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 11px;
            color: #94a3b8;
            padding: 4px 0;
        }}
        .part-indicator {{
            width: 10px;
            height: 10px;
            border-radius: 3px;
            display: inline-block;
            margin-right: 6px;
        }}
        .nav-hint {{
            position: absolute;
            bottom: 4px;
            right: 20px;
            font-size: 11px;
            color: #64748b;
            background: rgba(15, 23, 42, 0.7);
            padding: 6px 12px;
            border-radius: 8px;
        }}
        @media (max-width: 900px) {{
            .header-panel {{ left: 10px; top: 10px; max-width: calc(100vw - 20px); padding: 10px; }}
            .parts-panel {{ top: 150px; right: 10px; width: 230px; max-height: 28vh; }}
            .controls-panel {{ bottom: 30px; padding: 10px; }}
        }}
    </style>
</head>
<body>
    <div id="canvas-container"></div>

    <div class="header-panel">
        <h1>Liquid Mini-Channel Cold Plate System</h1>
        <p>Reviewed cold plate: 120 × 80 × 12 mm, with 2 × 5 × 70 mm interrupted channels. Corrected fittings, recessed gasket, aligned cover and blind mounting bores. Generic SCR envelope; external cooling loop not shown.</p>
        <span class="badge">Reviewed CAD geometry · 40 solid bodies</span>
        <span class="badge" style="border-color:#10b981; color:#34d399; background:rgba(16,185,129,0.15)">Academic concept · performance unverified</span>
    </div>

    <div class="parts-panel">
        <div class="parts-title">
            <span>Assembly Components</span>
            <span style="color:#38bdf8">17 Components</span>
        </div>
        <div id="part-list"></div>
    </div>

    <div class="controls-panel">
        <div class="control-group">
            <span class="control-label">Exploded View</span>
            <input type="range" id="explode-slider" min="0" max="100" value="0">
            <span id="explode-val" style="font-size:12px; color:#38bdf8; min-width:32px;">0%</span>
        </div>
        <button class="btn" id="btn-channels">Internal Channels</button>
        <button class="btn" id="btn-wireframe">Wireframe</button>
        <button class="btn" id="btn-reset">Reset View</button>
        <button class="btn" id="btn-autorotate">Auto-Rotate</button>
    </div>

    <div class="nav-hint">
        Left-click: Rotate | Right-click: Pan | Scroll: Zoom
    </div>

    <script>
        const compData = {json.dumps(components_data)};

        const container = document.getElementById('canvas-container');
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x0a0f16);

        const gridHelper = new THREE.GridHelper(260, 26, 0x1e293b, 0x0f172a);
        gridHelper.rotation.x = Math.PI / 2;
        gridHelper.position.set(40, 60, -85);
        scene.add(gridHelper);

        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 2000);
        camera.up.set(0, 0, 1);
        camera.position.set(210, -170, 185);

        const renderer = new THREE.WebGLRenderer({{ antialias: true }});
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(window.devicePixelRatio);
        renderer.shadowMap.enabled = true;
        renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        container.appendChild(renderer.domElement);

        const controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controls.target.set(40, 60, 10);
        controls.update();
        controls.saveState();

        const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
        scene.add(ambientLight);

        const dirLight1 = new THREE.DirectionalLight(0xffffff, 1.2);
        dirLight1.position.set(150, 200, 150);
        dirLight1.castShadow = true;
        scene.add(dirLight1);

        const dirLight2 = new THREE.DirectionalLight(0x38bdf8, 0.4);
        dirLight2.position.set(-150, -50, -100);
        scene.add(dirLight2);

        const meshObjects = [];
        const partListEl = document.getElementById('part-list');

        for (const [key, data] of Object.entries(compData)) {{
            const geometry = new THREE.BufferGeometry();
            const positions = new Float32Array(data.vertices);
            const indices = new Uint32Array(data.indices);

            geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
            geometry.setIndex(new THREE.BufferAttribute(indices, 1));
            geometry.setAttribute('normal', new THREE.BufferAttribute(new Float32Array(data.normals), 3));

            const material = new THREE.MeshStandardMaterial({{
                color: new THREE.Color(data.colors),
                metalness: data.metalness,
                roughness: data.roughness,
                side: THREE.DoubleSide
            }});

            const mesh = new THREE.Mesh(geometry, material);
            mesh.castShadow = true;
            mesh.receiveShadow = true;

            mesh.userData = {{
                compName: key,
                coldPlate: data.name.startsWith('01 '),
                originalPosition: new THREE.Vector3(0, 0, 0),
                explodeVector: new THREE.Vector3(...data.explode_vector)
            }};

            scene.add(mesh);
            meshObjects.push(mesh);

            const item = document.createElement('div');
            item.className = 'part-item';
            const cleanName = data.name;
            item.innerHTML = `
                <div>
                    <span class="part-indicator" style="background:${{data.colors}}"></span>
                    <span>${{cleanName}}</span>
                </div>
                <input type="checkbox" checked id="chk_${{key}}">
            `;
            partListEl.appendChild(item);

            document.getElementById(`chk_${{key}}`).addEventListener('change', (e) => {{
                mesh.visible = e.target.checked;
            }});
        }}

        const slider = document.getElementById('explode-slider');
        const explodeVal = document.getElementById('explode-val');
        slider.addEventListener('input', (e) => {{
            const factor = parseFloat(e.target.value) / 100.0;
            explodeVal.innerText = `${{e.target.value}}%`;
            meshObjects.forEach(m => {{
                const target = m.userData.explodeVector.clone().multiplyScalar(factor);
                m.position.copy(target);
            }});
        }});

        let channelMode = false;
        const channelButton = document.getElementById('btn-channels');
        let previousVisibility = [];
        channelButton.addEventListener('click', () => {{
            channelMode = !channelMode;
            channelButton.classList.toggle('active', channelMode);
            if (channelMode) previousVisibility = meshObjects.map(m => m.visible);
            meshObjects.forEach((m, i) => {{
                m.visible = channelMode ? m.userData.coldPlate : previousVisibility[i];
                const checkbox = document.getElementById(`chk_${{m.userData.compName}}`);
                checkbox.checked = m.visible;
                checkbox.disabled = channelMode;
            }});
            if (channelMode) {{
                camera.position.set(160, -120, -175);
                controls.target.set(40, 60, 4);
            }} else {{ controls.reset(); }}
            controls.update();
        }});

        let wireframeMode = false;
        document.getElementById('btn-wireframe').addEventListener('click', function() {{
            wireframeMode = !wireframeMode;
            this.classList.toggle('active', wireframeMode);
            meshObjects.forEach(m => m.material.wireframe = wireframeMode);
        }});

        document.getElementById('btn-reset').addEventListener('click', () => {{
            if (channelMode) channelButton.click();
            controls.reset();
            slider.value = 0;
            slider.dispatchEvent(new Event('input'));
            meshObjects.forEach(m => {{
                m.visible = true;
                m.material.wireframe = false;
                document.getElementById(`chk_${{m.userData.compName}}`).checked = true;
            }});
            wireframeMode = false;
            document.getElementById('btn-wireframe').classList.remove('active');
            autoRotate = false;
            controls.autoRotate = false;
            document.getElementById('btn-autorotate').classList.remove('active');
        }});

        let autoRotate = false;
        document.getElementById('btn-autorotate').addEventListener('click', function() {{
            autoRotate = !autoRotate;
            this.classList.toggle('active', autoRotate);
            controls.autoRotate = autoRotate;
            controls.autoRotateSpeed = 2.0;
        }});

        window.addEventListener('resize', () => {{
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        }});

        function animate() {{
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
        }}
        animate();
    </script>
</body>
</html>
"""

viewer_path = os.path.join(OUTPUT_DIR, "interactive_3d_viewer.html")
with open(viewer_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Updated interactive viewer: {viewer_path}")
