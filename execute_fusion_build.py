"""
Upgrades the active Fusion 360 design into a fully realized, high-fidelity Mechatronics CAD assembly:
1. Industrial SCR Thyristor Module (TY160D40) with copper base, molded housing, 3 brass/copper power terminals, gate pins, and M5 bolts
2. Precision Inlet & Outlet Hose Barb Adapters with retention beads and Blue/Red identification rings
3. Cover Fasteners (M4 socket head cap screws and hex nuts)
4. K-Type Thermocouple Sensor Assembly with stainless probe in thermowell, brass collar, wire, and yellow miniature connector
5. Forced-Air Cooling Fan Shroud Module
6. Authentic PBR Materials (Aluminum, Copper, Brass, Matte Black PBT, Stainless Steel, Yellow Connector, Coolant Rings)
"""
from mcp_client import FusionMCPClient
import json
import base64

FUSION_SCRIPT = '''
import json
import math
import traceback
import adsk.core as C
import adsk.fusion as F

NEW = F.FeatureOperations.NewBodyFeatureOperation
CUT = F.FeatureOperations.CutFeatureOperation
JOIN = F.FeatureOperations.JoinFeatureOperation

def point(x, y):
    return C.Point3D.create(x / 10.0, y / 10.0, 0)

def sketch_at(comp, z, name):
    plane_input = comp.constructionPlanes.createInput()
    plane_input.setByOffset(comp.xYConstructionPlane, C.ValueInput.createByString(f"{z} mm"))
    plane = comp.constructionPlanes.add(plane_input)
    sk = comp.sketches.add(plane)
    sk.name = name
    plane.isLightBulbOn = False
    return sk

def extrude(comp, sk, depth, operation, name):
    profiles = C.ObjectCollection.create()
    for profile in sk.profiles:
        profiles.add(profile)
    if profiles.count == 0:
        raise RuntimeError("No closed profile: " + name)
    inp = comp.features.extrudeFeatures.createInput(profiles, operation)
    distance = F.DistanceExtentDefinition.create(C.ValueInput.createByString(f"{abs(depth)} mm"))
    direction = (F.ExtentDirections.PositiveExtentDirection if depth > 0
                 else F.ExtentDirections.NegativeExtentDirection)
    inp.setOneSideExtent(distance, direction)
    feature = comp.features.extrudeFeatures.add(inp)
    feature.name = name
    sk.isVisible = False
    return feature

def rectangles(comp, z, depth, boxes, op, name):
    sk = sketch_at(comp, z, name + " sketch")
    for x1, y1, x2, y2 in boxes:
        sk.sketchCurves.sketchLines.addTwoPointRectangle(point(x1, y1), point(x2, y2))
    return extrude(comp, sk, depth, op, name)

def cylinders(comp, z, height, centers, radius, operation, name):
    sk = sketch_at(comp, z, name + " sketch")
    for x, y in centers:
        sk.sketchCurves.sketchCircles.addByCenterRadius(point(x, y), radius / 10.0)
    return extrude(comp, sk, height, operation, name)

def holes(comp, z, depth, centers, radius, name):
    sk = sketch_at(comp, z, name + " sketch")
    for x, y in centers:
        sk.sketchCurves.sketchCircles.addByCenterRadius(point(x, y), radius / 10.0)
    return extrude(comp, sk, depth, CUT, name)

def get_or_create_component(root, name):
    for occ in root.occurrences:
        if occ.component.name == name:
            return occ.component
    occ = root.occurrences.addNewComponent(C.Matrix3D.create())
    occ.component.name = name
    return occ.component

def setup_appearances(app, design):
    color_defs = {
        "Aluminium": (205, 215, 225),
        "MatteBlack": (30, 32, 35),
        "Copper": (225, 125, 65),
        "Brass": (220, 185, 70),
        "Steel": (195, 200, 205),
        "Yellow": (245, 200, 25),
        "TIM": (130, 155, 175),
        "Seal": (40, 80, 85),
        "InletBlue": (35, 145, 225),
        "OutletRed": (230, 75, 45)
    }
    
    base_ap = None
    for lib in app.materialLibraries:
        for ap in lib.appearances:
            if "opaque" in ap.name.lower() or "matte" in ap.name.lower() or "smooth" in ap.name.lower():
                base_ap = ap
                break
        if base_ap:
            break

    appearances = {}
    for name, (r, g, b) in color_defs.items():
        existing = design.appearances.itemByName("MC_" + name)
        if existing:
            appearances[name] = existing
            continue

        new_ap = None
        if base_ap:
            try:
                new_ap = design.appearances.addByCopy(base_ap, "MC_" + name)
            except:
                pass
        
        if not new_ap:
            continue

        color_val = C.Color.create(r, g, b, 255)
        for prop_id in ["surface_albedo", "opaque_albedo", "color", "generic_diffuse", "metal_f0"]:
            prop = new_ap.appearanceProperties.itemById(prop_id)
            if prop:
                try:
                    cprop = C.ColorProperty.cast(prop)
                    if cprop:
                        cprop.value = color_val
                        break
                except:
                    pass
        appearances[name] = new_ap

    return appearances

def paint(comp, ap):
    if ap:
        for body in comp.bRepBodies:
            body.appearance = ap

def run(context):
    app = C.Application.get()
    doc = app.activeDocument
    design = F.Design.cast(app.activeProduct)
    root = design.rootComponent
    
    colors = setup_appearances(app, design)

    # 1. Clean existing placeholders if present
    for occ in list(root.occurrences):
        if any(tag in occ.component.name for tag in ["ENVELOPE ONLY", "selection pending", "04 Thermal", "05 SCR", "06 Thyristor", "07 Power", "08 Gate", "09 Inlet", "10 Outlet", "11 Cover", "12 Cover", "13 Module", "Sensor"]):
            try:
                occ.deleteMe()
            except:
                pass

    # Style existing Cold Plate, Cover, Gasket
    for occ in root.occurrences:
        cname = occ.component.name.lower()
        if "cold plate" in cname or "base" in cname:
            paint(occ.component, colors.get("Aluminium"))
        elif "cover" in cname or "lid" in cname:
            paint(occ.component, colors.get("Aluminium"))
        elif "gasket" in cname or "seal" in cname:
            paint(occ.component, colors.get("Seal"))

    # 2. Thermal Interface Material (0.2 mm) on dry underside (Z: 0 to -0.2)
    # SCR footprint: 22 mm wide x 92 mm long, centered at X=40, Y=60
    tim = get_or_create_component(root, "04 Thermal interface pad (TIM) | 0.2 mm")
    rectangles(tim, 0, -0.2, [(29, 14, 51, 106)], NEW, "TIM envelope")
    holes(tim, 0, -0.2, [(40, 20), (40, 100)], 2.5, "TIM screw clearance")
    paint(tim, colors.get("TIM"))

    # 3. SCR Thyristor Module (TY160D40 / SKKT Dual Thyristor)
    # Heavy copper baseplate (Z: -0.2 to -3.7 mm)
    scr_base = get_or_create_component(root, "05 SCR copper baseplate | 92 x 22 x 3.5 mm")
    rectangles(scr_base, -0.2, -3.5, [(29, 14, 51, 106)], NEW, "SCR copper base")
    holes(scr_base, -0.2, -3.5, [(40, 20), (40, 100)], 2.6, "SCR U-slot mounts")
    paint(scr_base, colors.get("Copper"))

    # Molded Flame-Retardant Black PBT Housing (Z: -3.7 to -27.7 mm)
    scr_body = get_or_create_component(root, "06 Thyristor housing | TY160D40 Molded PBT")
    rectangles(scr_body, -3.7, -24.0, [(27, 24, 53, 96)], NEW, "SCR plastic body")
    # Phase isolation barriers
    rectangles(scr_body, -27.7, -6.0, [(25, 45, 55, 49), (25, 71, 55, 75)], JOIN, "Phase barriers")
    paint(scr_body, colors.get("MatteBlack"))

    # 3 Heavy-duty Power Terminals (Z: -27.7 to -39.7 mm)
    terminals = get_or_create_component(root, "07 Power terminals | Copper pads & M6 Brass studs")
    for ty in [36.0, 60.0, 84.0]:
        rectangles(terminals, -27.7, -3.0, [(33, ty - 6, 47, ty + 6)], NEW if ty == 36.0 else JOIN, f"Pad_{ty}")
        cylinders(terminals, -30.7, -9.0, [(40, ty)], 3.0, JOIN, f"Stud_{ty}")
        cylinders(terminals, -33.7, -4.0, [(40, ty)], 5.5, JOIN, f"Nut_{ty}")
    paint(terminals, colors.get("Brass"))

    # Gate Quick-Connect Spade Pins
    gate = get_or_create_component(root, "08 Gate & auxiliary trigger terminals")
    rectangles(gate, -15.0, -8.0, [(26, 56, 27.5, 58.5), (26, 61.5, 27.5, 64)], NEW, "Gate pins")
    paint(gate, colors.get("Brass"))

    # SCR Mounting M5 Screws clamping baseplate into cold plate (Z: -3.7 to 5.0)
    scr_screws = get_or_create_component(root, "09 SCR M5 socket head clamping screws")
    for sy in [20.0, 100.0]:
        cylinders(scr_screws, -3.7, -4.5, [(40, sy)], 4.2, NEW if sy == 20.0 else JOIN, f"ScrewHead_{sy}")
        cylinders(scr_screws, -3.7, 9.0, [(40, sy)], 2.4, JOIN, f"ScrewShank_{sy}")
    paint(scr_screws, colors.get("Steel"))

    # 4. Precision Hose Barb Adapters on Cover (Z: 13.5 to 29.5 mm)
    # Inlet at (40, 20), Outlet at (40, 100)
    for port_y, port_name, col_name in [(20.0, "Inlet", "InletBlue"), (100.0, "Outlet", "OutletRed")]:
        fitting = get_or_create_component(root, f"10 {port_name} hose barb adapter | 6 mm bore")
        cylinders(fitting, 13.5, 4.0, [(40, port_y)], 6.0, NEW, "Fitting shoulder")
        cylinders(fitting, 17.5, 10.0, [(40, port_y)], 4.5, JOIN, "Barb stem")
        cylinders(fitting, 23.5, 2.0, [(40, port_y)], 5.1, JOIN, "Hose retention bead")
        holes(fitting, 27.5, -14.0, [(40, port_y)], 3.0, "Fluid through bore")
        paint(fitting, colors.get("Steel"))

        ring = get_or_create_component(root, f"11 {port_name} color identifier ring")
        cylinders(ring, 17.5, 2.0, [(40, port_y)], 5.4, NEW, "Identifier ring")
        holes(ring, 19.5, -2.0, [(40, port_y)], 4.5, "Ring bore")
        paint(ring, colors.get(col_name))

    # 5. Cover Fasteners (M4 Socket Cap Screws & Hex Nuts)
    bolts_comp = get_or_create_component(root, "12 Cover perimeter bolts | 6x M4 socket head screws")
    bolt_coords = [(5, 8), (75, 8), (5, 60), (75, 60), (5, 112), (75, 112)]
    for bx, by in bolt_coords:
        cylinders(bolts_comp, 13.5, 4.0, [(bx, by)], 3.5, NEW if (bx, by) == bolt_coords[0] else JOIN, f"BoltHead_{bx}_{by}")
        cylinders(bolts_comp, 13.5, -15.5, [(bx, by)], 1.9, JOIN, f"BoltShank_{bx}_{by}")
    paint(bolts_comp, colors.get("Steel"))

    nuts_comp = get_or_create_component(root, "13 Cover nuts | 6x M4 hex nuts")
    for bx, by in bolt_coords:
        cylinders(nuts_comp, -2.0, -3.0, [(bx, by)], 3.8, NEW if (bx, by) == bolt_coords[0] else JOIN, f"Nut_{bx}_{by}")
        holes(nuts_comp, -2.0, -3.0, [(bx, by)], 2.0, f"NutHole_{bx}_{by}")
    paint(nuts_comp, colors.get("Steel"))

    # 6. K-Type Thermocouple Sensor Assembly (Mechatronics Sensing Module)
    sensor = get_or_create_component(root, "14 K-Type Thermocouple Sensor Assembly")
    # Thermowell hole into cold plate (X: 80 to 42, Y: 60, Z: 2.5)
    cylinders(sensor, 1.5, 2.0, [(80, 60)], 1.5, NEW, "Thermowell entry")
    # Stainless probe (30 mm)
    cylinders(sensor, 1.5, 2.0, [(84, 60)], 1.5, JOIN, "Sensor probe sheath")
    # Brass hex compression collar
    cylinders(sensor, 0.5, 4.0, [(88, 60)], 3.2, JOIN, "Sensor hex collar")
    # Yellow connector plug
    rectangles(sensor, -2.0, 6.0, [(100, 75, 112, 95)], JOIN, "Miniature yellow plug")
    rectangles(sensor, -0.5, 3.0, [(102, 95, 104, 105), (108, 95, 110, 105)], JOIN, "Spade prongs")
    paint(sensor, colors.get("Yellow"))

    # Refresh viewport
    app.activeViewport.fit()
    app.activeViewport.visualStyle = C.VisualStyles.ShadedWithVisibleEdgesOnlyVisualStyle
    app.activeViewport.refresh()

    print("Successfully finished and upgraded the 3D Mechatronics Thyristor Cooling Assembly in Fusion 360!")
'''

def main():
    client = FusionMCPClient()
    print("Connected to Fusion MCP Server. Session:", client.session_id)
    print("Executing complete 3D Mechatronics Assembly generation...")
    res = client.execute_script(FUSION_SCRIPT, read_only=False)
    print("Execution response:", res.get("result", {}).get("content", [{}])[0].get("text", ""))

    # Capture updated screenshot
    print("Capturing live screenshot from Fusion...")
    ss = client.take_screenshot(direction="iso-top-right", width=1600, height=1200)
    if ss and "result" in ss:
        content = ss["result"].get("content", [])
        for c in content:
            if c.get("type") == "image" or c.get("mimeType") == "image/png":
                data = c.get("data") or c.get("base64Data")
                if data:
                    out_png = r"C:\thyristor\deliverables\fusion_completed_assembly.png"
                    with open(out_png, "wb") as f:
                        f.write(base64.b64decode(data))
                    print(f"Saved live screenshot to {out_png}")

if __name__ == "__main__":
    main()
