# Slides Data: Act 2 (Day 2 - Threat Modeling & ATT&CK) & Act 3 (Day 3 - OSINT & STIX/TAXII)
# Slides 17 to 36

ACT2_ACT3_SLIDES = [
    # SLIDE 17: Day 2 Launch
    {
        "title": "Day 2 Launch & Objectives",
        "day": "DAY 02",
        "day_start": 2,
        "module": "MOD-02: THREAT MODELING",
        "session": "SES-02 (1:00–5:00 PM)",
        "ref": "Handbook Module 2",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-blue">MODULE 02 LAUNCH</div>
            <h2>Threat Modeling, MITRE ATT&CK & Structured Threat Hunting</h2>
            <p>Session ID: SES-02 | Scheduled Net Teaching: 220 Minutes | Refreshment Break: 3:00 PM (20 min)</p>
            
            <div class="grid-2" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 15px;">Target Learning Outcomes (PLO-2)</strong>
                <ul style="font-size: 13px; color: var(--text-secondary); margin-top: 10px; line-height: 1.7;">
                  <li><strong>Cyber Kill Chain vs. Diamond Model:</strong> Contrast linear prevention vs. non-linear graph pivoting.</li>
                  <li><strong>Pyramid of Pain:</strong> Calculate defensive ROI from hashes to adversary TTPs.</li>
                  <li><strong>MITRE ATT&CK Matrix v15:</strong> Navigate 14 enterprise tactics and sub-techniques.</li>
                  <li><strong>8 Core Enterprise Tactics:</strong> Initial Access through Impact deep-dive.</li>
                  <li><strong>ATT&CK Navigator v5:</strong> Execute layer algebra to surface detection blind spots.</li>
                  <li><strong>Threat Hunting & D3FEND:</strong> Hypothesize adversary tradecraft and map countermeasures.</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--electric-blue); font-size: 15px;">Hands-On Milestone: LAB-03</strong>
                <p style="font-size: 13px; margin-top: 10px;">
                  Every analyst will build custom JSON layers in ATT&CK Navigator v5, perform layer arithmetic (<code style="color: var(--neon-amber);">Score = max(Threat, Detect)</code>) to isolate defensive visibility gaps for threat actor <strong>UNC-PHOENIX</strong>, and export a verified coverage matrix.
                </p>
                <div style="margin-top: 16px; padding: 10px; background: rgba(79, 172, 254, 0.08); border-radius: 6px; border: 1px dashed var(--electric-blue); font-family: var(--font-mono); font-size: 12px; color: var(--electric-blue);">
                  TARGET FILE: unc_phoenix_coverage_layer.json // LAB-03 COMPLETE
                </div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Good afternoon, colleagues, and welcome back to Day 2 in LH3. I hope everyone had a good evening and that your hostel Wi-Fi cooperated—or at least gave you enough bandwidth to download today's lab materials! Today we move from identifying threat actors to mapping their exact behavioral tradecraft.",
        "notes_pedagogy": "HUMOR ANCHOR: Friendly nod to hostel Wi-Fi. Bridge cleanly from Day 1 indicator identification to Day 2 behavioral modeling."
    },

    # SLIDE 18: Cyber Kill Chain vs Diamond Model
    {
        "title": "Cyber Kill Chain vs. Diamond Model",
        "day": "DAY 02",
        "module": "MOD-02: THREAT MODELING",
        "session": "CON-01",
        "ref": "Handbook Day 2 Concept 1",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">MODEL COMPARISON</div>
            <h2>Cyber Kill Chain vs. Diamond Model of Intrusion Analysis</h2>
            <p>Two complementary lenses for deconstructing complex enterprise intrusions.</p>
            
            <div class="grid-2" style="margin-top: 24px;">
              <div class="cyber-card">
                <strong style="color: var(--neon-amber); font-size: 15px;">LOCKHEED MARTIN CYBER KILL CHAIN</strong>
                <ul style="font-size: 13px; color: var(--text-secondary); margin-top: 10px; line-height: 1.7;">
                  <li><strong>Philosophy:</strong> Strictly linear, sequential progression of 7 phases.</li>
                  <li><strong>Defensive Goal:</strong> Break any single link to completely disrupt the attack.</li>
                  <li><strong>Phases:</strong> Recon ➔ Weaponize ➔ Deliver ➔ Exploit ➔ Install ➔ C2 ➔ Actions on Objectives.</li>
                  <li><strong>Limitation:</strong> Poorly models modern internal lateral movement, Living-off-the-Land tradecraft, and insider threats.</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 15px;">CALTAGIRONE DIAMOND MODEL</strong>
                <ul style="font-size: 13px; color: var(--text-secondary); margin-top: 10px; line-height: 1.7;">
                  <li><strong>Philosophy:</strong> Non-linear, relational graph of vertices and meta-features.</li>
                  <li><strong>Defensive Goal:</strong> Mathematical pivoting to discover unknown adversary infrastructure.</li>
                  <li><strong>Vertices:</strong> Adversary ➔ Capability ➔ Infrastructure ➔ Victim.</li>
                  <li><strong>Strength:</strong> Excels at mapping supply-chain intrusions, cloud breaches, and multi-stage campaign evolutions.</li>
                </ul>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "The Cyber Kill Chain is like an assembly line: break one link and the whole chain halts. But modern adversaries do not walk in a straight line! They loop, they pivot, they live off the land. That is why we combine the Kill Chain's temporal phases with the Diamond Model's relational graph.",
        "notes_pedagogy": "Use the assembly line analogy for Kill Chain, and the detective conspiracy board analogy for Diamond Model."
    },

    # SLIDE 19: The Pyramid of Pain
    {
        "title": "David Bianco's Pyramid of Pain",
        "day": "DAY 02",
        "module": "MOD-02: THREAT MODELING",
        "session": "CON-02",
        "ref": "Handbook Day 2 Concept 2",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-crimson">DEFENSIVE ROI HIERARCHY</div>
            <h2>David Bianco's Pyramid of Pain</h2>
            <p>The higher you climb on the pyramid, the more operational pain you inflict on the adversary.</p>
            
            <div style="max-width: 800px; margin: 24px auto 0 auto;">
              <div class="cyber-card" style="margin-bottom: 8px; border-color: var(--alert-crimson); background: rgba(255,75,75,0.12);">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="color: var(--alert-crimson);">TTPs (Tactics, Techniques & Procedures)</strong>
                  <span class="cyber-badge badge-crimson">TOUGH (Pain: Severe)</span>
                </div>
                <div style="font-size: 12px; color: var(--text-secondary); margin-top: 4px;">Adversary behavior (Pass-the-Hash, Certutil staging). Forces adversary to completely retrain operators and rewrite tooling.</div>
              </div>
              <div class="cyber-card" style="margin-bottom: 8px; border-color: var(--neon-amber); background: rgba(255,179,0,0.1);">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="color: var(--neon-amber);">Tools (Mimikatz, Cobalt Strike, PsExec)</strong>
                  <span class="cyber-badge badge-amber">CHALLENGING (Pain: High)</span>
                </div>
                <div style="font-size: 12px; color: var(--text-secondary); margin-top: 4px;">Specific utilities dropped to disk. Adversary must re-engineer or find alternative bypass tools.</div>
              </div>
              <div class="cyber-card" style="margin-bottom: 8px; border-color: var(--electric-blue); background: rgba(79,172,254,0.1);">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="color: var(--electric-blue);">Network / Host Artifacts & Domain Names</strong>
                  <span class="cyber-badge badge-blue">ANNOYING / SIMPLE (Pain: Moderate)</span>
                </div>
                <div style="font-size: 12px; color: var(--text-secondary); margin-top: 4px;">URI patterns, registry run keys, registered domains. Costs $10 and 2 minutes to register a new domain.</div>
              </div>
              <div class="cyber-card" style="border-color: var(--cyber-cyan); background: rgba(0,242,254,0.06);">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="color: var(--cyber-cyan);">IP Addresses & Hash Values (MD5, SHA-256)</strong>
                  <span class="cyber-badge badge-cyan">TRIVIAL (Pain: Negligible)</span>
                </div>
                <div style="font-size: 12px; color: var(--text-secondary); margin-top: 4px;">Changing a hash takes 1 benign byte. Changing an IP takes 15 seconds on a cloud instance. Zero adversary pain.</div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "David Bianco gave us the Pyramid of Pain. Look at the bottom: Hashes and IP addresses. Changing a hash is as easy as changing your WhatsApp DP—takes three seconds, zero effort. Changing an IP is like buying a ten-rupee prepaid SIM card. But changing a TTP at the top? That is like asking an engineering student to stop studying at 2:00 AM the night before exams! It requires complete rewiring of their operational muscle memory.",
        "notes_pedagogy": "HUMOR ANCHOR: Changing hash = changing WhatsApp DP. Changing TTPs = breaking engineering student exam habits. Explains why behavioral defense matters."
    },

    # SLIDE 20: MITRE ATT&CK Matrix Architecture
    {
        "title": "MITRE ATT&CK Matrix Architecture",
        "day": "DAY 02",
        "module": "MOD-02: THREAT MODELING",
        "session": "CON-03",
        "ref": "Handbook Day 2 Concept 3",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">BEHAVIORAL TAXONOMY</div>
            <h2>MITRE ATT&CK Matrix v15 Enterprise Architecture</h2>
            <p>The definitive global encyclopedia of empirical adversary tradecraft.</p>
            
            <div class="grid-3" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 16px;">14 TACTICS (The 'WHY')</strong>
                <p style="font-size: 13px; margin-top: 8px;">The adversary's technical objective at each phase of the intrusion. From Initial Access to Lateral Movement and Impact.</p>
              </div>
              <div class="cyber-card">
                <strong style="color: var(--electric-blue); font-size: 16px;">TECHNIQUES (The 'HOW')</strong>
                <p style="font-size: 13px; margin-top: 8px;">The specific technical method used to achieve a tactical objective (e.g., T1059 Command and Scripting Interpreter).</p>
              </div>
              <div class="cyber-card">
                <strong style="color: var(--neon-amber); font-size: 16px;">PROCEDURES (The 'WHAT')</strong>
                <p style="font-size: 13px; margin-top: 8px;">The exact command-line execution or script observed in a specific campaign (e.g., <code>certutil.exe -urlcache -split -f http://...</code>).</p>
              </div>
            </div>
            
            <div class="terminal-buffer" style="margin-top: 18px;">
              <div class="terminal-header">
                <div class="terminal-dots"><span class="dot dot-red"></span><span class="dot dot-yellow"></span><span class="dot dot-green"></span></div>
                <span>ATT&CK MATRIX TAXONOMY SCHEMA HIERARCHY</span>
              </div>
              <div class="terminal-body" style="font-size: 12px;">
TACTIC: Execution [TA0002] ➔ TECHNIQUE: Command & Scripting Interpreter [T1059] 
  ➔ SUB-TECHNIQUE: PowerShell [T1059.001]
  ➔ PROCEDURE: UNC-PHOENIX executes base64-encoded download cradle via `powershell.exe -enc ...`
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Notice the hierarchy: Tactics are the WHY (Execution). Techniques are the HOW (PowerShell). Procedures are the WHAT (the exact base64 command). The adversary can change their IP, but they cannot hide their procedure.",
        "notes_pedagogy": "Establish the Tactic ➔ Technique ➔ Sub-technique ➔ Procedure hierarchy."
    },

    # SLIDE 21: 8 Core Enterprise Tactics Deep-Dive
    {
        "title": "8 Core Enterprise Tactics in Depth",
        "day": "DAY 02",
        "module": "MOD-02: THREAT MODELING",
        "session": "CON-04",
        "ref": "Handbook Day 2 Concept 4",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-blue">TACTICAL BREAKDOWN</div>
            <h2>The 8 Core Enterprise Tactics: Initial Access to Impact</h2>
            <p>Understanding the standard kill chain progression through the ATT&CK lens.</p>
            
            <div class="grid-4" style="margin-top: 20px; font-size: 12px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan);">1. Initial Access</strong>
                <p style="margin-top: 4px;">Spearphishing attachments (T1566), valid VPN credentials, public edge exploits.</p>
              </div>
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan);">2. Execution</strong>
                <p style="margin-top: 4px;">PowerShell (T1059.001), Windows Command Shell, WMI process execution.</p>
              </div>
              <div class="cyber-card">
                <strong style="color: var(--electric-blue);">3. Persistence</strong>
                <p style="margin-top: 4px;">Registry Run keys (T1547), Scheduled Tasks (T1053), service creation.</p>
              </div>
              <div class="cyber-card">
                <strong style="color: var(--electric-blue);">4. Privilege Escalation</strong>
                <p style="margin-top: 4px;">Token impersonation, DLL search order hijacking, Kerberoasting (T1558).</p>
              </div>
              <div class="cyber-card">
                <strong style="color: var(--neon-amber);">5. Defense Evasion</strong>
                <p style="margin-top: 4px;">Living-off-the-Land (LOLBins), process injection (T1055), log clearing.</p>
              </div>
              <div class="cyber-card">
                <strong style="color: var(--neon-amber);">6. Discovery</strong>
                <p style="margin-top: 4px;">Network share scanning (T1135), AD enumeration (<code>nltest /dclist</code>).</p>
              </div>
              <div class="cyber-card">
                <strong style="color: var(--alert-crimson);">7. Lateral Movement</strong>
                <p style="margin-top: 4px;">Pass-the-Hash (T1550.002), Remote Desktop Protocol, SMB file execution.</p>
              </div>
              <div class="cyber-card" style="border-color: var(--alert-crimson);">
                <strong style="color: var(--alert-crimson);">8. Exfiltration & Impact</strong>
                <p style="margin-top: 4px;">Automated cloud sync exfil (T1567), data encryption for ransom (T1486).</p>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Walk through these eight core tactics. Notice how an attacker moves from Initial Access down to Exfiltration and Impact. Every tactic leaves telemetry behind.",
        "notes_pedagogy": "Guide students to view intrusions not as isolated events, but as a linked chain of tactical goals."
    },

    # SLIDE 22: ATT&CK Navigator & Layer Algebra
    {
        "title": "ATT&CK Navigator v5 & Layer Algebra",
        "day": "DAY 02",
        "module": "MOD-02: THREAT MODELING",
        "session": "CON-05",
        "ref": "Handbook Day 2 Concept 5",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-amber">VISUAL COVERAGE MATRIX</div>
            <h2>ATT&CK Navigator v5: Visualizing Detection Blind Spots</h2>
            <p>Layer Algebra transforms subjective security opinions into objective mathematical coverage.</p>
            
            <div class="grid-2" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 15px;">Layer Arithmetic Formula:</strong>
                <div class="terminal-buffer" style="margin: 10px 0; font-size: 12px;">
                  <div class="terminal-body">
<span class="terminal-cmd">Score(T)</span> = Threat Actor Activity (Score: 100, Red)
<span class="terminal-cmd">Score(D)</span> = Internal SOC Detection Rule (Score: -100, Green)
<br><span style="color: var(--neon-amber); font-weight: 700;">GAP MATRIX:</span> Score(Combine) = Score(T) + Score(D)
* Red cells indicate critical detection blind spots!
                  </div>
                </div>
                <p style="font-size: 12px; color: var(--text-secondary);">
                  In Navigator v5, we export the combined layer JSON to identify which adversary techniques have zero detection coverage in our SIEM.
                </p>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--electric-blue); font-size: 15px;">Demonstration Takeaway:</strong>
                <ul style="font-size: 13px; color: var(--text-secondary); margin-top: 8px; line-height: 1.7;">
                  <li>Open <code>https://mitre-attack.github.io/attack-navigator/</code>.</li>
                  <li>Load <code>threat_unc_phoenix.json</code> (Threat Layer).</li>
                  <li>Load <code>internal_soc_detection.json</code> (Detection Layer).</li>
                  <li>Click <strong>Create Layer from Other Layers</strong>.</li>
                  <li>Formula: <code>b - a</code> ➔ surfaces unmonitored LOLBins!</li>
                </ul>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Layer algebra in Navigator v5 is pure mathematical threat modeling. Layer A is what the attacker does. Layer B is what your SIEM detects. When you subtract B from A, whatever remains in crimson is your blind spot. That tells you exactly which Sigma rule to write tomorrow.",
        "notes_pedagogy": "Prepare students for Lab 3 layer algebra calculations."
    },

    # SLIDE 23: Hypothesis-Driven Threat Hunting
    {
        "title": "Hypothesis-Driven Threat Hunting",
        "day": "DAY 02",
        "module": "MOD-02: THREAT MODELING",
        "session": "CON-06",
        "ref": "Handbook Day 2 Concept 6",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">PROACTIVE DEFENSE</div>
            <h2>Structured Hypothesis-Driven Threat Hunting</h2>
            <p>Threat hunting is not wandering around hoping to bump into an attacker. It is scientific inquiry.</p>
            
            <div class="grid-4" style="margin-top: 24px; font-size: 13px;">
              <div class="cyber-card">
                <span class="cyber-badge badge-blue">STEP 1: TRIGGER</span>
                <div style="font-weight: 700; color: #FFF; margin: 10px 0 4px 0;">CTI Advisory</div>
                <p style="font-size: 12px;">Threat bulletin notes UNC-PHOENIX abuses scheduled tasks for persistence in energy firms.</p>
              </div>
              <div class="cyber-card">
                <span class="cyber-badge badge-cyan">STEP 2: HYPOTHESIS</span>
                <div style="font-weight: 700; color: #FFF; margin: 10px 0 4px 0;">Testable Statement</div>
                <p style="font-size: 12px;"><em>"Adversaries have established scheduled tasks masquerading as edge updates on DMZ hosts."</em></p>
              </div>
              <div class="cyber-card">
                <span class="cyber-badge badge-amber">STEP 3: INVESTIGATION</span>
                <div style="font-weight: 700; color: #FFF; margin: 10px 0 4px 0;">Telemetry Query</div>
                <p style="font-size: 12px;">Query Windows Event ID 4698 across all domain controllers. Stack-rank task paths and binaries.</p>
              </div>
              <div class="cyber-card" style="border-color: var(--emerald-pass);">
                <span class="cyber-badge badge-crimson">STEP 4: AUTOMATION</span>
                <div style="font-weight: 700; color: #FFF; margin: 10px 0 4px 0;">Sigma Rule Build</div>
                <p style="font-size: 12px;">Deploy permanent detection rule into SIEM to convert hunt findings into automated 24/7 defense.</p>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Threat hunting is not like a first-year student wandering the campus trying to find free Wi-Fi without a password! Structured hunting starts with a testable hypothesis based on threat intelligence: 'Adversaries targeting South Indian energy firms use scheduled tasks for persistence. Let us inspect Event ID 4698 across all domain controllers.'",
        "notes_pedagogy": "HUMOR ANCHOR: Wandering campus for free Wi-Fi vs structured hunting. Emphasize the 4-step hunt model."
    },

    # SLIDE 24: MITRE D3FEND Countermeasure Graph
    {
        "title": "MITRE D3FEND Countermeasures",
        "day": "DAY 02",
        "module": "MOD-02: THREAT MODELING",
        "session": "D3FEND",
        "ref": "Handbook Day 2 Section 2.5",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-purple">DEFENSIVE ONTOLOGY</div>
            <h2>MITRE D3FEND: The Countermeasure Knowledge Graph</h2>
            <p>While ATT&CK catalogs offense, D3FEND catalogs precise defensive engineering countermeasures.</p>
            
            <div class="grid-3" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan);">MODEL & DETECT</strong>
                <ul style="font-size: 12px; color: var(--text-secondary); margin-top: 8px; line-height: 1.7;">
                  <li><strong>Process Lineage Analysis:</strong> Trace parent-child relationship (Word ➔ PowerShell).</li>
                  <li><strong>File Access Pattern:</strong> Detect rapid mass file encryption signatures.</li>
                  <li><strong>Identifier Activity Analysis:</strong> Detect pass-the-hash ticket reuse.</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--electric-blue);">ISOLATE & DECEIVE</strong>
                <ul style="font-size: 12px; color: var(--text-secondary); margin-top: 8px; line-height: 1.7;">
                  <li><strong>Process Segment Execution:</strong> Constrain unsigned binaries in isolated containers.</li>
                  <li><strong>Decoy Environment:</strong> Deploy honeypot Active Directory accounts (honeytokens).</li>
                  <li><strong>Network Traffic Filtering:</strong> Null-route suspicious egress IP sockets.</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--emerald-pass);">EVICT & RESTORE</strong>
                <ul style="font-size: 12px; color: var(--text-secondary); margin-top: 8px; line-height: 1.7;">
                  <li><strong>Credential Invalidation:</strong> Force immediate Kerberos TGT double-reset.</li>
                  <li><strong>Process Termination:</strong> Surgically kill injected memory threads.</li>
                  <li><strong>Artifact Eviction:</strong> Remove malicious scheduled tasks and persistence keys.</li>
                </ul>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "ATT&CK tells you how you get attacked; D3FEND tells you how to engineer the defense. Notice the categories: Model, Detect, Isolate, Deceive, and Evict.",
        "notes_pedagogy": "Introduce D3FEND as the engineering balance to ATT&CK offense."
    },

    # SLIDE 25: Guided Lab 3 Walkthrough
    {
        "title": "Guided Lab 3: ATT&CK Navigator Layering",
        "day": "DAY 02",
        "module": "MOD-02: THREAT MODELING",
        "session": "LAB-03",
        "ref": "Handbook Lab Manual 3",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-blue">HANDS-ON LABORATORY</div>
            <h2>Lab 3: ATT&CK Navigator Matrix Layering & Coverage Scoring</h2>
            <p>Workstation Target: <code>C:\\ThreatIntel_Labs\\Lab03_ATTACK\\</code> | Time Allocated: 60 Minutes</p>
            
            <div class="grid-2" style="margin-top: 16px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 14px;">20-Step Lab Milestones</strong>
                <ul style="font-size: 12px; color: var(--text-secondary); margin-top: 8px; line-height: 1.8;">
                  <li><strong>Steps 1–5:</strong> Open Navigator v5 locally, create enterprise matrix layer.</li>
                  <li><strong>Steps 6–10:</strong> Select techniques for UNC-PHOENIX (T1059.001, T1055, T1053, T1550).</li>
                  <li><strong>Steps 11–15:</strong> Assign Threat score (100) and color gradient (Deep Red).</li>
                  <li><strong>Steps 16–20:</strong> Import SOC detection layer, apply arithmetic, export JSON gap dossier.</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--neon-amber); font-size: 14px;">Lab Troubleshooting & Fallbacks</strong>
                <p style="font-size: 12px; margin-top: 8px;">
                  If the public MITRE Navigator website fails to render due to campus proxy timeouts, launch the local offline node instance:
                </p>
                <div class="terminal-buffer" style="margin: 8px 0; font-size: 11px;">
                  <div class="terminal-body">
<span class="terminal-cmd"># Local Classroom Navigator Server:</span>
cd C:\\ThreatIntel_Labs\\Lab03_ATTACK\\local_navigator\\
python -m http.server 8080 ➔ Browse http://localhost:8080
                  </div>
                </div>
                <div style="font-size: 11px; color: var(--text-muted);">Pass Criterion: Valid JSON layer showing calculated gap scores submitted.</div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Turn to your workstations. Launch ATT&CK Navigator. If campus egress is slow, run the local Python HTTP server on port 8080. You have 60 minutes to complete the 20 milestones.",
        "notes_pedagogy": "Reinforce the local fallback server to ensure smooth lab execution."
    },

    # SLIDE 26: Day 2 Knowledge Check
    {
        "title": "Day 2 Knowledge Check",
        "day": "DAY 02",
        "module": "MOD-02: THREAT MODELING",
        "session": "CHECKPOINT",
        "ref": "Trainer Handbook Section 2.7",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-amber">END-OF-DAY CHECKPOINT</div>
            <h2>Day 2 Knowledge Check: Threat Modeling Mastery</h2>
            <p>Evaluate your defensive reasoning before we transition into Day 3 OSINT standards.</p>
            
            <div class="interactive-decision-box" style="margin-top: 20px;">
              <strong style="color: #FFF; font-size: 15px;">Question for Pod 5 & Pod 6:</strong>
              <p style="font-size: 13px; color: var(--text-secondary); margin: 8px 0 14px 0;">
                Why does David Bianco place TTPs at the apex of the Pyramid of Pain, and what makes TTP detection fundamentally different from file hash detection?
              </p>
              <div class="decision-options">
                <button class="decision-btn" onclick="selectDecision(this, false, 'Incorrect: TTPs are actually harder to detect than hashes, but they inflict vastly greater operational disruption on the adversary.')">
                  <span>A) Because TTPs are easier to detect in firewalls than file hashes, so detection costs are lower.</span>
                  <span>➔</span>
                </button>
                <button class="decision-btn" onclick="selectDecision(this, true, 'Correct! Changing a hash costs an adversary 1 second. Breaking a TTP forces the adversary to retrain operators, rewrite malware frameworks, and redesign their entire attack methodology.')">
                  <span>B) Because changing a hash costs zero effort, whereas changing TTPs forces the adversary to completely reinvent their operational tradecraft.</span>
                  <span>➔</span>
                </button>
              </div>
              <div class="decision-explanation" style="margin-top: 12px; font-size: 13px; font-family: var(--font-mono);"></div>
            </div>
          </div>
        ''',
        "notes_say": "Pod 5 and Pod 6, review the question. Why are TTPs at the top? Excellent choice! Hashes cost nothing to change. Breaking TTPs forces the adversary to burn time, money, and tooling.",
        "notes_pedagogy": "Solidify the Pyramid of Pain lesson before moving into STIX/TAXII standards."
    },

    # SLIDE 27: Day 3 Launch
    {
        "title": "Day 3 Launch & Objectives",
        "day": "DAY 03",
        "day_start": 3,
        "module": "MOD-03: OSINT & STIX/TAXII",
        "session": "SES-03 (1:00–5:00 PM)",
        "ref": "Handbook Module 3",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">MODULE 03 LAUNCH</div>
            <h2>Open-Source Intelligence & Threat Sharing Standards (STIX 2.1 & TAXII 2.1)</h2>
            <p>Session ID: SES-03 | Scheduled Net Teaching: 220 Minutes | Refreshment Break: 3:00 PM (20 min)</p>
            
            <div class="grid-2" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 15px;">Target Learning Outcomes (PLO-3)</strong>
                <ul style="font-size: 13px; color: var(--text-secondary); margin-top: 10px; line-height: 1.7;">
                  <li><strong>Defensive OSINT:</strong> Execute passive reconnaissance across DNS, WHOIS, and SSL/TLS.</li>
                  <li><strong>Indicator Lifecycle:</strong> Track degradation and aging to prevent firewall bloat.</li>
                  <li><strong>STIX 2.1 Architecture:</strong> Construct valid SDOs, SCOs, and SROs in JSON.</li>
                  <li><strong>TAXII 2.1 Services:</strong> Query collections, API roots, and status endpoints.</li>
                  <li><strong>Contextual Enrichment:</strong> Combine Admiralty confidence with recency metrics.</li>
                  <li><strong>Enterprise Feeds:</strong> Contrast IBM X-Force Exchange with open-source MISP.</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--electric-blue); font-size: 15px;">Hands-On Milestone: LAB-02</strong>
                <p style="font-size: 13px; margin-top: 10px;">
                  Every analyst will write a Python script utilizing the official <code style="color: var(--cyber-cyan);">stix2</code> library to generate a valid STIX 2.1 Threat Bundle for <strong>UNC-PHOENIX</strong>, validate schema compliance, and query TAXII 2.1 collections via <code>taxii2-client</code>.
                </p>
                <div style="margin-top: 16px; padding: 10px; background: rgba(0, 242, 254, 0.08); border-radius: 6px; border: 1px dashed var(--cyber-cyan); font-family: var(--font-mono); font-size: 12px; color: var(--cyber-cyan);">
                  TARGET FILE: unc_phoenix_stix_bundle.json // LAB-02 COMPLETE
                </div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Good afternoon, colleagues, and welcome to Day 3 in LH3. Mid-week is here! I saw several of you debating at the canteen whether filter coffee or tea is the superior fuel for cyber defense. In LH3, both are acceptable as long as your packets are properly inspected! Today we tackle the universal language of threat intelligence: STIX 2.1 and TAXII 2.1.",
        "notes_pedagogy": "HUMOR ANCHOR: Friendly canteen coffee vs. tea debate. Introduce STIX 2.1 as the universal common language."
    },

    # SLIDE 28: Defensive OSINT & Passive Recon
    {
        "title": "Defensive OSINT & Passive Recon",
        "day": "DAY 03",
        "module": "MOD-03: OSINT & STIX/TAXII",
        "session": "CON-01",
        "ref": "Handbook Day 3 Concept 1",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-blue">PASSIVE RECONNAISSANCE</div>
            <h2>Defensive OSINT: Uncovering Infrastructure Without Alerting the Adversary</h2>
            <p>Gathering evidence from public repositories without touching adversary systems directly.</p>
            
            <div class="grid-3" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan);">CERTIFICATE TRANSPARENCY</strong>
                <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 6px;">Tool: crt.sh / Censys</div>
                <p style="font-size: 13px;">Public append-only cryptographic logs. Reveals adversary subdomains, staging infrastructure, and issuance times hours before an attack launches.</p>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--electric-blue);">PASSIVE DNS REPLICATION</strong>
                <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 6px;">Tool: SecurityTrails / VirusTotal</div>
                <p style="font-size: 13px;">Historical mapping of domain-to-IP resolutions. Exposes Fast-Flux rotation, hosting tenancy shifts, and related adversary staging domains.</p>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--neon-amber);">BGP & ASN ROUTING</strong>
                <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 6px;">Tool: BGPView / Hurricane Electric</div>
                <p style="font-size: 13px;">Autonomous System Number lookup. Identifies bulletproof hosting providers, transit routes, and geographic staging hubs.</p>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "What is OSINT? OSINT is basically the digital version of your neighborhood relatives! You haven't even received your semester marks card from the university portal yet, but your aunt in Ernakulam already called your mother to ask why you got a B+ in Operating Systems! How did she find out? Passive reconnaissance across public sources! Let us see how defensive security uses those same public signals to track adversary infrastructure.",
        "notes_pedagogy": "HUMOR ANCHOR: The neighborhood relative who knows your marks before you do! Demystifies passive reconnaissance."
    },

    # SLIDE 29: Indicator Lifecycle & Aging
    {
        "title": "Indicator Lifecycle & Aging Dynamics",
        "day": "DAY 03",
        "module": "MOD-03: OSINT & STIX/TAXII",
        "session": "CON-02",
        "ref": "Handbook Day 3 Concept 2",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-amber">OPERATIONAL LIFECYCLE</div>
            <h2>The Indicator Lifecycle: Managing Expiration & Degradation</h2>
            <p>Indicators decay over time. Without automated expiration, firewalls suffer catastrophic state bloat.</p>
            
            <div class="grid-4" style="margin-top: 24px; font-size: 13px;">
              <div class="cyber-card">
                <span class="cyber-badge badge-blue">PHASE 1: DISCOVERED</span>
                <div style="font-weight: 700; color: #FFF; margin: 10px 0 4px 0;">Observation</div>
                <p style="font-size: 12px;">New IP or hash identified in external bulletin or honeypot. Confidence: Pending verification.</p>
              </div>
              <div class="cyber-card" style="border-color: var(--alert-crimson);">
                <span class="cyber-badge badge-crimson">PHASE 2: ACTIVE</span>
                <div style="font-weight: 700; color: #FFF; margin: 10px 0 4px 0;">Enforced Blocking</div>
                <p style="font-size: 12px;">Corroborated by internal telemetry. Pushed to active perimeter blocklists. Lifespan timer starts.</p>
              </div>
              <div class="cyber-card">
                <span class="cyber-badge badge-amber">PHASE 3: DEPRECATED</span>
                <div style="font-weight: 700; color: #FFF; margin: 10px 0 4px 0;">Aging Out</div>
                <p style="font-size: 12px;">Zero adversary traffic observed for 30 days. Removed from active blocklist; retained in SIEM historical hunt index.</p>
              </div>
              <div class="cyber-card" style="border-color: var(--emerald-pass);">
                <span class="cyber-badge badge-cyan">PHASE 4: REVOKED</span>
                <div style="font-weight: 700; color: #FFF; margin: 10px 0 4px 0;">Decommissioned</div>
                <p style="font-size: 12px;">IP confirmed reassigned to legitimate cloud customer. Fully purged from blocklists to prevent false positives.</p>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Notice Phase 3 and Phase 4: Deprecated and Revoked. If your SOC never removes indicators, your firewall state tables become huge and inspection throughput slows to a crawl. Indicators are like milk in a college hostel fridge—they have an expiration date!",
        "notes_pedagogy": "HUMOR ANCHOR: Hostel fridge milk expiration date. Emphasize why indicator aging prevents false positives and firewall latency."
    },

    # SLIDE 30: STIX 2.1 Architecture
    {
        "title": "STIX 2.1 Graph Architecture",
        "day": "DAY 03",
        "module": "MOD-03: OSINT & STIX/TAXII",
        "session": "CON-03",
        "ref": "Handbook Day 3 Concept 3",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">OPEN STANDARDS</div>
            <h2>STIX 2.1 Architecture: SDOs, SCOs & SROs</h2>
            <p>OASIS Structured Threat Information Expression: JSON graph serialization of threat intelligence.</p>
            
            <div class="grid-3" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 15px;">SDOs (Domain Objects)</strong>
                <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 6px;">The conceptual building blocks</p>
                <ul style="font-size: 12px; color: var(--text-secondary); line-height: 1.6;">
                  <li><code>threat-actor</code> (UNC-PHOENIX)</li>
                  <li><code>attack-pattern</code> (T1059.001)</li>
                  <li><code>indicator</code> (Pattern match)</li>
                  <li><code>malware</code> (BlackCat)</li>
                  <li><code>identity</code> (Victim Org)</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--electric-blue); font-size: 15px;">SCOs (Cyber Observables)</strong>
                <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 6px;">The technical empirical facts</p>
                <ul style="font-size: 12px; color: var(--text-secondary); line-height: 1.6;">
                  <li><code>ipv4-addr</code> (198.51.100.45)</li>
                  <li><code>domain-name</code> (internal-sync.com)</li>
                  <li><code>file</code> (SHA-256 hash)</li>
                  <li><code>network-traffic</code> (TLS port 443)</li>
                  <li><code>user-account</code> (Compromised ID)</li>
                </ul>
              </div>
              
              <div class="cyber-card" style="border-color: var(--neon-amber);">
                <strong style="color: var(--neon-amber); font-size: 15px;">SROs (Relationship Objects)</strong>
                <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 6px;">The connective glue</p>
                <ul style="font-size: 12px; color: var(--text-secondary); line-height: 1.6;">
                  <li><code>relationship</code> (uses, indicates, targets)</li>
                  <li><code>sighting</code> (internal empirical detection)</li>
                  <li><em>Connects source_ref ➔ target_ref</em></li>
                  <li>Enables graph visualization!</li>
                </ul>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "STIX 2.1 is the universal language of threat sharing. Why do we need it? Imagine a college lab where every student writes code in a different format: one in Python, one on a ruled sheet, one in Malayalam, and one carved on the desk! The external examiner would reject everything. STIX 2.1 standardizes SDOs, SCOs, and SROs into clean JSON that every machine can parse.",
        "notes_pedagogy": "HUMOR ANCHOR: Submitting lab records in 4 different handwriting formats vs. standard JSON. Walk through the 3 core STIX object types."
    },

    # SLIDE 31: TAXII 2.1 Protocol
    {
        "title": "TAXII 2.1 Transport Protocol",
        "day": "DAY 03",
        "module": "MOD-03: OSINT & STIX/TAXII",
        "session": "CON-04",
        "ref": "Handbook Day 3 Concept 4",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-blue">SECURE TRANSPORT</div>
            <h2>TAXII 2.1: Trusted Automated eXchange of Intelligence Information</h2>
            <p>The RESTful API protocol engineered specifically to exchange STIX 2.1 bundles over HTTPS.</p>
            
            <div class="grid-2" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 15px;">TAXII 2.1 Endpoint Hierarchy:</strong>
                <div class="terminal-buffer" style="margin: 10px 0; font-size: 12px;">
                  <div class="terminal-body">
<span class="terminal-cmd">GET /taxii2/</span> ➔ Server Discovery & Title
<span class="terminal-cmd">GET /api-root-1/</span> ➔ Max Content Length & Auth
<span class="terminal-cmd">GET /api-root-1/collections/</span> ➔ List Threat Feeds
<span class="terminal-cmd">GET /collections/{id}/objects/</span> ➔ Download STIX Bundle
<span class="terminal-cmd">POST /collections/{id}/objects/</span> ➔ Ingest Intelligence
                  </div>
                </div>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--electric-blue); font-size: 15px;">Operational Protocol Mechanics:</strong>
                <ul style="font-size: 13px; color: var(--text-secondary); margin-top: 8px; line-height: 1.7;">
                  <li><strong>Header Requirement:</strong> <code>Accept: application/taxii+json;version=2.1</code></li>
                  <li><strong>Authentication:</strong> HTTP Basic, API Bearer Tokens, or mTLS certificates.</li>
                  <li><strong>Pagination:</strong> <code>?limit=100&added_after=2026-10-01T00:00:00Z</code></li>
                  <li><strong>Delivery Metaphor:</strong> If STIX is the letter, TAXII is the postman delivering it to your firewall!</li>
                </ul>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "If STIX is the letter, TAXII is the postman. Or better yet: STIX is the hot samosa, and TAXII is the canteen boy who brings it straight to your table at 4:15 PM! It uses pure RESTful HTTPS, JSON headers, and collection endpoints.",
        "notes_pedagogy": "HUMOR ANCHOR: Samosa and canteen delivery boy analogy. Emphasize the required TAXII 2.1 Accept header."
    },

    # SLIDE 32: Contextual Enrichment & Scoring
    {
        "title": "Contextual Enrichment & Scoring",
        "day": "DAY 03",
        "module": "MOD-03: OSINT & STIX/TAXII",
        "session": "CON-05",
        "ref": "Handbook Day 3 Concept 5",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-amber">SCORING ALGORITHM</div>
            <h2>Contextual Indicator Scoring: Beyond Raw Reputation</h2>
            <p>Calculating composite confidence from multiple weighted intelligence dimensions.</p>
            
            <div class="grid-3" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan);">DIMENSION 1: SOURCE PEDIGREE</strong>
                <p style="font-size: 13px; margin-top: 6px;">NATO Admiralty Reliability score. Government DFIR bulletin (B) carries vastly greater weight than anonymous pastebins (E/F).</p>
                <div style="font-family: var(--font-mono); font-size: 11px; color: var(--text-highlight);">Weight: 35% of composite</div>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--electric-blue);">DIMENSION 2: RECENCY & AGING</strong>
                <p style="font-size: 13px; margin-top: 6px;">First observed vs. Last observed. Indicators decay rapidly: confidence degrades 50% after 14 days without active C2 telemetry.</p>
                <div style="font-family: var(--font-mono); font-size: 11px; color: var(--text-highlight);">Weight: 30% of composite</div>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--neon-amber);">DIMENSION 3: SIGHTINGS & CONTEXT</strong>
                <p style="font-size: 13px; margin-top: 6px;">Corroborating sightings in internal SIEM logs or sandbox detonation traces. Multi-source sightings eliminate false positives.</p>
                <div style="font-family: var(--font-mono); font-size: 11px; color: var(--text-highlight);">Weight: 35% of composite</div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Never rely on a single vendor's reputation score. We calculate a composite score: 35% source pedigree, 30% recency, and 35% internal sightings. That is how enterprise SOCs avoid blocking benign infrastructure.",
        "notes_pedagogy": "Walk through the 3-part composite scoring formula."
    },

    # SLIDE 33: Enterprise Feeds: IBM X-Force & MISP
    {
        "title": "Enterprise Threat Feeds: IBM X-Force & MISP",
        "day": "DAY 03",
        "module": "MOD-03: OSINT & STIX/TAXII",
        "session": "FEEDS",
        "ref": "Handbook Day 3 Section 3.4",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">ECOSYSTEM COMPARISON</div>
            <h2>Commercial vs. Open-Source Threat Intelligence Platforms</h2>
            <p>Integrating commercial scale with community-driven collaborative defense.</p>
            
            <div class="grid-2" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--electric-blue); font-size: 15px;">IBM X-FORCE EXCHANGE</strong>
                <ul style="font-size: 13px; color: var(--text-secondary); margin-top: 8px; line-height: 1.7;">
                  <li><strong>Scale:</strong> Billions of daily web requests, spam traps, and global sensor networks.</li>
                  <li><strong>Strengths:</strong> High-fidelity threat group profiling, automated risk scores, commercial SLA.</li>
                  <li><strong>Integration:</strong> Native integration with QRadar SIEM and SOAR playbooks.</li>
                  <li><strong>Format:</strong> RESTful API with STIX 2.1 and TAXII 2.1 collection feeds.</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 15px;">MISP (MALWARE INFORMATION SHARING PLATFORM)</strong>
                <ul style="font-size: 13px; color: var(--text-secondary); margin-top: 8px; line-height: 1.7;">
                  <li><strong>Scale:</strong> Open-source, peer-to-peer threat sharing communities globally.</li>
                  <li><strong>Strengths:</strong> Complete on-premise data sovereignty, zero licensing cost, flexible tagging.</li>
                  <li><strong>Integration:</strong> OpenCTI, Zeek, Suricata, and custom Python ingestion pipelines.</li>
                  <li><strong>Format:</strong> MISP JSON, STIX 2.1, CSV, Snort, Suricata, and Bro/Zeek formats.</li>
                </ul>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Notice how IBM X-Force and MISP complement each other. IBM gives you global enterprise scale and verified research. MISP gives you trusted sector-specific community sharing and complete data sovereignty.",
        "notes_pedagogy": "Highlight both IBM X-Force and MISP as realistic tools in an enterprise security architecture."
    },

    # SLIDE 34: Demonstration 3 Walkthrough
    {
        "title": "Demonstration 3: Python STIX 2.1 Bundle Generation",
        "day": "DAY 03",
        "module": "MOD-03: OSINT & STIX/TAXII",
        "session": "DEMO-03",
        "ref": "Handbook Demonstration 3",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">TRAINER DEMONSTRATION</div>
            <h2>Demo 3: Programmatic STIX 2.1 Generation via Python</h2>
            <p>Creating verified SDOs, SCOs, and SROs using the official <code>stix2</code> Python SDK.</p>
            
            <div class="terminal-buffer" style="margin-top: 16px;">
              <div class="terminal-header">
                <div class="terminal-dots"><span class="dot dot-red"></span><span class="dot dot-yellow"></span><span class="dot dot-green"></span></div>
                <span>generate_stix_bundle.py // PYTHON 3.11</span>
              </div>
              <div class="terminal-body" style="font-size: 12px;">
<span style="color: #64748B;"># Import official OASIS stix2 library:</span>
<span class="terminal-cmd">from stix2 import ThreatActor, Indicator, Relationship, Bundle</span>

<span style="color: #64748B;"># 1. Define Threat Actor SDO:</span>
actor = ThreatActor(name=<span style="color: #A5D6A7;">"UNC-PHOENIX"</span>, threat_actor_types=[<span style="color: #A5D6A7;">"cybercrime"</span>])

<span style="color: #64748B;"># 2. Define Indicator SDO with STIX Pattern:</span>
indicator = Indicator(indicator_types=[<span style="color: #A5D6A7;">"malicious-activity"</span>],
                      pattern=<span style="color: #A5D6A7;">"[ipv4-addr:value = '198.51.100.45']"</span>, pattern_type=<span style="color: #A5D6A7;">"stix"</span>)

<span style="color: #64748B;"># 3. Connect via SRO Relationship:</span>
rel = Relationship(source_ref=indicator.id, relationship_type=<span style="color: #A5D6A7;">"indicates"</span>, target_ref=actor.id)

<span style="color: #64748B;"># 4. Export Validated Bundle:</span>
bundle = Bundle(objects=[actor, indicator, rel])
print(bundle.serialize(pretty=True))
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Look at the terminal code on screen. In just ten lines of Python using the stix2 library, we construct a ThreatActor, an Indicator with a formal STIX pattern, and bind them with an 'indicates' relationship into a valid Bundle.",
        "notes_pedagogy": "Demonstrate the clean syntax of the Python stix2 library. Show that STIX is just readable JSON under the hood."
    },

    # SLIDE 35: Guided Lab 2 Walkthrough
    {
        "title": "Guided Lab 2: STIX 2.1 & TAXII 2.1 Execution",
        "day": "DAY 03",
        "module": "MOD-03: OSINT & STIX/TAXII",
        "session": "LAB-02",
        "ref": "Handbook Lab Manual 2",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-blue">HANDS-ON LABORATORY</div>
            <h2>Lab 2: STIX 2.1 Bundle Construction & TAXII 2.1 Ingestion</h2>
            <p>Workstation Target: <code>C:\\ThreatIntel_Labs\\Lab02_STIX_TAXII\\</code> | Time Allocated: 60 Minutes</p>
            
            <div class="grid-2" style="margin-top: 16px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 14px;">20-Step Lab Milestones</strong>
                <ul style="font-size: 12px; color: var(--text-secondary); margin-top: 8px; line-height: 1.8;">
                  <li><strong>Steps 1–5:</strong> Activate Python venv, verify <code>pip show stix2 taxii2-client</code>.</li>
                  <li><strong>Steps 6–10:</strong> Write Python script to instantiate ThreatActor, Malware, and IPv4 SCO.</li>
                  <li><strong>Steps 11–15:</strong> Construct bidirectional SROs: <code>uses</code>, <code>indicates</code>, and <code>targets</code>.</li>
                  <li><strong>Steps 16–20:</strong> Query local TAXII server, validate bundle schema, export final JSON.</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--neon-amber); font-size: 14px;">Lab Troubleshooting & Fallbacks</strong>
                <p style="font-size: 12px; margin-top: 8px;">
                  If schema validation throws <code>InvalidObjectError: Missing required property 'pattern'</code>, verify your STIX pattern syntax:
                </p>
                <div class="terminal-buffer" style="margin: 8px 0; font-size: 11px;">
                  <div class="terminal-body">
<span class="terminal-cmd"># Correct Pattern Syntax:</span>
pattern="[file:hashes.'SHA-256' = 'e3b0c44...']"
                  </div>
                </div>
                <div style="font-size: 11px; color: var(--text-muted);">Pass Criterion: Schema-validated STIX 2.1 JSON bundle submitted.</div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Turn to your workstations. Open Lab 2. You will write the Python script to generate the STIX bundle for UNC-PHOENIX and push it to the local TAXII endpoint. You have 60 minutes.",
        "notes_pedagogy": "Guide students to watch out for exact STIX pattern quotation rules (single vs. double quotes)."
    },

    # SLIDE 36: Day 3 Knowledge Check
    {
        "title": "Day 3 Knowledge Check",
        "day": "DAY 03",
        "module": "MOD-03: OSINT & STIX/TAXII",
        "session": "CHECKPOINT",
        "ref": "Trainer Handbook Section 3.7",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-amber">END-OF-DAY CHECKPOINT</div>
            <h2>Day 3 Knowledge Check: Standards & Ingestion</h2>
            <p>Verify your mastery of STIX and TAXII before we move into engine-room telemetry.</p>
            
            <div class="interactive-decision-box" style="margin-top: 20px;">
              <strong style="color: #FFF; font-size: 15px;">Question for Pod 1 & Pod 2:</strong>
              <p style="font-size: 13px; color: var(--text-secondary); margin: 8px 0 14px 0;">
                Why does STIX 2.1 strictly separate Cyber Observable Objects (SCOs) like an IPv4 address from Indicator SDOs?
              </p>
              <div class="decision-options">
                <button class="decision-btn" onclick="selectDecision(this, false, 'An IP is not inherently malicious. A raw IP address is just a network observable fact.')">
                  <span>A) Because every IPv4 address observed in threat intelligence is automatically malicious.</span>
                  <span>➔</span>
                </button>
                <button class="decision-btn" onclick="selectDecision(this, true, 'Correct! An IPv4 address is an objective network observable (SCO). It only becomes an Indicator (SDO) when bound to an explicit detection pattern, time window, and confidence rationale.')">
                  <span>B) Because an IP is an objective observable fact. It only becomes an Indicator when paired with malicious context and detection patterns.</span>
                  <span>➔</span>
                </button>
              </div>
              <div class="decision-explanation" style="margin-top: 12px; font-size: 13px; font-family: var(--font-mono);"></div>
            </div>
          </div>
        ''',
        "notes_say": "Pod 1 and Pod 2, review the question. Why does STIX separate observables from indicators? Exactly! An IP address is just an observable fact. It only becomes an indicator when bound to a malicious pattern. That distinction is the core of modern threat sharing.",
        "notes_pedagogy": "Reinforce the SCO vs SDO distinction. Bridge smoothly to Day 4: telemetry correlation."
    }
]
