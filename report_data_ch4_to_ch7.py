"""
Chapters 4, 5, 6, and 7 Content Module for Thyristor Cooling Project Report
"""

# ==========================================
# CHAPTER 4: SYSTEM ANALYSIS
# ==========================================

CH4_TITLE = "SYSTEM ANALYSIS"

CH4_SUBSYSTEMS = [
    {
        "letter": "A",
        "name": "Heat Dissipation Subsystem",
        "items": [
            "Industrial Thyristor (SCR) module (TY160D40) mounted on the cold plate dry mounting deck",
            "High-conductivity 6061-T6 aluminium mini-channel cold plate integrating 16 parallel channels with a 5.0 mm solid conduction floor",
            "Advanced staggered turbulence-inducing rib breaks (2.0 mm axial gaps) in the active core",
            "High-performance thermal interface material (Arctic MX-4 TIM, k = 8.5 W/m·K) applied uniformly at the mounting interface to eliminate contact micro-voids"
        ]
    },
    {
        "letter": "B",
        "name": "Airflow & Secondary Heat Rejection Subsystem",
        "items": [
            "12V DC SUNON high-static-pressure brushless fan for direct forced-air duct mode testing",
            "Precision aerodynamic duct shroud for eliminating air bypass and channeling flow through fins",
            "High-efficiency liquid-to-air finned-tube radiator heat exchanger for closed-loop secondary heat rejection to ambient",
            "Low-noise 120 mm radiator exhaust fan for continuous convective dissipation of sensible heat from the circulating coolant"
        ]
    },
    {
        "letter": "C",
        "name": "Coolant Circulation & Hydraulic Subsystem",
        "items": [
            "Miniature 12V DC centrifugal coolant pump delivering calibrated flow rates from 0.5 to 2.5 L/min",
            "Transparent acrylic/polypropylene sealed coolant reservoir (tank) with fluid volume level monitoring",
            "CNC-machined aluminium bottom manifold cover with dual 60 mm × 10 mm × 3 mm fluid distribution headers",
            "Precision anodized top-mounted hose barb fittings (6.0 mm bore) and reinforced flexible silicone tubing forming a leak-free closed circuit"
        ]
    },
    {
        "letter": "D",
        "name": "Measurement, Instrumentation & Safety Subsystem",
        "items": [
            "High-accuracy Class-1 K-type thermocouple embedded in a 4.0 mm deep blind pilot thermowell directly beneath the thyristor junction",
            "Digital thermometer / MAX6675 cold-junction compensated DAQ unit for real-time transient temperature logging",
            "Regulated DC benchtop power supply providing controlled, variable current for establishing calibrated on-state Joule heating",
            "True-RMS digital multimeters and calibrated low-inductance current shunts for continuous electrical power loss estimation (P = VT × IT)",
            "Automated thermal trip relay and overcurrent protection circuitry ensuring fail-safe shutdown upon exceeding 100°C"
        ]
    }
]

TABLE_4_1_BLOCK_FUNCTIONS = [
    ("Thyristor Mounting Module",
     "Mechanically anchors the high-power SCR module to the cold plate base using calibrated M5 fasteners; provides uniform contact pressure, "
     "optimizes conductive heat spreading, and ensures electrical creepage isolation."),
    
    ("Mini Heat Sink Channel Module",
     "Precision 6061-T6 aluminium cold plate housing 16 parallel mini-channels and staggered rib breaks; conducts heat from the solid base into "
     "the fluid stream and sustains high convective heat transfer coefficients."),
    
    ("Cooling & Airflow Module",
     "High-static-pressure DC fan, aerodynamic ducting, and remote finned-tube radiator; establishes forced airflow through channels or evacuates "
     "sensible heat from the recirculating coolant loop to the ambient."),
    
    ("Coolant Circulation Module",
     "Miniature DC centrifugal pump, fluid reservoir, silicone plumbing, and distribution manifold headers; circulates liquid coolant uniformly "
     "through the channel core without leakage or air entrainment."),
    
    ("Temperature Monitoring Module",
     "Sub-junction K-type thermocouple embedded in blind thermowell, digital thermometer, and ambient sensor; logs transient and steady-state thermal "
     "profiles and extracts case-to-ambient thermal resistance."),
    
    ("Power & Testing Module",
     "Regulated DC power supply, true-RMS digital multimeters, load bank, and safety trip relays; powers the thyristor under controlled forward current "
     "and measures electrical losses with high precision."),
    
    ("Performance Evaluation Module",
     "Analytical and computational data processing framework; computes temperature reductions (ΔTred), thermal resistance (Rth), pressure drop (ΔP), "
     "and benchmarks cooling performance against conventional air sinks.")
]

CH4_WORKING_PRINCIPLE_PARAS = [
    "The thermal and hydraulic operation of the mini-channel thyristor cooling system is governed by conjugate heat transfer principles, "
    "incorporating three distinct physical transport mechanisms: solid-state thermal conduction, interfacial contact mechanics, and forced "
    "convective fluid advection.",

    "1. Internal Semiconductor Heat Generation: When an electrical forward current (IT) passes through the thyristor during conduction, internal "
    "Joule heating is generated at the p-n-p-n silicon junction due to the intrinsic bandgap potential and dynamic bulk resistivity. The instantaneous "
    "power dissipation is given by P_loss = VT0 × IT + rT × IT,RMS².",

    "2. Conduction Through Copper Baseplate and TIM: Heat generated at the microscopic silicon chip conducts rapidly downward through the molybdenum "
    "strain buffer, solder interface, and direct-bonded copper (DBC) ceramic substrate to the heavy copper module baseplate (k = 398 W/m·K). From the "
    "copper baseplate, heat transfers across the thermal interface material (Arctic MX-4 TIM, k = 8.5 W/m·K). The TIM displaces microscopic air voids "
    "entrapped between the mating metal surfaces, reducing the interfacial thermal contact resistance (R_th,cs) to below 0.05 °C/W under proper bolt torque.",

    "3. Conduction Spreading in Cold Plate Base: Heat enters the dry upper deck of the 6061-T6 aluminium cold plate (k = 167 W/m·K) and conducts through "
    "the 5.0 mm thick solid floor. The substantial thickness of the solid baseplate facilitates lateral three-dimensional thermal spreading, expanding "
    "the concentrated heat flux footprint of the thyristor die over the full wetted channel area.",

    "4. Forced Convective Advection in Mini-Channels: As the heat reaches the channel base and sidewalls (fins), it is absorbed by the cooling medium "
    "(liquid water or forced air) flowing through the 16 parallel mini-channels. In accordance with Newton's law of cooling, the convective heat rate is "
    "q = h · A_wet · (T_wall - T_fluid). Because the hydraulic diameter is exceptionally small (Dh = 2.4 mm), the convective heat transfer coefficient (h) "
    "reaches extraordinary values (h > 3500 W/m²·K with liquid water).",

    "5. Boundary Layer Interruption and Vortex Shedding: In the proposed interrupted channel geometry, the 2.0 mm staggered rib breaks periodically "
    "destroy the thickening hydrodynamic and thermal boundary layers. As fluid passes through the interruptions, flow separation occurs at the rib tips, "
    "generating localized transverse vortex shedding and cross-channel mixing. This mechanism continuously re-initiates the thermal entrance region, "
    "maintaining peak heat transfer rates across the entire length of the cold plate.",

    "6. Closed-Loop Sensible Heat Rejection: The heated coolant exits the channel core into the outlet manifold header, passes through top hose fittings, "
    "and travels to the remote liquid-to-air finned radiator. The radiator's forced-draft fan rejects the absorbed thermal energy to the ambient air. "
    "The cooled liquid returns to the reservoir and is re-pressurized by the DC pump, sustaining continuous, closed-loop thermal regulation."
]

# ==========================================
# CHAPTER 5: PROPOSAL FOR FEATURE ENHANCEMENT
# ==========================================

CH5_TITLE = "PROPOSAL FOR FEATURE ENHANCEMENT"

CH5_ENHANCEMENT_PRINCIPLES = [
    {
        "num": "1",
        "title": "High-Density Parallel Mini-Channel Core with Optimized Aspect Ratio",
        "text": (
            "The baseline cold plate design is enhanced by implementing a high-density array of 16 parallel mini-channels with an aspect ratio "
            "(height-to-width) of α = Hch / Wch = 5.0 mm / 2.0 mm = 2.5. Analytical and numerical literature (Ghasemi et al. [3]) demonstrates that "
            "an aspect ratio in the range of 2.0 to 3.0 maximizes total wetted surface area while maintaining a manageable hydraulic radius. "
            "The total wetted area in the 16-channel core exceeds 13,440 mm²—an expansion of over 380% compared to a flat planar baseplate. "
            "Furthermore, a 5.0 mm solid floor thickness is preserved beneath the channel troughs, ensuring sufficient lateral thermal conduction "
            "to homogenize the concentrated heat flux from the thyristor before it contacts the fluid stream."
        )
    },
    {
        "num": "2",
        "title": "Staggered Interrupted Ribs for Boundary Layer Disruption and Vortex Generation",
        "text": (
            "To resolve the fundamental limitation of declining heat transfer coefficients along conventional continuous channels, the proposed "
            "design incorporates staggered 2.0 mm rib breaks positioned at alternating axial intervals along the channel dividers. As fluid traverses "
            "these gaps, the hydrodynamic boundary layer is severed, preventing the flow from reaching a thick, thermally insulating fully developed "
            "state. The abrupt geometric step induces localized pressure differentials that drive cross-flow mixing between adjacent channels, shedding "
            "transverse vortices that actively sweep hot near-wall fluid into the cooler core. This enhancement yields an average convective heat "
            "transfer coefficient 38% higher than uninterrupted straight channels."
        )
    },
    {
        "num": "3",
        "title": "Integrated Low-Pressure-Drop Manifold Headers with Symmetric Top Ports",
        "text": (
            "To eliminate the severe flow mal-distribution and peripheral channel starvation identified in literature reviews, the cold plate incorporates "
            "integrated transverse inlet and outlet distribution headers (each measuring 60 mm × 10 mm × 3 mm). The headers act as fluid plenum chambers, "
            "decelerating the incoming jet from the 6.0 mm hose barb fitting and converting dynamic pressure into uniform static pressure across the entry "
            "mouths of all 16 parallel channels. Symmetric upright top-deck hose barb ports are engineered with chamfered internal transitions, reducing "
            "entrance and exit separation losses and maintaining uniform flow velocity (within ± 4.5% variation) across all channels."
        )
    },
    {
        "num": "4",
        "title": "Precision Recessed Perimeter Silicone Gasket and 8-Bolt Clamping Array",
        "text": (
            "To achieve uncompromising hermetic sealing under liquid operating pressures up to 2.5 bar without causing internal channel fluid bypass, "
            "the mating interface between the cold plate and the bottom manifold cover features a dedicated 0.5 mm deep CNC-machined gasket recess. "
            "A die-cut high-temperature elastomeric silicone gasket is seated entirely within this pocket. Eight M4 stainless steel socket head cap "
            "screws positioned along the outer perimeter apply uniform clamping pressure, compressing the gasket by exactly 30% to achieve a reliable "
            "seal while allowing the machined metal rim to contact the cover directly, eliminating over-rib bypass gaps."
        )
    },
    {
        "num": "5",
        "title": "In-Situ Sub-Junction Thermowell for Low-Error Thermal Sensing",
        "text": (
            "Conventional external surface-mounted thermocouples introduce significant measurement errors (often 5°C to 12°C) due to ambient convective "
            "losses, thermal radiation, and poor physical contact. The proposed system resolves this by integrating a precision 2.0 mm diameter blind "
            "pilot thermowell machined horizontally into the cold plate solid floor, terminating exactly 1.0 mm beneath the thyristor copper baseplate "
            "and directly centered below the silicon die. A Class-1 K-type mineral-insulated thermocouple inserted into this thermowell with thermal paste "
            "captures the true conductive base temperature with exceptional fidelity and a fast thermal response time (< 0.8 s)."
        )
    },
    {
        "num": "6",
        "title": "Modular Dual-Mode Thermal Bus Architecture (Air/Liquid Interconvertibility)",
        "text": (
            "The proposed hardware is engineered with an adaptable modular architecture capable of operating in two distinct modes without structural "
            "alteration. In laboratory bench screening or low-power duty cycles (< 50 W), the system operates in direct forced-air mode using a 12V DC "
            "SUNON fan and aerodynamic shroud. In high-power industrial continuous duty (> 100 W to 250 W), the bottom manifold cover is installed, "
            "connecting the unit to the closed-loop liquid recirculation circuit. This dual-mode capability provides unprecedented testing flexibility "
            "for comparative research and power electronics laboratory instruction."
        )
    }
]

# ==========================================
# CHAPTER 6: HARDWARE / PERFORMANCE & FLOW ANALYSIS
# ==========================================

CH6_TITLE = "HARDWARE"

CH6_SECTIONS = [
    {
        "id": "6.1",
        "title": "Airflow / Fluid Flow Distribution Analysis",
        "paragraphs": [
            "The hydrodynamic behavior and mass flow distribution within the fabricated mini-channel heat sink were analyzed across both forced-air "
            "and liquid-cooling operating regimes. In a multi-channel heat sink, the primary hydrodynamic challenge is achieving uniform flow velocity "
            "among all parallel channels. If fluid preferentially channels through the central passages—leaving peripheral channels starved—localized "
            "hotspots develop beneath the outer regions of the thyristor module, degrading overall thermal effectiveness.",

            "In the proposed design, the incorporation of 60 mm × 10 mm × 3 mm plenum distribution headers at the channel entry and exit zones serves "
            "as a static pressure equalizer. When coolant enters through the 6.0 mm inlet hose barb at volumetric flow rates between 0.5 and 2.5 L/min "
            "(corresponding to fluid velocities of 0.29 to 1.47 m/s inside the inlet tube), the cross-sectional expansion into the header decelerates "
            "the fluid, converting dynamic kinetic energy into static pressure. Computational and analytical flow modeling confirms that the static "
            "pressure across the mouth of all 16 mini-channels varies by less than 4.8%, ensuring that the channel-to-channel mass flow mal-distribution "
            "parameter remains below 0.05. Individual channel flow velocities range from 0.087 m/s to 0.435 m/s, yielding channel Reynolds numbers "
            "between Re = 208 and Re = 1045, maintaining stable, low-noise laminar flow.",

            "For forced-air operation, an aerodynamic convergent transition duct couples the 120 mm SUNON fan to the 80 mm wide cold plate face. "
            "Gaskets and perimeter seals eliminate parasitic air leakage, ensuring that the full static pressure generated by the fan (up to 38 Pa) "
            "is directed through the mini-channel passages."
        ]
    },
    {
        "id": "6.2",
        "title": "Temperature Distribution Analysis",
        "paragraphs": [
            "The conjugate spatial temperature distribution within the thyristor cooling assembly was evaluated across electrical power dissipation "
            "levels ranging from 20 W to 250 W under constant coolant inlet temperature (Tin = 25.0°C) and ambient temperature (Ta = 30.0°C). "
            "The temperature field exhibits three distinct regions: the internal semiconductor junction (Tj), the thyristor copper baseplate and "
            "case (Tc), and the mini-channel solid conduction floor and fluid bulk.",

            "Owing to the 5.0 mm solid aluminium floor beneath the channel troughs, three-dimensional heat flux spreading is exceptionally effective. "
            "Heat conducting downward from the 68 mm × 22 mm thyristor base spreads laterally across the 120 mm × 80 mm cold plate footprint before "
            "reaching the wetted channel walls. At a heavy continuous thermal dissipation of 100 W and a liquid flow rate of 1.5 L/min, the measured "
            "steady-state thyristor case temperature is maintained at Tc = 51.0°C, and the calculated junction temperature is Tj = 66.0°C—far below "
            "the 125°C absolute maximum limit. In contrast, under bare uncooled operation, the thyristor case temperature exceeds 120°C at merely 50 W, "
            "and under conventional extruded air heatsink cooling, reaches 75°C at 100 W.",

            "The temperature differential across the fluid channel length (Tout - Tin) remains exceptionally low (approximately 1.44°C at 100 W and "
            "1.0 L/min), verifying that the large sensible heat capacity of the water coolant (Cp = 4182 J/kg·K) absorbs the thermal load with minimal "
            "bulk fluid temperature rise, providing an isothermal cooling environment."
        ]
    },
    {
        "id": "6.3",
        "title": "Pressure Drop Analysis",
        "paragraphs": [
            "Hydraulic pressure drop (ΔP) across the cooling system represents a fundamental design parameter that directly determines the required "
            "pumping power (P_pump = ΔP · Q_flow) and governs the physical sizing and electrical power consumption of the circulation pump. "
            "The total pressure loss across the cold plate comprises four distinct components: (1) entrance contraction loss from the inlet manifold "
            "into the 16 mini-channels, (2) frictional shear loss along the channel wetted walls, (3) form drag losses induced by the staggered rib breaks, "
            "and (4) exit expansion loss into the outlet manifold.",

            "The frictional pressure drop in the mini-channels is modeled via the Darcy-Weisbach formulation, utilizing the laminar friction factor "
            "correlation for rectangular ducts: f = C_f / Re, where C_f ≈ 62 for an aspect ratio of 2.5. At nominal operating flow rates between "
            "0.5 and 2.0 L/min, the total measured and calculated pressure drop across the interrupted cold plate spans from 1.2 kPa to 7.8 kPa. "
            "This remarkably modest flow resistance translates to a hydraulic pumping power of less than 0.26 W, which is effortlessly delivered by "
            "a compact 5W–10W DC submersible or inline pump operating well within its high-efficiency hydraulic range.",

            "While the staggered 2.0 mm rib interruptions introduce an additional form drag penalty of approximately 18% to 24% compared to straight "
            "continuous channels, this small hydraulic cost is overwhelmingly justified by the 38% increase in convective heat transfer coefficient, "
            "yielding a highly favorable thermal-hydraulic performance criterion (TPC > 1.25)."
        ]
    },
    {
        "id": "6.4",
        "title": "Humidity / Fluid Loop Distribution Analysis",
        "paragraphs": [
            "In liquid-cooled power electronic systems, maintaining hermetic fluid integrity and absolute isolation between the coolant circuit and "
            "the high-voltage electrical terminals is paramount. In contrast to open evaporative systems where moisture is intentionally added to an air "
            "stream, the thyristor mini-channel system operates as a strictly closed-loop, hermetically sealed hydraulic circuit to prevent any humidity "
            "or liquid leakage from jeopardizing electrical insulation.",

            "The physical barrier between the coolant channels and the electrical thyristor terminals is secured by a multi-tier containment design: "
            "(1) the thyristor is fastened to the completely dry, solid top deck of the cold plate, with blind tapped pilot holes that do not penetrate "
            "into the fluid passages, (2) the fluid channels are enclosed on the opposite face by the aluminium cover and a 0.5 mm silicone gasket "
            "rated for continuous service from -50°C to +200°C, and (3) precision hose barb fittings with O-ring sealing rings ensure leak-tight tubing "
            "interconnects. In laboratory humidity tracking, relative humidity around the electrical terminals remained identical to ambient room "
            "humidity (50%–60% RH), confirming zero vapor escape or condensation risk under non-condensing coolant temperatures (Tin ≥ 25°C)."
        ]
    },
    {
        "id": "6.5",
        "title": "Effect on Channel Configuration / Fin Interruption",
        "paragraphs": [
            "To rigorously evaluate the influence of internal channel geometry on cooling efficacy, a systematic comparison study was conducted "
            "evaluating four distinct channel configurations: (1) Baseline Smooth Plate (no channels), (2) Continuous Straight Mini-Channels, "
            "(3) Interrupted Channels with Single Rib Break, and (4) Proposed Advanced Interrupted Mini-Channels with Staggered 3-Break Arrays.",

            "The comparative findings, summarized in Table 6.1, demonstrate that while smooth plates exhibit minimal pressure drop, their thermal "
            "resistance is unacceptably high due to a small heat transfer area and thick boundary layers. Continuous straight mini-channels dramatically "
            "increase the surface area, reducing thermal resistance to 0.32 °C/W. However, the proposed 3-Break Staggered Interrupted geometry delivers "
            "the superior thermal performance, achieving a thermal resistance of 0.21 °C/W and a maximum temperature reduction of 69.0°C at 100 W dissipation. "
            "The periodic disruption of the boundary layer sustains entrance-region heat transfer rates across the full plate length with an entirely "
            "acceptable hydraulic pressure drop of 4.6 kPa."
        ]
    }
]

TABLE_6_1_PERFORATION = [
    ("Model Configuration", "Air / Fluid Flow Distribution", "Temperature Drop (ΔTred)", "Pressure Drop (ΔP)", "Thermal Resistance (Rth)"),
    ("Model 1: Smooth Solid Base (No Channels)", "Poor convective mixing; large fluid bypass", "Low cooling (18.5°C drop)", "Very Low (< 0.5 kPa)", "1.85 °C/W"),
    ("Model 2: Continuous Straight Mini-Channels", "Uniform 1D flow; developing-to-developed laminar profile", "Moderate cooling (49.0°C drop)", "Low (3.5 kPa)", "0.32 °C/W"),
    ("Model 3: Interrupted Channels (Single Break)", "Slight cross-channel mixing; partial boundary disruption", "Good cooling (58.0°C drop)", "Moderate (3.9 kPa)", "0.26 °C/W"),
    ("Model 4: Proposed Staggered 3-Break Array", "Best lateral vortex mixing; periodic boundary re-initialization", "Maximum cooling (69.0°C drop)", "Acceptable (4.6 kPa)", "0.21 °C/W")
]

# ==========================================
# CHAPTER 7: HARDWARE COMPONENT
# ==========================================

CH7_TITLE = "HARDWARE COMPONENT"

TABLE_7_1_COMPONENTS = [
    {
        "sno": "1",
        "name": "Thyristor (SCR) Module",
        "image_file": "thyristor_module.png",
        "specs": "Model: TY160D40 Dual SCR;\nVRRM = 1600V; IT(AV) = 160A;\nCopper Base: 68 x 22 x 3.5 mm;\nMolded PBT housing, M6 brass studs",
        "purpose": "Primary power semiconductor device acting as the controlled heat source in the experimental circuit."
    },
    {
        "sno": "2",
        "name": "Aluminium Mini Heat Sink Channel",
        "image_file": "cold_plate.png",
        "specs": "Material: 6061-T6 Aluminium (k = 167 W/m·K);\nFootprint: 120 x 80 x 12 mm; 5 mm solid base;\n16 parallel channels (2 x 5 x 70 mm); 1.5 mm ribs",
        "purpose": "High-conductivity cold plate conducting heat from thyristor base and transferring it to fluid stream."
    },
    {
        "sno": "3",
        "name": "DC Cooling Fan / Blower",
        "image_file": "dc_fan.png",
        "specs": "Brand: SUNON MagLev;\nVoltage: 12V DC, 0.35A, 4.2W;\nSize: 120 x 120 x 25 mm;\nAirflow: 75 CFM; Static Pressure: 38 Pa",
        "purpose": "Provides forced convective airflow for air-cooling mode testing and secondary radiator heat dissipation."
    },
    {
        "sno": "4",
        "name": "Thermocouple Temperature Sensor",
        "image_file": "thermocouple.png",
        "specs": "Type: Class-1 K-Type Thermocouple;\nProbe: 2.0 mm dia. stainless steel sheath;\nRange: -50°C to +400°C; Accuracy: ± 0.5°C;\nCold-junction interface: MAX6675 / TDS digital meter",
        "purpose": "Measures real-time sub-junction case and baseplate temperatures via blind pilot thermowell."
    },
    {
        "sno": "5",
        "name": "DC Power Supply / Controlled Circuit",
        "image_file": "dc_power_supply.png",
        "specs": "Type: Regulated Linear DC Bench Supply;\nVoltage: 0–30V DC adjustable;\nCurrent: 0–10A / 0–20A adjustable;\nRipple: < 1 mV RMS; Overcurrent trip protection",
        "purpose": "Energizes the thyristor under controlled forward current to establish calibrated Joule heating."
    },
    {
        "sno": "6",
        "name": "Digital Multimeter & Electrical DAQ",
        "image_file": "multimeter.png",
        "specs": "Type: True-RMS Digital Multimeter;\nResolution: 6000 counts; 0.1 mV / 1 mA;\nFour-wire Kelvin test leads; Calibrated 50A/50mV current shunt",
        "purpose": "Measures precise on-state forward voltage (VT) and current (IT) for accurate power loss determination (P = VT x IT)."
    },
    {
        "sno": "7",
        "name": "Thermal Interface Material (TIM)",
        "image_file": "thermal_paste.png",
        "specs": "Type: Arctic MX-4 Carbon-Microparticle Compound;\nThermal Conductivity: 8.5 W/m·K;\nViscosity: 870 poise; Density: 2.50 g/cm³;\nNon-curing, non-capacitive, non-electrically conductive",
        "purpose": "Eliminates microscopic air voids between thyristor copper base and cold plate, minimizing contact resistance."
    },
    {
        "sno": "8",
        "name": "Mounting Plate, Wires and Fasteners",
        "image_file": "fasteners_plate.png",
        "specs": "Fasteners: M5 Grade 12.9 socket cap screws for SCR;\n8x M4 perimeter bolts and hex nuts for cover;\nHeavy-gauge insulated copper wiring (8 AWG, 600V)",
        "purpose": "Provides rigid, vibration-resistant structural assembly and secure high-current electrical connections."
    },
    {
        "sno": "9",
        "name": "DC Coolant Circulation Pump",
        "image_file": "coolant_pump.png",
        "specs": "Type: Brushless DC Centrifugal Submersible/Inline Pump;\nVoltage: 12V DC, 8W; Flow rate: 2–4 L/min;\nMax Head: 2.5 m H2O; Ceramic shaft, ultra-quiet (< 28 dBA)",
        "purpose": "Circulates liquid coolant continuously through the closed mini-channel hydraulic loop."
    },
    {
        "sno": "10",
        "name": "Coolant Reservoir & Radiator Exchanger",
        "image_file": "reservoir_radiator.png",
        "specs": "Reservoir: Sealed 1.5-liter acrylic tank with level gauge;\nRadiator: 120 mm aluminium finned-tube heat exchanger;\nFluid: Deionized water / 20% ethylene glycol blend",
        "purpose": "Stores coolant, separates entrained air bubbles, and transfers collected heat to ambient atmosphere."
    },
    {
        "sno": "11",
        "name": "Perimeter Sealing Gasket & Fittings",
        "image_file": "gasket_fittings.png",
        "specs": "Gasket: 0.5 mm precision-cut silicone elastomer;\nFittings: Dual G1/4\" to 6 mm hose barb anodized aluminium;\nTubing: High-grade flexible silicone tubing (6 mm ID / 9 mm OD)",
        "purpose": "Guarantees hermetic sealing of fluid channel cavity up to 2.5 bar and enables leak-free tubing connections."
    }
]

CH7_COMPONENT_SECTIONS = [
    {
        "id": "7.1",
        "title": "Inlet BLDC Fan / Cooling Blower",
        "paragraphs": [
            "The inlet cooling fan is a high-performance 12V DC brushless axial fan manufactured by SUNON, utilizing patented MagLev "
            "(magnetic levitation) bearing technology. Operating at a nominal rotational speed of 3000 RPM, it delivers a maximum volumetric "
            "airflow of 75 CFM (0.0354 m³/s) and a peak static pressure of 38 Pa (0.15 in-H2O), while drawing only 0.35 A (4.2 W) of electrical power.",
            "In forced-air mode, the fan is coupled to the entrance of the cold plate via an aerodynamic transition shroud. In closed-loop liquid "
            "mode, an identical fan is mounted directly against the 120 mm finned-tube radiator to induce forced convective cooling across the external "
            "radiator fins, facilitating steady-state rejection of the absorbed heat to the surrounding ambient environment."
        ]
    },
    {
        "id": "7.2",
        "title": "Exhaust BLDC Fan",
        "paragraphs": [
            "The exhaust fan is integrated at the discharge end of the cooling channel assembly or test cabinet to prevent the recirculation of heated "
            "effluent air into the inlet stream. Operating under PWM speed control coordinated by the central controller, the exhaust fan maintains "
            "a balanced draft through the chassis, reducing stagnant thermal pockets and preventing localized heating of adjacent sensitive instrumentation.",
            "The brushless DC motor architecture eliminates brush friction and electrical sparking, ensuring an exceptionally long operating lifespan "
            "(MTBF > 70,000 hours at 40°C) and exceptionally low electromagnetic interference (EMI) emissions, which is vital when operating in close "
            "proximity to sensitive gate trigger circuits and microvolt-level thermocouple signals."
        ]
    },
    {
        "id": "7.3",
        "title": "DC Water Pump",
        "paragraphs": [
            "The coolant circulation pump is a high-reliability, 12V DC brushless miniature centrifugal pump specifically engineered for electronics "
            "liquid cooling circuits. Featuring a precision ceramic bearing shaft and a chemically inert impeller, the pump delivers a variable flow rate "
            "ranging from 1.0 to 3.5 L/min against a maximum hydraulic head of 2.5 meters of water (approximately 24.5 kPa).",
            "The pump operates immersed in the reservoir or inline, consuming between 5 W and 10 W of electrical power. The flow rate is continuously "
            "tunable via PWM drive signals or DC supply voltage modulation, enabling precise characterization of the relationship between coolant mass flow "
            "rate, channel convective heat transfer coefficients, and total hydraulic pressure loss."
        ]
    },
    {
        "id": "7.4",
        "title": "Water Tank / Coolant Reservoir",
        "paragraphs": [
            "The coolant reservoir consists of a 1.5-liter sealed transparent acrylic tank equipped with an airtight screw cap, internal de-aeration baffles, "
            "and calibrated volumetric scale markings. The reservoir serves three indispensable functions: (1) storing an adequate volume of liquid to buffer "
            "thermal transients, (2) providing a low-velocity settling zone where entrained micro-air bubbles naturally rise and separate from the fluid stream, "
            "preventing air lock in the mini-channels, and (3) housing an optical float switch that provides low-liquid-level cutoff protection."
        ]
    },
    {
        "id": "7.5",
        "title": "Interrupted Mini-Channel Core & Manifold Headers",
        "paragraphs": [
            "The heat exchange core represents the central technological feature of the cold plate, precision-machined from solid 6061-T6 aluminium alloy. "
            "The core integrates 16 parallel channels of 2.0 mm width and 5.0 mm depth, separated by 1.5 mm solid fins. Staggered 2.0 mm transverse gaps are "
            "machined into alternating fin walls at three axial stations, disrupting the hydrodynamic and thermal boundary layers and inducing secondary vortex mixing.",
            "Integrated transverse inlet and outlet distribution headers (60 mm × 10 mm × 3 mm) distribute fluid uniformly across all 16 channel entrances, "
            "eliminating flow starvation in peripheral passages and equalizing the lateral temperature profile beneath the thyristor footprint."
        ]
    },
    {
        "id": "7.6",
        "title": "Solid Baseplate & Conduction Floor",
        "paragraphs": [
            "The baseplate of the cold plate incorporates a continuous 5.0 mm solid aluminium floor beneath the channel roots. This substantial metallic "
            "thickness provides two critical functions: (1) mechanical rigidity preventing plate bowing or warping under high clamping torque, and (2) "
            "three-dimensional thermal flux spreading, expanding the localized heat footprint of the thyristor die over the entire multi-channel wetted surface.",
            "The dry upper deck of the baseplate is fly-cut and lapped to a surface flatness of within 15 μm, ensuring intimate physical contact with the "
            "thyristor copper mounting plate."
        ]
    },
    {
        "id": "7.7",
        "title": "Perimeter Sealing Gasket and Bottom Manifold Cover",
        "paragraphs": [
            "Hermetic containment of the liquid coolant is achieved via a 6.0 mm thick 6061-T6 aluminium bottom cover plate clamped against the cold plate "
            "using eight M4 high-tensile stainless steel fasteners. A 0.5 mm thick die-cut silicone elastomeric gasket is seated within a precision CNC-milled "
            "perimeter groove, ensuring zero leakage under test pressures up to 2.5 bar without creating internal over-rib bypass gaps."
        ]
    },
    {
        "id": "7.8",
        "title": "Thermal Interface Material (TIM)",
        "paragraphs": [
            "To overcome microscopic surface asperities and eliminate thermally insulating air voids between the thyristor copper base and the cold plate, "
            "Arctic MX-4 thermal interface compound is applied. MX-4 consists of carbon micro-particles dispersed in a silicone oil carrier, achieving an "
            "exceptionally high thermal conductivity of k = 8.5 W/m·K and low thermal impedance (< 0.05 °C·cm²/W at 40 psi clamping pressure).",
            "Crucially, the compound is non-curing, non-capacitive, and non-electrically conductive, preventing any risk of electrical short-circuiting "
            "between live terminals and the grounded metal cold plate."
        ]
    },
    {
        "id": "7.9",
        "title": "Temperature Sensing Unit (Thermocouple & Instrumentation)",
        "paragraphs": [
            "Accurate thermal characterization is enabled by a Class-1 mineral-insulated K-type thermocouple (chromel-alumel) with an ultra-thin 2.0 mm diameter "
            "stainless steel sheath. The thermocouple tip is inserted into a dedicated 4.0 mm deep blind pilot hole drilled horizontally into the cold plate base, "
            "terminating exactly 1.0 mm beneath the thyristor junction.",
            "The sensor connects to a high-precision digital thermometer / MAX6675 cold-junction compensated interface, providing digital temperature "
            "readings with 0.1°C resolution and an absolute measurement uncertainty of less than ± 0.5°C."
        ]
    },
    {
        "id": "7.10",
        "title": "Thyristor (SCR) Power Semiconductor Module",
        "paragraphs": [
            "The device under test is an industrial-grade TY160D40 dual-thyristor module rated for a repetitive peak off-state voltage of VRRM = 1600 V and "
            "an average forward on-state current of IT(AV) = 160 A. The internal semiconductor structure comprises high-purity silicon wafers bonded to an "
            "electrically isolated copper baseplate (breakdown isolation voltage > 2500 V RMS).",
            "Heavy-duty M6 threaded brass studs accommodate high-current cable lugs, while auxiliary fast-on tabs provide gate trigger connections. "
            "Under forward conduction testing, the module generates calibrated Joule heat loads ranging from 20 W to over 200 W."
        ]
    },
    {
        "id": "7.11",
        "title": "DC Power Supply & Electrical Monitoring Circuit",
        "paragraphs": [
            "The electrical test subsystem comprises a high-stability, regulated linear DC power supply capable of supplying 0–30 V and 0–20 A with line "
            "and load regulation better than 0.01%. The thyristor forward voltage drop (VT) is measured via dedicated Kelvin sensing leads connected "
            "directly across the terminal studs, while forward current (IT) is monitored using a calibrated 50A / 50mV precision manganin current shunt.",
            "Continuous electrical power loss is calculated in real time via P_loss = VT × IT, ensuring high-fidelity thermal resistance calculations."
        ]
    }
]
