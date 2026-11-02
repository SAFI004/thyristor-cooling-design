"""
Master Fusion 360 Script for Liquid Mini-Channel Thyristor Cooling System (Upright Top-Port Layout)
"""
import os
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
        raise RuntimeError("No closed profile found for: " + name)
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

def get_appearance(design, app, lib_name, item_name):
    try:
        ap = design.appearances.itemByName(item_name)
        if ap: return ap
    except:
        pass
    try:
        lib = app.materialLibraries.itemByName(lib_name)
        if lib:
            match = lib.appearances.itemByName(item_name)
            if match:
                try:
                    return design.appearances.addByCopy(match, item_name)
                except:
                    return match
    except:
        pass
    return None

def paint(comp, ap):
    if ap:
        for body in comp.bRepBodies:
            body.appearance = ap

def run(context):
    app = C.Application.get()
    doc = app.activeDocument
    design = F.Design.cast(app.activeProduct)
    design.designType = F.DesignTypes.ParametricDesignType
    design.unitsManager.distanceDisplayUnits = F.DistanceUnits.MillimeterDistanceUnits
    root = design.rootComponent

    # 1. Clear existing components
    for occ in list(root.occurrences):
        try:
            occ.deleteMe()
        except:
            pass

    # 2. Authentic PBR appearances
    LIB = "Fusion Appearance Library"
    mat_al = get_appearance(design, app, LIB, "Aluminum - Satin")
    mat_al_blue = get_appearance(design, app, LIB, "Aluminum - Anodized Glossy (Blue)")
    mat_al_red = get_appearance(design, app, LIB, "Aluminum - Anodized Glossy (Red)")
    mat_copper = get_appearance(design, app, LIB, "Copper - Polished")
    mat_brass = get_appearance(design, app, LIB, "Brass - Polished")
    mat_black = get_appearance(design, app, LIB, "Plastic - Glossy (Black)")
    mat_yellow = get_appearance(design, app, LIB, "Paint - Enamel Glossy (Yellow)")
    mat_steel = get_appearance(design, app, LIB, "Steel - Polished") or get_appearance(design, app, LIB, "Stainless Steel")
    mat_rubber = get_appearance(design, app, LIB, "Rubber - Soft")

    def make_comp(name):
        occ = root.occurrences.addNewComponent(C.Matrix3D.create())
        occ.component.name = name
        return occ.component

    bolt_coords = [(5, 8), (75, 8), (5, 40), (75, 40), (5, 80), (75, 80), (5, 112), (75, 112)]

    # 01. ALUMINUM MINI-CHANNEL COLD PLATE (120 x 80 x 12 mm)
    cp = make_comp("01 Cold plate | 6061-T6 Aluminium | 120 x 80 x 12 mm")
    rectangles(cp, 0, 12, [(0, 0, 80, 120)], NEW, "Cold plate stock")

    channels = [(12.75 + i * 3.5, 25, 14.75 + i * 3.5, 95) for i in range(16)]
    rectangles(cp, 0, 5, channels, CUT, "16 Mini-Channels | 2 x 5 x 70 mm")
    rectangles(cp, 0, 5, [(10, 10, 70, 25), (10, 95, 70, 110)], CUT, "Headers")

    breaks = []
    for i in range(15):
        rx = 14.75 + i * 3.5
        for ry in ((42, 68) if i % 2 == 0 else (52, 78)):
            breaks.append((rx - 0.05, ry, rx + 1.55, ry + 2.5))
    rectangles(cp, 0, 5, breaks, CUT, "Boundary-layer breaks")

    for j, box in enumerate([(7, 7, 73, 9), (7, 111, 73, 113), (7, 9, 9, 111), (71, 9, 73, 111)]):
        rectangles(cp, 0, 0.5, [box], CUT, f"Gasket groove {j+1}")

    holes(cp, 12, -7, [(40, 17), (40, 103)], 3.0, "Fluid port through-bores")
    holes(cp, 12, -12, bolt_coords, 2.2, "Cover bolt holes")
    holes(cp, 12, -8, [(40, 32), (40, 88)], 2.1, "SCR M5 tapped holes")
    cylinders(cp, 6.0, 3.0, [(78, 60)], 2.5, JOIN, "Thermowell entry boss")
    paint(cp, mat_al)

    # 02. RECESSED FLAT GASKET (0.5 mm Silicone)
    gasket = make_comp("02 Perimeter sealing gasket | 0.5 mm silicone")
    rectangles(gasket, 0, -0.5, [(7, 7, 73, 113)], NEW, "Gasket blank")
    rectangles(gasket, 0, -0.5, [(9, 9, 71, 111)], CUT, "Gasket fluid aperture")
    paint(gasket, mat_rubber)

    # 03. BOTTOM ENCLOSURE COVER (120 x 80 x 6 mm Aluminium)
    cover = make_comp("03 Bottom manifold cover | 6061-T6 Aluminium")
    rectangles(cover, -0.5, -6.0, [(0, 0, 80, 120)], NEW, "Bottom cover slab")
    holes(cover, -0.5, -6.0, bolt_coords, 2.2, "Cover bolt holes")
    paint(cover, mat_al)

    # 04. HOSE BARB FITTINGS & ANODIZED RINGS
    for py, pname, pmat, rmat in [
        (17.0, "Inlet", mat_steel, mat_al_blue),
        (103.0, "Outlet", mat_steel, mat_al_red)
    ]:
        fitting = make_comp(f"04 {pname} hose barb fitting | 6 mm bore")
        cylinders(fitting, 12.0, 4.0, [(40, py)], 6.0, NEW, "Hex collar")
        cylinders(fitting, 16.0, 12.0, [(40, py)], 4.5, JOIN, "Barb stem")
        cylinders(fitting, 22.0, 2.5, [(40, py)], 5.2, JOIN, "Retention barb bead")
        holes(fitting, 28.0, -16.0, [(40, py)], 3.0, "Continuous fluid bore")
        paint(fitting, pmat)

        ring = make_comp(f"05 {pname} anodized identification ring")
        cylinders(ring, 16.0, 2.5, [(40, py)], 5.4, NEW, "Identifier ring")
        holes(ring, 16.0, 2.5, [(40, py)], 4.5, "Ring bore")
        paint(ring, rmat)

    # 06. THERMAL INTERFACE MATERIAL
    tim = make_comp("06 Thermal interface pad (TIM) | 0.2 mm")
    rectangles(tim, 12.0, 0.2, [(29, 26, 51, 94)], NEW, "TIM envelope")
    holes(tim, 12.0, 0.2, [(40, 32), (40, 88)], 2.5, "TIM bolt clearance")
    paint(tim, mat_al_blue)

    # 07. INDUSTRIAL THYRISTOR SCR MODULE
    z_scr = 12.2
    scr_base = make_comp("07 SCR copper baseplate | 92 x 22 x 3.5 mm")
    rectangles(scr_base, z_scr, 3.5, [(29, 26, 51, 94)], NEW, "Copper baseplate")
    holes(scr_base, z_scr, 3.5, [(40, 32), (40, 88)], 2.6, "U-bolt mounting slots")
    paint(scr_base, mat_copper)

    scr_body = make_comp("08 Thyristor housing | TY160D40 Molded PBT")
    rectangles(scr_body, 15.7, 24.0, [(27, 34, 53, 86)], NEW, "SCR plastic body")
    rectangles(scr_body, 39.7, 5.0, [(25, 48, 55, 52), (25, 68, 55, 72)], JOIN, "Phase isolation barriers")
    paint(scr_body, mat_black)

    terminals = make_comp("09 Power terminals | Copper pads & M6 Brass studs")
    z_term = 39.7
    for ty in [42.0, 60.0, 78.0]:
        rectangles(terminals, z_term, 3.0, [(33, ty - 5.0, 47, ty + 5.0)], NEW if ty == 42.0 else JOIN, f"Pad_{ty}")
        cylinders(terminals, z_term + 3.0, 8.0, [(40, ty)], 3.0, JOIN, f"Stud_{ty}")
        cylinders(terminals, z_term + 5.5, 4.0, [(40, ty)], 5.5, JOIN, f"Nut_{ty}")
    paint(terminals, mat_brass)

    gate = make_comp("10 Gate & auxiliary trigger terminals")
    rectangles(gate, 26.0, 6.0, [(26, 56, 27.5, 58.5), (26, 61.5, 27.5, 64)], NEW, "Gate pins")
    paint(gate, mat_brass)

    scr_screws = make_comp("11 SCR M5 socket head cap screws")
    for sy in [32.0, 88.0]:
        cylinders(scr_screws, 15.7, 4.5, [(40, sy)], 4.2, NEW if sy == 32.0 else JOIN, f"Head_{sy}")
        cylinders(scr_screws, 15.7, -9.0, [(40, sy)], 2.4, JOIN, f"Shank_{sy}")
    paint(scr_screws, mat_steel)

    # 12. COVER CLAMPING FASTENERS
    cover_bolts = make_comp("12 Cover perimeter bolts | 8x M4 socket cap screws")
    for bx, by in bolt_coords:
        cylinders(cover_bolts, 12.0, 4.0, [(bx, by)], 3.5, NEW if (bx, by) == bolt_coords[0] else JOIN, f"BHead_{bx}_{by}")
        cylinders(cover_bolts, 12.0, -18.5, [(bx, by)], 1.9, JOIN, f"BShank_{bx}_{by}")
    paint(cover_bolts, mat_steel)

    cover_nuts = make_comp("13 Cover nuts | 8x M4 hex nuts")
    for bx, by in bolt_coords:
        cylinders(cover_nuts, -6.5, -3.0, [(bx, by)], 3.8, NEW if (bx, by) == bolt_coords[0] else JOIN, f"Nut_{bx}_{by}")
        holes(cover_nuts, -6.5, -3.0, [(bx, by)], 2.0, f"NutBore_{bx}_{by}")
    paint(cover_nuts, mat_steel)

    # 14. K-TYPE THERMOCOUPLE SENSOR
    sensor = make_comp("14 K-Type Thermocouple Sensor Assembly")
    cylinders(sensor, 6.5, 2.0, [(80, 60)], 1.5, NEW, "Sensor probe in thermowell")
    cylinders(sensor, 6.5, 2.0, [(84, 60)], 1.5, JOIN, "Probe sheath")
    cylinders(sensor, 5.5, 4.0, [(88, 60)], 3.2, JOIN, "Brass compression gland")
    rectangles(sensor, 3.0, 6.0, [(102, 70, 114, 90)], JOIN, "Yellow connector plug")
    rectangles(sensor, 4.5, 3.0, [(104, 90, 106, 98), (110, 90, 112, 98)], JOIN, "Spade prongs")
    paint(sensor, mat_yellow)

    # 15. LAB BENCH ELEVATION STANDOFFS
    legs = make_comp("15 Lab test bench elevation standoffs & feet")
    for sx, sy in [(6, 6), (74, 6), (6, 114), (74, 114)]:
        cylinders(legs, -6.5, -16.0, [(sx, sy)], 4.0, NEW if (sx, sy) == (6, 6) else JOIN, f"Leg_{sx}_{sy}")
        cylinders(legs, -22.5, -3.0, [(sx, sy)], 6.0, JOIN, f"Foot_{sx}_{sy}")
    paint(legs, mat_al)

    # 16. CAMERA & EXPORT
    vp = app.activeViewport
    camera = vp.camera
    camera.cameraType = C.CameraTypes.PerspectiveCameraType
    camera.target = C.Point3D.create(4.0, 6.0, 1.2)
    camera.eye = C.Point3D.create(22.0, -16.0, 22.0)
    camera.upVector = C.Vector3D.create(0, 0, 1)
    camera.isFitView = True
    camera.isSmoothTransition = False
    vp.camera = camera
    vp.visualStyle = C.VisualStyles.ShadedWithVisibleEdgesOnlyVisualStyle
    vp.refresh()
    adsk.doEvents()

    out_dir = r"C:\thyristor\deliverables"
    manager = design.exportManager
    try:
        manager.execute(manager.createFusionArchiveExportOptions(f"{out_dir}\\Thyristor_Liquid_ColdPlate_Assembly.f3d"))
        manager.execute(manager.createSTEPExportOptions(f"{out_dir}\\Thyristor_Liquid_ColdPlate_Assembly.step"))
    except:
        pass
    print("SUCCESS")
