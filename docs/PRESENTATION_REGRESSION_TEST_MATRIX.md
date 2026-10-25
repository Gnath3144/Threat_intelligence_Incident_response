# Presentation Regression Test Matrix
**Course:** Threat Intelligence & Incident Response — Live Animated Classroom Keynote System  
**Test Engine:** Playwright Headless Chromium Suite (`run_full_presentation_regression.py`)  
**Test Date:** Sunday, 25 October 2026  
**Status Key:**
- `PASS`: Interactive component responded to action with correct state update and without layout collision or navigation side-effect.
- `FAIL`: Execution error, unclickable hitbox, or broken visual state.
- `NOT TESTED`: Out of scope or untestable in current environment.
- `BLOCKED`: Dependency unavailable.

---

## 1. Master Portal Regression Results

| Scope / Component | Viewport | Action Tested | Expected Output | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Master Portal Header** | 1920×1080 | Page Load | Title rendered, 3D particle canvas initialized | **PASS** |
| **Day 01–06 Launch Cards** | 1920×1080 | Element Query | All 6 daily keynote launch cards rendered | **PASS** (6/6) |
| **Governance Document Links** | 1920×1080 | Hyperlink Check | 5 documentation buttons point to valid paths | **PASS** (5/5) |
| **Master Portal Header** | 1366×768 | Page Load | Grid cards wrap cleanly to 3 columns | **PASS** |
| **Master Portal Header** | 1024×768 | Page Load | Grid cards wrap to 2 columns | **PASS** |
| **Master Portal Header** | 375×667 | Page Load | Grid cards stack single-column, zero horizontal scroll | **PASS** |

---

## 2. Multi-Viewport Daily Presentation Regression Matrix

### A. 1080p Desktop Kiosk (1920 × 1080)

| Day | Slide # | Interactive Component | Action Tested | Output / State Observed | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Day 01** | Global | Shortcuts Modal | Click `KEYS [?]` | Modal overlay displayed with keybindings table | **PASS** |
| **Day 01** | Global | Shortcuts Modal Close | Click `CLOSE SHORTCUTS` | Modal hidden; returns focus to slide | **PASS** |
| **Day 01** | 06 | Dormitory Incursion Dilemma | Click Option B (`.decision-btn`) | Feedback rendered: "Correct! Query passive DNS..." | **PASS** |
| **Day 01** | 11 | 6-Stage Intelligence Cycle | Click Stage 3 ("Processing") | Node active; GSAP progress bar animates to 50% | **PASS** |
| **Day 01** | 12 | NATO Indicator Station | Click IP Pill (`198.51.100.44`) | Detail panel renders Admiralty rating `B2` + context | **PASS** |
| **Day 01** | 13 | Caltagirone Diamond Model | Click Adversary Vertex | Node glow active; renders Threat Actor Nexus details | **PASS** |
| **Day 01** | 13 | Caltagirone Diamond Model | Click Capability Vertex | Node glow active; renders Tools & Exploits details | **PASS** |
| **Day 01** | 13 | Caltagirone Diamond Model | Click Infrastructure Vertex | Node glow active; renders C2 & Transit details | **PASS** |
| **Day 01** | 13 | Caltagirone Diamond Model | Click Victim Vertex | Node glow active; renders Target Assets details | **PASS** |
| **Day 01** | 13 | Caltagirone Diamond Model | Click Intrusion Event Hub | Hub glow active; renders Core Intrusion Hub & pivots | **PASS** |
| **Day 01** | 22 | Analytical Checkpoint | Click Option B (`.decision-btn`) | Feedback: "Correct! On shared cloud infrastructure..." | **PASS** |
| **Day 02** | Global | Shortcuts Modal | Click `KEYS [?]` / Close | Modal opens and closes properly | **PASS** |
| **Day 02** | 03 | Threat Triage Dilemma | Click Alert B (`triage-alert-card`) | Card selected; feedback panel displays Critical rating | **PASS** |
| **Day 02** | 16 | Pyramid of Pain Checkpoint | Click Option B (`.decision-btn`) | Feedback: "Correct! Changing a hash costs zero effort..." | **PASS** |
| **Day 03** | Global | Shortcuts Modal | Click `KEYS [?]` / Close | Modal opens and closes properly | **PASS** |
| **Day 03** | 16 | STIX 2.1 Schema Checkpoint | Click Option A (`.decision-btn`) | Feedback: "Correct! STIX 2.1 uses standard JSON..." | **PASS** |
| **Day 04** | Global | Shortcuts Modal | Click `KEYS [?]` / Close | Modal opens and closes properly | **PASS** |
| **Day 04** | 04 | Sysmon EID 1 Log Inspector | Click `CommandLine` Hotspot | Explanation drawer updates with LOLBin analysis | **PASS** |
| **Day 04** | 17 | LOLBins Masquerading Check | Click Option B (`.decision-btn`) | Feedback: "Correct! When Word spawns PowerShell..." | **PASS** |
| **Day 05** | Global | Shortcuts Modal | Click `KEYS [?]` / Close | Modal opens and closes properly | **PASS** |
| **Day 05** | 04 | Breach Timeline | Click Milestone 2 (Day 2) | Timeline drawer updates with DCSync attack evidence | **PASS** |
| **Day 05** | 04 | Volatility Decision Gate | Click Volatile RAM Action | Decision explanation updates with memory triage | **PASS** |
| **Day 05** | 17 | RFC 3227 Volatility Order | Click Option A (`.decision-btn`) | Feedback: "Correct! CPU registers and RAM first..." | **PASS** |
| **Day 06** | Global | Shortcuts Modal | Click `KEYS [?]` / Close | Modal opens and closes properly | **PASS** |
| **Day 06** | 02 | Phishing Email Dissector | Click From Hotspot | Threat callout box displays SPF/DMARC failure | **PASS** |
| **Day 06** | 21 | SCADA Air-Gap Breaker | Click Emergency Severance | Badge switches to SEVERED; Modbus traffic dropped | **PASS** |
| **Day 06** | 31 | Executive Briefing Dossier | Click Attributed Actor Tab | Tab switches to UNC-PHOENIX profile and TTPs | **PASS** |
| **Day 06** | 32 | Regulatory Reporting Check | Click Option B (`.decision-btn`) | Feedback: "Correct! CERT-In requires mandatory 6-hr..." | **PASS** |

---

### B. Standard Laptop Viewport (1366 × 768)

| Day | Slide # | Interactive Component | Action Tested | Output / State Observed | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Day 01** | Global | Shortcuts Modal | Open / Close | Modal opens centered; blur overlay intact | **PASS** |
| **Day 01** | 06 | Scenario Decision | Click Option B | Explanation box visible without scrolling | **PASS** |
| **Day 01** | 11 | Intel Cycle Stepper | Click Stages 1–6 | All 6 stage nodes clickable, progress updates | **PASS** |
| **Day 01** | 12 | NATO Indicator Station | Click Pills | Detail box fits cleanly within 768px height | **PASS** |
| **Day 01** | 13 | Caltagirone Diamond Model | Click All 5 Nodes | Stage fits cleanly, vertices distinct, zero overlap | **PASS** |
| **Day 01** | 22 | Knowledge Check Quiz | Click Options | Buttons and explanations render cleanly | **PASS** |
| **Day 02** | 03 | Threat Triage Dilemma | Click Alert Cards | 3 cards fit side-by-side without horizontal scroll | **PASS** |
| **Day 02** | 16 | Knowledge Check Quiz | Click Options | Explanations visible without viewport clipping | **PASS** |
| **Day 03** | 16 | Knowledge Check Quiz | Click Options | Explanation box renders in green | **PASS** |
| **Day 04** | 04 | Sysmon Log Hotspot | Click Hotspots | Hotspot clicks trigger explanation drawer | **PASS** |
| **Day 04** | 17 | Knowledge Check Quiz | Click Options | Correct option triggers emerald highlight | **PASS** |
| **Day 05** | 04 | Breach Timeline | Click Milestones | Milestones 1–5 clickable; drawer updates | **PASS** |
| **Day 05** | 17 | Knowledge Check Quiz | Click Options | Explanation text renders without overflow | **PASS** |
| **Day 06** | 02 | Phishing Dissector | Click Hotspots | Red dashed hotspots trigger callout explanations | **PASS** |
| **Day 06** | 21 | Air-Gap Breaker Switch | Click Toggle | Emergency air-gap severance triggers green status | **PASS** |
| **Day 06** | 31 | Executive Briefing Dossier | Click Tabs | 4 tabs switch active states and dossier text | **PASS** |

---

### C. Tablet Landscape Viewport (1024 × 768)

| Day | Slide # | Interactive Component | Action Tested | Output / State Observed | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Day 01** | Global | Telemetry Status Bar | Responsive Scaling | Bar compacts gap spacing to 8px; zero overflow | **PASS** |
| **Day 01** | 13 | Caltagirone Diamond Model | Click All 5 Nodes | Nodes maintain distinct touch targets (>44px) | **PASS** |
| **Day 02** | 03 | Threat Triage Challenge | Click Cards | Cards remain touchable and responsive | **PASS** |
| **Day 04** | 04 | Sysmon Log Hotspots | Click Hotspots | Hotspots clickable with adequate finger tap target | **PASS** |
| **Day 05** | 04 | Breach Timeline | Click Milestones | Milestones 1–5 clickable; layout stable | **PASS** |
| **Day 06** | 21 | Air-Gap Breaker | Click Toggle | Button full-width touchable; state updates | **PASS** |
| **Day 06** | 31 | Executive Briefing Dossier | Click Tabs | Tab row wraps gracefully; content updates | **PASS** |

---

### D. Mobile Portrait Viewport (375 × 667)

| Day | Slide # | Interactive Component | Action Tested | Output / State Observed | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Day 01** | Global | Telemetry Status Bar | Responsive Mode | `.status-center` hidden; navigation controls visible | **PASS** |
| **Day 01** | Global | Shortcuts Modal | Click `KEYS [?]` | Modal fits 90% mobile width; close button active | **PASS** |
| **Day 01** | 06 | Scenario Decision | Click Option B | Buttons stack vertically; explanation rendered | **PASS** |
| **Day 01** | 11 | Intel Cycle Stepper | Click Stage 3 | Stages fit on mobile grid; explanation updates | **PASS** |
| **Day 01** | 12 | NATO Indicator Station | Click IP Pill | Pill row scrollable; detail panel renders | **PASS** |
| **Day 01** | 13 | Caltagirone Diamond Model | Click All 5 Nodes | Stage height 290px; nodes clickable; details fit | **PASS** |
| **Day 01** | 22 | Knowledge Check Quiz | Click Option | Decision buttons stack cleanly; text wraps | **PASS** |
| **Day 02** | 03 | Threat Triage Challenge | Click Alert A | Cards stack vertically; feedback panel updates | **PASS** |
| **Day 02** | 16 | Knowledge Check Quiz | Click Option | Quiz options selectable; zero horizontal overflow | **PASS** |
| **Day 03** | 16 | Knowledge Check Quiz | Click Option | Decision options selectable on small screen | **PASS** |
| **Day 04** | 04 | Sysmon Log Hotspot | Click Hotspots | Hotspots wrap within line-height; drawer updates | **PASS** |
| **Day 04** | 17 | Knowledge Check Quiz | Click Option | Explanation box wraps within 375px bounds | **PASS** |
| **Day 05** | 04 | Breach Timeline | Click Milestone 2 | Milestone row fits 375px; evidence drawer readable | **PASS** |
| **Day 05** | 17 | Knowledge Check Quiz | Click Option | Quiz options selectable; zero layout breakage | **PASS** |
| **Day 06** | 02 | Phishing Dissector | Click Hotspots | Email mockup wraps cleanly; callout box visible | **PASS** |
| **Day 06** | 21 | Air-Gap Breaker | Click Toggle | Breaker button triggers state change to ISOLATED | **PASS** |
| **Day 06** | 31 | Executive Briefing Dossier | Click Tabs | Tabs stack into 2x2 grid; dossier readable | **PASS** |

---

## 3. Summary of Regression Results

- **Total Test Cases Executed:** 84 interaction checkpoints across 4 responsive viewports.
- **Pass Count:** 84
- **Fail Count:** 0
- **Blocked Count:** 0
- **Regression Pass Rate:** **100.0%**
- **Residual Defects / Open Items:** None. The presentation system is verified fully stable and ready for live classroom delivery.
