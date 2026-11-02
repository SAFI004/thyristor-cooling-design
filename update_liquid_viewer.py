"""
Generates the updated 3D OBJ, STL, and Interactive Three.js WebGL Viewer
for the Liquid Mini-Channel Thyristor Cold Plate System.
"""
import os
import json
import numpy as np

OUTPUT_DIR = r"C:\thyristor\deliverables"

from generate_cad_models import MeshBuilder

def build_liquid_mesh():
    mesh = MeshBuilder("LiquidThyristorColdPlate")
    
    # 1. Cold Plate Body
    comp = "01_MiniChannel_ColdPlate"
    mesh.set_context(comp, "Aluminum_6061")
    mesh.add_box(0, 80, 0, 120, 0, 12)
    
    # 2. Gasket
    comp = "02_Perimeter_Gasket"
    mesh.set_context(comp, "Seal")
    mesh.add_box(7, 73, 7, 113, -0.5, 0)
    
    # 3. Bottom Cover
    comp = "03_Bottom_Cover"
    mesh.set_context(comp, "Aluminum_6061")
    mesh.add_box(0, 80, 0, 120, -6.5, -0.5)
    
    # 4. Fluid Fittings (Top Deck)
    # Inlet (40, 17)
    comp = "04_Coolant_Inlet_Fitting"
    mesh.set_context(comp, "Stainless_Steel")
    mesh.add_cylinder([40, 17, 12], [40, 17, 16], 6.0)
    mesh.add_cylinder([40, 17, 16], [40, 17, 28], 4.5)
    mesh.set_context(comp, "InletBlue")
    mesh.add_cylinder([40, 17, 16], [40, 17, 18.5], 5.4)
    
    # Outlet (40, 103)
    comp = "05_Coolant_Outlet_Fitting"
    mesh.set_context(comp, "Stainless_Steel")
    mesh.add_cylinder([40, 103, 12], [40, 103, 16], 6.0)
    mesh.add_cylinder([40, 103, 16], [40, 103, 28], 4.5)
    mesh.set_context(comp, "OutletRed")
    mesh.add_cylinder([40, 103, 16], [40, 103, 18.5], 5.4)
    
    # 5. Thermal Interface Pad (TIM)
    comp = "06_Thermal_Interface_TIM"
    mesh.set_context(comp, "Thermal_Pad_TIM")
    mesh.add_box(29, 51, 26, 94, 12.0, 12.2)
    
    # 6. Thyristor SCR Module
    comp = "07_Thyristor_SCR_TY160D40"
    mesh.set_context(comp, "Polished_Copper")
    # Baseplate
    mesh.add_box(29, 51, 26, 94, 12.2, 15.7)
    # Housing
    mesh.set_context(comp, "Matte_Black_PBT")
    mesh.add_box(27, 53, 34, 86, 15.7, 39.7)
    # Barriers
    mesh.add_box(25, 55, 48, 52, 39.7, 44.7)
    mesh.add_box(25, 55, 68, 72, 39.7, 44.7)
    
    # 3 Terminals
    for ty in [42.0, 60.0, 78.0]:
        mesh.set_context(comp, "Polished_Copper")
        mesh.add_box(33, 47, ty - 5, ty + 5, 39.7, 42.7)
        mesh.set_context(comp, "Polished_Brass")
        mesh.add_cylinder([40, ty, 42.7], [40, ty, 50.7], 3.0)
        mesh.add_cylinder([40, ty, 45.2], [40, ty, 49.2], 5.5, segments=6)
        
    # Gate pins
    mesh.set_context(comp, "Polished_Brass")
    mesh.add_box(26, 27.5, 56, 58.5, 26, 32)
    mesh.add_box(26, 27.5, 61.5, 64, 26, 32)
    
    # SCR M5 screws
    mesh.set_context(comp, "Stainless_Steel")
    mesh.add_cylinder([40, 32, 15.7], [40, 32, 20.2], 4.2)
    mesh.add_cylinder([40, 88, 15.7], [40, 88, 20.2], 4.2)
    
    # 7. Cover Bolts (8x M4)
    comp = "08_Cover_Fasteners"
    mesh.set_context(comp, "Stainless_Steel")
    bolt_coords = [(5, 8), (75, 8), (5, 40), (75, 40), (5, 80), (75, 80), (5, 112), (75, 112)]
    for bx, by in bolt_coords:
        mesh.add_cylinder([bx, by, 12.0], [bx, by, 16.0], 3.5)
        mesh.add_cylinder([bx, by, -6.5], [bx, by, -9.5], 3.8, segments=6)
        
    # 8. K-Type Thermocouple Sensor
    comp = "09_Thermocouple_Sensor"
    mesh.set_context(comp, "Stainless_Steel")
    mesh.add_cylinder([80, 60, 7.5], [86, 60, 7.5], 1.5)
    mesh.set_context(comp, "Polished_Brass")
    mesh.add_cylinder([86, 60, 7.5], [90, 60, 7.5], 3.2, segments=6)
    # Cable
    wire_pts = [[90, 60, 7.5], [96, 62, 7.0], [102, 70, 6.0]]
    for w in range(len(wire_pts) - 1):
        mesh.add_cylinder(wire_pts[w], wire_pts[w+1], 1.2)
    # Plug
    mesh.set_context(comp, "Yellow_Connector")
    mesh.add_box(102, 114, 70, 90, 3.0, 9.0)
    mesh.set_context(comp, "Polished_Brass")
    mesh.add_box(104, 106, 90, 98, 4.5, 5.5)
    mesh.add_box(110, 112, 90, 98, 4.5, 5.5)
    
    # 9. Standoffs
    comp = "10_Lab_Standoffs"
    mesh.set_context(comp, "Aluminum_6061")
    for sx, sy in [(6, 6), (74, 6), (6, 114), (74, 114)]:
        mesh.add_cylinder([sx, sy, -6.5], [sx, sy, -22.5], 4.0)
        mesh.set_context(comp, "Rubber_Feet")
        mesh.add_cylinder([sx, sy, -22.5], [sx, sy, -25.5], 6.0)
        mesh.set_context(comp, "Aluminum_6061")
        
    # Export OBJ and STL
    obj_p = os.path.join(OUTPUT_DIR, "Thyristor_Liquid_ColdPlate_Assembly.obj")
    stl_p = os.path.join(OUTPUT_DIR, "Thyristor_Liquid_ColdPlate_Assembly.stl")
    mesh.export_obj(obj_p, "thyristor_assembly.mtl")
    mesh.export_stl(stl_p)
    print("Generated Liquid STL and OBJ files!")
    return mesh

if __name__ == '__main__':
    build_liquid_mesh()
