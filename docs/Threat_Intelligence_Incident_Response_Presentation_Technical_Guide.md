# Threat Intelligence and Incident Response — Presentation Technical Guide
**Live Keynote Application & Instructional Facilitator System with Advanced Motion & 3D Engineering**

---

### Executive Overview & Training Profile
- **Course Title:** Threat Intelligence and Incident Response
- **Venue:** LH3 – 4th Floor (Equipped with 24 High-Performance SOC Analyst Workstations & High-Lumen Dual Laser Projector)
- **Scheduled Dates:** 26–31 October 2026
- **Instructional Volume:** 6 Operational Days | 26.50 Gross Hours | 23.42 Net Teaching Hours (1,405 Net Minutes)
- **Target Audience:** Indian Engineering & Computer Science College Students (specialized pedagogical alignment for Kerala & South Indian cohorts)
- **Primary Deliverables:**
  - Threat_Intelligence_Incident_Response_Animated_Presentation/index.html (Master Portal & Launchpad)
  - day-01/index.html through day-06/index.html (6 Day-Wise Interactive Keynote Presentations)
  - shared/js/characters.js (Cyber Cartoon Mascots & Expressive Reactions)
  - shared/js/cyber-3d.js (Three.js WebGL Interactive 3D Scenes)
  - shared/js/gsap-narratives.js (GSAP Animation Pipelines & Simulations)

---

## 1. System Architecture & Directory Structure

The upgraded presentation suite is built on an enterprise-grade, offline-first presentation framework combining Reveal.js v5.1.0, GSAP v3.12.5, Three.js r128 UMD, and SVG mascot engines.

`
Threat_Intelligence_Incident_Response_Animated_Presentation/
├── index.html                   # Master presentation portal with mascot showcase & system readiness
├── day-01/index.html            # Day 1: CTI Fundamentals (17 slides, 3D Globe, Intel Cycle)
├── day-02/index.html            # Day 2: Threat Modeling & ATT&CK (11 slides, 3D Defense Mesh)
├── day-03/index.html            # Day 3: OSINT & STIX/TAXII (11 slides, Evidence Robot, JSON Inspector)
├── day-04/index.html            # Day 4: Multi-Source Telemetry (12 slides, Telemetry Correlator)
├── day-05/index.html            # Day 5: NIST IR & Forensics (12 slides, Volatile Memory Ladder)
├── day-06/index.html            # Day 6: Capstone, Phishing & AeroGrid (15 slides, Phishing Dissector, 3D Shield, Air-Gap Breaker)
├── shared/
│   ├── css/
│   │   ├── reset.css            # CSS normalization baseline
│   │   ├── reveal.css           # Core Reveal.js presentation layout engine
│   │   ├── theme-cyber-soc.css  # Dark Cyber-SOC military command palette & typography
│   │   ├── animations.css       # Hardware-accelerated radar sweeps & pulse keyframes
│   │   └── interactive-experiences.css # Styles for 3D canvases, mascots, and GSAP narratives
│   └── js/
│       ├── reveal.js            # Reveal.js v5.1.0 presentation engine (offline-ready)
│       ├── gsap.min.js          # GSAP v3.12.5 timeline and tween engine (bundled locally)
│       ├── three.min.js         # Three.js r128 UMD WebGL renderer (bundled locally)
│       ├── characters.js        # SVG/CSS Cyber Mascot Engine (Detective, Alert Bot, Guardian, etc.)
│       ├── cyber-3d.js          # Three.js 3D Viewport Controllers (Globe, Mesh, Shield)
│       ├── gsap-narratives.js   # GSAP Narrative Pipelines & Interactive Simulators
│       └── presentation-app.js  # Presentation controller, HUD teleprompter & telemetry sync
└── previews/
    └── animated_redesign_inspect.webp # Full recorded browser session validating 100% functionality
`

---

## 2. Dependency Register & Offline Compatibility

The presentation is engineered to function **100% offline without internet dependency**. All critical styles, scripts, libraries, and layout engines are locally bundled.

| Dependency Component | Version | Source Location | Operational Purpose | Offline Fallback Strategy |
| :--- | :--- | :--- | :--- | :--- |
| **Reveal.js Engine** | v5.1.0 | shared/js/reveal.js | Slide navigation, fragment transitions, keyboard events, slide scaling | Local bundled JS (92.5 KB); zero CDN requests required |
| **GSAP Animation Core** | v3.12.5 | shared/js/gsap.min.js | Coordinated timeline reveals, progressive flow animations, alert staggering | Local bundled JS (72.9 KB); zero external CDN requests |
| **Three.js WebGL Engine** | r128 UMD | shared/js/three.min.js | Hardware-accelerated 3D viewports (Threat Globe, Defense Mesh, Cryptographic Shield) | Local bundled UMD JS (603 KB); WebGL error handling with CSS fallbacks |
| **Cyber Mascot Engine** | Custom | shared/js/characters.js | Procedural SVG vector mascots with expressive reactions (Alert, Thinking, Success) | Pure inline SVG vector rendering; zero external image assets required |
| **Cyber 3D Scenes** | Custom | shared/js/cyber-3d.js | Orbit-controlled interactive 3D spheres, wireframe meshes, and lighting | Dynamically attached to slide change events; auto-pause on inactive slides |
| **GSAP Narratives** | Custom | shared/js/gsap-narratives.js | Phishing dissector, 6-stage Intel Cycle, telemetry correlation, SCADA breaker | Pure JavaScript event-driven pipelines with instant user feedback |
| **Cyber-SOC Theme** | v2.0.0 | shared/css/theme-cyber-soc.css | Military command center dark palette, glassmorphism cards, terminal buffers | Custom local CSS authored directly in workspace |
| **Interactive Styles** | v1.0.0 | shared/css/interactive-experiences.css | 3D canvas containers, hotspot pins, breaker switches, character speech callouts | Hardware-accelerated transitions; zero CSS frameworks required |
| **Facilitator HUD** | v2.0.0 | shared/js/presentation-app.js | Real-time teleprompter drawer parsing SHOW, SAY, DO, OBSERVE, ASK, REVEAL | Pure ES6 JavaScript; handles slide-in HUD on keypress 'S' |

---

## 3. Cyber Mascot Engine Specification

To balance technical rigor with engaging visual storytelling for Indian engineering students, five original SVG-based cybersecurity mascots are procedurally rendered:

1. **Threat Detective (ThreatDetective):**
   - *Visual Identity:* Deep charcoal trenchcoat, angled fedora, cyan glowing holographic visor, and interactive magnifying glass.
   - *Pedagogical Role:* Leads investigations, inspects anomalous headers, highlights suspicious indicators, and asks probing questions.
   - *Interactive States:* Idle scan, inspecting evidence (magnifying glass pulsed over artifact), and discovery eureka.
2. **Alert Bot (AlertBot):**
   - *Visual Identity:* Rugged spherical telemetry droid with antenna beacon, rotating radar ear, and glowing dual optic lenses.
   - *Pedagogical Role:* Reacts to incoming SIEM alerts, illustrates alert fatigue, and differentiates true positives from benign telemetry noise.
   - *Interactive States:* Green monitoring pulse, amber triage state, and red flashing emergency alert.
3. **Security Guardian (SecurityGuardian):**
   - *Visual Identity:* Armored defender with faceted crystalline breastplate, neon cyan visor, and glowing cryptographic shield.
   - *Pedagogical Role:* Illustrates defensive controls, zero-trust boundary verification, and enterprise hardening.
   - *Interactive States:* Defending posture, shield activation pulse, and policy enforcement confirmation.
4. **Phishing Impostor (PhishingImpostor):**
   - *Visual Identity:* Shrouded hooded adversary with disguised business suit collar, glowing crimson eyes, and a dangling barbed hook concealed in an email envelope.
   - *Pedagogical Role:* Personifies social engineering deception, urgency manipulation, and domain typosquatting.
   - *Interactive States:* Sneak posture, lure deployment, and exposed/caught state upon student dissection.
5. **Evidence Robot (EvidenceRobot):**
   - *Visual Identity:* Heavy-duty forensics droid with magnetic specimen clamps, volatile RAM storage chamber, and holographic scanner bar.
   - *Pedagogical Role:* Enforces the RFC 3227 order of volatility, chain-of-custody logging, and cryptographic hash verification.
   - *Interactive States:* Scanning telemetry, locking evidence container, and verifying SHA-256 integrity.

---

## 4. Interactive 3D & GSAP Narratives

### A. 3D Threat Globe (
enderThreatGlobe)
- *Location:* Day 01, Slide 10 (Adversary Infrastructure & Global C2 Routing).
- *Implementation:* Three.js particle wireframe sphere with latitude/longitude lines, pulsating C2 nodes, and animated Great-Circle telemetry arcs tracing attacker traffic across continents.
- *Interactivity:* Mouse drag or touch orbit controls allow students to rotate the globe and inspect offshore bulletproof hosting clusters.

### B. 6-Stage Intelligence Cycle Pipeline (initIntelCycle)
- *Location:* Day 01, Slide 11 (CTI Operational Lifecycle).
- *Implementation:* GSAP-coordinated horizontal pipeline featuring Direction &rarr; Collection &rarr; Processing &rarr; Analysis &rarr; Dissemination &rarr; Feedback.
- *Interactivity:* Clicking any stage animates the progress track, highlights active dependencies, and updates the technical inspection panel with real-world SOPs.

### C. 3D Enterprise Defense Mesh (
enderDefenseMesh)
- *Location:* Day 02, Slide 06 (MITRE ATT&CK Defense-in-Depth Topology).
- *Implementation:* Layered Three.js nodal mesh demonstrating perimeter firewalls, DMZ, Active Directory domain controllers, and internal server segments.
- *Interactivity:* Drag-to-rotate viewport exposing how attackers pivot laterally through unmonitored trust boundaries.

### D. Multi-Source Telemetry Correlator (initTelemetryCorrelator)
- *Location:* Day 04, Slide 07 (Multi-Source Telemetry Pivoting).
- *Implementation:* GSAP-driven triage simulation correlating disparate event sources: Network Zeek conn.log &rarr; Identity Kerberos Event 4768 &rarr; Endpoint Sysmon Event 1 (Process Creation).
- *Interactivity:* Clicking 'EXECUTE CROSS-SOURCE CORRELATION' animates a glowing photon pulse across data streams, assembling the unified kill chain in real time.

### E. RFC 5322 Phishing Email Dissector (initPhishingDissector)
- *Location:* Day 06, Slide 02 (Phishing Email Header Analysis).
- *Implementation:* Interactive synthetic email viewer with clearly marked hotspots:
  - Spoofed Display Name (CEO <attacker@evil-domain.com>)
  - Authentication Mismatch (SPF=fail, DKIM=none, DMARC=reject)
  - Artificial Urgency Cue (*'WIRE IMMEDIATELY WITHIN 30 MINUTES'*)
  - Malicious Macro Attachment (Invoice_Q3.xlsm)
- *Interactivity:* Clicking any hotspot triggers an instant Threat Detective investigation badge explaining the operational significance and defense countermeasures.

### F. 3D Cryptographic Defense Shield (
enderSecurityShield)
- *Location:* Day 06, Slide 05 (Incident Containment Architecture).
- *Implementation:* Faceted 3D shield model rendered in Three.js with metallic iridescence and rotating orbital rings representing layered defense controls.

### G. AeroGrid SCADA Air-Gap Breaker Simulator (initAeroGridBreaker)
- *Location:* Day 06, Slide 09 (AeroGrid ICS/SCADA Tabletop Crisis).
- *Implementation:* Interactive industrial isolation breaker switch controlling network bridging between enterprise IT and substation OT.
- *Interactivity:* Clicking the switch triggers a mechanical sound effect, shifts the status badge from red 'COMPROMISED (IT PROPAGATION)' to green 'ISOLATED (OT GRID SAFE)', and updates the incident response decision matrix.

---

## 5. Facilitator HUD & Verbatim Script Teleprompter

Pressing **S** on any slide opens the integrated **Facilitator HUD teleprompter drawer**. The HUD parser has been upgraded to format structured classroom delivery cues with dedicated high-contrast badges:

- [SHOW:] &rarr; Cyan badge indicating what visual element or animation should be displayed.
- [SAY:] &rarr; Yellow badge displaying the verbatim spoken dialogue, complete with culturally resonant Indian classroom analogies (Bangalore traffic, canteen filter coffee vs. instant tea, Onam feast discipline).
- [DO:] &rarr; Magenta badge instructing the trainer on exact mouse clicks, button toggles, or terminal commands.
- [OBSERVE:] &rarr; Green badge detailing what students should see happen on screen.
- [ASK:] &rarr; Blue badge providing Socratic inquiry questions to pose to the class.
- [EXPECTED ANSWER:] &rarr; Violet badge indicating the ideal student response.
- [REVEAL:] &rarr; Orange badge indicating when to click the reveal button to show the solution.
- [EXPLAIN:] &rarr; Purple badge providing deeper technical context and authoritative handbook citations.

---

## 6. Classroom Keyboard Controls & Navigation

| Keybinding | Action | Functional Description |
| :--- | :--- | :--- |
| **Spacebar** / **&rarr;** | Next Slide / Reveal | Advances forward to the next slide or reveals the next bullet/card fragment. |
| **&larr;** / **Page Up** | Previous Slide | Navigates backwards to the preceding slide. |
| **S** | **Toggle Facilitator HUD** | Opens/closes the slide-out teleprompter drawer with structured delivery badges. |
| **F** | **Full-Screen Keynote** | Enters/exits browser fullscreen mode (1920x1080 display lock). |
| **1** to **6** | Day Jump (Acts 1–6) | Instantly jumps to the launch slide of Day 1 through Day 6. |
| **?** or **H** | Shortcuts Cheat Sheet | Toggles the modal overlay displaying all classroom keybindings. |
| **Esc** | Close Overlays | Closes any open modal overlay or the Facilitator HUD drawer. |

---

## 7. Display Calibration & Performance Tuning

- **Base Resolution:** 1280 &times; 720 (16:9 widescreen ratio) with automatic aspect ratio scaling up to 4K UHD and down to 1024 &times; 768.
- **Hardware Acceleration:** All 3D canvases use requestAnimationFrame throttling; rendering pauses automatically when a slide is inactive to preserve laptop battery and prevent GPU overheating.
- **High-Contrast Dark Theme:** Calibrated specifically for high-lumen laser projectors in LH3 – 4th Floor. Text contrast exceeds **7.2:1** against deep space navy.
- **Reduced Motion Support:** Respects operating system accessibility settings (prefers-reduced-motion: reduce), instantly replacing animated transitions with instant visibility toggles.

---
*Technical Guide authored by the Chief AI Knowledge Architect & Frontend Motion Lead | Threat Intelligence and Incident Response Training Program | Venue: LH3 – 4th Floor.*
