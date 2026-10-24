# Threat Intelligence & Incident Response — GitHub Pages Deployment Guide
**Target Repository:** `https://github.com/Gnath3144/Threat_intelligence_Incident_response`  
**Deployment Platform:** GitHub Pages via GitHub Actions (Official Workflow)  
**Live Target URL:** `https://gnath3144.github.io/Threat_intelligence_Incident_response/`  
**Security Classification:** Public Keynote & Course Portal (Zero Secrets / Credentials)  

---

## 1. Project Architecture & Output Directory
The presentation suite is structured as a modern, high-performance static web application requiring zero backend server execution:
- **Root Entry Point:** `index.html` (Master 6-Day Presentation Control Portal).
- **Day-Wise Keynotes:**
  - `day-01/index.html` (23 designed slides including 7-slide LAB-01).
  - `day-02/index.html` (17 designed slides including 7-slide LAB-03).
  - `day-03/index.html` (17 designed slides including 7-slide LAB-02).
  - `day-04/index.html` (18 designed slides including 7-slide LAB-04).
  - `day-05/index.html` (18 designed slides including 7-slide LAB-06).
  - `day-06/index.html` (33 designed slides including 7-slide LAB-05, LAB-07, LAB-08).
- **Shared Assets:**
  - `shared/css/`: `reset.css`, `reveal.css`, `theme-cyber-soc.css`, `animations.css`, `interactive-experiences.css`.
  - `shared/js/`: `reveal.js`, `gsap.min.js`, `three.min.js`, `characters.js`, `cyber-3d.js`, `gsap-narratives.js`, `presentation-app.js`.
  - `docs/`: Audited governance registers, test matrices, and PDF companion documents.

---

## 2. GitHub Actions Deployment Workflow (`.github/workflows/deploy-pages.yml`)
The repository includes a certified GitHub Actions deployment workflow utilizing the official GitHub Pages deployment actions:

```yaml
name: Deploy Threat Intelligence Presentation to GitHub Pages

on:
  push:
    branches: ["main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Setup GitHub Pages
        uses: actions/configure-pages@v5

      - name: Upload Pages Artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: '.'

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

---

## 3. Path Resolution & Subpath Verification
Because GitHub Pages serves project repositories under a subpath (`/<repository-name>/`), all asset references and internal hyperlinks were audited and verified:
1. **Root Portal (`index.html`):**
   - Stylesheets: `shared/css/reset.css`, `shared/css/theme-cyber-soc.css`, etc. (Relative -> Resolves perfectly).
   - Daily Deck Links: `day-01/index.html`, `day-02/index.html`, etc. (Relative -> Resolves perfectly).
   - Scripts: `shared/js/characters.js`. (Relative -> Resolves perfectly).
2. **Daily Decks (`day-XX/index.html`):**
   - Portal Home Button: `../index.html`. (Relative -> Resolves perfectly).
   - Day Navigation Buttons: `../day-02/index.html`, etc. (Relative -> Resolves perfectly).
   - Stylesheets: `../shared/css/...`. (Relative -> Resolves perfectly).
   - Scripts: `../shared/js/...`. (Relative -> Resolves perfectly).
3. **Zero Local/Absolute Dependencies:**
   - No hardcoded `localhost:8000` or local filesystem paths (`C:\...`) exist in any client-side link or asset loader.
   - External Google Fonts (`JetBrains Mono`, `Plus Jakarta Sans`, `Space Grotesk`) load over secure HTTPS CDN.

---

## 4. Security & Privacy Audit
Prior to deployment, the repository was audited for sensitive information:
- **API Keys / Tokens:** Zero embedded tokens, secrets, or passwords in any HTML, JS, or CSS file.
- **Facilitator Script Separation:** All facilitator teleprompter notes, answers, and verbal cues were removed from the projected presentation and isolated into `Threat_Intelligence_Incident_Response_Facilitator_Notes.pdf`.
- **Telemetry Data:** All log extracts, IP addresses, domains, and hashes used in the presentation are synthetic academic entities.

---

## 5. Deployment Step-by-Step Instructions
1. Push the committed files to the `main` branch of `https://github.com/Gnath3144/Threat_intelligence_Incident_response.git`.
2. In the GitHub repository, navigate to **Settings** → **Pages**.
3. Under **Build and deployment** → **Source**, ensure **GitHub Actions** is selected.
4. The workflow will automatically trigger, build the artifact, and publish to:
   `https://gnath3144.github.io/Threat_intelligence_Incident_response/`
