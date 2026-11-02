"""
Complete 3D Mechatronics Package Generator:
1. Assembly OBJ + MTL (Full Materials & Colors)
2. Assembly Binary STL (Universal 3D Printing & CAD)
3. Individual Component STLs:
   - 01_MiniChannel_HeatSink.stl
   - 02_Thyristor_SCR_TY160D40.stl
   - 03_SUNON_Cooling_Fan.stl
   - 04_Airflow_Duct_Shroud.stl
   - 05_Thermocouple_K_Type.stl
   - 06_Lab_Bench_Baseplate.stl
4. Standalone Three.js Interactive 3D Viewer (HTML/WebGL) with Exploded View & Inspections
"""
import os
import struct
import json
import numpy as np

OUTPUT_DIR = r"C:\thyristor\deliverables"
os.makedirs(OUTPUT_DIR, exist_ok=True)

class MeshBuilder:
    def __init__(self, name="Assembly"):
        self.name = name
        self.vertices = []
        self.faces = [] # list of (v_indices, material_name, component_name)
        self.current_material = "default"
        self.current_component = name

    def set_context(self, comp_name, mat_name):
        self.current_component = comp_name
        self.current_material = mat_name

    def add_vertex(self, x, y, z):
        self.vertices.append([float(x), float(y), float(z)])
        return len(self.vertices) - 1

    def add_triangle(self, v0, v1, v2):
        self.faces.append(([v0, v1, v2], self.current_material, self.current_component))

    def add_quad(self, v0, v1, v2, v3):
        self.faces.append(([v0, v1, v2], self.current_material, self.current_component))
        self.faces.append(([v0, v2, v3], self.current_material, self.current_component))

    def add_box(self, x_min, x_max, y_min, y_max, z_min, z_max):
        v000 = self.add_vertex(x_min, y_min, z_min)
        v100 = self.add_vertex(x_max, y_min, z_min)
        v110 = self.add_vertex(x_max, y_max, z_min)
        v010 = self.add_vertex(x_min, y_max, z_min)
        v001 = self.add_vertex(x_min, y_min, z_max)
        v101 = self.add_vertex(x_max, y_min, z_max)
        v111 = self.add_vertex(x_max, y_max, z_max)
        v011 = self.add_vertex(x_min, y_max, z_max)

        self.add_quad(v000, v100, v110, v010)
        self.add_quad(v001, v011, v111, v101)
        self.add_quad(v000, v010, v011, v001)
        self.add_quad(v100, v101, v111, v110)
        self.add_quad(v000, v001, v101, v100)
        self.add_quad(v010, v110, v111, v011)

    def add_cylinder(self, p1, p2, radius, segments=20):
        p1 = np.array(p1, dtype=float)
        p2 = np.array(p2, dtype=float)
        v = p2 - p1
        length = np.linalg.norm(v)
        if length < 1e-6:
            return
        axis = v / length
        if abs(axis[0]) < 0.8:
            perp1 = np.cross(axis, [1, 0, 0])
        else:
            perp1 = np.cross(axis, [0, 1, 0])
        perp1 /= np.linalg.norm(perp1)
        perp2 = np.cross(axis, perp1)
        perp2 /= np.linalg.norm(perp2)

        ring1 = []
        ring2 = []
        for i in range(segments):
            angle = 2.0 * np.pi * i / segments
            offset = radius * (np.cos(angle) * perp1 + np.sin(angle) * perp2)
            ring1.append(self.add_vertex(*(p1 + offset)))
            ring2.append(self.add_vertex(*(p2 + offset)))

        center1 = self.add_vertex(*p1)
        center2 = self.add_vertex(*p2)

        for i in range(segments):
            i_next = (i + 1) % segments
            self.add_quad(ring1[i], ring1[i_next], ring2[i_next], ring2[i])
            self.add_triangle(center1, ring1[i_next], ring1[i])
            self.add_triangle(center2, ring2[i], ring2[i_next])

    def export_stl(self, filepath, filter_comp=None):
        filtered_faces = [f for f in self.faces if (filter_comp is None or f[2] == filter_comp)]
        if not filtered_faces:
            return
        faces_count = len(filtered_faces)
        header = f"Mechatronics CAD: {filter_comp or self.name}".encode('ascii')[:80].ljust(80, b'\0')
        with open(filepath, 'wb') as f:
            f.write(header)
            f.write(struct.pack('<I', faces_count))
            verts = np.array(self.vertices)
            for (idx, _, _) in filtered_faces:
                v0, v1, v2 = verts[idx[0]], verts[idx[1]], verts[idx[2]]
                normal = np.cross(v1 - v0, v2 - v0)
                norm = np.linalg.norm(normal)
                if norm > 1e-9:
                    normal /= norm
                else:
                    normal = np.array([0.0, 0.0, 1.0])
                f.write(struct.pack('<3f', *normal))
                f.write(struct.pack('<3f', *v0))
                f.write(struct.pack('<3f', *v1))
                f.write(struct.pack('<3f', *v2))
                f.write(struct.pack('<H', 0))

    def export_obj(self, filepath, mtl_filename="thyristor_assembly.mtl"):
        with open(filepath, 'w') as f:
            f.write(f"# Wavefront OBJ Export - Thyristor Mechatronics Cooling\n")
            f.write(f"mtllib {mtl_filename}\n")
            for v in self.vertices:
                f.write(f"v {v[0]:.4f} {v[1]:.4f} {v[2]:.4f}\n")

            current_mat = None
            for idx, mat, comp in self.faces:
                if mat != current_mat:
                    current_mat = mat
                    f.write(f"usemtl {mat}\n")
                    f.write(f"g {comp}_{mat}\n")
                f.write(f"f {idx[0]+1} {idx[1]+1} {idx[2]+1}\n")


def generate_all():
    mesh = MeshBuilder("ThyristorMechatronicsAssembly")

    materials = {
        "Aluminum_6061": {"Kd": "0.78 0.82 0.85", "Ks": "0.9 0.9 0.9", "Ns": "80", "color": "#cad4dc", "metalness": 0.9, "roughness": 0.25},
        "Matte_Black_PBT": {"Kd": "0.08 0.08 0.09", "Ks": "0.2 0.2 0.2", "Ns": "25", "color": "#1e2022", "metalness": 0.1, "roughness": 0.75},
        "Fan_Gloss_Black": {"Kd": "0.12 0.12 0.13", "Ks": "0.6 0.6 0.6", "Ns": "60", "color": "#282a2d", "metalness": 0.2, "roughness": 0.35},
        "Polished_Copper": {"Kd": "0.85 0.45 0.22", "Ks": "0.95 0.7 0.4", "Ns": "100", "color": "#d9743c", "metalness": 0.95, "roughness": 0.2},
        "Polished_Brass": {"Kd": "0.82 0.68 0.25", "Ks": "0.9 0.8 0.4", "Ns": "90", "color": "#d6b245", "metalness": 0.9, "roughness": 0.25},
        "Stainless_Steel": {"Kd": "0.75 0.76 0.78", "Ks": "0.85 0.85 0.85", "Ns": "95", "color": "#c0c4c8", "metalness": 0.85, "roughness": 0.25},
        "Yellow_Connector": {"Kd": "0.95 0.82 0.12", "Ks": "0.3 0.3 0.3", "Ns": "30", "color": "#f1c40f", "metalness": 0.1, "roughness": 0.4},
        "Thermal_Pad_TIM": {"Kd": "0.45 0.55 0.65", "Ks": "0.1 0.1 0.1", "Ns": "10", "color": "#6c8299", "metalness": 0.05, "roughness": 0.9},
        "Clear_Air_Shroud": {"Kd": "0.3 0.5 0.7", "Ks": "0.8 0.8 0.8", "Ns": "120", "color": "#5dade2", "metalness": 0.1, "roughness": 0.1, "opacity": 0.6},
        "Bench_Mount_Base": {"Kd": "0.25 0.27 0.30", "Ks": "0.5 0.5 0.5", "Ns": "40", "color": "#34495e", "metalness": 0.7, "roughness": 0.4},
        "Rubber_Feet": {"Kd": "0.04 0.04 0.04", "Ks": "0.05 0.05 0.05", "Ns": "10", "color": "#111111", "metalness": 0.0, "roughness": 0.9}
    }

    # Write MTL
    mtl_path = os.path.join(OUTPUT_DIR, "thyristor_assembly.mtl")
    with open(mtl_path, 'w') as f:
        for name, p in materials.items():
            f.write(f"newmtl {name}\n")
            f.write(f"  Kd {p['Kd']}\n  Ks {p['Ks']}\n  Ns {p['Ns']}\n  d {p.get('opacity', 1.0)}\n  illum 2\n\n")

    # 1. Mini-Channel Heat Sink
    comp = "01_MiniChannel_HeatSink"
    mesh.set_context(comp, "Aluminum_6061")
    L_hs, W_hs, H_hs = 100.0, 80.0, 36.0
    t_base = 6.0
    W_deck = 42.0

    # Solid base plate
    mesh.add_box(0, W_hs, 0, L_hs, 0, t_base)
    # Upper mounting deck
    mesh.add_box((W_hs - W_deck)/2, (W_hs + W_deck)/2, 0, L_hs, 28, H_hs)

    # 9 Internal mini-channel fins with staggered turbulence-promoting breaks
    num_ribs = 9
    rib_th = 1.6
    channel_w = 2.4
    x_start = 21.0
    for r in range(num_ribs):
        rx1 = x_start + r * (rib_th + channel_w)
        rx2 = rx1 + rib_th
        if r % 2 == 0:
            mesh.add_box(rx1, rx2, 0, 28, t_base, 28)
            mesh.add_box(rx1, rx2, 34, L_hs, t_base, 28)
        else:
            mesh.add_box(rx1, rx2, 0, 64, t_base, 28)
            mesh.add_box(rx1, rx2, 70, L_hs, t_base, 28)

    # 12 Longitudinal External Cooling Fins (6 left, 6 right)
    fin_th = 1.4
    fin_pitch = 2.6
    for f in range(6):
        lx1 = 2.0 + f * (fin_th + fin_pitch)
        mesh.add_box(lx1, lx1 + fin_th, 0, L_hs, t_base, H_hs - 2.0)
        rx1 = 62.0 + f * (fin_th + fin_pitch)
        mesh.add_box(rx1, rx1 + fin_th, 0, L_hs, t_base, H_hs - 2.0)

    # Corner fan mount bosses
    boss_coords = [(6, 6), (74, 6), (6, 30), (74, 30)]
    for bx, bz in boss_coords:
        mesh.add_cylinder([bx, 0, bz], [bx, 4, bz], 4.5, segments=16)
        mesh.add_cylinder([bx, L_hs - 4, bz], [bx, L_hs, bz], 4.5, segments=16)

    # Thermowell port on side
    mesh.add_cylinder([W_hs - 1, 50, 18], [W_hs + 3, 50, 18], 4.0, segments=16)

    # 2. Thermal Interface TIM
    comp = "02_Thermal_Interface_TIM"
    mesh.set_context(comp, "Thermal_Pad_TIM")
    mesh.add_box(29, 51, 4, 96, H_hs, H_hs + 0.3)

    # 3. Thyristor SCR Module
    comp = "03_Thyristor_SCR_TY160D40"
    mesh.set_context(comp, "Polished_Copper")
    z_scr_base = H_hs + 0.3
    t_scr_base = 3.5
    # Copper baseplate
    mesh.add_box(29, 51, 4, 96, z_scr_base, z_scr_base + t_scr_base)

    # Black molded housing
    mesh.set_context(comp, "Matte_Black_PBT")
    z_body_start = z_scr_base + t_scr_base
    h_body = 26.0
    mesh.add_box(27, 53, 14, 86, z_body_start, z_body_start + h_body)
    mesh.add_box(25, 55, 38, 42, z_body_start + h_body, z_body_start + h_body + 6.0)
    mesh.add_box(25, 55, 58, 62, z_body_start + h_body, z_body_start + h_body + 6.0)

    # 3 Power Terminals
    z_term_top = z_body_start + h_body
    for ty in [26.0, 50.0, 74.0]:
        mesh.set_context(comp, "Polished_Copper")
        mesh.add_box(32, 48, ty - 6, ty + 6, z_term_top, z_term_top + 3)
        mesh.set_context(comp, "Polished_Brass")
        mesh.add_cylinder([40, ty, z_term_top + 3], [40, ty, z_term_top + 12], 3.2, segments=16)
        mesh.add_cylinder([40, ty, z_term_top + 6], [40, ty, z_term_top + 10], 5.8, segments=6)
        mesh.set_context(comp, "Stainless_Steel")
        mesh.add_cylinder([40, ty, z_term_top + 3], [40, ty, z_term_top + 5], 6.5, segments=16)

    # Gate terminals
    mesh.set_context(comp, "Polished_Brass")
    mesh.add_box(26, 27.5, 46, 48.5, z_body_start + 12, z_body_start + 20)
    mesh.add_box(26, 27.5, 51.5, 54, z_body_start + 12, z_body_start + 20)

    # SCR Mounting M5 Screws
    mesh.set_context(comp, "Stainless_Steel")
    for sy in [8.5, 91.5]:
        mesh.add_cylinder([40, sy, z_scr_base + t_scr_base], [40, sy, z_scr_base + t_scr_base + 6], 4.5, segments=16)
        mesh.set_context(comp, "Matte_Black_PBT")
        mesh.add_cylinder([40, sy, z_scr_base + t_scr_base + 3], [40, sy, z_scr_base + t_scr_base + 6.1], 2.2, segments=6)
        mesh.set_context(comp, "Stainless_Steel")

    # 4. Airflow Duct Shroud
    comp = "04_Airflow_Duct_Shroud"
    mesh.set_context(comp, "Clear_Air_Shroud")
    y_shroud_front = -12.0
    y_shroud_back = 0.0

    v_b1 = mesh.add_vertex(0, y_shroud_back, 36)
    v_b2 = mesh.add_vertex(80, y_shroud_back, 36)
    v_f2 = mesh.add_vertex(80, y_shroud_front, 58)
    v_f1 = mesh.add_vertex(0, y_shroud_front, 58)
    mesh.add_quad(v_b1, v_b2, v_f2, v_f1)

    v_bb1 = mesh.add_vertex(0, y_shroud_back, 0)
    v_bb2 = mesh.add_vertex(80, y_shroud_back, 0)
    v_bf2 = mesh.add_vertex(80, y_shroud_front, -22)
    v_bf1 = mesh.add_vertex(0, y_shroud_front, -22)
    mesh.add_quad(v_bb1, v_bf1, v_bf2, v_bb2)

    mesh.add_box(0, 3, y_shroud_front, y_shroud_back, -22, 58)
    mesh.add_box(77, 80, y_shroud_front, y_shroud_back, -22, 58)

    # 5. SUNON Cooling Fan
    comp = "05_SUNON_Cooling_Fan"
    mesh.set_context(comp, "Matte_Black_PBT")
    y_fan_front = -37.0
    y_fan_back = -12.0
    w_fan_rim = 5.0
    mesh.add_box(0, 80, y_fan_front, y_fan_back, 58 - w_fan_rim, 58)
    mesh.add_box(0, 80, y_fan_front, y_fan_back, -22, -22 + w_fan_rim)
    mesh.add_box(0, w_fan_rim, y_fan_front, y_fan_back, -22, 58)
    mesh.add_box(80 - w_fan_rim, 80, y_fan_front, y_fan_back, -22, 58)

    fan_corners = [(6, -16), (74, -16), (6, 52), (74, 52)]
    for cx, cz in fan_corners:
        mesh.add_cylinder([cx, y_fan_front, cz], [cx, y_fan_back, cz], 5.0, segments=16)

    # Fan motor hub
    mesh.set_context(comp, "Fan_Gloss_Black")
    mesh.add_cylinder([40, y_fan_front, 18], [40, y_fan_back + 4, 18], 18.0, segments=24)

    # 7 Blades
    num_blades = 7
    r_hub = 18.0
    r_tip = 37.0
    for b in range(num_blades):
        angle = 2.0 * np.pi * b / num_blades
        dx, dz = np.cos(angle), np.sin(angle)
        vr1 = mesh.add_vertex(40 + r_hub * dx, y_fan_front + 4, 18 + r_hub * dz)
        vr2 = mesh.add_vertex(40 + r_hub * dx, y_fan_back - 4, 18 + r_hub * dz)
        vt2 = mesh.add_vertex(40 + r_tip * dx, y_fan_back - 2, 18 + r_tip * dz)
        vt1 = mesh.add_vertex(40 + r_tip * dx, y_fan_front + 8, 18 + r_tip * dz)
        mesh.add_quad(vr1, vr2, vt2, vt1)

    mesh.set_context(comp, "Stainless_Steel")
    for cx, cz in fan_corners:
        mesh.add_cylinder([cx, y_fan_front - 3, cz], [cx, y_fan_front, cz], 4.2, segments=16)
        mesh.add_cylinder([cx, y_fan_front, cz], [cx, 6.0, cz], 2.0, segments=12)

    # 6. Thermocouple Sensor
    comp = "06_Thermocouple_Sensor"
    mesh.set_context(comp, "Stainless_Steel")
    mesh.add_cylinder([42, 50, 18], [88, 50, 18], 1.5, segments=12)
    mesh.set_context(comp, "Polished_Brass")
    mesh.add_cylinder([86, 50, 18], [92, 50, 18], 3.2, segments=6)
    mesh.set_context(comp, "Stainless_Steel")
    wire_points = [[92, 50, 18], [102, 52, 16], [110, 60, 12], [115, 75, 8], [116, 92, 6]]
    for w in range(len(wire_points) - 1):
        mesh.add_cylinder(wire_points[w], wire_points[w+1], 1.2, segments=8)

    mesh.set_context(comp, "Yellow_Connector")
    plug_x, plug_y, plug_z = 116, 92, 6
    mesh.add_box(plug_x - 5, plug_x + 5, plug_y, plug_y + 22, plug_z - 4, plug_z + 4)
    mesh.set_context(comp, "Polished_Brass")
    mesh.add_box(plug_x - 3.5, plug_x - 2.0, plug_y + 22, plug_y + 32, plug_z - 0.5, plug_z + 0.5)
    mesh.add_box(plug_x + 2.0, plug_x + 3.5, plug_y + 22, plug_y + 32, plug_z - 0.5, plug_z + 0.5)

    # 7. Lab Baseplate
    comp = "07_Lab_Bench_Baseplate"
    mesh.set_context(comp, "Bench_Mount_Base")
    z_chassis = -28.0
    mesh.add_box(-10, 90, -45, 115, z_chassis, z_chassis + 4.0)
    mesh.set_context(comp, "Rubber_Feet")
    for fx, fy in [(-5, -40), (85, -40), (-5, 110), (85, 110)]:
        mesh.add_cylinder([fx, fy, z_chassis - 6], [fx, fy, z_chassis], 7.0, segments=16)
    mesh.set_context(comp, "Aluminum_6061")
    for sx, sy in [(10, 10), (70, 10), (10, 90), (70, 90)]:
        mesh.add_cylinder([sx, sy, z_chassis + 4], [sx, sy, 0], 5.0, segments=16)

    # Export main Assembly files
    obj_path = os.path.join(OUTPUT_DIR, "Thyristor_MiniChannel_Assembly.obj")
    stl_path = os.path.join(OUTPUT_DIR, "Thyristor_MiniChannel_Assembly.stl")
    mesh.export_obj(obj_path, "thyristor_assembly.mtl")
    mesh.export_stl(stl_path)

    # Export individual STLs
    components = [
        "01_MiniChannel_HeatSink",
        "02_Thermal_Interface_TIM",
        "03_Thyristor_SCR_TY160D40",
        "04_Airflow_Duct_Shroud",
        "05_SUNON_Cooling_Fan",
        "06_Thermocouple_Sensor",
        "07_Lab_Bench_Baseplate"
    ]
    for c in components:
        c_stl = os.path.join(OUTPUT_DIR, f"{c}.stl")
        mesh.export_stl(c_stl, filter_comp=c)

    print("Successfully generated all assembly & component CAD files in deliverables.")
    return mesh, materials

if __name__ == "__main__":
    generate_all()
