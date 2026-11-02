"""
Comprehensive report content data module for:
DESIGN AND DEVELOPMENT OF A MINI HEAT SINK CHANNEL FOR THYRISTOR COOLING
Thiagarajar College of Engineering - Mechatronics Engineering
Student: SARVESH P T (2303917711521045)
Guide: Dr. G. KUMARAGURUPARAN
"""

PROJECT_TITLE = "DESIGN AND DEVELOPMENT OF A MINI HEAT SINK CHANNEL FOR THYRISTOR COOLING"
COURSE_CODE = "22MT730 PROJECT III"
DEGREE_TEXT = "Submitted in partial fulfillment for the requirement of B.E. degree in\nMechatronics Engineering of Anna University"
STUDENT_NAME = "SARVESH P T"
STUDENT_ROLL = "2303917711521045"
GUIDE_NAME = "Dr. G. KUMARAGURUPARAN"
GUIDE_DESIGNATION = "Professor"
HOD_TITLE = "Signature of H.D.MCT"
DEPARTMENT = "Department of Mechatronics Engineering"
COLLEGE_NAME = "THIAGARAJAR COLLEGE OF ENGINEERING"
COLLEGE_AFFILIATION = "(A Govt. Aided, Autonomous Institution, Affiliated to Anna University)"
LOCATION = "MADURAI – 15"
SUBMISSION_DATE = "NOVEMBER 2026"
ACADEMIC_YEAR = "2026 – 2027"

CERTIFICATE_TEXT = (
    "Certified that this is a bonafide record of the 22MT730 Project III & Viva Voce done "
    "by Sarvesh P T (2303917711521045) of Seventh Semester B.E., Mechatronics Engineering "
    "during the year 2026 – 2027."
)

DECLARATION_TEXT = (
    "This is to certify that the 22MT730 Project Report entitled Design and Development "
    "of a Mini Heat Sink Channel for Thyristor Cooling, being submitted by SARVESH P T "
    "(2303917711521045), in partial fulfillment for the requirement of Bachelor of Engineering "
    "Degree in Mechatronics Engineering, is a record of Bonafide work. The results embodied in "
    "this report have not been submitted to any other university or institute for the award of "
    "any degree or diploma."
)

ACKNOWLEDGEMENT_TEXT = [
    "I take this opportunity to express my gratitude and deep regards to my guide Dr. G. Kumaraguruparan "
    "for his exemplary guidance, monitoring, and encouragement throughout the course of this project.",
    
    "I am extremely grateful to Dr. G. Kumaraguruparan, Professor and Head of the Department of "
    "Mechatronics Engineering, Thiagarajar College of Engineering, for providing his valuable "
    "suggestions in completing the project.",
    
    "I would like to extend my sincere thanks and gratitude to Dr. L. Ashok Kumar, Principal, "
    "Thiagarajar College of Engineering, for providing all the necessary facilities for completing the project.",
    
    "I express my thanks to the faculty of the Mechatronics Engineering Department for their valuable advice. "
    "I also thank all my friends and classmates who have directly or indirectly helped me in completing "
    "this project work."
]

ABSTRACT_PARAS = [
    "Thyristors (Silicon Controlled Rectifiers - SCRs) represent foundational semiconductor switching "
    "devices in industrial high-power conversion systems, including phase-controlled rectifiers, High Voltage "
    "Direct Current (HVDC) transmission stations, static var compensators, uninterruptible power supplies (UPS), "
    "and heavy AC/DC motor drives. During forward conduction and high-frequency commutation, significant internal "
    "Joule losses are generated across the p-n-p-n junctions due to finite on-state forward voltage drops and dynamic "
    "switching overlaps. If this concentrated thermal load is not dissipated rapidly and reliably, the junction "
    "temperature escalates beyond safe operating thresholds (typically 125°C), precipitating catastrophic thermal runaway, "
    "accelerated gate triggering degradation, thermo-mechanical fatigue, and permanent semiconductor failure. "
    "To resolve this pressing challenge, this project focuses on the comprehensive design, hydrodynamic modeling, "
    "parametric optimization, and experimental prototyping of an advanced aluminium mini-channel heat sink channel "
    "specifically engineered for high-power thyristor cooling.",

    "The investigation initiates with a rigorous, categorized review of contemporary literature encompassing conjugate "
    "heat transfer, hydrodynamic boundary layer development in narrow passages, interrupted fin architectures, and "
    "two-phase micro/mini-channel thermal management. Recognizing that conventional extruded air heat sinks exhibit "
    "unacceptable volumetric bulk and high thermal resistance, while microchannels suffer from prohibitive hydraulic pressure "
    "drops and clogging hazards, a customized mini-channel cold plate architecture (hydraulic diameter Dh = 2.4 mm) "
    "is formulated. The fabricated prototype comprises a high-conductivity 6061-T6 aluminium baseplate integrating 16 parallel "
    "mini-channels with staggered turbulence-inducing rib breaks. Heat is conducted from the thyristor module (TY160D40) "
    "through a high-performance thermal interface material (TIM) into the cold plate, where it is transferred by forced "
    "convection into an advected cooling medium. The engineered architecture supports dual-mode operation: high-velocity "
    "forced airflow via a high-static-pressure DC fan, and closed-loop liquid recirculation driven by a DC pump coupled to "
    "an external finned heat exchanger and reservoir.",

    "Detailed system analysis, functional decomposition, and module integration plans are developed to delineate the "
    "interdependence among electrical power input, fluid flow distribution, boundary layer disruption, and thermal resistance. "
    "Hydrodynamic and conjugate heat transfer analyses are conducted to investigate flow velocity uniformity across parallel "
    "channels, localized heat flux spreading, and pressure drop characteristics. A comprehensive numerical simulation model "
    "is implemented in MATLAB to quantify thermal resistance networks, predict junction and case temperatures across varying "
    "dissipation loads (20 W to 250 W), evaluate hydraulic pressure losses across laminar and transitional regimes (Re = 100 to 1500), "
    "and benchmark convective heat transfer coefficients against fluid pumping power for straight baseline and interrupted "
    "channel geometries.",

    "The experimental and simulation findings confirm that the proposed interrupted mini-channel architecture significantly "
    "enhances thermal performance, reducing total case-to-ambient thermal resistance from 1.85 °C/W (uncooled bare device) and "
    "0.45 °C/W (conventional forced-air heatsink) down to 0.21 °C/W under liquid mini-channel operation at 1.5 L/min. "
    "Furthermore, the staggered fin breaks effectively re-initialize the hydrodynamic and thermal boundary layers, increasing "
    "the average convective heat transfer coefficient by over 38% compared to continuous straight channels with minimal pumping "
    "penalties. The completed Phase-I work validates the physical architecture, component selection, sensor thermowell integration, "
    "and mathematical framework, establishing a robust engineering foundation for CNC prototype fabrication, automated multi-sensor "
    "DAQ logging, and full-scale experimental load characterization in the subsequent project phase."
]

SYMBOLS_ABBREVIATIONS = [
    ("SCR", "Silicon Controlled Rectifier (Thyristor)"),
    ("TIM", "Thermal Interface Material"),
    ("DC", "Direct Current"),
    ("AC", "Alternating Current"),
    ("CFD", "Computational Fluid Dynamics"),
    ("FVM", "Finite Volume Method"),
    ("CAD", "Computer Aided Design"),
    ("PWM", "Pulse Width Modulation"),
    ("DAQ", "Data Acquisition System"),
    ("COP", "Coefficient of Performance"),
    ("HVDC", "High Voltage Direct Current"),
    ("FACTS", "Flexible AC Transmission Systems"),
    ("UPS", "Uninterruptible Power Supply"),
    ("P_loss", "Electrical power dissipated in the thyristor (W)"),
    ("V_T", "On-state forward voltage drop across thyristor (V)"),
    ("I_T", "On-state forward conduction current (A)"),
    ("V_T0", "Thyristor threshold on-state voltage (V)"),
    ("r_T", "Thyristor dynamic slope resistance (mΩ)"),
    ("T_j", "Thyristor semiconductor junction temperature (°C)"),
    ("T_c", "Thyristor case temperature (°C)"),
    ("T_a", "Ambient air temperature (°C)"),
    ("T_in", "Coolant fluid inlet temperature (°C)"),
    ("T_out", "Coolant fluid outlet temperature (°C)"),
    ("ΔT_red", "Temperature reduction achieved by the cooling system (°C)"),
    ("R_th", "Thermal resistance (°C/W)"),
    ("R_th,jc", "Junction-to-case thermal resistance (°C/W)"),
    ("R_th,cs", "Case-to-heatsink contact thermal resistance (°C/W)"),
    ("R_th,sa", "Heatsink-to-ambient convective thermal resistance (°C/W)"),
    ("R_th,ca", "Total case-to-ambient thermal resistance (°C/W)"),
    ("D_h", "Hydraulic diameter of the channel (mm)"),
    ("W_ch", "Width of individual mini-channel (mm)"),
    ("H_ch", "Height / depth of mini-channel (mm)"),
    ("W_fin", "Thickness of channel dividing fin rib (mm)"),
    ("L", "Length of mini-channel (mm)"),
    ("A_c", "Channel cross-sectional flow area (m²)"),
    ("P_w", "Wetted channel perimeter (m)"),
    ("Re", "Reynolds number (dimensionless)"),
    ("Nu", "Nusselt number (dimensionless)"),
    ("Pr", "Prandtl number (dimensionless)"),
    ("f", "Darcy-Weisbach friction factor (dimensionless)"),
    ("ΔP", "Hydraulic pressure drop across the channel (kPa)"),
    ("P_pump", "Hydraulic pumping power consumed by fluid (W)"),
    ("h", "Convective heat transfer coefficient (W/m²·K)"),
    ("k_s", "Thermal conductivity of solid heat sink material (W/m·K)"),
    ("k_f", "Thermal conductivity of working fluid (W/m·K)"),
    ("ρ", "Density of cooling fluid (kg/m³)"),
    ("μ", "Dynamic viscosity of cooling fluid (Pa·s)"),
    ("C_p", "Specific heat capacity of cooling fluid (J/kg·K)"),
    ("Q_flow", "Volumetric flow rate of coolant (L/min or m³/s)"),
    ("e", "Thermal cooling effectiveness / efficiency (dimensionless)")
]
