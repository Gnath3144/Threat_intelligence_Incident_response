# Threat Intelligence & Incident Response — Laboratory Content Audit
**Audit Authority:** Chief AI Knowledge Architect & Independent QA Auditor  
**Primary Standards:** Approved Courseware, IBM ICE Framework, NATO STANAG 2198, NIST SP 800-61r3, OASIS STIX 2.1  
**Total Course Labs:** 8 Hands-on Practical Laboratories (100% Audited)  
**Slide Structure Standard:** 7-Slide Structured Modules (Slide A through G)  

---

## 1. Laboratory Specification Audit Summary

| Lab ID | Training Day | Title | Duration | PLO Mapping | Slide Count | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **LAB-01** | Day 1 | Threat Intelligence Source Evaluation & OSINT Analysis | 80 Min | PLO-1 | 7 Slides (A–G) | **APPROVED (100%)** |
| **LAB-03** | Day 2 | Mapping Multi-Stage Behaviors to MITRE ATT&CK v15 | 85 Min | PLO-3 | 7 Slides (A–G) | **APPROVED (100%)** |
| **LAB-02** | Day 3 | IOC Enrichment & Contextual Threat Scoring (STIX 2.1) | 85 Min | PLO-2 | 7 Slides (A–G) | **APPROVED (100%)** |
| **LAB-04** | Day 4 | Security Telemetry Analysis & SIEM Log Correlation | 85 Min | PLO-4 | 7 Slides (A–G) | **APPROVED (100%)** |
| **LAB-06** | Day 5 | Enterprise Incident Triage & Forensic Timeline (NIST) | 60 Min | PLO-5 | 7 Slides (A–G) | **APPROVED (100%)** |
| **LAB-05** | Day 6 (Morn) | Phishing Header Forensics & Malicious Artifact Triage | 90 Min | PLO-6 | 7 Slides (A–G) | **APPROVED (100%)** |
| **LAB-07** | Day 6 (Aft) | Incident Response Playbook Engineering & SOAR Design | 90 Min | PLO-7 | 7 Slides (A–G) | **APPROVED (100%)** |
| **LAB-08** | Day 6 (Cap) | Capstone Enterprise Incident Response Tabletop Simulation | 60 Min | PLO-8 | 7 Slides (A–G) | **APPROVED (100%)** |

---

## 2. Detailed Technical Audit by Laboratory

### LAB-01: Threat Intelligence Source Evaluation & OSINT Analysis
- **Day & Module:** Day 1 | MOD-01: CTI Fundamentals & Diamond Modeling
- **Slide Modules Verified:**
  - **Slide A (Intro):** Explicit objectives, NATO Admiralty scoring framework, 80-minute timeline.
  - **Slide B (Setup):** Workstation paths (`C:\ThreatIntel_Labs\Lab01_OSINT\`), pre-flight `Test-Path` and `curl -I https://crt.sh`.
  - **Slide C (Procedure):** 3-Phase protocol: Admiralty B2 rating, crt.sh SAN extraction for `internal-sync.com`, Diamond Model construction.
  - **Slide D (Output):** Verbatim crt.sh certificate log table, Let's Encrypt automated issuance cluster inspection.
  - **Slide E (Interpretation):** Confirms infrastructure weaponization; clearly articulates that internal breach is *not* established.
  - **Slide F (Troubleshooting):** Immediate fallback command for crt.sh 504 timeouts using local mirror `cache\crtsh_dump.json`.
  - **Slide G (Assessment):** 4-item deliverable checklist and 100-point rubric (40% Admiralty, 30% OSINT, 30% Diamond Model).

### LAB-03: Mapping Multi-Stage Behaviors to MITRE ATT&CK v15
- **Day & Module:** Day 2 | MOD-02: Threat Modeling & MITRE ATT&CK Matrix
- **Slide Modules Verified:**
  - **Slide A (Intro):** Operation SolarPhish narrative deconstruction, Navigator v5 objectives.
  - **Slide B (Setup):** Local offline Navigator initialization, `attack_layer_template.json` syntax check.
  - **Slide C (Procedure):** Mapping Events A–E to T1566.001, T1059.001/T1105, T1053.005, T1003.001, T1047.
  - **Slide D (Output):** Complete JSON layer schema with v15 attack version tag, scores 1–5, and color palette.
  - **Slide E (Interpretation):** Defensive chokepoints: macro child-process blocking, Credential Guard, RPC filtering.
  - **Slide F (Troubleshooting):** Python JSON validation one-liner to pinpoint syntax errors.
  - **Slide G (Assessment):** Rubric (40% mapping accuracy, 30% Navigator layer, 30% D3FEND mitigations).

### LAB-02: IOC Enrichment & Contextual Threat Scoring (STIX 2.1)
- **Day & Module:** Day 3 | MOD-03: STIX/TAXII Protocols & Threat Intelligence Feeds
- **Slide Modules Verified:**
  - **Slide A (Intro):** IOC defanging, multi-factor risk scoring, OASIS STIX 2.1 serialization.
  - **Slide B (Setup):** SOC virtual environment `venv_soc`, `stix2 (v3.0.1)` verification command.
  - **Slide C (Procedure):** Defang regex, scoring formula `(Age*0.3)+(Rep*0.4)+(Sight*0.3)`, Python STIX 2.1 Bundle instantiation.
  - **Slide D (Output):** Validated STIX JSON bundle with canonical UUIDv4 IDs and referential relationship integrity.
  - **Slide E (Interpretation):** Operational decision tiers (Score 80–100 -> EDR block; 50–79 -> Sandbox; 0–49 -> Baseline).
  - **Slide F (Troubleshooting):** Resolving `stix2.exceptions.InvalidValueError` by checking pattern bracket syntax.
  - **Slide G (Assessment):** Rubric (30% defanging, 40% STIX validity, 30% scoring rationale).

### LAB-04: Security Telemetry Analysis & SIEM Indicator Correlation
- **Day & Module:** Day 4 | MOD-04: Multi-Source Telemetry Correlation & Sigma Rules
- **Slide Modules Verified:**
  - **Slide A (Intro):** Telemetry Triad, Windows EID 4624/4625/4688, Suricata IDS correlation.
  - **Slide B (Setup):** Pandas environment, `auth_events.json` (2,500 records), `network_alerts.json` (1,200 records).
  - **Slide C (Procedure):** Filter EID 4625 brute force cluster, identify EID 4624 Logon Type 10, decode PowerShell base64 UTF-16LE.
  - **Slide D (Output):** Decoded PowerShell downloader syntax, correlated master chronology table.
  - **Slide E (Interpretation):** Identifies compromised `svc_backup_admin`, transpiles validated Sigma rule YAML.
  - **Slide F (Troubleshooting):** Handling memory limits using `chunksize=500`; resolving CyberChef text encoding mismatches.
  - **Slide G (Assessment):** Rubric (35% auth triage, 35% de-obfuscation, 30% cross-sensor correlation).

### LAB-06: Enterprise Incident Triage & Forensic Timeline Reconstruction
- **Day & Module:** Day 5 | MOD-05: Incident Response Lifecycle & Forensic Triage
- **Slide Modules Verified:**
  - **Slide A (Intro):** NIST SP 800-61r3 triage, SEV-1 classification, UTC chronology, Chain of Custody.
  - **Slide B (Setup):** Evidence manifest, SHA-256 pre-flight integrity verification.
  - **Slide C (Procedure):** Apply functional/information impact matrix, normalize 4 timestamps to UTC, sign Chain of Custody form.
  - **Slide D (Output):** Master Chronology table (14:12 to 14:32 UTC), completed Chain of Custody form `EVD-20261026-001`.
  - **Slide E (Interpretation):** Scoping Patient Zero (`WS-22`) vs lateral Domain Admin pivot (`DC-01`).
  - **Slide F (Troubleshooting):** Resolving timezone offsets (+5:30 vs UTC); working only on forensic clones.
  - **Slide G (Assessment):** Rubric (40% severity justification, 40% chronology normalization, 20% chain of custody).

### LAB-05: Phishing Header Forensics & Malicious Artifact Triage
- **Day & Module:** Day 6 (Morning) | MOD-06A: Phishing Triage & Safe Artifact Analysis
- **Slide Modules Verified:**
  - **Slide A (Intro):** RFC-5322 header forensics, SPF/DKIM/DMARC alignment, CyberChef safe decoding.
  - **Slide B (Setup):** Offline CyberChef v10.19.4, `sample_phishing_email.eml` text inspection.
  - **Slide C (Procedure):** Trace Received hop headers bottom-up, inspect DMARC alignment failure, extract ISO attachment magic bytes.
  - **Slide D (Output):** Verbatim Authentication-Results header, extracted SHA-256 and defanged phishing URL.
  - **Slide E (Interpretation):** Policy hardening: DMARC `p=reject`, blocking inbound `.iso`/`.vhd` containers at mail gateway.
  - **Slide F (Troubleshooting):** Preventing accidental execution; trimming MIME boundary tags in CyberChef.
  - **Slide G (Assessment):** Rubric (35% hop path, 35% DMARC analysis, 30% CyberChef triage).

### LAB-07: Incident Response Playbook Engineering & SOAR Design
- **Day & Module:** Day 6 (Afternoon) | MOD-06B: SOAR Playbook Engineering
- **Slide Modules Verified:**
  - **Slide A (Intro):** Ransomware containment architecture, SOAR workflow modeling, human approval gates.
  - **Slide B (Setup):** Draw.io / Mermaid.js environment, `soar_playbook_schema.json` verification.
  - **Slide C (Procedure):** 4-Phase containment logic: Trigger, Host Isolation, Human Gate 1 (KRBTGT reset), Offline Restore.
  - **Slide D (Output):** Mermaid flowchart architecture with decision diamonds; validated JSON playbook schema.
  - **Slide E (Interpretation):** Blast radius vs velocity: why automated destructive actions require human authorization.
  - **Slide F (Troubleshooting):** Whitelisting EDR management ports; escaping special characters in Mermaid labels.
  - **Slide G (Assessment):** Rubric (40% playbook logic, 30% human gate rigor, 30% JSON schema).

### LAB-08: Capstone Enterprise Incident Response Tabletop Simulation
- **Day & Module:** Day 6 (Afternoon) | MOD-06C: Capstone APT Crisis Simulation (AeroGrid Dynamics)
- **Slide Modules Verified:**
  - **Slide A (Intro):** Full-spectrum multi-stage APT crisis response, executive reporting, pod defense.
  - **Slide B (Setup):** Unified workbench (CyberChef, ATT&CK Navigator, Python), `capstone_incident_dossier.md`.
  - **Slide C (Procedure):** Ingest Injection 1 (Beacon), Injection 2 (WMI Lateral), Injection 3 (1.2GB Exfiltration Spike).
  - **Slide D (Output):** Mandatory 6-section Executive Incident Response Final Report schema.
  - **Slide E (Interpretation):** Root Cause Analysis: lack of micro-segmentation and lack of MFA on external gateway; 90-day roadmap.
  - **Slide F (Troubleshooting):** Pod time management protocol; dividing investigative roles to prevent bottlenecks.
  - **Slide G (Assessment):** Graduation rubric (30% timeline, 30% ATT&CK mapping, 40% executive report & RCA).

---

## 3. Compliance & Quality Verdict
All 8 practical laboratories satisfy the 7-Slide Structured Module requirement without exception. All procedures, commands, datasets, and rubrics strictly mirror the approved courseware.
