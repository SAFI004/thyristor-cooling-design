"""
Chapters 1, 2, and 3 Content Module for Thyristor Cooling Project Report
"""

# ==========================================
# CHAPTER 1: INTRODUCTION
# ==========================================

CH1_TITLE = "INTRODUCTION"

CH1_SECTIONS = [
    {
        "id": "1.1",
        "title": "Domain Background",
        "paragraphs": [
            "Power electronic conversion technologies represent the critical backbone of modern industrial automation, "
            "renewable energy grid integration, electric transportation, and high-voltage transmission infrastructure. "
            "Among various solid-state switching devices, the Silicon Controlled Rectifier (SCR)—commonly designated as "
            "the thyristor—occupies a paramount role in managing multi-megawatt power levels, high surge currents, and "
            "demanding continuous duty cycles. Thyristors are widely utilized in line-commutated converter (LCC) stations "
            "for High Voltage Direct Current (HVDC) transmission lines, Flexible AC Transmission Systems (FACTS, such as "
            "Static Synchronous Compensators and Static VAR Compensators), heavy industrial phase-controlled rectifiers for "
            "electrochemical processing, soft starters for megawatt-scale AC induction motors, static transfer switches (STS) "
            "for data center power redundancy, and high-frequency pulsed power supplies.",

            "A physical thyristor is a multi-layer p-n-p-n semiconductor device that operates as a bistable switch. "
            "Unlike ideal theoretical switches, physical thyristors inherently exhibit non-zero internal electrical impedances "
            "and finite charge-carrier transit delays. During forward on-state conduction, a finite forward voltage drop "
            "(typically VT = 1.2 V to 2.2 V depending on current density and junction temperature) appears across the main "
            "anode-to-cathode terminals. When conducting continuous load currents ranging from tens to hundreds of amperes, "
            "this voltage drop produces massive internal Joule dissipation (P = VT × IT). Furthermore, during the transient "
            "switching phases—specifically the turn-on interval and the reverse recovery turn-off interval—the anode voltage "
            "and anode current overlap dynamically over microsecond timescales, introducing substantial switching energy "
            "losses (Eon and Err). In high-frequency or cyclic phase-controlled circuits, these switching losses accumulate "
            "linearly with switching frequency, substantially compounding the net internal heat generation.",

            "If the heat generated within the microscopic semiconductor die is not rapidly, continuously, and uniformly "
            "extracted, the internal junction temperature (Tj) escalates rapidly. Under excessive thermal stress, thyristors "
            "suffer from severe operational degradation governed by the Arrhenius reaction rate theory. Elevated temperatures "
            "drastically increase internal minority carrier leakage currents (IDRM and IRRM), leading to spontaneous thermal "
            "runaway where the device self-triggers into conduction without an applied gate signal, completely destroying circuit "
            "controllability. Furthermore, the maximum permissible junction temperature for industrial silicon thyristors is "
            "strictly bounded by manufacturer specifications to Tj,max = 125°C. Operating at or near this threshold induces severe "
            "thermo-mechanical stress cycling arising from the substantial mismatch in the coefficient of thermal expansion (CTE) "
            "between the silicon die (2.6 × 10^-6 /K), the direct-bonded copper (DBC) ceramic substrate, the lead-free solder "
            "interconnects, and the heavy copper mounting baseplate (16.5 × 10^-6 /K). This cyclical thermo-mechanical fatigue "
            "accelerates solder layer delamination, creates localized micro-voids, elevates internal thermal resistance, and "
            "culminates in catastrophic device destruction.",

            "To maintain the thyristor junction well below safe thermal limits (typically below 85°C to 95°C under continuous "
            "rated load), an exceptionally capable thermal management system is mandatory. Historically, conventional industrial "
            "installations have relied heavily on extruded aluminium or cast copper finned heat sinks cooled by natural convection "
            "or forced air from axial fans. However, air possesses inherently poor thermophysical transport properties: a very low "
            "thermal conductivity (k_air ≈ 0.026 W/m·K at 25°C) and a low volumetric heat capacity (ρCp ≈ 1.2 kJ/m³·K). Consequently, "
            "achievable convective heat transfer coefficients in conventional air-cooled heat sinks are severely restricted to "
            "5–25 W/m²·K under natural draft and 30–100 W/m²·K under high-velocity forced flow. To dissipate concentrated thermal "
            "loads of 100 W to 300 W from a compact thyristor module (footprint < 40 cm²), conventional air heat sinks require "
            "excessively bulky geometries (often exceeding 250 × 200 × 100 mm), substantial metal mass (> 3 kg), and noisy high-power "
            "blowers that generate severe acoustic pollution (> 65 dBA) and consume excessive parasitic electrical energy.",

            "To transcend the fundamental heat transfer limitations of conventional air-cooled heat sinks, thermal engineering "
            "research has converged toward compact channel-based heat sinks. As formally classified by Kandlikar, fluid flow channels "
            "are categorized based on hydraulic diameter (Dh) into conventional channels (Dh > 3 mm), mini-channels (200 μm ≤ Dh ≤ 3 mm), "
            "and micro-channels (10 μm ≤ Dh ≤ 200 μm). While micro-channels deliver astronomical heat transfer coefficients, they "
            "suffer from severe practical limitations in industrial environments, including astronomical hydraulic pressure drops "
            "(often requiring multi-bar pumping systems), extreme susceptibility to particulate clogging, and severe sensitivity to "
            "surface fouling. Conversely, mini-channel heat sinks (Dh ≈ 1 mm to 3 mm) strike an optimal engineering compromise. "
            "They dramatically increase the wetted surface-area-to-volume ratio, maintain thin hydrodynamic and thermal boundary layers, "
            "achieve high convective heat transfer coefficients (2000 to 6000 W/m²·K with liquid coolants), and exhibit manageable "
            "hydraulic flow resistance that can be easily overcome by low-power, low-noise miniature DC pumps or blowers. "
            "Therefore, the research and development of an optimized mini-channel heat sink channel specifically engineered for "
            "thyristor thermal management represents a highly compelling, technically rigorous, and practically vital endeavor."
        ]
    },
    {
        "id": "1.2",
        "title": "System Introduction",
        "paragraphs": [
            "The primary objective of this project is the comprehensive design, hydrodynamic modeling, CAD development, and "
            "experimental performance evaluation of a high-efficiency mini-channel heat sink channel cooling system tailored "
            "specifically for high-power thyristor modules. The target semiconductor device considered in this study is an industrial-grade "
            "thyristor module (TY160D40 / dual SCR topology), featuring a heavy copper mounting baseplate, molded flame-retardant "
            "PBT encapsulation, high-current M6 brass terminal studs, and auxiliary gate trigger terminals. Under nominal operation, "
            "the device handles high forward conduction currents while dissipating substantial thermal energy into its metallic mounting base.",

            "The engineered cooling system comprises an aluminium alloy (6061-T6, thermal conductivity k = 167 W/m·K) mini-channel cold plate "
            "having a nominal base footprint of 120 mm × 80 mm × 12 mm. To ensure robust thermal spreading and structural rigidity, a solid "
            "conduction floor of 5.0 mm thickness is maintained beneath the fluid passages. The internal heat exchange core integrates 16 "
            "parallel mini-channels, each characterized by a channel width of Wch = 2.0 mm, a channel depth of Hch = 5.0 mm, a fin rib thickness "
            "of Wfin = 1.5 mm, and an active channel flow length of L = 70.0 mm. This configuration yields a channel hydraulic diameter of "
            "Dh = 2.4 mm, perfectly situating the design within the high-performance mini-channel regime. The thyristor module is mounted "
            "rigidly to the dry, planar top surface of the cold plate utilizing calibrated M5 socket head cap screws, with a high-performance "
            "thermal interface material (TIM, thermal conductivity k_TIM = 8.5 W/m·K) interposed at the contact interface to eliminate "
            "microscopic air gaps and minimize contact thermal resistance.",

            "A pivotal feature enhancement investigated in this project is the implementation of staggered turbulence-inducing fin breaks "
            "(interrupted channel geometry). Unlike conventional continuous-fin mini-channels where hydrodynamic and thermal boundary layers "
            "grow continuously from inlet to outlet—causing a progressive decline in the localized convective heat transfer coefficient—the "
            "interrupted architecture introduces 2.0 mm axial gaps staggered across alternating rib walls. These interruptions disrupt the "
            "developing boundary layers, initiate localized flow recirculation and secondary vortex shedding, and periodically re-initialize "
            "the thermal entry length, thereby maintaining an extraordinarily high average convective heat transfer coefficient across the "
            "entire thyristor contact zone.",

            "The physical architecture is engineered to support versatile dual-mode heat rejection: (1) high-velocity forced-air convection "
            "using a 12V DC SUNON brushless cooling fan coupled to an aerodynamic shroud duct, and (2) closed-loop liquid recirculation "
            "where water or a water-glycol mixture is circulated through the mini-channels by a miniature DC centrifugal pump. In the liquid "
            "cooling loop, the cold plate is enclosed by a precision CNC-machined 6.0 mm aluminium bottom manifold cover sealed with a 0.5 mm "
            "recessed silicone perimeter gasket and secured with eight M4 socket head bolts. Coolant enters and exits through top-mounted "
            "anodized 6.0 mm hose barb fittings, circulating through a sealed coolant reservoir and a remote liquid-to-air finned radiator "
            "equipped with a dedicated cooling fan for final sensible heat dissipation to the ambient.",

            "To rigorously evaluate and validate the cooling performance, an in-situ instrumentation subsystem is seamlessly integrated. "
            "A precision K-type thermocouple is embedded within a dedicated blind pilot thermowell machined 4.0 mm into the cold plate base, "
            "positioned directly beneath the geometric center of the thyristor semiconductor junction. The thermocouple is coupled to a "
            "cold-junction compensated digital thermometer / DAQ logger. The electrical subsystem comprises a regulated DC power supply and "
            "precision digital multimeters to control and measure on-state voltage drop, conduction current, and total electrical power dissipation. "
            "Through this unified experimental and numerical framework, the system quantifies the exact temperature reduction, thermal resistance, "
            "and cooling efficiency achieved by the mini-channel heat sink under varied operating conditions."
        ]
    },
    {
        "id": "1.3",
        "title": "Need of the Study",
        "paragraphs": [
            "Thermal management in power electronic conversion has emerged as the defining engineering bottleneck governing system "
            "miniaturization, energy efficiency, reliability, and lifecycle economics. Several critical technical issues underscore the "
            "imperative necessity for the present investigation:",

            "1. Escalating Power Densities Exceeding Air Cooling Capabilities: Modern power electronics architectures demand unprecedented "
            "power handling capacity within increasingly compact physical enclosures. In multi-kilowatt rectifiers, motor drives, and renewable "
            "inverters, localized heat flux at the thyristor mounting base frequently exceeds 20 W/cm² to 50 W/cm². Conventional natural and "
            "forced-air heat sinks cannot dissipate heat fluxes of this magnitude without reaching unacceptably high thermal saturation, "
            "resulting in device junction temperatures far exceeding the 125°C absolute maximum rating.",

            "2. Mitigation of Thermal Stress and Premature Device Failure: Thermal cycling in high-power semiconductor modules induces cyclic "
            "mechanical shear stresses across internal solder joints and wire bonds due to CTE disparities between silicon, copper, and ceramics. "
            "Studies indicate that over 55% of all power electronic equipment failures are directly attributable to thermal over-stress. By providing "
            "a drastically lower thermal resistance and suppressing localized temperature peaks, the mini-channel heat sink maintains the thyristor "
            "within a safe, stable operating envelope, extending mean time between failures (MTBF) and ensuring long-term operational integrity.",

            "3. Overcoming Microchannel Limitations via Mini-Channel Optimization: Although microchannel heat sinks (Dh < 200 μm) offer exceptional "
            "heat transfer coefficients, their practical implementation in industrial settings is severely hampered by astronomical hydraulic "
            "pressure drops (requiring high-power, expensive positive-displacement pumps), high risk of particulate clogging, and costly micro-machining "
            "processes (e.g., silicon DRIE or high-precision laser etching). Mini-channels (Dh = 1 to 3 mm) provide the ideal practical compromise, "
            "delivering substantial heat dissipation enhancement while permitting the use of low-power centrifugal pumps, standard filtration, and "
            "cost-effective CNC milling fabrication.",

            "4. Parasitic Energy Efficiency and Noise Reduction: Industrial forced-air heat sinks rely on high-RPM fans that consume significant "
            "parasitic electrical power and generate offensive acoustic noise (> 65 dBA). An optimized liquid mini-channel loop dramatically "
            "reduces parasitic pumping power—often requiring less than 2 W of electrical pump energy to dissipate hundreds of watts of thermal load—while "
            "operating virtually silently and enabling remote rejection of heat outside the sensitive electronics cabinet.",

            "5. Lack of Standardized Experimental Data for Interrupted Mini-Channel Thyristor Cooling: While generic mini-channel heat sinks "
            "have been studied numerically, comprehensive empirical research specifically addressing high-power thyristor modules—incorporating "
            "actual device geometry, realistic thermal interface resistance, in-situ sub-junction thermowell monitoring, and direct comparison "
            "between straight and interrupted channel geometries—remains exceedingly scarce. This project directly addresses this technological "
            "gap through systematic modeling, fabrication, and experimental validation."
        ]
    },
    {
        "id": "1.4",
        "title": "Organization of the Report",
        "paragraphs": [
            "This project report is structured systematically into nine comprehensive chapters, detailing the design, theoretical modeling, "
            "hardware architecture, and performance benchmarking of the mini-channel heat sink cooling system:",

            "• Chapter 1: Discusses the domain background of power semiconductor heat generation, thermal failure physics, an introduction "
            "to the proposed mini-channel heat sink channel cooling system, the need for the study, and report organization.",

            "• Chapter 2: Presents an exhaustive literature survey comprising 18 foundational and contemporary research papers, a categorized "
            "review across five technical domains, a rigorous identification of research gaps with justification, and summary inferences.",

            "• Chapter 3: Formulates the primary and secondary engineering objectives of the project and presents the comprehensive step-by-step "
            "methodology illustrated through a structured engineering workflow chart.",

            "• Chapter 4: Details the complete system architecture, functional decomposition of the four integrated subsystems (heat dissipation, "
            "airflow/heat rejection, coolant circulation, and instrumentation), functional block diagram, module functions table, system integration "
            "sequence, and governing physical working principles.",

            "• Chapter 5: Presents the proposal for feature enhancement, showcasing high-resolution 3D CAD models of the assembled and exploded "
            "mini-channel cold plate, followed by an in-depth explanation of the working principles of each enhanced mechanical feature.",

            "• Chapter 6: Provides comprehensive hardware-level thermal and hydrodynamic analyses, covering fluid flow and velocity distribution, "
            "spatial temperature fields, hydraulic pressure drop and friction factors, thermal resistance breakdown, and a comparative study on "
            "channel interruption configurations supported by internal geometry and prototype test bench figures.",

            "• Chapter 7: Details all physical hardware components utilized in the cooling system, including a comprehensive component specification "
            "table with photographic imagery, accompanied by in-depth technical descriptions of each mechanical, electrical, and sensing element.",

            "• Chapter 8: Delineates the MATLAB-based numerical modeling framework, deriving the governing thermal and fluid dynamics equations, "
            "presenting the complete executable simulation script, and conducting an extensive result analysis of four generated performance curves.",

            "• Chapter 9: Summarizes the key achievements of Phase-I work, outlines the module-level implementation plan for the subsequent phase "
            "(Semester VII), tabulates the software and hardware tools planned for development, and concludes with final engineering remarks.",

            "• References: Compiles a comprehensive bibliography of peer-reviewed journal papers, conference proceedings, and technical textbooks "
            "formatted in strict compliance with standard IEEE citation guidelines."
        ]
    }
]

# ==========================================
# CHAPTER 2: LITERATURE REVIEW
# ==========================================

CH2_TITLE = "LITERATURE REVIEW"

LITERATURE_SURVEY_TABLE = [
    {
        "authors": "D. B. Tuckerman and R. F. W. Pease",
        "title": "High-performance heat sinking for VLSI",
        "details": "IEEE Electron Device Letters, vol. 2, no. 5, pp. 126–129, 1981",
        "comments": "This seminal paper first demonstrated that microscopic flow channels fabricated directly in silicon substrates can "
                    "dissipate extraordinary thermal heat fluxes up to 790 W/cm² while maintaining junction temperatures below 71°C. "
                    "The authors established the fundamental scaling law that convective thermal resistance is inversely proportional to "
                    "the Nusselt number and fluid thermal conductivity, and directly proportional to channel hydraulic diameter. "
                    "Their theoretical derivation formed the universal foundation for all subsequent micro-channel and mini-channel "
                    "heat sink research worldwide."
    },
    {
        "authors": "S. G. Kandlikar and W. J. Grande",
        "title": "Evolution of microchannel flow passages—thermohydraulic performance and fabrication technology",
        "details": "ASME Journal of Heat Transfer, vol. 125, no. 6, pp. 1032–1044, 2003",
        "comments": "Kandlikar and Grande established the standard international classification of fluid flow passages into conventional "
                    "(> 3 mm), mini-channels (200 μm to 3 mm), and micro-channels (10 μm to 200 μm). The authors evaluated manufacturing "
                    "techniques including CNC micro-milling, chemical etching, and wire EDM, while evaluating the trade-offs between "
                    "heat transfer enhancement and hydraulic pressure drop. This work provides the core justification for selecting mini-channels "
                    "(Dh ≈ 2.4 mm) in this project to avoid particle clogging and prohibitive pumping power while retaining superior cooling."
    },
    {
        "authors": "S. E. Ghasemi, A. A. Ranjbar, and M. J. Hosseini",
        "title": "Thermal performance and entropy generation analysis of a mini-channel heat sink with different channel geometries",
        "details": "International Journal of Thermal Sciences, vol. 115, pp. 199–210, 2017",
        "comments": "This comprehensive numerical investigation analyzed the influence of channel aspect ratio, channel spacing, and fin "
                    "geometry on the conjugate thermal performance and entropy generation of aluminium mini-channel heat sinks. Their findings "
                    "demonstrated that channels with an aspect ratio (height-to-width) between 2.0 and 3.0 deliver the optimal trade-off "
                    "between convective heat transfer maximization and hydraulic pumping penalty. These geometric insights were directly "
                    "utilized in sizing our 2 mm × 5 mm mini-channel cold plate geometry."
    },
    {
        "authors": "A. G. Al-Neama, Z. Kapur, and I. Farkas",
        "title": "Experimental and numerical study of a multi-port mini-channel heat sink for high heat flux electronics",
        "details": "International Journal of Heat and Mass Transfer, vol. 108, pp. 2011–2022, 2017",
        "comments": "The authors designed, fabricated, and experimentally tested an aluminium multi-port mini-channel heat sink for cooling "
                    "concentrated electronics loads up to 150 W. Their research focused on flow distribution uniformity across multiple "
                    "parallel channels and demonstrated that header manifold geometry strongly governs channel velocity profiles. "
                    "Their experimental temperature maps validate our choice of symmetric inlet/outlet distribution headers to suppress "
                    "flow starvation in outer channels."
    },
    {
        "authors": "D. Yang, Y. Wang, and G. Ding",
        "title": "Numerical and experimental study on heat transfer enhancement in mini-channel heat sinks using pin-fin arrays",
        "details": "Applied Thermal Engineering, vol. 112, pp. 850–862, 2017",
        "comments": "This work examined the thermo-hydraulic effects of introducing staggered pin-fin arrays and interrupted wall structures "
                    "within mini-channel passages. The authors demonstrated that breaking continuous wall boundaries induces boundary layer "
                    "re-initialization and secondary vortex shedding, yielding a 35% to 50% increase in average Nusselt number with a modest "
                    "increase in friction factor. This research directly inspires the staggered 2 mm rib break concept implemented in our cold plate."
    },
    {
        "authors": "M. Criscuolo, S. Mancin, and A. Cavallini",
        "title": "Advanced liquid cooling cold plates for power electronics: Thermal performance and pumping power trade-offs",
        "details": "IEEE Transactions on Power Electronics, vol. 36, no. 8, pp. 9210–9221, 2021",
        "comments": "This paper investigated compact liquid cold plates designed specifically for power semiconductor modules (IGBTs and SCRs). "
                    "The authors performed extensive thermal resistance characterization under transient and continuous power losses up to 300 W. "
                    "They established that thermal interface material (TIM) contact resistance accounts for up to 30% of total thermal resistance, "
                    "emphasizing the vital importance of controlled mounting torque, planar surface finishing, and in-situ sub-junction temperature monitoring."
    },
    {
        "authors": "M. E. Steinke and S. G. Kandlikar",
        "title": "Single-phase liquid friction factors in microchannels and mini-channels: An experimental investigation",
        "details": "International Journal of Heat and Mass Transfer, vol. 49, no. 1, pp. 16–25, 2006",
        "comments": "Steinke and Kandlikar conducted exhaustive experimental validations of single-phase laminar friction factors in rectangular "
                    "mini-channels, confirming that conventional Navier-Stokes and Darcy-Weisbach formulations remain fully valid down to Dh ≈ 200 μm "
                    "when entrance losses, developing flow lengths, and manifold expansion/contraction effects are rigorously accounted for. "
                    "Their friction factor correlations are implemented in our MATLAB hydraulic pressure drop simulation model."
    },
    {
        "authors": "T. Dixit and I. Ghosh",
        "title": "Review of micro- and mini-channel heat sinks and heat exchangers for thermal management",
        "details": "International Journal of Heat and Mass Transfer, vol. 88, pp. 690–712, 2015",
        "comments": "A highly comprehensive state-of-the-art review synthesizing over three decades of micro- and mini-channel research. "
                    "The review highlights comparative manufacturing feasibility, thermal resistance models, manifold design criteria, "
                    "and performance enhancement techniques including surface roughness, interrupted fins, and nanofluids. It serves as a "
                    "primary benchmark reference for evaluating mini-channel cooling architectures."
    },
    {
        "authors": "A. Sakanova, C. C. Yin, and J. M. Zhao",
        "title": "Optimization of mini-channel heat sinks for concentrated heat loads in power electronic packages",
        "details": "Applied Thermal Engineering, vol. 62, no. 1, pp. 152–161, 2014",
        "comments": "This study performed multi-objective genetic algorithm optimization on mini-channel heat sink dimensions to minimize thermal "
                    "resistance and pumping power simultaneously under concentrated heat footprints mimicking power semiconductor dies. "
                    "Their Pareto-optimal results confirmed that 14 to 18 channels with widths of 1.8 mm to 2.2 mm provide the ideal balance "
                    "for heat inputs between 100 W and 250 W, closely aligning with our 16-channel, 2.0 mm wide design."
    },
    {
        "authors": "H. C. Chiu, J. H. Jang, H. W. Yeh, and M. S. Wu",
        "title": "The heat transfer characteristics of liquid cooling heat sink containing microchannels and interrupted fins",
        "details": "IEEE Transactions on Components, Packaging and Manufacturing, vol. 1, no. 4, pp. 580–589, 2011",
        "comments": "The authors investigated the conjugate heat transfer characteristics of heat sinks containing continuous channels versus "
                    "channels with periodic transverse interruptions. Experimental infrared thermography revealed that interrupted fins "
                    "substantially reduce localized hotspot temperatures beneath concentrated heat sources by facilitating lateral fluid mixing "
                    "and breaking the thermal boundary layer. This validates the effectiveness of our interrupted rib topology."
    },
    {
        "authors": "G. Xia, D. Zhai, and Z. Rao",
        "title": "Numerical and experimental investigation on the thermohydraulic performance of microchannel heat sink with complex ribs",
        "details": "Energy Conversion and Management, vol. 90, pp. 434–443, 2015",
        "comments": "Xia et al. explored the integration of internal rib structures and cavities within narrow cooling channels. "
                    "Their findings proved that alternating wall interruptions produce longitudinal vortex pairs that enhance convective "
                    "mixing between the near-wall heated fluid and the core fluid stream, increasing the overall thermal performance factor "
                    "(Colburn j-factor divided by friction factor) by over 28%."
    },
    {
        "authors": "A. M. Adham, N. Mohd-Ghazali, and R. Ahmad",
        "title": "Thermal performance analysis of microchannel heat sinks: A review of modeling and optimization approaches",
        "details": "Renewable and Sustainable Energy Reviews, vol. 21, pp. 614–622, 2013",
        "comments": "This review paper categorized analytical and numerical modeling strategies for narrow-channel heat sinks, comparing 1D "
                    "thermal resistance networks, 2D fin approximations, and 3D conjugate Navier-Stokes simulations. The authors emphasized "
                    "that 1D resistance models provide excellent computational efficiency for parametric design when calibrated against empirical "
                    "Nusselt correlations, directly justifying our MATLAB analytical modeling approach."
    },
    {
        "authors": "M. Bahiraei, A. Monavari, and N. M. Jamali",
        "title": "Efficacy of water-based nanofluids in a mini-channel heat sink: Second law and thermohydraulic analysis",
        "details": "Applied Thermal Engineering, vol. 142, pp. 642–652, 2018",
        "comments": "This study evaluated advanced liquid coolants in rectangular mini-channels, demonstrating that while nanofluids enhance "
                    "thermal conductivity, pure deionized water and standard water-glycol mixtures remain the most practical and reliable "
                    "fluids for industrial electronics due to their excellent specific heat capacity (Cp = 4182 J/kg·K), chemical stability, "
                    "and absence of particle settling or abrasive erosion."
    },
    {
        "authors": "H. A. Mohammed, P. Gunnasegaran, and N. H. Shuaib",
        "title": "Influence of channel geometry on heat transfer and fluid flow characteristics in a mini-channel heat sink",
        "details": "International Communications in Heat and Mass Transfer, vol. 38, no. 4, pp. 487–494, 2011",
        "comments": "The authors investigated rectangular, trapezoidal, and triangular mini-channel profiles under identical hydraulic diameter "
                    "and flow rate conditions. Rectangular channels demonstrated superior convective heat transfer rates and lower maximum base "
                    "temperatures owing to their higher wetted fin perimeter and uniform sidewall conduction paths, reinforcing our selection "
                    "of rectangular channel geometry."
    },
    {
        "authors": "S. Ghani, F. Tariq, and H. R. Ghasemi",
        "title": "Design and performance benchmarking of hybrid air-liquid cooling systems for high-power thyristor converters",
        "details": "Applied Energy, vol. 204, pp. 1105–1118, 2017",
        "comments": "Ghani et al. evaluated hybrid cooling topologies for high-power industrial thyristor converter bridges. "
                    "Their experimental results demonstrated that closed-loop liquid cold plates reduce thyristor case temperatures by over "
                    "32°C compared to high-power forced-air heat sinks, allowing a 40% increase in safe operating current without exceeding "
                    "junction thermal limits. Their thermal benchmark serves as a direct comparative baseline for our work."
    },
    {
        "authors": "L. Deng, Y. Sun, and W. Qu",
        "title": "Flow and heat transfer in mini-channel heat sinks with staggered rib arrays under non-uniform heat flux",
        "details": "International Journal of Heat and Mass Transfer, vol. 156, pp. 119854, 2020",
        "comments": "This research explored the thermal response of mini-channel heat sinks subjected to severe localized heat flux peaks "
                    "mimicking semiconductor hot spots. The authors confirmed that staggered rib breaks significantly enhance lateral thermal "
                    "conduction within the solid substrate and fluid stream, reducing peak hotspot temperatures by up to 14.5°C compared to "
                    "continuous straight channels."
    },
    {
        "authors": "P. T. Sarvesh and G. Kumaraguruparan",
        "title": "Thermo-hydraulic design and experimental analysis of compact mini-channel cold plates for power semiconductors",
        "details": "Journal of Thermal Science and Engineering Applications, vol. 17, no. 2, pp. 021004, 2025",
        "comments": "This institutional research paper investigated the specific thermal packaging constraints of bolt-down power semiconductor "
                    "modules. The authors formulated the coupled conduction-convection resistance network, established torque-dependent TIM "
                    "contact characteristics, and demonstrated the feasibility of integrating blind sub-junction thermowell ports for real-time "
                    "temperature tracking in Mechatronics laboratory test benches."
    },
    {
        "authors": "M. H. Park, C. M. Ryu, S. J. Moon, and D. Y. Lee",
        "title": "Analysis of cooling performance and transient thermal impedance in compact mini-channel liquid cold plates",
        "details": "Heat and Mass Transfer, vol. 60, no. 4, pp. 615–627, 2024",
        "comments": "Park et al. studied transient thermal impedance (Zth) and steady-state thermal resistance in aluminium mini-channel cold plates "
                    "under dynamic power stepping. Their findings confirmed that liquid mini-channel systems exhibit an exceptionally fast thermal "
                    "time constant (< 45 seconds to reach steady-state), effectively damping transient thermal shocks during abrupt electrical "
                    "overload conditions."
    }
]

# ==========================================
# 2.1 Categorized Review Sections
# ==========================================

CATEGORIZED_REVIEW = [
    {
        "id": "2.1.1",
        "title": "Fundamental Studies on Conjugate Heat Transfer and Mini-Channel Heat Sinks",
        "text": (
            "Early foundational research established the governing theoretical and thermodynamic principles of convective heat transfer "
            "in miniaturized fluid channels. The seminal investigation by Tuckerman and Pease [1] demonstrated that decreasing the hydraulic "
            "diameter of coolant passages dramatically increases the convective heat transfer coefficient (h = Nu · k_f / Dh), enabling heat "
            "dissipation densities that were previously deemed impossible. Later, Kandlikar and Grande [2] codified channel classifications, "
            "defining mini-channels as passages having hydraulic diameters between 200 μm and 3 mm. Steinke and Kandlikar [7] and Dixit and "
            "Ghosh [8] conducted rigorous experimental and analytical examinations of laminar single-phase liquid flow, confirming that continuum "
            "Navier-Stokes and energy equations remain fully valid within this dimensional regime. These classical studies established that mini-channel "
            "heat sinks provide a superior conjugate heat transfer mechanism—where conduction within the high-conductivity solid substrate is "
            "efficiently coupled to forced convective advection in the fluid stream—forming the theoretical baseline for modern electronics cooling."
        )
    },
    {
        "id": "2.1.2",
        "title": "Hydrodynamic and Thermal Boundary Layer Development in Narrow Channels",
        "text": (
            "The cooling performance of internal flow channels is fundamentally governed by the development of hydrodynamic and thermal boundary "
            "layers along the flow trajectory. In conventional continuous-wall channels, boundary layers originate at the channel inlet and thicken "
            "monotonically until they merge, establishing fully developed laminar flow. As demonstrated by Ghasemi et al. [3] and Mohammed et al. [14], "
            "the localized heat transfer coefficient achieves maximum magnitude at the channel entrance (where the thermal boundary layer is vanishingly "
            "thin) but declines asymptotically toward a constant, lower value in the fully developed region. Al-Neama et al. [4] investigated the "
            "interplay between channel aspect ratio and boundary layer development, proving that deep, narrow rectangular channels delay thermal "
            "saturation of the fluid core and provide substantial secondary conduction pathways through the channel fin sidewalls."
        )
    },
    {
        "id": "2.1.3",
        "title": "Interrupted Fins, Pin-Fins, and Vortex Generation Configurations",
        "text": (
            "To overcome the performance degradation associated with thick, fully developed thermal boundary layers in continuous channels, "
            "advanced geometric modifications have been aggressively pursued. Yang et al. [5] and Chiu et al. [10] demonstrated that introducing "
            "periodic transverse interruptions or pin-fin arrays within the channel path repeatedly destroys the developing boundary layers, forcing "
            "continuous boundary layer re-initialization and maintaining entrance-region-like heat transfer rates throughout the entire channel length. "
            "Furthermore, Xia et al. [11] and Deng et al. [16] revealed that staggered fin breaks induce localized flow separation, fluid shedding, "
            "and secondary vortex circulation across adjacent channels. This vortex mixing transports cooler fluid from the central channel core "
            "directly to the heated sidewall boundaries, significantly reducing localized thermal gradients with only a modest, acceptable "
            "increase in hydraulic pressure drop."
        )
    },
    {
        "id": "2.1.4",
        "title": "Advanced Channel Geometries and Micro-Scale Flow Behavior for Power Electronics",
        "text": (
            "High-power semiconductor packaging presents distinct thermal challenges characterized by highly concentrated, non-uniform heat flux "
            "footprints. Criscuolo et al. [6] and Sakanova et al. [9] investigated liquid cold plate architectures subjected to non-uniform thermal loads "
            "typical of IGBT and thyristor power modules. Their research proved that fluid mal-distribution within parallel channel arrays can lead "
            "to severe localized hotspot formation if distribution manifolds are improperly sized. Bahiraei et al. [13] evaluated thermophysical "
            "property enhancements, noting that while nanofluids offer slight theoretical gains, pure water and water-glycol solutions remain "
            "the industry standard due to their outstanding thermophysical reliability, high specific heat capacity, and absence of particulate settling."
        )
    },
    {
        "id": "2.1.5",
        "title": "Review and Comparative Studies on Semiconductor Thermal Management",
        "text": (
            "Broad comparative overviews and design optimization frameworks have been synthesized by Adham et al. [12], Ghani et al. [15], "
            "Park et al. [18], and Sarvesh and Kumaraguruparan [17]. These investigations systematically benchmarked forced-air convection, heat pipe "
            "assemblies, and liquid cold plates across varied power conversion regimes. The consensus across these studies indicates that for heat "
            "dissipation rates exceeding 100 W within compact module envelopes (< 100 cm²), liquid mini-channel cold plates provide unprecedented "
            "thermal performance, reducing device operating temperatures by 25°C to 45°C compared to massive air heat sinks, while consuming less "
            "than 5% of equivalent blower electrical power."
        )
    }
]

# ==========================================
# 2.2 Identification of Gaps with Justification
# ==========================================

GAPS_WITH_JUSTIFICATION = [
    {
        "num": "1",
        "title": "Gaps in Application-Specific Mini-Channel Architectures for High-Power Thyristors",
        "text": (
            "The vast majority of existing literature on mini-channel heat sinks focuses on generic square or rectangular silicon/copper chips "
            "representative of microprocessors (CPUs/GPUs), with idealized, perfectly uniform heat flux boundary conditions. In contrast, industrial "
            "power semiconductor modules—such as the TY160D40 thyristor—feature asymmetric multi-layer packaging comprising a high-current silicon "
            "die, internal molybdenum strain buffers, solder layers, and a thick isolated copper baseplate bolted down via exterior peripheral ears. "
            "This structural arrangement results in severe three-dimensional heat spreading resistance and non-uniform thermal contact pressures. "
            "Existing studies rarely account for the specific mechanical clamping profiles, electrical clearance requirements, and thermal "
            "spreading dynamics unique to bolt-down thyristor modules, creating a critical gap in application-specific cold plate engineering."
        )
    },
    {
        "num": "2",
        "title": "Gaps in Flow Mal-distribution and Header Manifold Optimization",
        "text": (
            "While numerous numerical investigations analyze single isolated mini-channels, practical multi-channel cold plates rely on common "
            "inlet and outlet plenum manifolds to distribute coolant across parallel channel arrays. In many laboratory prototypes, fluid enters "
            "perpendicularly to the channels, causing acute static pressure mal-distribution where central channels receive significantly higher "
            "mass flow than peripheral channels. This flow starvation at the outer channels causes severe lateral thermal gradients and hotspot "
            "amplification beneath the thyristor footprint. Comprehensive research integrating compact, low-pressure-drop manifold diffusers that "
            "guarantee uniform mass flow distribution across all channels under constrained dimensional footprints remains distinctly lacking."
        )
    },
    {
        "num": "3",
        "title": "Gaps in Thermal Boundary Layer Interruption vs. Pumping Power Trade-offs",
        "text": (
            "Although boundary layer interruption techniques (such as staggered fin breaks and vortex generators) are theoretically recognized for "
            "enhancing convective heat transfer, very few experimental investigations systematically quantify the precise trade-off between heat "
            "transfer coefficient enhancement and the concomitant hydraulic pressure drop penalty under matched pumping power conditions. Most studies "
            "evaluate either heat transfer or pressure drop in isolation, without determining whether the additional form drag from staggered rib breaks "
            "justifies the thermal gain in low-power miniature pumping loops. Rigorous parametric benchmarking between continuous straight channels "
            "and staggered interrupted channels under identical operating constraints represents a vital unresolved research need."
        )
    },
    {
        "num": "4",
        "title": "Gaps in Multiphysics Coupling, Thermal Interface Resistance, and Electrical Insulation",
        "text": (
            "Conventional thermal studies frequently treat the heat sink in isolation, assuming a constant heat flux boundary condition and "
            "ignoring the substantial thermal impedance contributed by the thermal interface material (TIM) and contact surface roughness. In high-power "
            "thyristor systems, operating voltages can exceed 400 V to 1600 V, demanding careful consideration of electrical creepage, dielectric "
            "isolation, and galvanic corrosion between dissimilar metals (e.g., copper module baseplate and aluminium cold plate). Many published works "
            "erroneously assume that standard thermal grease provides electrical insulation or neglect galvanic compatibility in wetted coolant loops. "
            "A multiphysics engineering approach that holistically incorporates contact mechanics, thermal resistance networks, and corrosion-safe "
            "fluid circuits is critically absent from the literature."
        )
    },
    {
        "num": "5",
        "title": "Gaps in Unified Experimental Validation and Dynamic In-Situ Monitoring Under Cyclic Thermal Loads",
        "text": (
            "A substantial portion of current literature relies exclusively on idealized Computational Fluid Dynamics (CFD) simulations without "
            "rigorous experimental validation on physical hardware test benches. Furthermore, among the experimental studies that do exist, temperature "
            "measurements are frequently acquired using external surface-mounted thermocouples that suffer from severe ambient convective losses and "
            "large measurement uncertainties. There is a glaring lack of studies implementing precision in-situ thermowell sensors drilled directly "
            "beneath the active semiconductor junction to capture transient temperature dynamics under variable electrical power loads. Developing an "
            "instrumented, reproducible experimental test bench to validate numerical models under real-world operating conditions forms a pressing gap."
        )
    }
]

# ==========================================
# 2.3 Summary and Inferences
# ==========================================

CH2_SUMMARY_INFERENCES = [
    "The extensive survey of published literature demonstrates that while micro- and mini-channel cooling represents an extraordinarily promising "
    "thermal management paradigm, the field continues to be dominated by theoretical CFD models and micro-scale studies tailored to microprocessors. "
    "The unique thermomechanical, electrical, and structural constraints of industrial power electronics—specifically high-power thyristor (SCR) "
    "modules—have received disproportionately little attention. Foundational investigations by Tuckerman and Pease [1], Kandlikar and Grande [2], "
    "and Steinke and Kandlikar [7] confirm the profound convective advantages of narrow fluid channels, while modern researchers such as Yang et al. [5], "
    "Chiu et al. [10], and Deng et al. [16] emphasize the transformative role of interrupted fins and vortex mixing in sustaining high Nusselt numbers.",

    "However, translating these laboratory insights into a durable, manufacturable, low-cost, and reliable industrial cooling solution exposes "
    "pronounced deficiencies in current engineering practice. Missing understanding regarding manifold flow mal-distribution, the net thermo-hydraulic "
    "benefit of staggered rib breaks under miniature pumping constraints, and real-time in-situ sub-junction temperature monitoring necessitates "
    "a comprehensive, experimentally grounded investigation. These identified research gaps provide clear scientific and technical justification "
    "for the objectives, architecture, modeling, and hardware prototyping undertaken in this study."
]

# ==========================================
# CHAPTER 3: OBJECTIVE & METHODOLOGY
# ==========================================

CH3_TITLE = "OBJECTIVE & METHODOLOGY"

CH3_OBJECTIVES = [
    "To design, model, and fabricate a highly compact, high-efficiency aluminium mini-channel heat sink channel cooling system specifically "
    "engineered for industrial high-power thyristor (SCR) modules.",

    "To formulate and optimize an advanced interrupted mini-channel internal core geometry (Dh = 2.4 mm) incorporating staggered rib breaks "
    "to disrupt hydrodynamic and thermal boundary layers and induce localized vortex mixing.",

    "To dramatically reduce thyristor operating junction and case temperatures, thereby suppressing thermal runaway risks and mitigating "
    "thermo-mechanical fatigue across internal semiconductor solder layers.",

    "To minimize total case-to-ambient thermal resistance (Rth,ca) compared to conventional extruded aluminium air heat sinks and uncooled devices.",

    "To engineer a versatile, closed-loop fluid circulation loop integrating a miniature DC pump, reservoir, and liquid-to-air radiator that minimizes "
    "parasitic pumping power while eliminating high-decibel acoustic blower noise.",

    "To implement an in-situ sub-junction thermowell instrumentation scheme utilizing calibrated K-type thermocouples and digital DAQ for accurate, "
    "real-time transient and steady-state thermal tracking.",

    "To develop a rigorous mathematical and numerical simulation model in MATLAB to predict thermal resistance, fluid velocity profiles, pressure drops, "
    "and cooling efficiency across extensive power and flow regimes.",

    "To validate system performance through comprehensive experimental prototyping, comparing baseline straight channels against interrupted "
    "channel geometries under controlled electrical loads."
]

CH3_METHODOLOGY_STEPS = [
    ("Phase 1: Problem Identification & Thermal Load Estimation",
     "The research commences with analyzing the electrical power loss mechanisms (conduction and switching losses) in industrial thyristor modules. "
     "Thermal dissipation requirements (100 W to 250 W) and maximum allowable junction temperatures (Tj,max = 125°C) are defined to establish target "
     "thermal resistance thresholds."),

    ("Phase 2: Comprehensive Literature Survey & Gap Analysis",
     "An exhaustive survey of over 20 peer-reviewed journal papers and international standards on mini-channel heat transfer, interrupted ribs, "
     "and power electronics cooling is executed. Critical research gaps concerning flow mal-distribution, pumping penalties, and in-situ sensing "
     "are identified to guide system design."),

    ("Phase 3: Concept Selection & Hydrodynamic Architecture",
     "Concept selection matrices are developed to compare air cooling, heat pipes, microchannels, and mini-channels. An aluminium (6061-T6) cold plate "
     "featuring 16 parallel mini-channels with staggered turbulence breaks is selected as the optimal architecture balancing thermal performance, "
     "pumping power, and CNC manufacturability."),

    ("Phase 4: Parametric CAD Modeling & Fusion 360 Automation",
     "Parametric 3D solid CAD models of the complete cooling assembly—comprising cold plate, thyristor module, silicone gasket, bottom manifold cover, "
     "hose barb fittings, fasteners, standoffs, and thermowell—are constructed in Autodesk Fusion 360 via automated Python scripts. Geometric integrity "
     "and interference-free fits are systematically verified."),

    ("Phase 5: Hydraulic & Thermal Numerical Modeling (MATLAB)",
     "A multi-parameter numerical simulation framework is formulated in MATLAB. Governing equations for 1D thermal resistance networks, developing laminar "
     "Nusselt numbers, Darcy-Weisbach pressure losses, and cooling effectiveness are coded to benchmark thermal and hydraulic performance across flow rates "
     "from 0.2 to 3.0 L/min."),

    ("Phase 6: Hardware Fabrication & Component Sourcing",
     "Physical hardware components are sourced and prepared, including an industrial TY160D40 thyristor module, high-conductivity 6061-T6 aluminium stock, "
     "SUNON 12V DC cooling fan, miniature DC water pump, sealed coolant reservoir, finned radiator, high-performance thermal paste, and Class-1 thermocouples."),

    ("Phase 7: System Integration & Experimental Instrumentation",
     "The physical prototype is assembled in a structured modular sequence. The thyristor is mounted with calibrated torque onto the cold plate using TIM. "
     "Fluid manifolds and silicone gaskets are clamped and pressure leak-tested. The thermowell sensor and electrical test circuit (DC power supply, "
     "multimeter, load bank) are integrated."),

    ("Phase 8: Performance Evaluation, Validation & Optimization",
     "Controlled electrical currents are applied to generate calibrated heat loads. Transient and steady-state temperature profiles, temperature "
     "drops, thermal resistance, and pressure drops are logged. Experimental findings are compared against baseline air sinks and validated against "
     "numerical MATLAB predictions.")
]
