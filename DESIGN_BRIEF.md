# Liquid mini-channel heat sink for thyristor cooling

Status: provisional CAD concept, not qualified for fabrication. User selected liquid cooling.

## Corrected architecture

Reservoir -> pump -> cold plate inlet header -> parallel mini-channels -> outlet header -> radiator with fan -> reservoir.

The thyristor mounts on the dry, flat underside of the cold plate base. Coolant remains in the enclosed passages on the other side. The fan rejects heat at the radiator. A tank alone cannot provide sustained heat rejection unless it has a separately designed cooling mechanism.

## Corrections to the supplied review

- Replace the inconsistent air/liquid architecture with the loop above. The hardware list must add a pump, radiator, reservoir, tubing, compatible fittings, gasket, and flow monitoring.
- Describe the objective as reducing operating temperature and thermal resistance. Do not claim that a cold plate eliminates the electrical power dissipated by the thyristor.
- Add distribution headers, a sealed cover, dry fastener positions, and a continuous sealing land.
- Select the pump from its pressure-flow curve against total loop resistance. Free-flow pump ratings are insufficient.
- Match all wetted materials and coolant chemistry. Do not assume bare aluminium and copper parts can be mixed without corrosion controls.
- Select electrical isolation from the actual thyristor datasheet. Thermal paste is not automatically an electrical insulator.
- Measure inlet/outlet coolant temperatures, flow, base/case temperature and device heat input. Supply voltage times load current is not automatically the heat dissipated in the thyristor.
- Compare both designs at matched heat input and inlet temperature; report pressure drop and pumping power as well as temperature. Consider equal pumping-power comparisons.
- Treat the review's claims of improvement as expected outcomes. No measurements, verified part selections or performance evidence were supplied.

## Initial geometry assumptions

| Item | Provisional value |
| --- | --- |
| Base footprint | 120 x 80 mm |
| Base stock thickness | 8 mm |
| Solid floor beneath channels | 5 mm |
| Parallel channels | 16 |
| Channel width / depth / length | 2 / 3 / 70 mm |
| Rib thickness | 1.5 mm |
| Hydraulic diameter of uninterrupted channel | 2.4 mm |
| Headers | 60 x 10 x 3 mm each |
| Cover | 5 mm aluminium, alloy unselected |
| Gasket | 0.5 mm uncompressed placeholder |
| Cover fastening | Six nominal M4 clearance holes; bolts/nuts not modeled |
| Inlet / outlet | 6 mm bore placeholders, not finished fitting seats |
| Device envelope | 40 x 40 x 20 mm placeholder, no verified mounting holes |

The experimental version adds 2 mm gaps in alternating ribs at staggered positions. The research hypothesis is that this changes local mixing and thermal boundary-layer development. It may also cause bypass or extra pressure loss. Improvement and originality are unproven; retain the straight-channel baseline for comparison.

The gasket thickness leaves a small over-rib clearance in this first concept. Compression, sealing force, lid deflection, bypass and gasket material require review. Square internal corners require machining radii. Device mount holes/clamping, port fitting seats/threads, seal qualification, pressure rating and fastener sizing are not finalized.

## Illustrative energy balance only

Assume 100 W heat dissipation, 1 L/min water flow, density 1000 kg/m3 and specific heat 4180 J/(kg K).

Coolant rise = Q/(mass flow x specific heat) = 1.44 K. This is the bulk coolant temperature rise, NOT a prediction of thyristor or base temperature.

At equal flow distribution, nominal channel velocity is 0.174 m/s. With illustrative water viscosity 0.001 Pa s, Reynolds number is about 417. Distribution and interrupted-channel behavior require further analysis. These assumed inputs are not project specifications.

Actual device losses, maximum junction temperature, junction-to-case resistance, interface resistance, coolant inlet conditions, pump curve and radiator performance are needed to establish adequacy.

## Fusion automation

Script: fusion/ThyristorColdPlate/ThyristorColdPlate.py

In Fusion, open Scripts and Add-Ins, add the ThyristorColdPlate script folder and run it. It creates two new documents without modifying existing documents, builds separate components, checks for solid bodies, and exports F3D and STEP under the script's output folder. Re-running overwrites those generated exports.

The source is syntax checked locally. It has NOT yet run in Fusion. Export success, geometric validity in Fusion, visual quality and assembly fit remain pending until Fusion is installed. The timeline contains editable features; changing Python dimensions and rerunning regenerates the concept. It is not yet a fully constrained, user-parameter-driven CAD model.

## Sources

- User-supplied SARVESH_45_REVIEW 2.pptx, all 11 slides including diagrams.
- Fusion trial: https://www.autodesk.com/products/fusion-360/free-trial
- Autodesk scripts: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/WritingDebugging_UM.htm
- Autodesk extrusion API: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/ExtrudeFeatureSample_Sample.htm
- Eaton coolant corrosion guidance: https://www.eaton.com/us/en-us/products/thermal-management-solutions/materials-finishes/avoiding-galvanic-corrosion.html

## Deliverable scope

Current: design brief and unexecuted Fusion generator. Next: execute and inspect in Fusion, correct geometry, complete assembly presentation and export verified files. Thermal simulation, measured performance, manufacturing drawings and validated build specifications are not yet available.
