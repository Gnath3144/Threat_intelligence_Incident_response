/**
 * gsap-narratives.js - Coordinated GSAP Timelines & Interactive Case Studies
 * Upgraded Interactive Version with Complete Event Isolation (stopPropagation)
 * Designed for Threat Intelligence & Incident Response Keynote Suite
 */

window.CyberGSAP = {
  // 1. Interactive 6-Stage Intelligence Cycle Narrative
  initIntelCycle: function(containerId) {
    const container = document.getElementById(containerId);
    if (!container || typeof gsap === 'undefined') return;

    container.addEventListener('click', (e) => e.stopPropagation());

    const stages = [
      { name: '1. Direction', icon: '🎯', desc: 'Define Priority Intelligence Requirements (PIRs) based on board risk and infrastructure criticality.' },
      { name: '2. Collection', icon: '📡', desc: 'Gather multi-source telemetry: OSINT, certificate logs, dark web mentions, and commercial ISAC feeds.' },
      { name: '3. Processing', icon: '⚙️', desc: 'Normalize, deduplicate, translate foreign languages, and parse raw PCAPs into structured schemas.' },
      { name: '4. Analysis', icon: '🔍', desc: 'Synthesize data into actionable hypotheses using Admiralty scoring, Diamond Model, and ATT&CK mapping.' },
      { name: '5. Dissemination', icon: '📤', desc: 'Distribute tactical STIX 2.1 bundles to firewalls and executive post-mortem briefings to the board.' },
      { name: '6. Feedback', icon: '🔄', desc: 'Measure detection effectiveness, prune expired indicators, and refine PIRs for the next cycle.' }
    ];

    let currentStage = 0;
    const stageNodes = container.querySelectorAll('.intel-stage-node');
    const descBox = container.querySelector('.intel-stage-desc');
    const progressBar = container.querySelector('.intel-progress-bar');

    window.activateIntelStage = function(idx, event) {
      if (event) {
        event.stopPropagation();
      } else if (window.event) {
        window.event.stopPropagation();
      }

      currentStage = idx;
      stageNodes.forEach((node, i) => {
        if (i === idx) {
          node.classList.add('active');
          gsap.to(node, { scale: 1.15, borderColor: '#00F2FE', duration: 0.3 });
        } else {
          node.classList.remove('active');
          gsap.to(node, { scale: 1.0, borderColor: 'rgba(56, 189, 248, 0.2)', duration: 0.3 });
        }
      });

      if (progressBar) {
        const percent = ((idx + 1) / stages.length) * 100;
        gsap.to(progressBar, { width: `${percent}%`, duration: 0.4, ease: 'power2.out' });
      }

      if (descBox) {
        gsap.fromTo(descBox, 
          { opacity: 0, y: 10 }, 
          { opacity: 1, y: 0, duration: 0.35, onStart: () => {
              descBox.innerHTML = `
                <div style="font-family: var(--font-heading); font-size: 1.1rem; color: #00F2FE; margin-bottom: 4px;">
                  ${stages[idx].icon} ${stages[idx].name}
                </div>
                <div style="font-size: 0.85rem; color: #CBD5E1; line-height: 1.5;">
                  ${stages[idx].desc}
                </div>
              `;
            }
          }
        );
      }
    };

    window.nextIntelStage = function(event) {
      if (event) event.stopPropagation();
      else if (window.event) window.event.stopPropagation();
      const nextIdx = (currentStage + 1) % stages.length;
      window.activateIntelStage(nextIdx);
    };

    // Auto-activate first stage
    window.activateIntelStage(0);
  },

  // 2. Interactive Phishing Email Hotspot Dissector
  initPhishingDissector: function(containerId) {
    const container = document.getElementById(containerId);
    if (!container || typeof gsap === 'undefined') return;

    container.addEventListener('click', (e) => e.stopPropagation());

    const findings = {
      'display-name': {
        title: '🚩 Spoofed Display Name & Cognitive Lure',
        desc: 'The display name says "Dr. K. Narayanan, Director", but the actual RFC 5321 envelope return path originates from an unregistered domain <code>executive-urgent.com</code>. Attackers leverage authority bias.'
      },
      'auth-results': {
        title: '🚩 Cryptographic Authentication Failures',
        desc: 'Authentication-Results header indicates <code>spf=fail</code> and <code>dmarc=fail</code>. The sending MTA IP (198.51.100.44) is completely unauthorized to emit mail for the recipient organization.'
      },
      'encoded-url': {
        title: '🚩 Obfuscated Base64 Credential Harvester',
        desc: 'The embedded link disguises an HTTP redirect through a Base64-encoded parameter (<code>aHR0cHM6Ly9...</code>). CyberChef decoding reveals a fake Microsoft 365 credential harvesting portal.'
      },
      'urgency-lure': {
        title: '🚩 Artificial Urgency & Coercion Signal',
        desc: '"MANDATORY POLICY REVIEW BEFORE 11:00 AM" creates panic to bypass analytical skepticism. The classic mark of social engineering.'
      }
    };

    const calloutBox = container.querySelector('.phish-callout-box');
    const mascotBox = container.querySelector('.phish-mascot-reaction');

    window.inspectPhishHotspot = function(key, el, event) {
      if (event) event.stopPropagation();
      else if (window.event) window.event.stopPropagation();

      const finding = findings[key];
      if (!finding) return;

      // Pulse hotspot
      gsap.fromTo(el, { scale: 1 }, { scale: 1.08, duration: 0.2, yoyo: true, repeat: 1 });

      if (calloutBox) {
        gsap.fromTo(calloutBox, 
          { opacity: 0, scale: 0.95 },
          { opacity: 1, scale: 1, duration: 0.3, onStart: () => {
              calloutBox.innerHTML = `
                <div style="color: #FF4B4B; font-weight: 700; font-size: 0.95rem; margin-bottom: 4px;">
                  ${finding.title}
                </div>
                <div style="font-size: 0.8rem; color: #E2E8F0; line-height: 1.5;">
                  ${finding.desc}
                </div>
              `;
            }
          }
        );
      }

      if (mascotBox && window.CyberCharacters) {
        mascotBox.innerHTML = window.CyberCharacters.getDetective('inspecting', 90, 90);
        gsap.fromTo(mascotBox, { rotation: -10 }, { rotation: 0, duration: 0.3 });
      }
    };
  },

  // 3. Cross-Source Telemetry Correlator (Day 4)
  initTelemetryCorrelator: function(containerId) {
    const container = document.getElementById(containerId);
    if (!container || typeof gsap === 'undefined') return;

    container.addEventListener('click', (e) => e.stopPropagation());

    const pipelineSteps = container.querySelectorAll('.telemetry-step-card');
    const resultBox = container.querySelector('.telemetry-correlation-result');

    window.triggerCorrelationPipeline = function(event) {
      if (event) event.stopPropagation();
      else if (window.event) window.event.stopPropagation();

      const tl = gsap.timeline();

      pipelineSteps.forEach((card, idx) => {
        tl.to(card, {
          borderColor: '#00F2FE',
          backgroundColor: 'rgba(0, 242, 254, 0.1)',
          duration: 0.4,
          ease: 'power1.out'
        }, idx * 0.45);
      });

      tl.to(resultBox, {
        opacity: 1,
        y: 0,
        duration: 0.5,
        ease: 'back.out(1.7)'
      });
    };
  },

  // 4. AeroGrid Emergency OT Air-Gap Severance Simulation (Day 6)
  initAeroGridBreaker: function(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.addEventListener('click', (e) => e.stopPropagation());

    const statusBadge = container.querySelector('.aerogrid-status-badge');
    const telemetryText = container.querySelector('.aerogrid-telemetry-text');
    const switchBtn = container.querySelector('.aerogrid-switch-btn');
    const breakerGraphic = container.querySelector('.breaker-state-graphic');

    let isSevered = false;
    window.toggleAirGapBreaker = function(event) {
      if (event) event.stopPropagation();
      else if (window.event) window.event.stopPropagation();

      isSevered = !isSevered;
      if (isSevered) {
        statusBadge.textContent = 'AIR-GAP ISOLATED (SECURE)';
        statusBadge.style.color = '#00E676';
        statusBadge.style.borderColor = '#00E676';
        statusBadge.style.backgroundColor = 'rgba(0, 230, 118, 0.15)';
        telemetryText.innerHTML = '<span style="color:#00E676;">[FIREWALL ACTIVE]</span> Port 502 Modbus & Port 3389 RDP Dropped at DMZ Gateway. SCADA Turbines Protected.';
        switchBtn.textContent = 'RESTORE OT CONNECTION (RE-ENGAGE)';
        switchBtn.style.background = '#FFB300';
        if (breakerGraphic) breakerGraphic.style.transform = 'rotate(-35deg)';
      } else {
        statusBadge.textContent = 'BREACH ACTIVE: OT AT RISK';
        statusBadge.style.color = '#FF4B4B';
        statusBadge.style.borderColor = '#FF4B4B';
        statusBadge.style.backgroundColor = 'rgba(255, 75, 75, 0.15)';
        telemetryText.innerHTML = '<span style="color:#FF4B4B;">[ALERT TRIGGERED]</span> Unauthorized Modbus Function 05 (Write Single Coil) attempting to trip distribution grid!';
        switchBtn.textContent = 'EXECUTE EMERGENCY AIR-GAP SEVERANCE';
        switchBtn.style.background = '#FF4B4B';
        if (breakerGraphic) breakerGraphic.style.transform = 'rotate(0deg)';
      }
    };
  },

  // 5. Interactive Indicator Investigation Station
  initIndicatorStation: function(containerId) {
    const container = document.getElementById(containerId);
    if (!container || typeof gsap === 'undefined') return;
    container.addEventListener('click', (e) => e.stopPropagation());

    const indicators = {
      'fqdn': {
        title: '🌐 Domain: updates-aerogrid.internal-sync[.]com',
        type: 'Fully Qualified Domain Name (FQDN) | Admiralty: B2',
        meaning: 'Newly registered subdomain impersonating AeroGrid corporate IT infrastructure. Hosted on dynamic cloud infrastructure.',
        limitation: 'Adversaries can abandon or re-route domains rapidly once detected. Low-to-moderate adversary pain threshold.',
        next_step: 'Query Certificate Transparency logs for wildcard sibling certificates. Sinkhole DNS requests at enterprise resolvers.'
      },
      'ip': {
        title: '📡 IP: 198.51.100.44 (C2 Listener)',
        type: 'IPv4 Address | Admiralty: C3',
        meaning: 'Direct egress destination for outbound beacon traffic on Port 443. High-velocity transit hop.',
        limitation: 'IP addresses are frequently ephemeral or shared multi-tenant proxies. Blocking solely by IP risks high false positives.',
        next_step: 'Pivot to NetFlow and firewall egress telemetry to identify all internal hosts communicating with this endpoint.'
      },
      'hash': {
        title: '🔑 Hash: 8f4b23...a9c1 (Dropper Payload)',
        type: 'SHA-256 File Hash | Admiralty: A1',
        meaning: 'Cryptographic fingerprint of the weaponized Excel spreadsheet `Q3_Executive_Bonus_Matrix.xlsm`.',
        limitation: 'Trivial for the adversary to alter. Modifying one byte or metadata property generates an entirely new SHA-256 hash.',
        next_step: 'Decompile VBA macros using `olevba` without executing the spreadsheet. Extract embedded strings and URLs.'
      }
    };

    const pills = container.querySelectorAll('.indicator-pill-btn');
    const detailPanel = container.querySelector('.indicator-detail-panel');

    window.inspectIndicator = function(key, el, event) {
      if (event) event.stopPropagation();
      else if (window.event) window.event.stopPropagation();

      const item = indicators[key];
      if (!item) return;

      pills.forEach(p => p.classList.remove('active'));
      el.classList.add('active');

      if (detailPanel) {
        gsap.fromTo(detailPanel, { opacity: 0, y: 8 }, {
          opacity: 1, y: 0, duration: 0.3, onStart: () => {
            detailPanel.innerHTML = `
              <div style="color: var(--cyber-cyan); font-weight: 700; font-size: 1rem; margin-bottom: 4px;">
                ${item.title}
              </div>
              <div style="font-family: var(--font-mono); font-size: 11px; color: var(--neon-amber); margin-bottom: 6px;">
                ${item.type}
              </div>
              <div style="font-size: 12px; color: #E2E8F0; line-height: 1.5; margin-bottom: 8px;">
                <strong>Context:</strong> ${item.meaning}
              </div>
              <div style="font-size: 11px; color: var(--text-muted); line-height: 1.4; margin-bottom: 6px;">
                <span style="color: #FF8A8A;">⚠️ Limitation:</span> ${item.limitation}
              </div>
              <div style="font-size: 11px; color: var(--emerald-pass); line-height: 1.4;">
                <span>🎯 Recommended Action:</span> ${item.next_step}
              </div>
            `;
          }
        });
      }
    };
  },

  // 6. Interactive Threat-Triage Challenge
  initThreatTriage: function(containerId) {
    const container = document.getElementById(containerId);
    if (!container || typeof gsap === 'undefined') return;
    container.addEventListener('click', (e) => e.stopPropagation());

    const feedback = {
      'alert-a': {
        status: 'LOW PRIORITY (BACKGROUND NOISE)',
        color: '#FFB300',
        msg: 'Automated external port scanning occurs constantly across internet ranges. Investigating this while internal workstations execute unknown payloads introduces fatal triage latency. Do not chase the decoy!'
      },
      'alert-b': {
        status: 'CRITICAL PRIORITY — INVESTIGATE FIRST!',
        color: '#00E676',
        msg: 'CORRECT! Encoded PowerShell executing from `Downloads\\` on `WS-041` represents active Initial Access & Execution (T1059.001). The blast radius is expanding right now. Immediate triage and endpoint isolation are mandatory!'
      },
      'alert-c': {
        status: 'MEDIUM PRIORITY (MONITOR & ENRICH)',
        color: '#FFB300',
        msg: 'Multiple failed logons on a disabled account require investigation, but there is no evidence of active code execution or perimeter traversal. Keep this in queue, but prioritize Alert B!'
      }
    };

    const cards = container.querySelectorAll('.triage-alert-card');
    const feedbackBox = container.querySelector('.triage-feedback-panel');

    window.selectTriageAlert = function(alertKey, el, event) {
      if (event) event.stopPropagation();
      else if (window.event) window.event.stopPropagation();

      const item = feedback[alertKey];
      if (!item) return;

      cards.forEach(c => c.classList.remove('selected'));
      el.classList.add('selected');

      if (feedbackBox) {
        gsap.fromTo(feedbackBox, { opacity: 0, y: 6 }, {
          opacity: 1, y: 0, duration: 0.3, onStart: () => {
            feedbackBox.innerHTML = `
              <div style="color: ${item.color}; font-weight: 700; font-size: 0.95rem; margin-bottom: 4px;">
                ${item.status}
              </div>
              <div style="font-size: 12px; color: #E2E8F0; line-height: 1.5;">
                ${item.msg}
              </div>
            `;
          }
        });
      }
    };
  },

  // 7. Interactive Log Inspector (Sysmon EID 1 / Event 4688)
  initLogInspector: function(containerId) {
    const container = document.getElementById(containerId);
    if (!container || typeof gsap === 'undefined') return;
    container.addEventListener('click', (e) => e.stopPropagation());

    const fields = {
      'timestamp': {
        title: '🕒 Telemetry Pivot Timestamp (2026-10-26 13:42:10 UTC)',
        desc: 'The exact moment of execution. Analysts must pivot to proxy and email logs +/- 60 seconds around this timestamp to identify the initial delivery vector.'
      },
      'parent': {
        title: '📂 Parent Process: explorer.exe [PID: 2840]',
        desc: 'Parent is the Windows GUI Shell. When Word or Excel spawns PowerShell, it is 99% malicious. When explorer.exe spawns it, the user launched a shortcut or clicked a downloaded file directly.'
      },
      'cmdline': {
        title: '⚡ Obfuscated Command Line: powershell.exe -w hidden -enc JABz...',
        desc: 'Flag `-w hidden` hides the console window from the user. Flag `-enc` precedes a Base64-encoded string. Decoding in CyberChef reveals an uncompiled memory injection script.'
      },
      'user': {
        title: '👤 User Security Context: AEROGRID\\j.smith',
        desc: 'Identifies the compromised security identity. We must immediately check Active Directory group memberships to verify if this user possesses Domain Admin or backup privileges.'
      }
    };

    const drawer = container.querySelector('.log-explanation-drawer');

    window.inspectLogField = function(key, el, event) {
      if (event) event.stopPropagation();
      else if (window.event) window.event.stopPropagation();

      const item = fields[key];
      if (!item) return;

      if (drawer) {
        gsap.fromTo(drawer, { opacity: 0, scale: 0.98 }, {
          opacity: 1, scale: 1, duration: 0.25, onStart: () => {
            drawer.innerHTML = `
              <div style="color: var(--matrix-teal); font-weight: 700; font-size: 0.9rem; margin-bottom: 4px;">
                ${item.title}
              </div>
              <div style="font-size: 12px; color: #CBD5E1; line-height: 1.5;">
                ${item.desc}
              </div>
            `;
          }
        });
      }
    };
  },

  // 8. Visual Incident Timeline Explorer
  initIncidentTimeline: function(containerId) {
    const container = document.getElementById(containerId);
    if (!container || typeof gsap === 'undefined') return;
    container.addEventListener('click', (e) => e.stopPropagation());

    const milestones = [
      {
        day: 'DAY 1 (OCT 26)',
        title: 'INITIAL ACCESS & FOOTHOLD',
        status: 'VERIFIED EVIDENCE (ESTABLISHED)',
        color: '#00E676',
        desc: 'Spearphishing email delivered to `j.smith@aerogrid.com`. Weaponized Excel macro executed; outbound beacon connected to `198.51.100.44`.'
      },
      {
        day: 'DAY 2 (OCT 27)',
        title: 'PERSISTENCE STAGING',
        status: 'VERIFIED EVIDENCE (ESTABLISHED)',
        color: '#00E676',
        desc: 'Scheduled task `WindowsHealthCheck` registered via T1053.005. Beacon beaconing interval configured to 60s with 15% jitter.'
      },
      {
        day: 'DAY 3 (OCT 28)',
        title: 'RECONNAISSANCE & MAPPING',
        status: 'VERIFIED EVIDENCE (ESTABLISHED)',
        color: '#00E676',
        desc: 'Internal Active Directory enumeration via lightweight LDAP queries. Threat graph correlates actor infrastructure to UNC-PHOENIX.'
      },
      {
        day: 'DAY 4 (OCT 29)',
        title: 'CREDENTIAL HARVESTING',
        status: 'HIGH CONFIDENCE HYPOTHESIS (UNCONFIRMED)',
        color: '#FFB300',
        desc: 'Sysmon Event ID 10 detected on `lsass.exe`. Suspected Mimikatz memory injection. Forensic memory dump required for verification.'
      },
      {
        day: 'DAY 5 (OCT 30)',
        title: 'LATERAL MOVEMENT ATTEMPT',
        status: 'CRITICAL THREAT IN PROGRESS',
        color: '#FF4B4B',
        desc: 'WMI authentication from `WS-041` to Domain Controller `DC-01`. Immediate network isolation and RFC 3227 memory triage initiated!'
      }
    ];

    const nodes = container.querySelectorAll('.timeline-node-item');
    const drawer = container.querySelector('.timeline-evidence-drawer');

    window.inspectTimelineMilestone = function(idx, el, event) {
      if (event) event.stopPropagation();
      else if (window.event) window.event.stopPropagation();

      const m = milestones[idx];
      if (!m) return;

      nodes.forEach(n => n.classList.remove('active'));
      el.classList.add('active');

      if (drawer) {
        gsap.fromTo(drawer, { opacity: 0, y: 8 }, {
          opacity: 1, y: 0, duration: 0.3, onStart: () => {
            drawer.innerHTML = `
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="font-family: var(--font-mono); font-size: 11px; color: var(--neon-amber); font-weight: 700;">${m.day}</span>
                <span style="font-family: var(--font-mono); font-size: 10px; color: ${m.color}; font-weight: 700;">${m.status}</span>
              </div>
              <div style="font-size: 0.95rem; font-weight: 700; color: #FFF; margin-bottom: 4px;">
                ${m.title}
              </div>
              <div style="font-size: 12px; color: #CBD5E1; line-height: 1.5;">
                ${m.desc}
              </div>
            `;
          }
        });
      }
    };
  },

  // 9. Incident Response Decision: RFC 3227 Volatility
  initIRDecision: function(containerId) {
    const container = document.getElementById(containerId);
    if (!container || typeof gsap === 'undefined') return;
    container.addEventListener('click', (e) => e.stopPropagation());

    const outcomes = [
      {
        verdict: 'FATAL FORENSIC ERROR: REBOOT DESTROYS EVIDENCE!',
        color: '#FF4B4B',
        desc: 'Rebooting purges volatile RAM. The unencrypted Cobalt Strike beacon, in-memory process injection, active network connections, and cryptographic keys are erased forever!'
      },
      {
        verdict: 'OPTIMAL CSIRT ACTION: ACQUIRE RAM + NETWORK ISOLATION',
        color: '#00E676',
        desc: 'CORRECT! Adheres strictly to RFC 3227 Order of Volatility. Captures volatile memory via EDR or winpmem while isolating the host to halt lateral movement without destroying live artifacts.'
      },
      {
        verdict: 'FLAWED ACTION: ANTIVIRUS SCAN CONTAMINATES METADATA',
        color: '#FFB300',
        desc: 'Running a disk scan touches thousands of files, updating NTFS $MFT Access Timestamps ($STANDARD_INFORMATION) and destroying the forensic timeline. Never scan a live suspect system!'
      }
    ];

    const btns = container.querySelectorAll('.decision-btn');
    const panel = container.querySelector('.decision-feedback-panel');

    window.selectIRChoice = function(idx, el, event) {
      if (event) event.stopPropagation();
      else if (window.event) window.event.stopPropagation();

      const o = outcomes[idx];
      if (!o) return;

      btns.forEach(b => b.classList.remove('selected'));
      el.classList.add('selected');

      if (panel) {
        gsap.fromTo(panel, { opacity: 0, y: 6 }, {
          opacity: 1, y: 0, duration: 0.3, onStart: () => {
            panel.innerHTML = `
              <div style="color: ${o.color}; font-weight: 700; font-size: 0.95rem; margin-bottom: 4px;">
                ${o.verdict}
              </div>
              <div style="font-size: 12px; color: #E2E8F0; line-height: 1.5;">
                ${o.desc}
              </div>
            `;
          }
        });
      }
    };
  },

  // 10. Final Incident Briefing Dossier (Day 6)
  initBriefingDossier: function(containerId) {
    const container = document.getElementById(containerId);
    if (!container || typeof gsap === 'undefined') return;
    container.addEventListener('click', (e) => e.stopPropagation());

    const sections = {
      'patient-zero': '<strong>Patient Zero:</strong> Workstation <code>WS-041</code> assigned to Finance Analyst (j.smith). Compromised via spearphishing attachment at 13:42 UTC on Oct 26.',
      'threat-actor': '<strong>Attributed Actor:</strong> <code>UNC-PHOENIX</code> (State-Sponsored Aerospace Espionage). Motivation: SCADA intellectual property and turbine telemetry.',
      'lateral-path': '<strong>Lateral Movement:</strong> Spearphish -> Macro Execution -> WMI Process Creation -> LSASS In-Memory Dump -> Domain Controller DC-01 Foothold.',
      'containment': '<strong>Remediation Executed:</strong> Workstation isolated via SOAR; KRBTGT password reset performed TWICE with 10-hour replication window; C2 domains sinkholed.'
    };

    const tabs = container.querySelectorAll('.briefing-tab-btn');
    const contentBox = container.querySelector('.briefing-tab-content');

    window.switchBriefingTab = function(key, el, event) {
      if (event) event.stopPropagation();
      else if (window.event) window.event.stopPropagation();

      const text = sections[key];
      if (!text) return;

      tabs.forEach(t => t.classList.remove('active'));
      el.classList.add('active');

      if (contentBox) {
        gsap.fromTo(contentBox, { opacity: 0, y: 6 }, {
          opacity: 1, y: 0, duration: 0.25, onStart: () => {
            contentBox.innerHTML = text;
          }
        });
      }
    };
  }
};

