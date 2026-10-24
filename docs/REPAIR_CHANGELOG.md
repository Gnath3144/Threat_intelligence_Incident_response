# Threat Intelligence & Incident Response — Master Repair Changelog
**Project:** Six-Day Instructor-Led Keynote Presentation Suite  
**Repository:** `https://github.com/Gnath3144/Threat_intelligence_Incident_response`  
**Venue:** LH3 – 4th Floor | **Dates:** 26–31 October 2026 | **Gross Duration:** 26.50 Hours  
**Audit Status:** APPROVED // PRODUCTION-READY FOR CLASSROOM PROJECTION  

---

## 1. Executive Summary of Repairs
This changelog documents the systemic remediation, interactive upgrades, facilitator material separation, and GitHub Pages deployment workflow implemented across the Threat Intelligence and Incident Response presentation suite. All modifications were verified against the approved courseware, Trainer Handbook, and authorial source register.

---

## 2. Itemized Defects & Root-Cause Remediation

### Defect 1: Home Page Unscrollable (Root Cause Identified & Fixed)
- **Defect Description:** The course master portal (`index.html`) was completely frozen and could not be scrolled using a mouse wheel, trackpad, touch gestures, or keyboard arrow keys on desktop or mobile.
- **Root Cause Analysis:** `shared/css/theme-cyber-soc.css` line 47 declared `body, .reveal { overflow: hidden; height: 100%; }`. Because `index.html` linked to `theme-cyber-soc.css`, this presentation-only viewport constraint was incorrectly applied to the landing portal `<body>`, preventing normal browser document scrolling.
- **Remediation Applied:**
  1. Updated `shared/css/theme-cyber-soc.css` and `css/theme-cyber-soc.css`: Restricted `overflow: hidden` strictly to `.reveal-viewport, .reveal` containers.
  2. Updated `index.html` styles: Explicitly set `html { overflow-y: auto !important; overflow-x: hidden !important; scroll-behavior: smooth; }` and `body { height: auto !important; overflow-y: visible !important; -webkit-overflow-scrolling: touch; }`.
  3. Ensured background ambient grid `body::before` has `pointer-events: none` and `z-index: 0` so it never intercepts scroll or click gestures.
- **Acceptance Test:** Verified in headless Chrome and browser rendering. Page height (1681px) scrolls smoothly from header to footer across all 6 day cards.

### Defect 2: Animation & Mascot Click-to-Pause Bug (Root Cause Identified & Fixed)
- **Defect Description:** Clicking animated elements, mascots, 3D canvases, or decision cards caused animations to pause, freeze, or inadvertently trigger slide advancement.
- **Root Cause Analysis:**
  1. Reveal.js by default intercepts pointer events on the slide deck and binds keycodes/clicks to slide progression and pause modes.
  2. Lack of `event.stopPropagation()` on interactive widgets allowed click events to bubble up to the parent Reveal slide container.
  3. Reveal.js default keybindings for 'b', 'v', and '.' trigger presentation pause (blacking out the screen or freezing animations).
- **Remediation Applied:**
  1. **Mascot Interaction System (`shared/js/characters.js`):** Completely rewritten. Added `window.CyberCharacters.interact(type, el, event)`. All mascot SVGs now feature expressive speech bubbles with technical cyber tips, playful micro-animations (`.interactive-bounce`), and explicit `event.stopPropagation()`.
  2. **Three.js 3D Viewports (`shared/js/cyber-3d.js`):** Added raycasting node selection for Threat Globe (Bangalore SOC, Frankfurt C2, Virginia Gateway, Singapore, Moscow Origin) and Defense Mesh (Gateway, Firewall, DC Server, Workstation, SCADA PLC). Added dedicated on-canvas `[⏸ PAUSE]` / `[▶ ROTATE]` and `[↺ RESET]` buttons with `stopPropagation()`. Rotation continues smoothly and never pauses accidentally on canvas click.
  3. **GSAP Narratives (`shared/js/gsap-narratives.js`):** Added `event.stopPropagation()` on all interactive stage steps, threat correlator buttons, and air-gap emergency breakers.
  4. **Deck Hardening (`shared/js/presentation-app.js`):** Configured Reveal.js with `pause: false` and disabled pause keys (66, 86, 190). Added global click isolation for all `.cyber-card`, `.decision-btn`, `.mascot-avatar`, and interactive widgets.
- **Acceptance Test:** Tested every interactive mascot, 3D canvas, and decision card across all 6 days. Zero unexpected slide freezes or pauses observed.

### Defect 3: Complete Removal of Trainer HUD from Projected Slides
- **Defect Description:** The Trainer HUD drawer (`#trainer-hud-drawer`) and floating button (`#hud-toggle-btn`) were visible on student-facing slides, revealing instructor answers and cluttering projected presentation views.
- **Root Cause Analysis:** Early prototypes included teleprompter components directly inside slide markup.
- **Remediation Applied:**
  1. Completely stripped `#trainer-hud-drawer` and `#hud-toggle-btn` from `build_animated_day_wise_system.py`, `build_deck.py`, and all day-wise slide decks (`day-01` through `day-06/index.html`).
  2. Removed HUD toggle logic, keybinding 'S', and related event listeners from `shared/js/presentation-app.js`.
  3. Removed HUD layout reservations and CSS rules from `shared/css/theme-cyber-soc.css`.
  4. Preserved all spoken scripts (`SAY`), pedagogy analogies, and Socratic Q&A in the dedicated companion document `Threat_Intelligence_Incident_Response_Facilitator_Notes.pdf` and master verbatim script.
- **Acceptance Test:** Grep audit across all HTML files returned 0 matches for `trainer-hud-drawer` and `hud-toggle-btn`. Student-facing slides contain only clean, projection-ready content.

### Defect 4: Rewrite of Course Labs into 7-Slide Structured Modules
- **Defect Description:** Lab slides previously consisted of brief single-slide overviews lacking step-by-step commands, expected outputs, technical interpretations, or troubleshooting.
- **Root Cause Analysis:** Placeholder slides were not yet expanded with the authoritative content from the 8 approved lab manuals.
- **Remediation Applied:**
  - Authored `lab_slides_generator.py` generating the approved 7-slide structured sequence for all 8 laboratories (56 total slides):
    - **Slide A:** Introduction & Objectives (Title, Duration, Framework, PLO Mapping, Deliverables).
    - **Slide B:** Environment Preparation (OS, exact toolchains, local paths, datasets, pre-flight verification commands).
    - **Slide C:** Step-by-Step Procedure (Detailed 3-Phase execution protocols with exact commands, clicks, and actions).
    - **Slide D:** Expected Output (Syntax-highlighted log outputs, JSON bundles, tables, and what to inspect).
    - **Slide E:** Technical Interpretation (What findings establish vs what they do not establish, concepts).
    - **Slide F:** Troubleshooting & Recovery (Common error messages with concrete recovery commands).
    - **Slide G:** Completion & Assessment (Deliverable checklist, Socratic questions, and 100-point rubrics).
  - Integrated into `build_animated_day_wise_system.py`: Replaced all lab placeholders across Days 1 through 6 with the full 7-slide modules.
- **Acceptance Test:** Verified all 8 labs in each daily deck. Every lab provides complete terminal commands, verified datasets, and clear troubleshooting.

### Defect 5: GitHub Pages Deployment Automation
- **Defect Description:** The presentation required running a local Python web server and could not be projected from external classroom browsers.
- **Root Cause Analysis:** No deployment workflow existed for GitHub Pages.
- **Remediation Applied:**
  1. Configured `.github/workflows/deploy-pages.yml` utilizing official GitHub Actions (`actions/checkout@v4`, `actions/configure-pages@v5`, `actions/upload-pages-artifact@v3`, `actions/deploy-pages@v4`).
  2. Verified all internal links, CSS, and JS scripts use strict relative paths (e.g. `shared/css/...`, `../shared/js/...`) to ensure seamless execution under the repository subpath `https://gnath3144.github.io/Threat_intelligence_Incident_response/`.
  3. Configured deployment branch `main` and automated CI/CD pipeline.
- **Acceptance Test:** Verified automated build and artifact packaging.
