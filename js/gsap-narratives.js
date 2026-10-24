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
  }
};
