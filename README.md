# Thyristor Cooling Design

Academic CAD project for a liquid mini-channel cold plate used to cool a thyristor. Includes the reviewed Fusion assembly, STEP exports, interactive 360-degree HTML viewer, reference images, report content, and generation/review scripts.

## View the design

Download this repository using **Code → Download ZIP**, extract it, and open `deliverables/interactive_3d_viewer.html` in a browser. An internet connection is required to load Three.js and OrbitControls. No Python or CAD installation is required for the viewer.

Drag to rotate, scroll to zoom, and use the exploded-view slider, component visibility controls, Auto-Rotate, or Internal Channels.

## Reviewed CAD deliverables

- `deliverables/Thyristor_Reviewed_Final.f3d`: assembled design for Autodesk Fusion.
- `deliverables/Thyristor_Reviewed_Exploded.f3d`: exploded presentation for Autodesk Fusion.
- `deliverables/Thyristor_Reviewed_Final.step`: CAD interchange export.
- `deliverables/Reviewed_Assembly.png`, `Reviewed_Internal_Channels.png`, and `Reviewed_Exploded.png`: presentation images.
- `deliverables/Reviewed_Verification.json`: recorded CAD geometry checks.
- `deliverables/READ_ME_REVIEWED.md`: completed corrections and remaining engineering work.

Use the reviewed files above for the latest handoff. Earlier designs, diagnostic outputs, and the older CAD ZIP package are retained as project history; the HTML viewer has been updated separately after that ZIP was produced.

## Project files

- `fusion/ThyristorColdPlate/`: Fusion generation scripts and native exports.
- `reference/` and `extracted_images/`: source and report images.
- `report_content.py`: project report text.
- `DESIGN_BRIEF.md`: initial concept brief and assumptions; some status and geometry details predate the reviewed handoff.
- Root Python scripts: earlier generators, local Fusion bridge, review/repair automation, and viewer generation.

## Rebuild the current viewer

With Python installed, run:

```sh
python generate_liquid_viewer.py
```

This uses `deliverables/reviewed_viewer_mesh.json` and rewrites the HTML viewer. To refresh the mesh from CAD, open the reviewed assembly in Fusion and run `export_reviewed_viewer_mesh.py` with the local Fusion MCP bridge available at `127.0.0.1:27182`. That exporter currently uses the original Windows workspace path `C:\thyristor`; update paths before using it elsewhere.

Several historical generators also use that Windows path and require NumPy. Fusion scripts depend on Autodesk's `adsk` API inside Fusion. Review scripts can modify the active CAD document; read them before running them.

## Design scope

The reviewed assembly contains 17 components and 40 solid bodies. The cold plate is nominally 120 × 80 × 12 mm with 2 × 5 × 70 mm interrupted channels and a 6 mm cover. The external pump, radiator, reservoir, and tubing are not modeled.

This is an academic concept. Device geometry and fitting/seal details require further engineering. CAD checks do not establish cooling performance, pressure rating, electrical isolation, or suitability for manufacture. See the reviewed handoff for details.
