"""
build_animated_day_wise_system.py
Compiles the upgraded, animated, interactive 6 Day-Wise HTML Presentations
and the upgraded Master Presentation Portal with Three.js 3D scenes,
GSAP coordinated timelines, and original animated cybersecurity mascots.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRESENTATION_DIR = BASE_DIR if os.path.exists(os.path.join(BASE_DIR, "day-01")) else os.path.join(BASE_DIR, "Threat_Intelligence_Incident_Response_Animated_Presentation")
SHARED_DIR = os.path.join(PRESENTATION_DIR, "shared")

sys.path.append(PRESENTATION_DIR)
from slides_act0_act1 import ACT0_ACT1_SLIDES
from slides_act2_act3 import ACT2_ACT3_SLIDES
from slides_act4_act5 import ACT4_ACT5_SLIDES
from slides_act6 import ACT6_SLIDES

# Make deep copies of slide sets to customize with interactive visual components
import copy
slides_d1 = copy.deepcopy(ACT0_ACT1_SLIDES)
slides_d2 = copy.deepcopy(ACT2_ACT3_SLIDES[:10])
slides_d3 = copy.deepcopy(ACT2_ACT3_SLIDES[10:])
slides_d4 = copy.deepcopy(ACT4_ACT5_SLIDES[:11])
slides_d5 = copy.deepcopy(ACT4_ACT5_SLIDES[11:])
slides_d6 = copy.deepcopy(ACT6_SLIDES)

# ==============================================================================
# INJECT ENHANCED INTERACTIVE SCENES & MASCOTS INTO TARGET SLIDES
# ==============================================================================

# --- DAY 1 ENHANCEMENTS ---
# Slide 01: Welcome with Threat Detective Mascot
slides_d1[0]["content"] = '''
  <div style="text-align: center; padding: 25px 20px;">
    <div style="display: flex; justify-content: center; align-items: center; gap: 18px; margin-bottom: 12px;">
      <div id="mascot-title-detective" data-mascot="detective" data-mood="neutral" data-width="65" data-height="65"></div>
      <div class="cyber-badge badge-cyan animate-fade-up">OPERATIONAL CYBERSECURITY IMMERSION</div>
      <div id="mascot-title-guardian" data-mascot="guardian" data-mood="defending" data-width="65" data-height="65"></div>
    </div>
    <h1 class="animate-fade-up delay-1" style="font-size: 2.6em; margin-bottom: 8px;">Threat Intelligence &<br><span style="color: var(--cyber-cyan);">Incident Response</span></h1>
    <p class="animate-fade-up delay-2" style="font-size: 1.1em; color: var(--text-secondary); max-width: 800px; margin: 0 auto 24px auto;">
      Transforming Alert Janitors into Adversary-Centric Defenders Across Multi-Source Enterprise Telemetry
    </p>
    
    <div class="grid-3 animate-fade-up delay-3" style="max-width: 900px; margin: 0 auto; text-align: left;">
      <div class="cyber-card">
        <div style="color: var(--cyber-cyan); font-family: var(--font-mono); font-size: 11px;">TRAINING VENUE</div>
        <div style="font-size: 15px; font-weight: 700; color: #FFF; margin-top: 4px;">LH3 – 4th Floor</div>
        <div style="color: var(--text-muted); font-size: 12px;">SOC Pod Setup (24 Workstations)</div>
      </div>
      <div class="cyber-card">
        <div style="color: var(--electric-blue); font-family: var(--font-mono); font-size: 11px;">SCHEDULE & VOLUME</div>
        <div style="font-size: 15px; font-weight: 700; color: #FFF; margin-top: 4px;">26–31 October 2026</div>
        <div style="color: var(--text-muted); font-size: 12px;">26.5h Gross / 23.4h Net (6 Days)</div>
      </div>
      <div class="cyber-card">
        <div style="color: var(--neon-amber); font-family: var(--font-mono); font-size: 11px;">LEAD INSTRUCTOR</div>
        <div style="font-size: 15px; font-weight: 700; color: #FFF; margin-top: 4px;">Gopinath A</div>
        <div style="color: var(--text-muted); font-size: 12px;">Chief AI Knowledge Architect</div>
      </div>
    </div>
  </div>
  <script>
    setTimeout(() => {
      const d = document.getElementById('mascot-title-detective');
      const g = document.getElementById('mascot-title-guardian');
      if (d && window.CyberCharacters) d.innerHTML = window.CyberCharacters.getDetective('neutral', 65, 65);
      if (g && window.CyberCharacters) g.innerHTML = window.CyberCharacters.getGuardian('defending', 65, 65);
    }, 100);
  </script>
'''

# Slide 06: Opening Scenario with Alert Bot Alarm
slides_d1[5]["content"] = '''
  <div style="text-align: left;">
    <div style="display: flex; justify-content: space-between; align-items: center;">
      <div class="cyber-badge badge-red">OPENING ENGAGEMENT SCENARIO</div>
      <div id="mascot-opening-alert" data-mascot="alertBot" data-mood="alarm" data-width="60" data-height="60"></div>
    </div>
    <h2>The Unsanctioned Dormitory Hotspot & Lateral Pivot</h2>
    <p>A Real-World Engineering Dilemma: Triage Under Time Pressure</p>
    
    <div class="grid-2" style="margin-top: 14px;">
      <div class="cyber-card">
        <strong style="color: var(--alert-crimson); font-size: 14px;">The Incident Telemetry</strong>
        <p style="font-size: 12px; color: var(--text-secondary); margin-top: 6px; line-height: 1.6;">
          At 02:14 IST, the campus perimeter NIDS flags an outbound beacon from an IP registered to Student Hostel Block C. The user agent identifies as an outdated BitTorrent client, but the payload contains an encoded Cobalt Strike stager transmitting over Port 443 to a bulletproof server in Eastern Europe.
        </p>
        <div class="terminal-buffer" style="margin-top: 10px; font-size: 11px;">
          <div class="terminal-body">
[ALERT] 2026-10-26T02:14:09.112 IST<br>
SRC: 10.14.22.109 (Hostel-C-Room-304) -&gt; DST: 185.220.101.5:443<br>
SIG: ET MALWARE Cobalt Strike Beacon Observed (M2)<br>
ACTION: Alert Logged (Unblocked)
          </div>
        </div>
      </div>
      
      <div class="cyber-card">
        <strong style="color: var(--neon-amber); font-size: 14px;">The Operational Choice</strong>
        <p style="font-size: 12px; color: var(--text-secondary); margin-top: 6px;">
          You are the Tier-1 analyst on night shift. What is your immediate next move?
        </p>
        <div class="decision-options" style="margin-top: 10px; display: flex; flex-direction: column; gap: 8px;">
          <button class="decision-btn" onclick="selectDecision(this, false, 'Blackholing the IP alerts the threat actor that they are discovered and causes them to switch to dormant persistence mechanisms.')">
            A) Immediately null-route the IP at the core firewall.
          </button>
          <button class="decision-btn" onclick="selectDecision(this, true, 'Correct! Query passive DNS and flow telemetry to map the full blast radius before executing coordinated containment.')">
            B) Pivot into proxy logs and DHCP records to identify the infected host and map lateral movement.
          </button>
          <button class="decision-btn" onclick="selectDecision(this, false, 'Rebooting destroys the volatile memory containing the unencrypted Cobalt Strike beacon payload and inject keys.')">
            C) Call the hostel warden and ask them to restart the floor router.
          </button>
          <div class="decision-explanation" style="font-size: 11px; margin-top: 4px; min-height: 24px;"></div>
        </div>
      </div>
    </div>
  </div>
  <script>
    setTimeout(() => {
      const el = document.getElementById('mascot-opening-alert');
      if (el && window.CyberCharacters) el.innerHTML = window.CyberCharacters.getAlertBot('alarm', 60, 60);
    }, 100);
  </script>
'''

# Slide 10: Threat Actor Categorization with 3D Cyber Threat Globe
slides_d1[9]["content"] = '''
  <div style="text-align: left;">
    <div class="cyber-badge badge-blue">ADVERSARY TYPOLOGY</div>
    <h2>Threat Actor Spectrum & Geopolitical Motivation</h2>
    <p>Categorizing Motivation, Resources, Sophistication, and Attribution Confidence</p>
    
    <div class="grid-2" style="margin-top: 14px;">
      <div class="cyber-card">
        <strong style="color: var(--cyber-cyan); font-size: 14px;">The 4 Adversary Archetypes</strong>
        <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 8px;">
          <div style="background: rgba(255,255,255,0.03); padding: 6px 10px; border-left: 3px solid var(--text-muted); border-radius: 4px; font-size: 11px;">
            <strong style="color: #FFF;">1. Opportunistic / Script Kiddies:</strong> Commodity malware, public exploits, zero operational security.
          </div>
          <div style="background: rgba(255,179,0,0.05); padding: 6px 10px; border-left: 3px solid var(--neon-amber); border-radius: 4px; font-size: 11px;">
            <strong style="color: var(--neon-amber);">2. Cybercriminal Syndicates (FIN):</strong> Financial extortion, Ransomware-as-a-Service (RaaS), fast ROI.
          </div>
          <div style="background: rgba(179,136,255,0.05); padding: 6px 10px; border-left: 3px solid var(--purple-intel); border-radius: 4px; font-size: 11px;">
            <strong style="color: var(--purple-intel);">3. Hacktivists:</strong> Politically motivated defacements, DDoS, disruptive leaks, high visibility.
          </div>
          <div style="background: rgba(255,75,75,0.05); padding: 6px 10px; border-left: 3px solid var(--alert-crimson); border-radius: 4px; font-size: 11px;">
            <strong style="color: var(--alert-crimson);">4. Nation-State APTs:</strong> Multi-year persistence, custom zero-days, supply-chain infiltration.
          </div>
        </div>
      </div>
      
      <!-- 3D Globe Interactive Viewport -->
      <div>
        <div class="three-canvas-container" id="globe-3d-canvas">
          <div class="three-canvas-overlay">🌐 3D GLOBAL THREAT TELEMETRY // DRAG TO ROTATE</div>
          <svg viewBox="0 0 400 200" style="width:100%; height:100%; position:absolute; top:0; left:0; pointer-events:none;">
            <ellipse cx="200" cy="100" rx="160" ry="80" fill="none" stroke="rgba(0, 242, 254, 0.2)" stroke-dasharray="4,4"/>
            <ellipse cx="200" cy="100" rx="100" ry="80" fill="none" stroke="rgba(0, 242, 254, 0.15)"/>
            <line x1="40" y1="100" x2="360" y2="100" stroke="rgba(0, 242, 254, 0.25)"/>
            <path d="M 120 70 Q 180 20 280 110" fill="none" stroke="#FF4B4B" stroke-width="2.5" stroke-dasharray="6,4"/>
            <circle cx="120" cy="70" r="6" fill="#FF4B4B"/>
            <text x="120" y="55" fill="#FF4B4B" font-family="monospace" font-size="9" text-anchor="middle">Frankfurt C2 (198.51.100.45)</text>
            <circle cx="280" cy="110" r="6" fill="#00E676"/>
            <text x="280" y="130" fill="#00E676" font-family="monospace" font-size="9" text-anchor="middle">Bangalore SOC Pod (10.20.4.15)</text>
          </svg>
        </div>
        <div style="font-family: var(--font-mono); font-size: 10px; color: var(--text-muted); margin-top: 6px; text-align: center;">
          Active C2 telemetry arcs into Bangalore SOC Pod from Frankfurt & Virginia nodes.
        </div>
      </div>
    </div>
  </div>
'''

# Slide 11: The Traditional Intelligence Cycle with Interactive 6-Stage GSAP Pipeline
slides_d1[10]["content"] = '''
  <div style="text-align: left;">
    <div class="cyber-badge badge-cyan">INTELLIGENCE OPERATIONS</div>
    <h2>The 6-Stage Intelligence Cycle in Motion</h2>
    <p>From Tactical Consumer Requirements to Disseminated Threat Defense</p>
    
    <!-- Interactive 6-Stage Pipeline -->
    <div class="intel-cycle-container" id="intel-cycle-demo">
      <div class="intel-stages-grid">
        <div class="intel-stage-node active" onclick="activateIntelStage(0)">🎯 1. Direction</div>
        <div class="intel-stage-node" onclick="activateIntelStage(1)">📡 2. Collection</div>
        <div class="intel-stage-node" onclick="activateIntelStage(2)">⚙️ 3. Processing</div>
        <div class="intel-stage-node" onclick="activateIntelStage(3)">🔍 4. Analysis</div>
        <div class="intel-stage-node" onclick="activateIntelStage(4)">📤 5. Dissemination</div>
        <div class="intel-stage-node" onclick="activateIntelStage(5)">🔄 6. Feedback</div>
      </div>
      <div class="intel-progress-track"><div class="intel-progress-bar"></div></div>
      <div class="intel-stage-desc">Click any stage above to inspect operational intelligence flow.</div>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 10px;">
        <span style="font-family: var(--font-mono); font-size: 10px; color: var(--text-muted);">
          Click stages or button to advance through the intelligence lifecycle.
        </span>
        <button onclick="nextIntelStage()" style="padding: 6px 16px; background: var(--gradient-cyber); border: none; border-radius: 4px; font-weight: bold; cursor: pointer; color: #050814; font-size: 11px;">
          ADVANCE STAGE ▶
        </button>
      </div>
    </div>
  </div>
'''
slides_d1[10]["notes_say"] = """[SHOW:] Display the interactive 6-stage Intelligence Cycle pipeline.
[SAY:] 'Look at the pipeline on screen. Traditional training shows you a static circle with six words and expects you to memorize it. In reality, intelligence is a dynamic conveyor belt.'
[DO:] Click on Stage 1 (Direction) and advance to Stage 3 (Processing).
[OBSERVE:] The animated progress bar moves, highlighting how raw PCAPs and certificates are translated into structured data.
[ASK:] 'If an analyst skips Stage 3 (Processing) and feeds raw un-normalized logs directly into their SIEM, what happens?'
[EXPECTED ANSWER:] 'The SIEM chokes on format mismatches, false positive alerts explode, and analysts burn out.'
[REVEAL:] Click Stage 4 (Analysis) to show how structured Admiralty scoring synthesizes actionable hypotheses.
[EXPLAIN:] Connect this to our canteen coffee analogy: grinding and filtering beans produces coffee; dumping raw beans into boiling water produces chaos."""

# Slide 12: NATO Admiralty Source Scoring with Interactive Indicator Station
slides_d1[11]["content"] = '''
  <div style="text-align: left;">
    <div class="investigation-tracker-bar">
      <span style="color: var(--cyber-cyan); font-weight: bold;">🎯 MISSION: DEFEND AEROGRID // UNC-PHOENIX INVESTIGATION</span>
      <div class="tracker-progress-track"><div class="tracker-progress-fill" style="width: 16%;"></div></div>
      <span style="color: var(--text-muted);">PHASE 1: RECONNAISSANCE (DAY 1 OF 6)</span>
    </div>
    <div class="cyber-badge badge-cyan">EVIDENCE-BASED EVALUATION</div>
    <h2>NATO Admiralty Source Scoring & Indicator Station</h2>
    <p>Evaluate Source Reliability vs. Information Credibility (Click Indicators Below)</p>
    
    <div id="indicator-station-demo" class="indicator-station">
      <div style="font-family: var(--font-mono); font-size: 11px; color: #94A3B8; margin-bottom: 8px;">
        SELECT AN INCIDENT INDICATOR TO LAUNCH FORENSIC APPRAISAL:
      </div>
      <div class="indicator-pills-row">
        <button class="indicator-pill-btn active" onclick="inspectIndicator('fqdn', this)">🌐 updates-aerogrid.internal-sync[.]com</button>
        <button class="indicator-pill-btn" onclick="inspectIndicator('ip', this)">📡 198.51.100.44 (C2 Transit)</button>
        <button class="indicator-pill-btn" onclick="inspectIndicator('hash', this)">🔑 8f4b23...a9c1 (Macro Hash)</button>
      </div>
      <div class="indicator-detail-panel">
        <div style="color: var(--cyber-cyan); font-weight: 700; font-size: 1rem; margin-bottom: 4px;">
          🌐 Domain: updates-aerogrid.internal-sync[.]com
        </div>
        <div style="font-family: var(--font-mono); font-size: 11px; color: var(--neon-amber); margin-bottom: 6px;">
          Fully Qualified Domain Name (FQDN) | Admiralty: B2
        </div>
        <div style="font-size: 12px; color: #E2E8F0; line-height: 1.5; margin-bottom: 8px;">
          <strong>Context:</strong> Newly registered subdomain impersonating AeroGrid corporate IT infrastructure. Hosted on dynamic cloud infrastructure.
        </div>
        <div style="font-size: 11px; color: var(--text-muted); line-height: 1.4; margin-bottom: 6px;">
          <span style="color: #FF8A8A;">⚠️ Limitation:</span> Adversaries can abandon or re-route domains rapidly once detected. Low-to-moderate adversary pain threshold.
        </div>
        <div style="font-size: 11px; color: var(--emerald-pass); line-height: 1.4;">
          <span>🎯 Recommended Action:</span> Query Certificate Transparency logs for wildcard sibling certificates. Sinkhole DNS requests at enterprise resolvers.
        </div>
      </div>
    </div>
  </div>
'''

# --- DAY 2 ENHANCEMENTS ---
# Slide 03: Pyramid of Pain & Interactive Threat-Triage Challenge
slides_d2[2]["content"] = '''
  <div style="text-align: left;">
    <div class="investigation-tracker-bar">
      <span style="color: var(--electric-blue); font-weight: bold;">🎯 MISSION: DEFEND AEROGRID // UNC-PHOENIX INVESTIGATION</span>
      <div class="tracker-progress-track"><div class="tracker-progress-fill" style="width: 32%;"></div></div>
      <span style="color: var(--text-muted);">PHASE 2: FOOTHOLD & ATT&CK (DAY 2 OF 6)</span>
    </div>
    <div class="cyber-badge badge-blue">SOC TRIAGE CHALLENGE</div>
    <h2>Pyramid of Pain & Alert Prioritization Dilemma</h2>
    <p>Which Alert Demands Immediate Incident Commander Escalation? (Click to Choose)</p>
    
    <div id="threat-triage-demo">
      <div class="triage-challenge-grid">
        <div class="triage-alert-card" onclick="selectTriageAlert('alert-a', this)">
          <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
            <span style="font-family:var(--font-mono); font-size:10px; color:#94A3B8;">ALERT ID: 1041</span>
            <span class="cyber-badge badge-amber" style="font-size:9px;">SEV: MEDIUM</span>
          </div>
          <strong style="font-size:12px; color:#FFF;">Perimeter TCP SYN Scan</strong>
          <p style="font-size:11px; color:#94A3B8; margin-top:4px;">10,000 inbound probes on port 443 from commercial VPN exit node.</p>
        </div>
        
        <div class="triage-alert-card" onclick="selectTriageAlert('alert-b', this)">
          <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
            <span style="font-family:var(--font-mono); font-size:10px; color:#94A3B8;">ALERT ID: 1042</span>
            <span class="cyber-badge badge-red" style="font-size:9px;">SEV: CRITICAL</span>
          </div>
          <strong style="font-size:12px; color:#FF8A8A;">Encoded PowerShell on WS-041</strong>
          <p style="font-size:11px; color:#94A3B8; margin-top:4px;">powershell.exe -w hidden -enc spawning from Finance downloads folder.</p>
        </div>
        
        <div class="triage-alert-card" onclick="selectTriageAlert('alert-c', this)">
          <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
            <span style="font-family:var(--font-mono); font-size:10px; color:#94A3B8;">ALERT ID: 1043</span>
            <span class="cyber-badge badge-amber" style="font-size:9px;">SEV: LOW</span>
          </div>
          <strong style="font-size:12px; color:#FFF;">Disabled Guest Login Fails</strong>
          <p style="font-size:11px; color:#94A3B8; margin-top:4px;">3 failed NTLM auth attempts against legacy Guest account.</p>
        </div>
      </div>
      
      <div class="triage-feedback-panel">
        <span style="color:var(--text-muted); font-size:12px;">Click one of the three incoming alerts above to evaluate your triage decision.</span>
      </div>
    </div>
  </div>
'''

# Slide 20: MITRE ATT&CK Matrix Architecture with 3D Attack Surface Mesh
slides_d2[3]["content"] = '''
  <div style="text-align: left;">
    <div class="cyber-badge badge-blue">ADVERSARY BEHAVIOR</div>
    <h2>MITRE ATT&CK Matrix Architecture & 3D Topology</h2>
    <p>The Common Language of Defensive Engineering: 14 Enterprise Tactics & 3D Attack Paths</p>
    
    <div class="grid-2" style="margin-top: 14px;">
      <div class="cyber-card">
        <strong style="color: var(--cyber-cyan); font-size: 14px;">Tactics (Why) vs. Techniques (How)</strong>
        <p style="font-size: 12px; color: var(--text-secondary); margin-top: 6px; line-height: 1.6;">
          MITRE ATT&CK organizes real-world adversary behavior into 14 sequential tactical objectives (from Reconnaissance to Impact). Each tactic contains granular techniques and sub-techniques.
        </p>
        <div class="terminal-buffer" style="margin-top: 10px; font-size: 11px;">
          <div class="terminal-body">
TACTIC: Credential Access [TA0006]<br>
&nbsp;&nbsp;&boxur;&nbsp;TECHNIQUE: OS Credential Dumping [T1003]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&boxur;&nbsp;SUB-TECH: LSASS Memory [T1003.001]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&boxur;&nbsp;DETECTION: Sysmon Event ID 10 (ProcessAccess)
          </div>
        </div>
      </div>
      
      <!-- 3D Defense Mesh Viewport -->
      <div>
        <div class="three-canvas-container" id="defense-mesh-3d">
          <div class="three-canvas-overlay">🕸️ 3D ATTACK SURFACE TOPOLOGY // REAL-TIME MESH</div>
          <svg viewBox="0 0 400 180" style="width:100%; height:100%; position:absolute; top:0; left:0; pointer-events:none;">
            <line x1="80" y1="90" x2="160" y2="50" stroke="#00F2FE" stroke-width="2"/>
            <line x1="80" y1="90" x2="160" y2="130" stroke="#00F2FE" stroke-width="2"/>
            <line x1="160" y1="50" x2="260" y2="50" stroke="#4FACFE" stroke-width="2"/>
            <line x1="160" y1="130" x2="260" y2="130" stroke="#4FACFE" stroke-width="2"/>
            <line x1="260" y1="50" x2="330" y2="90" stroke="#00E676" stroke-width="2"/>
            <line x1="260" y1="130" x2="330" y2="90" stroke="#00E676" stroke-width="2"/>
            <rect x="50" y="75" width="60" height="30" rx="4" fill="#0F172A" stroke="#FF4B4B" stroke-width="1.5"/>
            <text x="80" y="94" fill="#FF4B4B" font-family="monospace" font-size="8" text-anchor="middle">DMZ Ingress</text>
            <rect x="130" y="35" width="60" height="30" rx="4" fill="#0F172A" stroke="#00F2FE" stroke-width="1.5"/>
            <text x="160" y="54" fill="#00F2FE" font-family="monospace" font-size="8" text-anchor="middle">Zeek Tap</text>
            <rect x="130" y="115" width="60" height="30" rx="4" fill="#0F172A" stroke="#4FACFE" stroke-width="1.5"/>
            <text x="160" y="134" fill="#4FACFE" font-family="monospace" font-size="8" text-anchor="middle">EDR Sysmon</text>
            <rect x="230" y="35" width="60" height="30" rx="4" fill="#0F172A" stroke="#FFB300" stroke-width="1.5"/>
            <text x="260" y="54" fill="#FFB300" font-family="monospace" font-size="8" text-anchor="middle">Tier 0 AD</text>
            <rect x="230" y="115" width="60" height="30" rx="4" fill="#0F172A" stroke="#B388FF" stroke-width="1.5"/>
            <text x="260" y="134" fill="#B388FF" font-family="monospace" font-size="8" text-anchor="middle">SIEM Pivot</text>
            <rect x="300" y="75" width="60" height="30" rx="4" fill="#0F172A" stroke="#00E676" stroke-width="1.5"/>
            <text x="330" y="94" fill="#00E676" font-family="monospace" font-size="8" text-anchor="middle">SOC Console</text>
          </svg>
        </div>
        <div style="font-family: var(--font-mono); font-size: 10px; color: var(--text-muted); margin-top: 6px; text-align: center;">
          Active nodes: Gateway (Cyan), DC Server (Amber), Workstations (Green), SCADA PLC (Red).
        </div>
      </div>
    </div>
  </div>
'''

# --- DAY 3 ENHANCEMENTS ---
# Slide 23: Indicator Aging & STIX 2.1 Graph Architecture
slides_d3[2]["content"] = '''
  <div style="text-align: left;">
    <div class="investigation-tracker-bar">
      <span style="color: var(--purple-intel); font-weight: bold;">🎯 MISSION: DEFEND AEROGRID // UNC-PHOENIX INVESTIGATION</span>
      <div class="tracker-progress-track"><div class="tracker-progress-fill" style="width: 48%;"></div></div>
      <span style="color: var(--text-muted);">PHASE 3: INFRASTRUCTURE & STIX (DAY 3 OF 6)</span>
    </div>
    <div class="cyber-badge badge-purple">INDICATOR AGING DYNAMICS</div>
    <h2>STIX 2.1 Graph & Temporal Confidence Decay</h2>
    <p>Adversary Infrastructure Lifecycle: Preventing Firewall Rule Bloat</p>
    
    <div class="grid-2" style="margin-top: 12px;">
      <div class="cyber-card">
        <strong style="color: var(--purple-intel); font-size: 13px;">STIX 2.1 Graph SDO/SRO Relationship</strong>
        <div class="terminal-buffer" style="margin-top: 8px; font-size: 11px;">
          <div class="terminal-body">
[SDO: Threat Actor] "UNC-PHOENIX" (Confidence: 90)<br>
&nbsp;&nbsp;&boxur;&nbsp;[SRO: uses] -&gt; [SDO: Tool] "Cobalt Strike"<br>
&nbsp;&nbsp;&boxur;&nbsp;[SRO: indicates] -&gt; [SDO: Indicator] "198.51.100.44"<br>
&nbsp;&nbsp;&boxur;&nbsp;[SRO: targets] -&gt; [SDO: Identity] "AeroGrid SCADA"
          </div>
        </div>
        <div style="font-size: 11px; color: var(--text-muted); margin-top: 8px;">
          STIX 2.1 links observations to actors, tools, and victims via unambiguous JSON objects.
        </div>
      </div>
      
      <div class="cyber-card">
        <strong style="color: var(--cyber-cyan); font-size: 13px;">Temporal Half-Life Decay Curve</strong>
        <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 10px;">
          <div style="display: flex; justify-content: space-between; font-size: 11px;">
            <span>Day 0 (Active Sighting):</span>
            <strong style="color: #00E676;">95% Confidence (Active Block)</strong>
          </div>
          <div style="display: flex; justify-content: space-between; font-size: 11px;">
            <span>Day 7 (No Sighting):</span>
            <strong style="color: var(--cyber-cyan);">75% Confidence (Alert Only)</strong>
          </div>
          <div style="display: flex; justify-content: space-between; font-size: 11px;">
            <span>Day 30 (Dormant):</span>
            <strong style="color: var(--neon-amber);">40% Confidence (Candidate Prune)</strong>
          </div>
          <div style="display: flex; justify-content: space-between; font-size: 11px;">
            <span>Day 90+ (Expired):</span>
            <strong style="color: var(--text-muted);">0% Confidence (Revoked/Removed)</strong>
          </div>
        </div>
        <div style="background: rgba(179,136,255,0.08); border-left: 2px solid var(--purple-intel); padding: 6px 10px; margin-top: 10px; font-size: 10px; color: #CBD5E1;">
          💡 Automatic decay prevents perimeter firewalls from choking on hundreds of thousands of stale IP blocks.
        </div>
      </div>
    </div>
  </div>
'''

# --- DAY 4 ENHANCEMENTS ---
# Slide 40: Sysmon EID 1 Process Creation Log Inspector
slides_d4[3]["content"] = '''
  <div style="text-align: left;">
    <div class="investigation-tracker-bar">
      <span style="color: var(--matrix-teal); font-weight: bold;">🎯 MISSION: DEFEND AEROGRID // UNC-PHOENIX INVESTIGATION</span>
      <div class="tracker-progress-track"><div class="tracker-progress-fill" style="width: 65%;"></div></div>
      <span style="color: var(--text-muted);">PHASE 4: TELEMETRY PIVOTING (DAY 4 OF 6)</span>
    </div>
    <div class="cyber-badge badge-teal">ENDPOINT TELEMETRY DISSECTION</div>
    <h2>Sysmon Event ID 1: Process Creation Dissector</h2>
    <p>Click Dashed Teal Hotspots to Discover Attacker Footprints and Attribution Evidence</p>
    
    <div id="log-inspector-demo" class="log-inspector-card">
      <div style="color: var(--matrix-teal); font-weight: bold; margin-bottom: 8px;">
        📋 SYSMON OPERATIONAL LOG RECORD // EVENT ID 1 (PROCESS_CREATE)
      </div>
      <div style="line-height: 1.8;">
        UtcTime: <span class="log-field-hotspot" onclick="inspectLogField('timestamp', this)">2026-10-26 13:42:10.491</span><br>
        ProcessGuid: {A1B2C3D4-E5F6-7890-1234-56789ABCDEF0}<br>
        ProcessId: 4912<br>
        Image: C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe<br>
        CommandLine: <span class="log-field-hotspot" onclick="inspectLogField('cmdline', this)">powershell.exe -w hidden -enc JABzACAAPQAgAE4AZQB3AC0ATwBiAGo...</span><br>
        ParentImage: <span class="log-field-hotspot" onclick="inspectLogField('parent', this)">C:\\Windows\\explorer.exe</span> [PID: 2840]<br>
        User: <span class="log-field-hotspot" onclick="inspectLogField('user', this)">AEROGRID\\j.smith</span>
      </div>
      <div class="log-explanation-drawer">
        Click any teal hotspot above to inspect why this field is vital for threat correlation.
      </div>
    </div>
  </div>
'''

# Slide 43: Cross-Source Telemetry Pivoting with Interactive Correlation Pipeline
slides_d4[6]["content"] = '''
  <div style="text-align: left;">
    <div class="cyber-badge badge-teal">CORRELATION ENGINEERING</div>
    <h2>Cross-Source Telemetry Pivoting & Root Cause Analysis</h2>
    <p>Bridging Perimeter Network Signals to Endpoint Process Trees</p>
    
    <div id="telemetry-correlator-demo" class="cyber-card" style="margin-top: 12px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
        <strong style="color: var(--cyber-cyan); font-size: 13px;">Live Multi-Source Telemetry Correlator</strong>
        <button onclick="triggerCorrelationPipeline()" style="background: var(--cyber-cyan); color: #050814; border: none; padding: 5px 14px; border-radius: 4px; font-weight: bold; cursor: pointer; font-size: 11px;">
          EXECUTE CORRELATION BEAM ⚡
        </button>
      </div>
      <div class="telemetry-pipeline-grid">
        <div class="telemetry-step-card">
          <span style="color: var(--neon-amber); font-weight: bold; font-size: 11px;">1. NETWORK NIDS (SURICATA)</span>
          <div style="font-size: 11px; color: #CBD5E1; margin-top: 4px;">Alert: Outbound C2 Beaconing to 198.51.100.44 on Port 443</div>
        </div>
        <div class="telemetry-step-card">
          <span style="color: var(--electric-blue); font-weight: bold; font-size: 11px;">2. IDENTITY LOGS (EVENT 4624)</span>
          <div style="font-size: 11px; color: #CBD5E1; margin-top: 4px;">Logon Type 3: Unusual NTLM authentication for 'svc_backup'</div>
        </div>
        <div class="telemetry-step-card">
          <span style="color: var(--alert-crimson); font-weight: bold; font-size: 11px;">3. ENDPOINT SYSMON (EID 10)</span>
          <div style="font-size: 11px; color: #CBD5E1; margin-top: 4px;">ProcessAccess: PowerShell opened LSASS handle with mask 0x1010</div>
        </div>
      </div>
      <div class="telemetry-correlation-result">
        <strong style="color: var(--emerald-pass); font-size: 12px;">✔ HIGH-CONFIDENCE HYPOTHESIS CONFIRMED:</strong>
        <div style="font-size: 11px; color: #CBD5E1; margin-top: 2px;">
          Compromised service account 'svc_backup' used to spawn remote PowerShell session and dump LSASS credentials for lateral movement.
        </div>
      </div>
    </div>
  </div>
'''
slides_d4[6]["notes_say"] = """[SHOW:] Display the Multi-Source Telemetry Event Correlator.
[SAY:] 'Look at how these three signals connect. In an immature SOC, three different analysts look at these alerts separately. The network analyst sees an outbound beacon. The identity team sees a logon. The endpoint team sees a PowerShell alert.'
[DO:] Click 'EXECUTE CORRELATION BEAM'.
[OBSERVE:] The animated beam links the three cards together, lighting up the green confirmed incident hypothesis.
[ASK:] 'Why is relying on only one of these three signals dangerous?'
[EXPECTED ANSWER:] 'Network alerts lack process context; endpoint alerts lack network destination; identity alerts lack execution proof.'
[REVEAL:] High-confidence root-cause isolation.
[EXPLAIN:] Telemetry pivoting transforms isolated noise into definitive forensic certainty."""

# --- DAY 5 ENHANCEMENTS ---
# Slide 48: The Golden Rule & RFC 3227 Volatility Decision Gate with 5-Day Breach Timeline
slides_d5[3]["content"] = '''
  <div style="text-align: left;">
    <div class="investigation-tracker-bar">
      <span style="color: var(--neon-amber); font-weight: bold;">🎯 MISSION: DEFEND AEROGRID // UNC-PHOENIX INVESTIGATION</span>
      <div class="tracker-progress-track"><div class="tracker-progress-fill" style="width: 82%;"></div></div>
      <span style="color: var(--text-muted);">PHASE 5: FORENSIC TRIAGE (DAY 5 OF 6)</span>
    </div>
    <div class="cyber-badge badge-amber">CRISIS CHRONOLOGY & FORENSIC TRIAGE</div>
    <h2>AeroGrid 5-Day Breach Timeline & RFC 3227 Decision Gate</h2>
    <p>Track Infiltration Milestones (Top) & Choose the Forensic Response Action (Bottom)</p>
    
    <div id="incident-timeline-demo" class="incident-timeline-wrapper">
      <div style="font-family: var(--font-mono); font-size: 11px; color: var(--neon-amber); font-weight: bold;">
        📅 INTERACTIVE BREACH TIMELINE (CLICK MILESTONES 1 THROUGH 5):
      </div>
      <div class="timeline-milestones-row">
        <div class="timeline-node-item active" onclick="inspectTimelineMilestone(0, this)">1</div>
        <div class="timeline-node-item" onclick="inspectTimelineMilestone(1, this)">2</div>
        <div class="timeline-node-item" onclick="inspectTimelineMilestone(2, this)">3</div>
        <div class="timeline-node-item" onclick="inspectTimelineMilestone(3, this)">4</div>
        <div class="timeline-node-item" onclick="inspectTimelineMilestone(4, this)">5</div>
      </div>
      <div class="timeline-evidence-drawer">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
          <span style="font-family: var(--font-mono); font-size: 11px; color: var(--neon-amber); font-weight: 700;">DAY 1 (OCT 26)</span>
          <span style="font-family: var(--font-mono); font-size: 10px; color: #00E676; font-weight: 700;">VERIFIED EVIDENCE (ESTABLISHED)</span>
        </div>
        <div style="font-size: 0.95rem; font-weight: 700; color: #FFF; margin-bottom: 4px;">
          INITIAL ACCESS & FOOTHOLD
        </div>
        <div style="font-size: 12px; color: #CBD5E1; line-height: 1.5;">
          Spearphishing email delivered to `j.smith@aerogrid.com`. Weaponized Excel macro executed; outbound beacon connected to `198.51.100.44`.
        </div>
      </div>
    </div>
    
    <div id="ir-decision-demo" style="margin-top: 14px; background: rgba(15,23,42,0.9); border: 1px solid rgba(255,179,0,0.3); border-radius: 8px; padding: 14px;">
      <div style="font-family: var(--font-mono); font-size: 11px; color: #FFF; font-weight: bold; margin-bottom: 8px;">
        THE GOLDEN RULE DECISION: Patient Zero WS-041 is actively beaconing. What is your action?
      </div>
      <div style="display: flex; gap: 8px; flex-wrap: wrap;">
        <button class="decision-btn" onclick="selectIRChoice(0, this)">A) Reboot Machine Immediately</button>
        <button class="decision-btn" onclick="selectIRChoice(1, this)">B) Live Memory Dump + Network Isolation</button>
        <button class="decision-btn" onclick="selectIRChoice(2, this)">C) Run Full Antivirus Disk Scan</button>
      </div>
      <div class="decision-feedback-panel" style="margin-top: 10px; min-height: 40px; font-size: 11px;"></div>
    </div>
  </div>
'''

# --- DAY 6 ENHANCEMENTS ---
# Slide 60: RFC 5322 Email Telemetry with Interactive Phishing Dissector
slides_d6[1]["content"] = '''
  <div style="text-align: left;">
    <div style="display: flex; justify-content: space-between; align-items: center;">
      <div class="cyber-badge badge-cyan">EMAIL TELEMETRY</div>
      <div id="mascot-phish-badge-area"></div>
    </div>
    <h2>SES-06A: Deconstructing RFC 5322 Email Telemetry</h2>
    <p>Never Trust the Display Name: Dissecting Mail Transfer Agent (MTA) Hops & Authentication Records</p>
    
    <div id="phishing-dissector-demo" class="phish-dissector-container">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
        <span style="font-family: var(--font-mono); font-size: 11px; color: #FF8A8A; font-weight: bold;">
          🔍 INTERACTIVE PHISHING EMAIL DISSECTOR (CLICK RED DASHED HOTSPOTS)
        </span>
        <div class="phish-mascot-reaction" style="height: 35px; display: flex; align-items: center;">
          <div id="mascot-phish-impostor" data-mascot="impostor" data-mood="luring" data-width="55" data-height="55"></div>
        </div>
      </div>
      <div class="phish-email-mockup">
        <div><strong>From:</strong> <span class="phish-hotspot" onclick="inspectPhishHotspot('display-name', this)">"Dr. K. Narayanan, Director" &lt;director@recipient-corp.com&gt;</span></div>
        <div><strong>MTA Received:</strong> <span class="phish-hotspot" onclick="inspectPhishHotspot('auth-results', this)">from mail.attacker-infra.xyz (198.51.100.44) [SPF=FAIL / DMARC=FAIL]</span></div>
        <div><strong>Subject:</strong> <span class="phish-hotspot" onclick="inspectPhishHotspot('urgency-lure', this)">URGENT: MANDATORY EXECUTIVE COMPENSATION REVIEW BEFORE 11:00 AM</span></div>
        <div style="margin-top: 6px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 6px;">
          Please download and verify your updated payroll breakdown here: 
          <span class="phish-hotspot" onclick="inspectPhishHotspot('encoded-url', this)">hxxps[://]auth-portal[.]xyz/verify?token=aHR0cHM6Ly9...</span>
        </div>
      </div>
      <div class="phish-callout-box">Click any red dashed hotspot above to launch Threat Detective forensic analysis.</div>
    </div>
  </div>
  <script>
    setTimeout(() => {
      const p = document.getElementById('mascot-phish-impostor');
      if (p && window.CyberCharacters) p.innerHTML = window.CyberCharacters.getPhishingImpostor('luring', 55, 55);
    }, 100);
  </script>
'''
slides_d6[1]["notes_say"] = """[SHOW:] Display the interactive Phishing Email Dissector.
[SAY:] 'Notice the email on screen. The display name says Dr. K. Narayanan, Director. But examine the red hotspots.'
[DO:] Click on the 'From' hotspot, then the 'MTA Received' hotspot.
[OBSERVE:] Threat Detective springs into action, highlighting the SPF and DMARC failures and the spoofed envelope.
[ASK:] 'If an employee receives this email and only looks at the display name, what happens?'
[EXPECTED ANSWER:] 'They assume authority, panic over the 11:00 AM deadline, and enter their credentials into the harvester.'
[REVEAL:] Click the Base64 link hotspot to show the decoded destination URL.
[EXPLAIN:] This is why automated MTA header verification and CyberChef defanging recipes are mandatory in modern SOC operations."""

# Slide 63: Strategic Containment with 3D Rotating Security Shield
slides_d6[4]["content"] = '''
  <div style="text-align: left;">
    <div class="cyber-badge badge-amber">INCIDENT CONTAINMENT</div>
    <h2>SES-06B: Strategic Containment & Blast Radius Mitigation</h2>
    <p>Balancing Operational Continuity vs. Threat Isolation Under NIST SP 800-61 Criteria</p>
    
    <div class="grid-2" style="margin-top: 14px;">
      <div class="cyber-card">
        <strong style="color: var(--cyber-cyan); font-size: 14px;">NIST SP 800-61 Containment Triad</strong>
        <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 8px;">
          <div style="background: rgba(0,242,254,0.05); padding: 6px 10px; border-left: 3px solid var(--cyber-cyan); border-radius: 4px; font-size: 11px;">
            <strong style="color: var(--cyber-cyan);">1. Network Isolation:</strong> 802.1X quarantine VLAN or host-based EDR isolation preserving memory while severing C2 beacons.
          </div>
          <div style="background: rgba(255,179,0,0.05); padding: 6px 10px; border-left: 3px solid var(--neon-amber); border-radius: 4px; font-size: 11px;">
            <strong style="color: var(--neon-amber);">2. Identity Revocation:</strong> Disable compromised AD accounts, revoke Kerberos TGT tickets, terminate OAuth tokens.
          </div>
          <div style="background: rgba(255,75,75,0.05); padding: 6px 10px; border-left: 3px solid var(--alert-crimson); border-radius: 4px; font-size: 11px;">
            <strong style="color: var(--alert-crimson);">3. Endpoint Nullification:</strong> Process suspension (freezing ransomware encryption threads without killing RAM).
          </div>
        </div>
      </div>
      
      <!-- 3D Security Shield Viewport -->
      <div>
        <div class="three-canvas-container" id="shield-3d-canvas">
          <div class="three-canvas-overlay">🛡️ 3D CRYPTOGRAPHIC DEFENSE SHIELD // ACTIVE CONTAINMENT</div>
          <svg viewBox="0 0 200 160" style="width:100%; height:100%; position:absolute; top:0; left:0; pointer-events:none;">
            <path d="M 100 15 L 165 35 L 155 105 C 145 130, 100 150, 100 150 C 100 150, 55 130, 45 105 L 35 35 Z" fill="#0F172A" stroke="#00F2FE" stroke-width="2.5"/>
            <circle cx="100" cy="75" r="14" fill="#00E676"/>
            <path d="M 94 75 L 98 79 L 107 70" fill="none" stroke="#050814" stroke-width="2.5" stroke-linecap="round"/>
          </svg>
        </div>
        <div style="font-family: var(--font-mono); font-size: 10px; color: var(--text-muted); margin-top: 6px; text-align: center;">
          Active cryptographic boundary isolating infected subnet 10.0.4.0/24.
        </div>
      </div>
    </div>
  </div>
'''

# Slide 67: AeroGrid Tabletop Crisis with Interactive Air-Gap Breaker
slides_d6[8]["content"] = '''
  <div style="text-align: left;">
    <div class="cyber-badge badge-red animate-pulse">CRISIS SIMULATION</div>
    <h2>SES-06C: AeroGrid Critical Infrastructure Tabletop Crisis</h2>
    <p>150 Minutes of High-Stakes Incident Response: Regional Power Grid SCADA Network Breach</p>
    
    <div id="aerogrid-breaker-demo" class="aerogrid-breaker-panel">
      <div class="aerogrid-status-badge" style="background: rgba(255,75,75,0.15); color: #FF4B4B; border: 1px solid #FF4B4B;">
        BREACH ACTIVE: OT AT RISK
      </div>
      <div class="aerogrid-telemetry-text" style="font-family: var(--font-mono); font-size: 12px; margin-bottom: 12px; color: #CBD5E1;">
        <span style="color:#FF4B4B;">[ALERT TRIGGERED]</span> Unauthorized Modbus Function 05 (Write Single Coil) attempting to trip distribution grid!
      </div>
      <button class="aerogrid-switch-btn" style="background: #FF4B4B;" onclick="toggleAirGapBreaker()">
        EXECUTE EMERGENCY AIR-GAP SEVERANCE
      </button>
      <div style="font-family: var(--font-mono); font-size: 10px; color: var(--text-muted); margin-top: 8px;">
        Click to sever the DMZ bridge (Port 502 Modbus & Port 3389 RDP) protecting Substation 4 turbines.
      </div>
    </div>
    
    <div class="grid-3" style="margin-top: 12px;">
      <div class="cyber-card" style="border-top: 2px solid var(--alert-crimson);">
        <strong style="color: var(--alert-crimson); font-size: 12px;">PHASE 1 (14:30 - 15:15)</strong>
        <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Alert Triage & Incursion: OT Gateway telemetry spikes.</p>
      </div>
      <div class="cyber-card" style="border-top: 2px solid var(--neon-amber);">
        <strong style="color: var(--neon-amber); font-size: 12px;">PHASE 2 (15:15 - 16:00)</strong>
        <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Lateral Movement: Mimikatz DCSync on IT-OT jump host.</p>
      </div>
      <div class="cyber-card" style="border-top: 2px solid var(--cyber-cyan);">
        <strong style="color: var(--cyber-cyan); font-size: 12px;">PHASE 3 (16:00 - 17:00)</strong>
        <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Post-Mortem & CERT-In 6-hour regulatory debrief.</p>
      </div>
    </div>
  </div>
'''
slides_d6[8]["notes_say"] = """[SHOW:] Display the AeroGrid Critical Infrastructure Tabletop Crisis & Emergency Air-Gap Breaker.
[SAY:] 'At 14:12, automated alarms triggered in Substation 4. Turbine telemetry sensors are reporting unauthorized Modbus commands.'
[DO:] Click 'EXECUTE EMERGENCY AIR-GAP SEVERANCE'.
[OBSERVE:] The breaker switches off, status turns emerald green, and Modbus command flow is dropped at the DMZ firewall.
[ASK:] 'What would happen if we hesitated for 15 minutes before severing this connection?'
[EXPECTED ANSWER:] 'The adversary trips distribution breakers, causing physical turbine equipment damage and cascading blackout.'
[REVEAL:] Emergency containment protocol confirmed.
[EXPLAIN:] In OT/ICS incident response, human safety and grid stability take absolute precedence."""

# Slide 71 (Index 12): The Post-Mortem Defense Plan & Executive Briefing Dossier
slides_d6[12]["content"] = '''
  <div style="text-align: left;">
    <div class="investigation-tracker-bar">
      <span style="color: var(--alert-crimson); font-weight: bold;">🎯 MISSION: DEFEND AEROGRID // UNC-PHOENIX INVESTIGATION</span>
      <div class="tracker-progress-track"><div class="tracker-progress-fill" style="width: 100%;"></div></div>
      <span style="color: var(--emerald-pass); font-weight: bold;">INCIDENT CONCLUDED (100%)</span>
    </div>
    <div class="cyber-badge badge-red">EXECUTIVE POST-MORTEM DOSSIER</div>
    <h2>AeroGrid Cyber Incident Final Executive Briefing</h2>
    <p>Evidence-Based Synthesis for Executive Leadership and CERT-In Regulatory Reporting</p>
    
    <div id="briefing-dossier-demo" class="briefing-dossier-card">
      <div class="briefing-tab-row">
        <button class="briefing-tab-btn active" onclick="switchBriefingTab('patient-zero', this)">1. PATIENT ZERO</button>
        <button class="briefing-tab-btn" onclick="switchBriefingTab('threat-actor', this)">2. ATTRIBUTED ACTOR</button>
        <button class="briefing-tab-btn" onclick="switchBriefingTab('lateral-path', this)">3. ATTACK PATH</button>
        <button class="briefing-tab-btn" onclick="switchBriefingTab('containment', this)">4. REMEDIATIONS</button>
      </div>
      <div class="briefing-tab-content">
        <strong>Patient Zero:</strong> Workstation <code>WS-041</code> assigned to Finance Analyst (j.smith). Compromised via spearphishing attachment at 13:42 UTC on Oct 26.
      </div>
    </div>
    
    <div class="grid-3" style="margin-top: 14px;">
      <div class="cyber-card" style="border-left: 3px solid var(--emerald-pass);">
        <strong style="color: var(--emerald-pass); font-size: 12px;">ROOT CAUSE ELIMINATED</strong>
        <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">Macro execution disabled tenant-wide via Group Policy (GPO).</p>
      </div>
      <div class="cyber-card" style="border-left: 3px solid var(--cyber-cyan);">
        <strong style="color: var(--cyber-cyan); font-size: 12px;">IDENTITY HARDENED</strong>
        <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">KRBTGT double reset completed; Kerberos Golden Tickets invalidated.</p>
      </div>
      <div class="cyber-card" style="border-left: 3px solid var(--purple-intel);">
        <strong style="color: var(--purple-intel); font-size: 12px;">INTEL DISSEMINATED</strong>
        <p style="font-size: 11px; color: var(--text-secondary); margin-top: 4px;">STIX 2.1 IOC bundle shared with National CERT-In & Energy ISAC.</p>
      </div>
    </div>
  </div>
'''

# ==============================================================================
# EXPAND ALL 8 PRACTICAL LABS INTO 7-SLIDE STRUCTURED MODULES (A through G)
# ==============================================================================
from lab_slides_generator import (
    get_lab01_slides, get_lab02_slides, get_lab03_slides, get_lab04_slides,
    get_lab05_slides, get_lab06_slides, get_lab07_slides, get_lab08_slides
)

# Expand Day 1 Lab 01 placeholder (index 14) into 7 structured slides
slides_d1[14:15] = get_lab01_slides()

# Expand Day 2 Lab 03 placeholder (index 8) into 7 structured slides
slides_d2[8:9] = get_lab03_slides()

# Expand Day 3 Lab 02 placeholder (index 8) into 7 structured slides
slides_d3[8:9] = get_lab02_slides()

# Expand Day 4 Lab 04 placeholder (index 9) into 7 structured slides
slides_d4[9:10] = get_lab04_slides()

# Expand Day 5 Lab 06 placeholder (index 9) into 7 structured slides
slides_d5[9:10] = get_lab06_slides()

# Expand Day 6 Labs (indices 11, 7, 3 in reverse order) into 7 structured slides each
slides_d6[11:12] = get_lab08_slides()
slides_d6[7:8] = get_lab07_slides()
slides_d6[3:4] = get_lab05_slides()

# ==============================================================================
# COMPILE DAY-WISE HTML DECKS WITH ALL ENGINES LINKED
# ==============================================================================

DAY_CONFIGS_ANIMATED = [
    {
        "id": "day-01", "num": 1, "name": "Day 01", "title": "CTI Fundamentals, Threat Actor Profiling & The Diamond Model",
        "date_str": "Monday, 26 October 2026", "time_str": "1:00 PM – 5:00 PM", "net_minutes": 220,
        "accent": "#00F2FE", "accent_name": "cyan", "slides": slides_d1,
        "labs": "DEMO-01: NATO Admiralty Code | LAB-01: OTX & crt.sh Reconnaissance",
        "prev_day": None, "next_day": "day-02",
        "description": "Foundational orientation, DIKW hierarchy, 4 CTI tiers, threat actor profiling, the 6-stage intelligence cycle, NATO source scoring, and the Diamond Model of Intrusion Analysis."
    },
    {
        "id": "day-02", "num": 2, "name": "Day 02", "title": "Threat Modeling, MITRE ATT&CK Matrix & Structured Threat Hunting",
        "date_str": "Tuesday, 27 October 2026", "time_str": "1:00 PM – 5:00 PM", "net_minutes": 220,
        "accent": "#4FACFE", "accent_name": "blue", "slides": slides_d2,
        "labs": "DEMO-02: ATT&CK Heatmap | LAB-03: ATT&CK Navigator Layer Algebra",
        "prev_day": "day-01", "next_day": "day-03",
        "description": "Cyber Kill Chain vs. Diamond Model, David Bianco's Pyramid of Pain, ATT&CK Matrix v15 14 enterprise tactics, Navigator layer arithmetic, and MITRE D3FEND defensive countermeasures."
    },
    {
        "id": "day-03", "num": 3, "name": "Day 03", "title": "Defensive OSINT, Indicator Lifecycle & STIX 2.1 / TAXII 2.1 Protocols",
        "date_str": "Wednesday, 28 October 2026", "time_str": "1:00 PM – 5:00 PM", "net_minutes": 220,
        "accent": "#B388FF", "accent_name": "purple", "slides": slides_d3,
        "labs": "DEMO-03: Python stix2 | LAB-02: Threat Intel Feeds, STIX 2.1 & TAXII 2.1",
        "prev_day": "day-02", "next_day": "day-04",
        "description": "Passive infrastructure reconnaissance, indicator confidence decay dynamics, STIX 2.1 SDO/SRO JSON graph modeling, TAXII 2.1 REST collections, and IBM X-Force / MISP integration."
    },
    {
        "id": "day-04", "num": 4, "name": "Day 04", "title": "Multi-Source Enterprise Telemetry Correlation & Sigma Detection Rules",
        "date_str": "Thursday, 29 October 2026", "time_str": "1:00 PM – 5:00 PM", "net_minutes": 220,
        "accent": "#00E5FF", "accent_name": "teal", "slides": slides_d4,
        "labs": "DEMO-04: Telemetry Pivot | LAB-04: Multi-Source Telemetry & Sigma Rules",
        "prev_day": "day-03", "next_day": "day-05",
        "description": "The Telemetry Triad (Endpoint, Network, Identity), Windows Security Events (4624, 4688), Sysmon EID 1/3/10/22, Zeek logs, Suricata EVE.json, cross-source pivoting, and Sigma rule transpilation."
    },
    {
        "id": "day-05", "num": 5, "name": "Day 05", "title": "NIST Incident Response, RFC 3227 Volatility & Forensic Triage Acquisition",
        "date_str": "Friday, 30 October 2026", "time_str": "2:00 PM – 5:00 PM", "net_minutes": 160,
        "accent": "#FFB300", "accent_name": "amber", "slides": slides_d5,
        "labs": "DEMO-05: Timeline Explorer | LAB-06: Triage Acquisition & Timestomping",
        "prev_day": "day-04", "next_day": "day-06",
        "description": "NIST SP 800-61r3 lifecycle, CSIRT role matrices, RFC 3227 Order of Volatility, The Golden Rule ('Do Not Reboot!'), volatile RAM triage, Eric Zimmerman KAPE compound targets, and $MFT timestomp analysis."
    },
    {
        "id": "day-06", "num": 6, "name": "Day 06", "title": "Phishing Triage, Containment, SOAR Automation & AeroGrid APT Crisis",
        "date_str": "Saturday, 31 October 2026", "time_str": "9:30 AM – 5:00 PM", "net_minutes": 390,
        "accent": "#FF4B4B", "accent_name": "red", "slides": slides_d6,
        "labs": "LAB-05: Phishing Triage | LAB-07: Shuffle SOAR | LAB-08: AeroGrid APT Tabletop",
        "prev_day": "day-05", "next_day": None,
        "description": "RFC 5322 email headers & CyberChef pipelines, Active Directory KRBTGT 10-hour double reset, event-driven Shuffle SOAR playbooks, the 150-min AeroGrid SCADA crisis simulation, and course graduation."
    }
]

def build_animated_daily_deck(cfg):
    day_id = cfg["id"]
    day_name = cfg["name"]
    title = cfg["title"]
    date_str = cfg["date_str"]
    time_str = cfg["time_str"]
    accent = cfg["accent"]
    slides = cfg["slides"]
    total_slides = len(slides)
    prev_day = cfg["prev_day"]
    next_day = cfg["next_day"]
    
    deck_dir = os.path.join(PRESENTATION_DIR, day_id)
    os.makedirs(deck_dir, exist_ok=True)
    out_file = os.path.join(deck_dir, "index.html")
    
    prev_link = f'<a href="../{prev_day}/index.html" class="nav-day-btn" title="Go to {prev_day.upper()}">◀ PREV DAY</a>' if prev_day else '<span class="nav-day-btn disabled">◀ START</span>'
    next_link = f'<a href="../{next_day}/index.html" class="nav-day-btn" title="Go to {next_day.upper()}">NEXT DAY ▶</a>' if next_day else '<span class="nav-day-btn disabled">END ▶</span>'

    html = []
    html.append(f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>{day_name.upper()} — {title} | Threat Intelligence & Incident Response</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
  
  <!-- Presentation Stylesheets (Referenced from shared/) -->
  <link rel="stylesheet" href="../shared/css/reset.css">
  <link rel="stylesheet" href="../shared/css/reveal.css">
  <link rel="stylesheet" href="../shared/css/theme-cyber-soc.css">
  <link rel="stylesheet" href="../shared/css/animations.css">
  <link rel="stylesheet" href="../shared/css/interactive-experiences.css">
  
  <style>
    :root {{
      --day-accent: {accent};
    }}
    .telemetry-status-bar {{
      border-bottom: 2px solid var(--day-accent);
    }}
    .nav-day-btn {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #FFF;
      padding: 3px 10px;
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 11px;
      text-decoration: none;
      transition: all 0.2s ease;
    }}
    .nav-day-btn:hover {{
      background: var(--day-accent);
      color: #050814;
      border-color: var(--day-accent);
    }}
    .nav-day-btn.disabled {{
      opacity: 0.3;
      cursor: not-allowed;
      border-color: transparent;
    }}
    .portal-home-btn {{
      background: rgba(0, 242, 254, 0.12);
      border: 1px solid var(--cyber-cyan);
      color: var(--cyber-cyan);
      padding: 3px 10px;
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      text-decoration: none;
      transition: all 0.2s ease;
    }}
    .portal-home-btn:hover {{
      background: var(--cyber-cyan);
      color: #050814;
    }}
  </style>
</head>
<body>

  <!-- Top Real-Time Telemetry Bar -->
  <div class="telemetry-status-bar">
    <div class="status-left">
      <a href="../index.html" class="portal-home-btn" title="Return to Course Master Portal">⊞ MASTER PORTAL</a>
      <div class="status-pill">
        <span class="live-indicator"></span>
        <span style="color: var(--day-accent); font-weight: 700;">{day_name.upper()}</span>
      </div>
      <div class="status-pill">
        <span>VENUE:</span> <strong style="color: #F8FAFC;">LH3 – 4TH FLOOR</strong>
      </div>
      <div class="status-pill">
        <span>SESSION:</span> <strong style="color: #F8FAFC;">{time_str}</strong>
      </div>
    </div>
    
    <div class="status-center">
      <div class="status-pill">
        <span>FOCUS:</span> <strong id="status-module" style="color: var(--day-accent);">{title[:36]}...</strong>
      </div>
    </div>
    
    <div class="status-right">
      {prev_link}
      {next_link}
      <button onclick="toggleShortcutModal()" style="background: none; border: 1px solid rgba(255,255,255,0.2); color: var(--text-muted); padding: 2px 8px; border-radius: 4px; font-family: var(--font-mono); font-size: 10px; cursor: pointer;">KEYS [?]</button>
      <button onclick="toggleFullScreen()" style="background: none; border: 1px solid rgba(255,255,255,0.2); color: var(--text-muted); padding: 2px 8px; border-radius: 4px; font-family: var(--font-mono); font-size: 10px; cursor: pointer;">FULL [F]</button>
    </div>
  </div>

  <!-- Bottom Custom Slide Counter -->
  <div id="custom-slide-counter" class="custom-slide-counter">{day_name.upper()}: SLIDE <span>01</span> / {total_slides:02d}</div>

  <!-- Keyboard Shortcuts Modal -->
  <div id="shortcut-modal" style="position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(5,8,20,0.85); backdrop-filter: blur(8px); z-index: 2000; display: none; align-items: center; justify-content: center;" onclick="if(event.target===this) toggleShortcutModal()">
    <div style="background: #0F172A; border: 1px solid var(--day-accent); border-radius: 12px; padding: 28px 36px; max-width: 500px; width: 90%; box-shadow: 0 0 40px rgba(0,242,254,0.3); text-align: left;">
      <h3 style="margin-top: 0; color: #FFF; font-family: var(--font-heading);">⌨️ {day_name.upper()} Navigation Shortcuts</h3>
      <table style="width: 100%; font-family: var(--font-mono); font-size: 12px; color: var(--text-secondary); border-collapse: collapse;">
        <tr><td style="padding: 6px 0; color: var(--day-accent);">Space / Right Arrow</td><td>Next Slide / Fragment</td></tr>
        <tr><td style="padding: 6px 0; color: var(--day-accent);">Left Arrow</td><td>Previous Slide</td></tr>
        <tr><td style="padding: 6px 0; color: var(--day-accent);">F</td><td>Toggle Full-Screen Mode</td></tr>
        <tr><td style="padding: 6px 0; color: var(--day-accent);">Esc / ?</td><td>Close Modal / Help</td></tr>
      </table>
      <div style="margin-top: 15px; display: flex; gap: 10px;">
        <a href="../index.html" style="display: block; text-align: center; flex: 1; padding: 8px; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.2); border-radius: 6px; color: #FFF; text-decoration: none; font-size: 12px;">RETURN TO PORTAL</a>
        <button onclick="toggleShortcutModal()" style="flex: 1; padding: 8px; background: var(--day-accent); border: none; border-radius: 6px; font-weight: 700; color: #050814; cursor: pointer; font-size: 12px;">CLOSE</button>
      </div>
    </div>
  </div>

  <!-- Reveal.js Container -->
  <div class="reveal">
    <div class="slides">
''')

    for s_idx, s in enumerate(slides, 1):
        day_attr = f' data-day="{day_name.upper()}"'
        mod_attr = f' data-module="{s.get("module", title)}"'
        sess_attr = f' data-session="{time_str}"'
        ref_attr = f' data-ref="{s.get("ref", "Master Handbook / Verbatim Script")}"'
        
        html.append(f'      <!-- {day_name.upper()} - SLIDE {s_idx:02d}: {s["title"]} -->')
        html.append(f'      <section{day_attr}{mod_attr}{sess_attr}{ref_attr}>')
        html.append(s['content'])
        
        html.append('        <aside class="notes">')
        html.append(f'          [SAY:] {s.get("notes_say", "")}')
        html.append(f'          [PEDAGOGY:] {s.get("notes_pedagogy", "")}')
        html.append('        </aside>')
        html.append('      </section>\n')

    # Wrap up slide
    wrap_html = f'''
      <!-- {day_name.upper()} - CONCLUSION & PORTAL RETURN -->
      <section data-day="{day_name.upper()}" data-module="WRAP-UP & ADJOURNMENT" data-session="{time_str}" data-ref="Course Syllabus">
        <div style="text-align: center; padding: 30px 10px;">
          <div class="cyber-badge badge-{cfg['accent_name']}" style="margin-bottom: 15px;">{day_name.upper()} ADJOURNMENT</div>
          <h2>Session Concluded: {title}</h2>
          <p style="color: var(--text-secondary); max-width: 780px; margin: 0 auto 25px auto; font-size: 15px;">
            You have completed all planned instructional milestones, practical demonstrations, and lab exercises for {date_str}.
          </p>
          
          <div class="grid-2" style="max-width: 800px; margin: 0 auto 30px auto; text-align: left;">
            <div class="cyber-card">
              <strong style="color: var(--day-accent); font-size: 14px;">Today's Completed Practical Milestones</strong>
              <div style="font-size: 12px; color: var(--text-secondary); margin-top: 8px;">
                {cfg['labs']}
              </div>
            </div>
            <div class="cyber-card">
              <strong style="color: var(--neon-amber); font-size: 14px;">Next Session Briefing</strong>
              <div style="font-size: 12px; color: var(--text-secondary); margin-top: 8px;">
                {DAY_CONFIGS_ANIMATED[cfg['num']]['title'] if cfg['num'] < 6 else 'Course Graduation & SOC Transition Complete!'}
              </div>
            </div>
          </div>
          
          <div style="display: flex; justify-content: center; gap: 15px;">
            <a href="../index.html" class="portal-home-btn" style="padding: 10px 24px; font-size: 13px;">⊞ RETURN TO MASTER PORTAL</a>
            {'<a href="../' + next_day + '/index.html" class="nav-day-btn" style="padding: 10px 24px; font-size: 13px; background: var(--day-accent); color: #050814; font-weight: bold;">LAUNCH ' + DAY_CONFIGS_ANIMATED[cfg['num']]['name'].upper() + ' ▶</a>' if next_day else ''}
          </div>
        </div>
      </section>
    '''
    html.append(wrap_html)

    html.append(f'''    </div>
  </div>

  <!-- Shared Script Engines: Cyber-BG, Reveal.js, GSAP, Three.js, Mascots & Narratives -->
  <script src="../shared/js/cyber-bg.js"></script>
  <script src="../shared/js/reveal.js"></script>
  <script src="../shared/js/gsap.min.js"></script>
  <script src="../shared/js/three.min.js"></script>
  <script src="../shared/js/characters.js"></script>
  <script src="../shared/js/cyber-3d.js"></script>
  <script src="../shared/js/gsap-narratives.js"></script>
  <script src="../shared/js/presentation-app.js"></script>
  <script>
    Reveal.on('slidechanged', event => {{
      const counterEl = document.getElementById('custom-slide-counter');
      if (counterEl) {{
        const current = Reveal.getSlidePastCount() + 1;
        const total = Reveal.getTotalSlides();
        counterEl.innerHTML = `{day_name.upper()}: SLIDE <span>${{String(current).padStart(2, '0')}}</span> / ${{String(total).padStart(2, '0')}}`;
      }}
    }});
    Reveal.on('ready', event => {{
      const counterEl = document.getElementById('custom-slide-counter');
      if (counterEl) {{
        const current = Reveal.getSlidePastCount() + 1;
        const total = Reveal.getTotalSlides();
        counterEl.innerHTML = `{day_name.upper()}: SLIDE <span>${{String(current).padStart(2, '0')}}</span> / ${{String(total).padStart(2, '0')}}`;
      }}
    }});
  </script>
</body>
</html>''')

    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(html))
    print(f"Generated Upgraded {day_name} Presentation: {out_file} ({total_slides + 1} slides)")

def build_upgraded_master_portal():
    portal_file = os.path.join(PRESENTATION_DIR, "index.html")
    
    html = []
    html.append('''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Threat Intelligence & Incident Response — Master Presentation Portal</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
  
  <link rel="stylesheet" href="shared/css/reset.css">
  <link rel="stylesheet" href="shared/css/theme-cyber-soc.css">
  <link rel="stylesheet" href="shared/css/animations.css">
  <link rel="stylesheet" href="shared/css/interactive-experiences.css">
  
  <style>
    :root {
      --bg-space: #050814;
      --bg-surface: #0A1128;
      --bg-card: rgba(15, 23, 42, 0.85);
      --border-subtle: rgba(56, 189, 248, 0.2);
      --cyber-cyan: #00F2FE;
      --electric-blue: #4FACFE;
      --matrix-teal: #00E5FF;
      --neon-amber: #FFB300;
      --alert-crimson: #FF4B4B;
      --emerald-pass: #00E676;
      --purple-intel: #B388FF;
      --text-primary: #F8FAFC;
      --text-secondary: #94A3B8;
      --text-muted: #64748B;
      --font-main: 'Plus Jakarta Sans', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --font-heading: 'Space Grotesk', sans-serif;
    }
    
    html {
      overflow-y: auto !important;
      overflow-x: hidden !important;
      scroll-behavior: smooth;
      height: auto !important;
    }
    
    body {
      background-color: var(--bg-space);
      color: var(--text-primary);
      font-family: var(--font-main);
      min-height: 100vh;
      height: auto !important;
      line-height: 1.6;
      position: relative;
      overflow-y: visible !important;
      overflow-x: hidden !important;
      -webkit-overflow-scrolling: touch;
    }

    /* Ambient cyber grid background */
    body::before {
      content: '';
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background-image: 
        linear-gradient(to right, rgba(14, 165, 233, 0.04) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(14, 165, 233, 0.04) 1px, transparent 1px);
      background-size: 40px 40px;
      pointer-events: none;
      z-index: 0;
    }

    .container {
      max-width: 1360px;
      margin: 0 auto;
      padding: 35px 24px;
      position: relative;
      z-index: 1;
    }

    /* Header Section */
    .portal-header {
      text-align: center;
      margin-bottom: 30px;
    }
    
    .status-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 5px 16px;
      border-radius: 20px;
      background: rgba(0, 242, 254, 0.1);
      border: 1px solid var(--cyber-cyan);
      color: var(--cyber-cyan);
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 1px;
      margin-bottom: 14px;
    }

    .pulse-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--emerald-pass);
      box-shadow: 0 0 10px var(--emerald-pass);
      animation: pulse 2s infinite;
    }

    @keyframes pulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.85); }
    }

    h1 {
      font-family: var(--font-heading);
      font-size: 2.7rem;
      font-weight: 700;
      letter-spacing: -0.5px;
      margin-bottom: 8px;
      background: linear-gradient(135deg, #FFF 60%, var(--cyber-cyan) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .lead {
      color: var(--text-secondary);
      font-size: 1.1rem;
      max-width: 820px;
      margin: 0 auto 20px auto;
    }

    /* Mascot Showcase Row */
    .mascot-showcase-row {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 30px;
      margin-bottom: 25px;
    }

    /* Meta Badges */
    .meta-bar {
      display: flex;
      justify-content: center;
      gap: 14px;
      flex-wrap: wrap;
      margin-bottom: 25px;
      font-family: var(--font-mono);
      font-size: 12px;
    }

    .meta-pill {
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid var(--border-subtle);
      padding: 6px 14px;
      border-radius: 6px;
      color: #CBD5E1;
    }

    .meta-pill strong {
      color: var(--cyber-cyan);
    }

    /* Overall Progress Bar */
    .progress-panel {
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 14px 22px;
      margin-bottom: 35px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 18px;
    }

    .progress-info {
      font-family: var(--font-mono);
      font-size: 12px;
    }

    .progress-bar-container {
      flex: 1;
      min-width: 250px;
      height: 8px;
      background: rgba(255, 255, 255, 0.08);
      border-radius: 4px;
      overflow: hidden;
      margin: 0 20px;
    }

    .progress-bar-fill {
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, var(--cyber-cyan), var(--emerald-pass));
    }

    /* Day Cards Grid */
    .days-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
      gap: 24px;
      margin-bottom: 40px;
    }

    .day-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 24px;
      transition: all 0.25s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      overflow: hidden;
    }

    .day-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.6);
    }

    .day-card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }

    .day-badge {
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 4px;
    }

    .day-status {
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--emerald-pass);
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 4px;
    }

    .day-title {
      font-family: var(--font-heading);
      font-size: 1.25rem;
      font-weight: 700;
      color: #FFF;
      margin-bottom: 8px;
      line-height: 1.35;
    }

    .day-schedule {
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--text-muted);
      margin-bottom: 12px;
    }

    .day-desc {
      font-size: 13px;
      color: var(--text-secondary);
      margin-bottom: 16px;
      line-height: 1.5;
      flex: 1;
    }

    .day-labs {
      background: rgba(0, 0, 0, 0.3);
      border-left: 3px solid var(--cyber-cyan);
      padding: 8px 12px;
      border-radius: 4px;
      font-size: 11px;
      color: #CBD5E1;
      margin-bottom: 18px;
      font-family: var(--font-mono);
    }

    .btn-launch {
      display: block;
      width: 100%;
      text-align: center;
      padding: 10px 0;
      border-radius: 6px;
      font-family: var(--font-heading);
      font-weight: 700;
      font-size: 13px;
      text-decoration: none;
      transition: all 0.2s ease;
      letter-spacing: 0.5px;
    }

    .btn-launch:hover {
      transform: scale(1.02);
      box-shadow: 0 4px 16px rgba(0, 242, 254, 0.4);
    }

    /* Documentation Section */
    .docs-panel {
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 24px 30px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
    }

    .doc-links {
      display: flex;
      gap: 14px;
      flex-wrap: wrap;
    }

    .doc-link {
      color: var(--cyber-cyan);
      text-decoration: none;
      font-family: var(--font-mono);
      font-size: 12px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      background: rgba(0, 242, 254, 0.08);
      border: 1px solid rgba(0, 242, 254, 0.2);
      border-radius: 4px;
      transition: all 0.2s ease;
    }

    .doc-link:hover {
      background: var(--cyber-cyan);
      color: #050814;
    }

    /* Footer */
    footer {
      text-align: center;
      margin-top: 45px;
      color: var(--text-muted);
      font-family: var(--font-mono);
      font-size: 12px;
    }
  </style>
</head>
<body>

  <div class="container">
    
    <!-- Header -->
    <header class="portal-header">
      <div class="status-badge">
        <span class="pulse-dot"></span>
        <span>COURSE MASTER PRESENTATION CONTROL PORTAL</span>
      </div>
      <h1>Threat Intelligence & Incident Response</h1>
      <p class="lead">
        Interactive 6-Day Keynote Experience with 3D Cyber Telemetry & Animated Tactical Simulations
      </p>

      <!-- Mascots Row -->
      <div class="mascot-showcase-row">
        <div id="mascot-p1"></div>
        <div id="mascot-p2"></div>
        <div id="mascot-p3"></div>
        <div id="mascot-p4"></div>
      </div>
      
      <div class="meta-bar">
        <div class="meta-pill">VENUE: <strong>LH3 – 4TH FLOOR</strong></div>
        <div class="meta-pill">SCHEDULE: <strong>26–31 OCTOBER 2026</strong></div>
        <div class="meta-pill">HOURS: <strong>26.5h Gross / 23.4h Net</strong></div>
        <div class="meta-pill">ENGINES: <strong>Reveal.js + GSAP + Three.js</strong></div>
        <div class="meta-pill">AUDIT: <strong style="color: var(--emerald-pass);">100% VERIFIED</strong></div>
      </div>
    </header>

    <!-- Progress Status Bar -->
    <div class="progress-panel">
      <div class="progress-info">
        <strong>COURSE READINESS:</strong> 6 of 6 Daily Keynotes Upgraded with GSAP & 3D (100%)
      </div>
      <div class="progress-bar-container">
        <div class="progress-bar-fill"></div>
      </div>
      <div class="progress-info">
        <span style="color: var(--emerald-pass); font-weight: bold;">✔ PRODUCTION READY FOR LH3</span>
      </div>
    </div>

    <!-- 6 Day Cards Grid -->
    <div class="days-grid">
''')

    for cfg in DAY_CONFIGS_ANIMATED:
        day_id = cfg["id"]
        day_name = cfg["name"]
        title = cfg["title"]
        date_str = cfg["date_str"]
        time_str = cfg["time_str"]
        accent = cfg["accent"]
        desc = cfg["description"]
        labs = cfg["labs"]
        slide_count = len(cfg["slides"]) + 1
        
        html.append(f'''
      <!-- {day_name} Card -->
      <div class="day-card" style="border-top: 3px solid {accent};">
        <div>
          <div class="day-card-header">
            <span class="day-badge" style="background: rgba({int(accent[1:3], 16)}, {int(accent[3:5], 16)}, {int(accent[5:7], 16)}, 0.15); color: {accent};">
              {day_name.upper()}
            </span>
            <span class="day-status">✔ ANIMATED & AUDITED</span>
          </div>
          <h2 class="day-title">{title}</h2>
          <div class="day-schedule">
            📅 {date_str} | ⏰ {time_str} ({cfg['net_minutes']} min net)
          </div>
          <p class="day-desc">{desc}</p>
          <div class="day-labs" style="border-left-color: {accent};">
            <strong>PRACTICAL LABS & ANIMATIONS:</strong><br>{labs}
          </div>
        </div>
        <div>
          <div style="font-family: var(--font-mono); font-size: 11px; color: var(--text-muted); margin-bottom: 10px; display: flex; justify-content: space-between;">
            <span>Volume: {slide_count} Designed Slides</span>
            <span style="color: {accent}; font-weight: bold;">GSAP & 3D Active</span>
          </div>
          <a href="{day_id}/index.html" class="btn-launch" style="background: {accent}; color: #050814;">
            🚀 LAUNCH {day_name.upper()} KEYNOTE
          </a>
        </div>
      </div>
''')

    html.append('''    </div>

    <!-- Documentation & Audit Links Panel -->
    <div class="docs-panel">
      <div>
        <h3 style="font-family: var(--font-heading); color: #FFF; font-size: 1.1rem; margin-bottom: 4px;">Audited Project Documentation & Governance</h3>
        <p style="font-size: 12px; color: var(--text-muted);">Authoritative source mappings, day-wise test matrices, and technical operational manuals.</p>
      </div>
      <div class="doc-links">
        <a href="docs/Threat_Intelligence_Incident_Response_Presentation_Technical_Guide.md" class="doc-link" target="_blank">📄 Technical Guide</a>
        <a href="docs/Overall_Presentation_Audit_Report.md" class="doc-link" target="_blank">🛡️ Master Audit Report</a>
        <a href="docs/Day_Wise_Presentation_Coverage_Matrix.xlsx" class="doc-link" target="_blank">📊 Coverage Matrix (XLSX)</a>
        <a href="docs/Day_Wise_Presentation_Test_Matrix.xlsx" class="doc-link" target="_blank">🧪 Test Matrix (XLSX)</a>
        <a href="docs/FINAL_QA_REPORT.md" class="doc-link" target="_blank">🛡️ Final QA Report</a>
      </div>
    </div>

    <!-- Footer -->
    <footer>
      Threat Intelligence and Incident Response Training Program | Venue: LH3 – 4th Floor | Dates: 26–31 October 2026<br>
      Engineered by the Chief AI Knowledge Architect | Upgraded with GSAP, Three.js & Animated Mascots
    </footer>

  </div>

  <!-- Live Cyber Particle Background & Shared Mascot Script -->
  <script src="shared/js/cyber-bg.js"></script>
  <script src="shared/js/characters.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      if (window.CyberCharacters && window.CyberCharacters.mountAll) {
        window.CyberCharacters.mountAll();
      }
    });
  </script>
</body>
</html>''')

    with open(portal_file, "w", encoding="utf-8") as f:
        f.write("\n".join(html))
    print(f"Generated Upgraded Master Presentation Portal: {portal_file}")

if __name__ == "__main__":
    print("Compiling Upgraded Animated Day-Wise Presentations with GSAP & Three.js...")
    for cfg in DAY_CONFIGS_ANIMATED:
        build_animated_daily_deck(cfg)
    
    print("\nCompiling Upgraded Master Presentation Portal...")
    build_upgraded_master_portal()
    print("\nSuccessfully Rebuilt All 6 Decks and Master Portal with Interactive Animations!")
