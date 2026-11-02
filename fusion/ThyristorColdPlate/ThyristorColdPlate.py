"""
Autodesk Fusion 360 Entry Script: Liquid Mini-Channel Thyristor Cold Plate
"""
import os
import sys
import importlib
import traceback
import adsk.core
import adsk.fusion

def run(context):
    app = adsk.core.Application.get()
    ui = app.userInterface
    try:
        folder = os.path.dirname(os.path.abspath(__file__))
        if folder not in sys.path:
            sys.path.insert(0, folder)

        import thyristor_final
        importlib.reload(thyristor_final)

        thyristor_final.run(context)

        ui.messageBox(
            "Liquid Mini-Channel Thyristor Cooling Assembly successfully generated!\n\n"
            "Features:\n"
            "- Upright Industrial SCR Thyristor Module (TY160D40)\n"
            "- 16 Parallel Mini-Channels with Staggered Vortex Breaks\n"
            "- Coolant Inlet (Blue) and Outlet (Red) Anodized Hose Barbs\n"
            "- K-Type Thermocouple Sensor Assembly with Thermowell\n"
            "- Perimeter M4 Fasteners and Lab Elevation Standoffs\n"
            "- Authentic Autodesk PBR Materials (6061-T6 Aluminum, Copper, Brass, PBT)\n\n"
            "Exports saved to C:\\thyristor\\deliverables",
            "Fusion 360 Generation Complete"
        )
    except Exception:
        ui.messageBox(traceback.format_exc(), "Fusion Script Error")
