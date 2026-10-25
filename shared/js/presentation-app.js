/**
 * presentation-app.js - Presentation Controller & Interactive Widget Engine
 * Completely Cleaned of Trainer HUD for Pure Student-Facing Classroom Projection
 * Includes Full Event Isolation (Prevents Accidental Slide Advances or Animation Pauses)
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Initialize Reveal.js Engine with Full Interaction Hardening
  if (typeof Reveal !== 'undefined') {
    Reveal.initialize({
      hash: true,
      slideNumber: false, // Handled by custom day-specific counter
      controls: true,
      controlsTutorial: false,
      progress: true,
      center: true,
      transition: 'fade',
      transitionSpeed: 'fast',
      backgroundTransition: 'fade',
      width: 1280,
      height: 720,
      margin: 0.04,
      minScale: 0.2,
      maxScale: 2.0,
      pause: false, // Disable presentation pause mode so animations never freeze
      keyboard: {
        // Disable pause keys (b, v, period) that cause black screen / freeze
        66: null, // 'b'
        86: null, // 'v'
        190: null // '.'
      }
    });

    Reveal.on('slidechanged', event => {
      updateTelemetryStatusBar(event);
      updateCustomCounter(event);
      triggerSlideInteractiveEngines(event.currentSlide);
      if (window.CyberCharacters && window.CyberCharacters.mountAll) {
        window.CyberCharacters.mountAll(event.currentSlide);
      }
    });

    Reveal.on('ready', event => {
      updateTelemetryStatusBar(event);
      updateCustomCounter(event);
      triggerSlideInteractiveEngines(event.currentSlide);
      if (window.CyberCharacters && window.CyberCharacters.mountAll) {
        window.CyberCharacters.mountAll(document);
      }
    });
  }

  // 2. Prevent clicks on interactive elements from bubbling beyond document
  document.addEventListener('click', (e) => {
    if (e.target.closest('.cyber-card, .interactive-decision-box, .three-canvas-container, .cyber-mascot, .terminal-buffer, .intel-cycle-container, .decision-btn, .phish-hotspot, button, a, [onclick], .cyber-badge, .nav-day-btn, .portal-home-btn, .decision-options, .indicator-station, .triage-alert-card, .log-inspector-card, .timeline-node-item, .briefing-tab-btn, .indicator-pill-btn, .log-field-hotspot, .timeline-evidence-drawer, .briefing-dossier-card')) {
      e.stopPropagation();
    }
  }, false);

  // 3. Telemetry Status Bar & Module Tracker
  function updateTelemetryStatusBar(event) {
    const slide = event.currentSlide;
    if (!slide) return;
    
    const dayLabel = slide.getAttribute('data-day') || 'DAY 01';
    const modLabel = slide.getAttribute('data-module') || 'COURSE OVERVIEW';
    const sessLabel = slide.getAttribute('data-session') || 'LH3 – 4TH FLOOR';

    const dayEl = document.getElementById('status-day');
    const modEl = document.getElementById('status-module');
    const sessEl = document.getElementById('status-session');

    if (dayEl) dayEl.textContent = dayLabel;
    if (modEl) modEl.textContent = modLabel;
    if (sessEl) sessEl.textContent = sessLabel;
  }

  // 4. Custom Slide Counter
  function updateCustomCounter(event) {
    const counterEl = document.getElementById('custom-slide-counter');
    if (!counterEl || !Reveal) return;
    
    const current = Reveal.getSlidePastCount() + 1;
    const total = Reveal.getTotalSlides();
    const dayBadge = Reveal.getCurrentSlide() ? (Reveal.getCurrentSlide().getAttribute('data-day') || 'DAY') : 'DAY';
    counterEl.innerHTML = `${dayBadge}: SLIDE <span>${String(current).padStart(2, '0')}</span> / ${String(total).padStart(2, '0')}`;
  }

  // 5. Global Keyboard Shortcuts Handler (Cleaned of Trainer HUD)
  document.addEventListener('keydown', e => {
    if (['INPUT', 'TEXTAREA'].includes(e.target.tagName)) return;

    if (e.key === '?' || e.key === 'h' || e.key === 'H') {
      e.preventDefault();
      toggleShortcutModal();
    } else if (e.key === 'f' || e.key === 'F') {
      e.preventDefault();
      toggleFullScreen();
    }
  });

  // 6. Shortcut Modal Controller
  const shortcutModal = document.getElementById('shortcut-modal');
  function toggleShortcutModal() {
    if (shortcutModal) {
      shortcutModal.classList.toggle('active');
    }
  }
  window.toggleShortcutModal = toggleShortcutModal;

  // 7. Fullscreen Toggle
  function toggleFullScreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      if (document.exitFullscreen) document.exitFullscreen();
    }
  }
  window.toggleFullScreen = toggleFullScreen;

  // 8. Interactive Slide Engines Trigger
  function triggerSlideInteractiveEngines(slide) {
    if (!slide) return;

    // A. Three.js Viewports
    const globeCanvas = slide.querySelector('#globe-3d-canvas');
    if (globeCanvas && window.Cyber3D) {
      setTimeout(() => window.Cyber3D.renderThreatGlobe('globe-3d-canvas'), 100);
    }

    const defenseMesh = slide.querySelector('#defense-mesh-3d');
    if (defenseMesh && window.Cyber3D) {
      setTimeout(() => window.Cyber3D.renderDefenseMesh('defense-mesh-3d'), 100);
    }

    const shieldCanvas = slide.querySelector('#shield-3d-canvas');
    if (shieldCanvas && window.Cyber3D) {
      setTimeout(() => window.Cyber3D.renderSecurityShield('shield-3d-canvas'), 100);
    }

    // B. GSAP Narratives
    const intelCycle = slide.querySelector('#intel-cycle-demo');
    if (intelCycle && window.CyberGSAP) {
      setTimeout(() => window.CyberGSAP.initIntelCycle('intel-cycle-demo'), 100);
    }

    const phishDissector = slide.querySelector('#phishing-dissector-demo');
    if (phishDissector && window.CyberGSAP) {
      setTimeout(() => window.CyberGSAP.initPhishingDissector('phishing-dissector-demo'), 100);
    }

    const telemetryCorrelator = slide.querySelector('#telemetry-correlator-demo');
    if (telemetryCorrelator && window.CyberGSAP) {
      setTimeout(() => window.CyberGSAP.initTelemetryCorrelator('telemetry-correlator-demo'), 100);
    }

    const aerogridBreaker = slide.querySelector('#aerogrid-breaker-demo');
    if (aerogridBreaker && window.CyberGSAP) {
      setTimeout(() => window.CyberGSAP.initAeroGridBreaker('aerogrid-breaker-demo'), 100);
    }

    const indicatorStation = slide.querySelector('#indicator-station-demo');
    if (indicatorStation && window.CyberGSAP) {
      setTimeout(() => window.CyberGSAP.initIndicatorStation('indicator-station-demo'), 100);
    }

    const threatTriage = slide.querySelector('#threat-triage-demo');
    if (threatTriage && window.CyberGSAP) {
      setTimeout(() => window.CyberGSAP.initThreatTriage('threat-triage-demo'), 100);
    }

    const logInspector = slide.querySelector('#log-inspector-demo');
    if (logInspector && window.CyberGSAP) {
      setTimeout(() => window.CyberGSAP.initLogInspector('log-inspector-demo'), 100);
    }

    const incidentTimeline = slide.querySelector('#incident-timeline-demo');
    if (incidentTimeline && window.CyberGSAP) {
      setTimeout(() => window.CyberGSAP.initIncidentTimeline('incident-timeline-demo'), 100);
    }

    const irDecision = slide.querySelector('#ir-decision-demo');
    if (irDecision && window.CyberGSAP) {
      setTimeout(() => window.CyberGSAP.initIRDecision('ir-decision-demo'), 100);
    }

    const briefingDossier = slide.querySelector('#briefing-dossier-demo');
    if (briefingDossier && window.CyberGSAP) {
      setTimeout(() => window.CyberGSAP.initBriefingDossier('briefing-dossier-demo'), 100);
    }
  }

  // 9. Interactive Quiz / Decision Widget Handler
  window.selectDecision = function(btnEl, isCorrect, explanation, event) {
    if (event) event.stopPropagation();
    else if (window.event) window.event.stopPropagation();

    const container = btnEl.closest('.interactive-decision-box, .decision-options, .cyber-card') || btnEl.parentElement;
    const expBox = container ? (container.querySelector('.decision-explanation') || (container.parentElement ? container.parentElement.querySelector('.decision-explanation') : null)) : null;
    
    if (container) {
      container.querySelectorAll('.decision-btn').forEach(btn => {
        btn.classList.remove('correct', 'incorrect');
      });
    }

    if (isCorrect) {
      btnEl.classList.add('correct');
      if (expBox) {
        expBox.innerHTML = `<strong>CORRECT:</strong> ${explanation}`;
        expBox.style.color = '#00E676';
      }
    } else {
      btnEl.classList.add('incorrect');
      if (expBox) {
        expBox.innerHTML = `<strong>INCORRECT:</strong> ${explanation}`;
        expBox.style.color = '#FF4B4B';
      }
    }
  };

  // 10. Diamond Model Interactive Vertex Inspector
  window.inspectDiamondVertex = function(vertexName, event) {
    if (event) event.stopPropagation();
    else if (window.event) window.event.stopPropagation();

    // Toggle active state on interactive nodes
    const allButtons = document.querySelectorAll('.diamond-vertex-btn, .diamond-hub-btn');
    allButtons.forEach(btn => {
      btn.classList.remove('active-vertex');
      if (btn.getAttribute('data-vertex') === vertexName) {
        btn.classList.add('active-vertex');
      }
    });

    const descEl = document.getElementById('diamond-vertex-desc');
    const dataMap = {
      'Adversary': {
        title: 'Adversary Vertex',
        color: '#FF6B6B',
        badge: 'THREAT ACTOR NEXUS',
        role: 'The entity wielding intent and capabilities against victim assets (e.g., UNC-PHOENIX, APT29, FIN7). Evaluates geopolitical motivation, operational sophistication, sponsorship, and operator working hours.',
        artifacts: 'Campaign identifiers, language code artifacts, keyboard layout markers, operational tempo timestamps.',
        pivot: '<strong>Pivot Strategy:</strong> Pivot from Adversary to Capability (what custom tools do they develop?) and Infrastructure (which bulletproof providers do they lease?).'
      },
      'Capability': {
        title: 'Capability Vertex',
        color: '#4FACFE',
        badge: 'TOOLS & EXPLOITS',
        role: 'All tools, techniques, exploits, and malware used by the adversary across the Cyber Kill Chain (e.g., Certutil staging, PowerShell LOLBins, Cobalt Strike M2, BlackCat ransomware).',
        artifacts: 'File hashes (SHA-256), YARA signatures, command-line arguments, API hooking patterns, CVE exploit code.',
        pivot: '<strong>Pivot Strategy:</strong> Pivot from Capability to Infrastructure (what C2 ports/protocols does the payload beacon to?) and Victim (what systems execute this payload?).'
      },
      'Infrastructure': {
        title: 'Infrastructure Vertex',
        color: '#FFB300',
        badge: 'C2 & TRANSIT NODES',
        role: 'The physical and logical network elements connecting adversary capability to the victim (e.g., Bulletproof VPS, Fast-Flux domains, Cloudflare reverse proxies, Let\'s Encrypt TLS certificates).',
        artifacts: 'IPv4/IPv6 addresses, FQDNs, Certificate Transparency SANs, ASN registrations, dynamic DNS records.',
        pivot: '<strong>Pivot Strategy:</strong> Pivot from Infrastructure to Capability (what payloads are downloaded from this IP?) and Adversary (who registered this domain cluster?).'
      },
      'Victim': {
        title: 'Victim Vertex',
        color: '#00F2FE',
        badge: 'TARGET ASSETS',
        role: 'The target organization, network subnet, host, software application, or user account under attack (e.g., AeroGrid Power Distribution Portal, Host WS-041, Domain Admin credentials).',
        artifacts: 'Hostnames, internal IP subnets, target industry vertical (energy, banking), compromised AD user accounts.',
        pivot: '<strong>Pivot Strategy:</strong> Pivot from Victim to Capability (what vulnerabilities did the victim expose?) and Infrastructure (what external IPs did the victim beacon out to?).'
      },
      'Event': {
        title: 'Intrusion Event Core',
        color: '#00E5FF',
        badge: 'CORE INTRUSION HUB',
        role: 'The mathematical binding point where Adversary, Capability, Infrastructure, and Victim intersect. Every intrusion is represented as a sequence of linked diamond events over time.',
        artifacts: 'Meta-Features: Timestamp, Kill Chain Phase (e.g., Exploitation), Result (Success/Failure), Directionality.',
        pivot: '<strong>Pivot Strategy:</strong> Graphing multiple diamond events reveals the adversary’s multi-phase attack graph, exposing backup C2 channels and lateral movement.'
      }
    };

    const item = dataMap[vertexName];
    if (descEl && item) {
      descEl.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
          <strong style="color: ${item.color}; font-size: 14px;">${item.title}</strong>
          <span class="cyber-badge" style="font-size: 9px; background: rgba(255,255,255,0.06); color: ${item.color}; border: 1px solid ${item.color};">${item.badge}</span>
        </div>
        <div style="font-size: 12px; color: #E2E8F0; line-height: 1.5; margin-bottom: 6px;">
          ${item.role}
        </div>
        <div style="font-size: 11px; color: #94A3B8; margin-bottom: 6px;">
          <strong style="color: #CBD5E1;">Key Telemetry:</strong> ${item.artifacts}
        </div>
        <div style="font-size: 11px; color: var(--emerald-pass); background: rgba(0, 230, 118, 0.08); padding: 5px 8px; border-radius: 4px; border-left: 2px solid var(--emerald-pass);">
          ${item.pivot}
        </div>
      `;
      descEl.style.borderColor = item.color;
    }
  };

  // 11. KRBTGT Double-Reset Countdown Simulation
  window.startKRBTGTTimer = function(event) {
    if (event) event.stopPropagation();
    else if (window.event) window.event.stopPropagation();

    const timerEl = document.getElementById('krbtgt-timer-display');
    if (!timerEl) return;
    
    let hoursRemaining = 10;
    timerEl.innerHTML = `<span style="color: #FFB300;">RESET #1 EXECUTED</span> | Ticket Aging Window: <strong>${hoursRemaining}:00:00</strong> remaining before Reset #2.`;
  };
});
