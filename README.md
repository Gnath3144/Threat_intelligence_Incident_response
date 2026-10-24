# Threat Intelligence & Incident Response — Master Keynote Portal

[![GitHub Pages Deployment](https://github.com/Gnath3144/Threat_intelligence_Incident_response/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/Gnath3144/Threat_intelligence_Incident_response/actions/workflows/deploy-pages.yml)

🌐 **Live Published Presentation:** [https://gnath3144.github.io/Threat_intelligence_Incident_response/](https://gnath3144.github.io/Threat_intelligence_Incident_response/)

Six-day interactive keynote presentation suite and hands-on laboratory environment for the **Threat Intelligence and Incident Response** instructor-led training program.

---

## 📅 Course Operational Schedule

| Training Day | Date | Gross Time | Net Instructional Time | Curriculum Focus & Hands-on Lab | Deck Slide Count |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Day 1** | Mon 26 Oct 2026 | 1:00 PM – 5:00 PM | 220 min (3.67h) | CTI Fundamentals, Diamond Model, Admiralty Code & **LAB-01** | 23 Slides |
| **Day 2** | Tue 27 Oct 2026 | 1:00 PM – 5:00 PM | 220 min (3.67h) | MITRE ATT&CK Matrix v15, Navigator Algebra & **LAB-03** | 17 Slides |
| **Day 3** | Wed 28 Oct 2026 | 1:00 PM – 5:00 PM | 220 min (3.67h) | Defensive OSINT, STIX 2.1 JSON Bundling, TAXII 2.1 & **LAB-02** | 17 Slides |
| **Day 4** | Thu 29 Oct 2026 | 1:00 PM – 5:00 PM | 220 min (3.67h) | Enterprise Telemetry Triad, Windows EID Triage, Sigma & **LAB-04** | 18 Slides |
| **Day 5** | Fri 30 Oct 2026 | 2:00 PM – 5:00 PM | 165 min (2.75h) | NIST SP 800-61r3, RFC 3227 Volatility, Master Chronology & **LAB-06** | 18 Slides |
| **Day 6** | Sat 31 Oct 2026 | 9:30 AM – 5:00 PM | 375 min (6.25h) | Phishing Forensics (**LAB-05**), SOAR (**LAB-07**), AeroGrid APT Tabletop (**LAB-08**) | 33 Slides |
| **Total Track** | **6 Days** | **26.50 Hours** | **1,405 Net Mins (23.42h)** | **8 Complete Modules, 8 Hands-on Labs, 1 Capstone Defense** | **126 Slides Total** |

---

## 🚀 Key Architectural Highlights

1. **Natural Landing Portal Scrolling:**
   - Smooth native mouse wheel, trackpad, and touch scrolling across desktop, laptop, and mobile devices.
2. **Interactive 3D Web & GSAP Timelines:**
   - Interactive Three.js **3D Cyber Threat Globe** and **3D Enterprise Defense Mesh** with raycasting node inspection.
   - Dedicated on-canvas `[⏸ PAUSE]` / `[▶ ROTATE]` / `[↺ RESET]` controls that never accidentally freeze presentation slides.
   - Animated original cybersecurity mascots (**Threat Detective**, **Alert Bot**, **Security Guardian**, **Phishing Impostor**, **Evidence Robot**) with reactive speech bubbles and cyber wisdom.
3. **8 Explicit 7-Slide Structured Laboratory Modules (Slides A through G):**
   - **Slide A:** Objectives, Prerequisites & Deliverables.
   - **Slide B:** Environment Preparation, OS, tools & pre-flight verification commands.
   - **Slide C:** 3-Phase step-by-step practical procedures with exact commands.
   - **Slide D:** Expected terminal outputs, JSON schemas, and log extracts.
   - **Slide E:** Technical interpretation (what findings establish vs what they do not establish).
   - **Slide F:** Common errors and recovery commands.
   - **Slide G:** Completion checklists, Socratic questions, and 100-point rubrics.
4. **Complete Separation of Facilitator Guidance (Zero HUD on Slides):**
   - Student-facing slides contain zero teleprompter clutter or answers.
   - All spoken cues (`SAY`), pedagogy intent, Socratic Q&A, and troubleshooting are preserved in the companion document `docs/Threat_Intelligence_Incident_Response_Facilitator_Notes.pdf`.
5. **Classroom Navigation Shortcuts:**
   - `Space` / `Right Arrow`: Advance slide or fragment.
   - `Left Arrow`: Previous slide.
   - `F`: Toggle Full-Screen mode.
   - `?` / `KEYS`: Toggle keyboard shortcuts cheatsheet.

---

## 🛡️ Repository Structure

```text
├── index.html                   # Master 6-Day Presentation Control Portal
├── day-01/index.html            # Day 1: CTI Fundamentals & LAB-01
├── day-02/index.html            # Day 2: ATT&CK Matrix v15 & LAB-03
├── day-03/index.html            # Day 3: STIX 2.1 / TAXII 2.1 & LAB-02
├── day-04/index.html            # Day 4: Telemetry Correlation & LAB-04
├── day-05/index.html            # Day 5: NIST SP 800-61r3 & LAB-06
├── day-06/index.html            # Day 6: Phishing, SOAR & AeroGrid Capstone
├── shared/
│   ├── css/                     # Reset, Reveal, Cyber-SOC theme, Animations
│   └── js/                      # Reveal, GSAP, Three.js, Mascots, 3D, Narratives
├── docs/
│   ├── REPAIR_CHANGELOG.md      # Detailed defect remediation changelog
│   ├── INTERACTION_TEST_MATRIX.xlsx # Complete interaction audit spreadsheet
│   ├── LAB_CONTENT_AUDIT.md     # 8-Lab authoritative courseware audit
│   ├── GITHUB_PAGES_DEPLOYMENT.md # Deployment specification & relative path audit
│   ├── FINAL_QA_REPORT.md       # 9-Expert Panel QA sign-off (10/10)
│   └── Threat_Intelligence_Incident_Response_Facilitator_Notes.pdf
└── .github/workflows/
    └── deploy-pages.yml         # Automated GitHub Pages CI/CD workflow
```

---

## 📜 Quality Assurance & Governance
Audited and approved under the 9 Expert Panels of the Quality Manifesto by the Chief AI Knowledge Architect. Meets WCAG AA accessibility standards with 100% relative path resolution for GitHub Pages.
