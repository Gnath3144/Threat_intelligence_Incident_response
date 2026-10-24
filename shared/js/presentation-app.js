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
    });

    Reveal.on('ready', event => {
      updateTelemetryStatusBar(event);
      updateCustomCounter(event);
      triggerSlideInteractiveEngines(event.currentSlide);
    });
  }

  // 2. Prevent clicks on interactive cards, buttons, widgets, and mascots from bubbling to Reveal.js
  document.addEventListener('click', (e) => {
    if (e.target.closest('.cyber-card, .interactive-decision-box, .three-canvas-container, .cyber-mascot, .terminal-buffer, .intel-cycle-container, .decision-btn, .phish-hotspot, button, a')) {
      e.stopPropagation();
    }
  }, true);

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
  }

  // 9. Interactive Quiz / Decision Widget Handler
  window.selectDecision = function(btnEl, isCorrect, explanation, event) {
    if (event) event.stopPropagation();
    else if (window.event) window.event.stopPropagation();

    const parent = btnEl.closest('.decision-options');
    const expBox = parent.querySelector('.decision-explanation');
    
    parent.querySelectorAll('.decision-btn').forEach(btn => {
      btn.classList.remove('correct', 'incorrect');
    });

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

    const descEl = document.getElementById('diamond-vertex-desc');
    const dataMap = {
      'Adversary': {
        title: 'Adversary Vertex',
        details: 'The threat actor or group behind the campaign (e.g., UNC-PHOENIX, APT41). Evaluates motivation (financial, geopolitical), sponsorship, capability tier, and operator skill level.'
      },
      'Capability': {
        title: 'Capability Vertex',
        details: 'The specific tools, techniques, exploits, and malware payloads wielded by the adversary (e.g., Certutil staging, Living-off-the-Land LOLBins, BlackCat ransomware encryptors).'
      },
      'Infrastructure': {
        title: 'Infrastructure Vertex',
        details: 'The logical and physical network nodes delivering capabilities and receiving C2 traffic (e.g., Bulletproof hosting IPs, Fast-Flux domains, Cloudflare CDN reverse proxies, SSL certificates).'
      },
      'Victim': {
        title: 'Victim Vertex',
        details: 'The organization, domain account, host, or network subnet targeted (e.g., AeroGrid Power Distribution Portal, Host 10.0.4.12, domain admin credentials).'
      }
    };

    if (descEl && dataMap[vertexName]) {
      descEl.innerHTML = `<strong>${dataMap[vertexName].title}:</strong> ${dataMap[vertexName].details}`;
      descEl.style.borderColor = '#00F2FE';
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
