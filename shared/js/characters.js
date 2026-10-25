/**
 * characters.js - Original Animated Cybersecurity Mascots & Expressive Reactions
 * Upgraded Interactive Version for Threat Intelligence & Incident Response
 * 
 * Features:
 * - Expressive SVG rendering with hardware-accelerated animations
 * - Interactive click handling with purposeful cybersecurity tips & reactions
 * - Event isolation (stopPropagation) preventing accidental slide navigation or animation pauses
 * - Dynamic cyber-speech bubble popovers with automatic dismissal
 */

window.CyberCharacters = {
  // Speech dialog bank
  dialogues: {
    detective: [
      "Evidence is only as reliable as its provenance! Always verify SHA-256 hashes and RFC 5322 headers before drawing conclusions.",
      "Notice subtle anomalies: a certificate issued 2 days ago for an enterprise portal is an immediate red flag!",
      "Remember NATO Admiralty Code B2: The source is usually reliable, and intelligence is probably true, but always corroborate independently.",
      "In the Diamond Model, never conflate the Adversary with the Infrastructure. A compromised VPS is just a pivot, not the operator."
    ],
    alertBot: [
      "Alert volume: 14,200 EPS! Prune false positives with strict Sigma conditions or your Tier 1 SOC analysts will burn out!",
      "Kerberos Event 4768 pre-authentication failed with status 0x18! That is bad password telemetry indicating an active spray.",
      "Network taps do not lie! Even if an attacker gains SYSTEM privileges on the endpoint, out-of-band Zeek still catches the C2 handshake.",
      "Do not treat every ping as an APT! Verify whether the telemetry represents benign Internet noise or targeted exploitation."
    ],
    guardian: [
      "Defense-in-depth verified! Multi-factor authentication, network segmentation, and zero-trust boundaries are active.",
      "Remember the KRBTGT double-reset rule: wait 10 hours for ticket lifetimes to expire between resets to prevent enterprise lockout!",
      "Containment must be targeted. Isolate the affected VLAN or host, but never pull the power plug and dump volatile RAM!",
      "Air-gapping is our ultimate containment tool for ICS/SCADA. When corporate IT is hit, sever the substation bridge immediately!"
    ],
    impostor: [
      "Busted! Look closely at that typosquatted domain and the SPF=fail header!",
      "Attackers rely on cognitive urgency: 'MANDATORY WIRE IN 30 MINUTES'. Calm down, check the RFC 5321 Return-Path, and verify out-of-band.",
      "Never enable macros on untrusted Office documents! Obfuscated VBA drops Living-off-the-Land Lolbins like certutil.",
      "Credential harvesters love fake Microsoft 365 login portals. Always inspect the SSL certificate CN and SAN before typing credentials."
    ],
    evidenceBot: [
      "RFC 3227 Order of Volatility: CPU registers & RAM first, swap second, disk third, remote logs fourth!",
      "DO NOT REBOOT! Power cycling a compromised machine instantly destroys running process memory, injected DLLs, and encryption keys.",
      "Chain of custody is sacred: hash evidence immediately with SHA-256 and store in write-blocked forensic containers.",
      "KAPE triage acquisition captures MFT, USN Journal, and Event Logs in under 90 seconds without altering disk evidence."
    ]
  },

  dialogueIndices: {
    detective: 0,
    alertBot: 0,
    guardian: 0,
    impostor: 0,
    evidenceBot: 0
  },

  // Interactive Click Handler
  interact: function(type, el, event) {
    if (event) {
      event.stopPropagation();
      event.preventDefault();
    }

    const mascotEl = el.closest('.cyber-mascot') || el;
    
    // 1. Trigger visual spring animation
    mascotEl.classList.remove('interactive-bounce');
    void mascotEl.offsetWidth; // Trigger reflow
    mascotEl.classList.add('interactive-bounce');

    // 2. Select dialog
    const list = this.dialogues[type] || this.dialogues.detective;
    const currentIdx = this.dialogueIndices[type] || 0;
    const message = list[currentIdx % list.length];
    this.dialogueIndices[type] = currentIdx + 1;

    // 3. Display speech popover
    this.showSpeechBubble(mascotEl, type, message);
  },

  showSpeechBubble: function(anchorEl, type, text) {
    // Remove existing bubble on this element
    const existing = document.querySelector('.cyber-speech-bubble');
    if (existing) existing.remove();

    const titles = {
      detective: "🔍 Threat Detective — Field Insight",
      alertBot: "🤖 Alert Bot — Telemetry Warning",
      guardian: "🛡️ Security Guardian — Defensive Policy",
      impostor: "⚠️ Phishing Impostor — Deception Exposed",
      evidenceBot: "💾 Evidence Robot — Forensics Directive"
    };

    const colors = {
      detective: "#00F2FE",
      alertBot: "#FFB300",
      guardian: "#00E676",
      impostor: "#FF4B4B",
      evidenceBot: "#B388FF"
    };

    const bubble = document.createElement('div');
    bubble.className = 'cyber-speech-bubble';
    bubble.style.cssText = `
      position: absolute;
      background: rgba(10, 17, 40, 0.96);
      border: 1px solid ${colors[type] || '#00F2FE'};
      border-radius: 8px;
      padding: 10px 14px;
      color: #F8FAFC;
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 11px;
      line-height: 1.5;
      max-width: 280px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.7), 0 0 15px ${colors[type] || '#00F2FE'}33;
      z-index: 10000;
      backdrop-filter: blur(10px);
      pointer-events: auto;
      animation: popIn 0.25s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    `;

    bubble.innerHTML = `
      <div style="font-family: 'Space Grotesk', sans-serif; font-weight: 700; color: ${colors[type] || '#00F2FE'}; font-size: 11px; margin-bottom: 4px; display: flex; justify-content: space-between; align-items: center;">
        <span>${titles[type] || 'Cyber Intelligence Tip'}</span>
        <span style="cursor: pointer; opacity: 0.7; font-size: 12px; margin-left: 8px;" onclick="this.closest('.cyber-speech-bubble').remove(); event.stopPropagation();">✕</span>
      </div>
      <div style="color: #CBD5E1;">${text}</div>
    `;

    document.body.appendChild(bubble);

    // Position bubble above or below the anchor element
    const rect = anchorEl.getBoundingClientRect();
    const bubbleRect = bubble.getBoundingClientRect();
    
    let top = rect.top - bubbleRect.height - 10;
    let left = rect.left + (rect.width / 2) - (bubbleRect.width / 2);

    if (top < 10) {
      top = rect.bottom + 10; // Flip below if off-screen top
    }
    if (left < 10) left = 10;
    if (left + bubbleRect.width > window.innerWidth - 10) {
      left = window.innerWidth - bubbleRect.width - 10;
    }

    bubble.style.top = `${top + window.scrollY}px`;
    bubble.style.left = `${left + window.scrollX}px`;

    // Prevent clicking inside bubble from closing or triggering slide navigation
    bubble.addEventListener('click', (e) => e.stopPropagation());

    // Auto-dismiss after 6 seconds
    setTimeout(() => {
      if (bubble.parentNode) {
        bubble.style.opacity = '0';
        bubble.style.transform = 'translateY(-4px)';
        bubble.style.transition = 'all 0.25s ease';
        setTimeout(() => bubble.remove(), 250);
      }
    }, 6000);
  },

  // Threat Detective SVG
  getDetective: function(state = 'neutral', width = 120, height = 120) {
    const isAlert = state === 'alert' || state === 'inspecting';
    const glassTransform = isAlert ? 'translate(10, -5) rotate(-15)' : 'translate(0, 0)';
    
    return `
      <div class="cyber-mascot detective ${state}" 
           title="Threat Detective (Click for analytical insight)" 
           onclick="window.CyberCharacters.interact('detective', this, event)"
           style="width:${width}px; height:${height}px; cursor: pointer;">
        <svg viewBox="0 0 100 100" width="100%" height="100%">
          <!-- Trench Coat Body -->
          <path d="M 25 95 L 35 48 L 65 48 L 75 95 Z" fill="#1E293B" stroke="#00F2FE" stroke-width="2"/>
          <!-- Trench Coat Collar -->
          <path d="M 35 48 L 50 62 L 65 48 L 50 42 Z" fill="#0F172A" stroke="#00F2FE" stroke-width="1.5"/>
          <!-- Tie / Badge -->
          <path d="M 48 48 L 52 48 L 54 70 L 50 75 L 46 70 Z" fill="#FFB300"/>
          
          <!-- Detective Fedora Hat -->
          <ellipse cx="50" cy="30" rx="36" ry="7" fill="#0A1128" stroke="#00F2FE" stroke-width="2"/>
          <path d="M 28 30 C 28 12, 72 12, 72 30 Z" fill="#0F172A" stroke="#00F2FE" stroke-width="2"/>
          <path d="M 29 27 Q 50 22 71 27" stroke="#FFB300" stroke-width="3" fill="none"/>
          
          <!-- Eyes / Sunglasses -->
          <g class="detective-eyes">
            <rect x="36" y="34" width="11" height="6" rx="2" fill="#00F2FE"/>
            <rect x="53" y="34" width="11" height="6" rx="2" fill="#00F2FE"/>
            <line x1="47" y1="37" x2="53" y2="37" stroke="#00F2FE" stroke-width="2"/>
          </g>

          <!-- Interactive Magnifying Glass -->
          <g class="detective-glass" transform="${glassTransform}" style="transition: transform 0.3s ease;">
            <circle cx="68" cy="48" r="14" fill="rgba(0, 242, 254, 0.2)" stroke="#00F2FE" stroke-width="3"/>
            <circle cx="68" cy="48" r="11" fill="none" stroke="#FFF" stroke-width="1" opacity="0.6"/>
            <line x1="78" y1="58" x2="92" y2="72" stroke="#FFB300" stroke-width="4" stroke-linecap="round"/>
            <line x1="64" y1="44" x2="72" y2="52" stroke="#FFF" stroke-width="2" stroke-linecap="round" opacity="0.7"/>
          </g>
        </svg>
      </div>
    `;
  },

  // Alert Bot SVG
  getAlertBot: function(state = 'calm', width = 100, height = 100) {
    const isAlarm = state === 'alarm' || state === 'panic';
    const eyeColor = isAlarm ? '#FF4B4B' : '#00E676';
    const antennaGlow = isAlarm ? '#FF4B4B' : '#00F2FE';

    return `
      <div class="cyber-mascot alert-bot ${state}" 
           title="Alert Bot (Click for telemetry check)" 
           onclick="window.CyberCharacters.interact('alertBot', this, event)"
           style="width:${width}px; height:${height}px; cursor: pointer;">
        <svg viewBox="0 0 100 100" width="100%" height="100%">
          <!-- Antenna -->
          <line x1="50" y1="18" x2="50" y2="30" stroke="#64748B" stroke-width="3"/>
          <circle cx="50" cy="14" r="6" fill="${antennaGlow}" class="antenna-bulb">
            <animate attributeName="opacity" values="0.4;1;0.4" dur="${isAlarm ? '0.4s' : '1.5s'}" repeatCount="indefinite"/>
          </circle>

          <!-- Head Chassis -->
          <rect x="22" y="30" width="56" height="42" rx="10" fill="#0F172A" stroke="${isAlarm ? '#FF4B4B' : '#00F2FE'}" stroke-width="2.5"/>
          
          <!-- Visor Display Screen -->
          <rect x="28" y="36" width="44" height="20" rx="5" fill="#020617" stroke="rgba(255,255,255,0.1)"/>
          
          <!-- Expressive Eyes -->
          <circle cx="39" cy="46" r="4.5" fill="${eyeColor}"/>
          <circle cx="61" cy="46" r="4.5" fill="${eyeColor}"/>
          ${isAlarm ? '<path d="M 34 40 L 44 44 M 66 40 L 56 44" stroke="#FF4B4B" stroke-width="2"/>' : ''}

          <!-- Mouth / Audio Waveform -->
          <path d="${isAlarm ? 'M 40 64 Q 50 58 60 64' : 'M 40 61 Q 50 67 60 61'}" fill="none" stroke="${eyeColor}" stroke-width="2" stroke-linecap="round"/>

          <!-- Ear Bolts -->
          <rect x="17" y="44" width="5" height="14" rx="2" fill="#64748B"/>
          <rect x="78" y="44" width="5" height="14" rx="2" fill="#64748B"/>

          <!-- Body Stand -->
          <path d="M 38 72 L 32 94 L 68 94 L 62 72 Z" fill="#1E293B" stroke="#00F2FE" stroke-width="1.5"/>
          <circle cx="50" cy="83" r="3" fill="#FFB300"/>
        </svg>
      </div>
    `;
  },

  // Security Guardian SVG
  getGuardian: function(state = 'defending', width = 110, height = 110) {
    return `
      <div class="cyber-mascot guardian ${state}" 
           title="Security Guardian (Click for defense policy)" 
           onclick="window.CyberCharacters.interact('guardian', this, event)"
           style="width:${width}px; height:${height}px; cursor: pointer;">
        <svg viewBox="0 0 100 100" width="100%" height="100%">
          <!-- Guardian Helm -->
          <path d="M 30 25 C 30 10, 70 10, 70 25 L 75 48 C 75 62, 50 72, 50 72 C 50 72, 25 62, 25 48 Z" fill="#0F172A" stroke="#00F2FE" stroke-width="2"/>
          <!-- Visor T-Slit -->
          <path d="M 36 36 L 64 36 L 50 48 Z" fill="#00E5FF" opacity="0.85"/>
          <!-- Protective Cyber Shield -->
          <path d="M 50 20 L 85 30 L 78 75 C 70 90, 50 96, 50 96 C 50 96, 30 90, 22 75 L 15 30 Z" 
                fill="url(#shieldGrad)" stroke="#4FACFE" stroke-width="2" opacity="0.9"/>
          <!-- Keyhole / Token Ingot -->
          <circle cx="50" cy="52" r="7" fill="#FFB300"/>
          <path d="M 48 56 L 52 56 L 54 68 L 46 68 Z" fill="#FFB300"/>
          <defs>
            <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="rgba(0, 242, 254, 0.4)"/>
              <stop offset="100%" stop-color="rgba(79, 172, 254, 0.1)"/>
            </linearGradient>
          </defs>
        </svg>
      </div>
    `;
  },

  // Phishing Impostor SVG
  getPhishingImpostor: function(state = 'luring', width = 110, height = 110) {
    return `
      <div class="cyber-mascot impostor ${state}" 
           title="Phishing Impostor (Click to expose social engineering lure)" 
           onclick="window.CyberCharacters.interact('impostor', this, event)"
           style="width:${width}px; height:${height}px; cursor: pointer;">
        <svg viewBox="0 0 100 100" width="100%" height="100%">
          <!-- Dark Disguised Silhouette -->
          <path d="M 28 85 C 28 50, 72 50, 72 85 Z" fill="#090D1A" stroke="#FF4B4B" stroke-width="2"/>
          <!-- Disguised Hood / Cowl -->
          <path d="M 30 45 C 30 18, 70 18, 70 45 C 70 60, 50 68, 50 68 C 50 68, 30 60, 30 45 Z" fill="#050814" stroke="#FF4B4B" stroke-width="2"/>
          
          <!-- Deceptive Glowing Red Eyes -->
          <ellipse cx="42" cy="42" rx="4" ry="2" fill="#FF4B4B" transform="rotate(-10 42 42)"/>
          <ellipse cx="58" cy="42" rx="4" ry="2" fill="#FF4B4B" transform="rotate(10 58 42)"/>

          <!-- Suspicious Envelope with Poison Fish Hook -->
          <g class="lure-envelope" transform="translate(32, 60)">
            <rect x="0" y="0" width="36" height="24" rx="2" fill="#1E293B" stroke="#FFB300" stroke-width="1.5"/>
            <path d="M 0 0 L 18 14 L 36 0" fill="none" stroke="#FFB300" stroke-width="1.5"/>
            <!-- Fish hook dangling -->
            <path d="M 18 -10 L 18 4 Q 18 10 12 10 Q 6 10 6 4 L 8 4" fill="none" stroke="#FF4B4B" stroke-width="2"/>
          </g>
        </svg>
      </div>
    `;
  },

  // Evidence Robot SVG
  getEvidenceRobot: function(state = 'analyzing', width = 100, height = 100) {
    return `
      <div class="cyber-mascot evidence-bot ${state}" 
           title="Evidence Robot (Click to verify RFC 3227 chain of custody)" 
           onclick="window.CyberCharacters.interact('evidenceBot', this, event)"
           style="width:${width}px; height:${height}px; cursor: pointer;">
        <svg viewBox="0 0 100 100" width="100%" height="100%">
          <!-- Scanner Eye Bar -->
          <rect x="25" y="24" width="50" height="34" rx="6" fill="#0F172A" stroke="#B388FF" stroke-width="2"/>
          <line x1="30" y1="41" x2="70" y2="41" stroke="#38BDF8" stroke-width="1" stroke-dasharray="2,2"/>
          <circle cx="50" cy="41" r="5" fill="#B388FF">
            <animate attributeName="cx" values="32;68;32" dur="2s" repeatCount="indefinite"/>
          </circle>
          
          <!-- Chest Artifact Register -->
          <rect x="30" y="62" width="40" height="26" rx="4" fill="#1E293B" stroke="#B388FF" stroke-width="1.5"/>
          <text x="50" y="74" fill="#00E676" font-family="monospace" font-size="7" text-anchor="middle">SHA-256</text>
          <text x="50" y="83" fill="#94A3B8" font-family="monospace" font-size="6" text-anchor="middle">RFC 3227</text>

          <!-- Treads / Base -->
          <ellipse cx="50" cy="94" rx="22" ry="4" fill="#64748B"/>
        </svg>
      </div>
    `;
  },

  // Aliases for resilience
  getImpostor: function(state, w, h) { return this.getPhishingImpostor(state, w, h); },
  getEvidenceBot: function(state, w, h) { return this.getEvidenceRobot(state, w, h); },

  // Auto-mount and Lifecycle Manager across Portal and Slides
  mountAll: function(root = document) {
    if (!root) root = document;

    // 1. Attribute-based mounts: [data-mascot]
    const elements = root.querySelectorAll ? root.querySelectorAll('[data-mascot]') : [];
    elements.forEach(el => {
      if (el.hasChildNodes() && el.querySelector('.cyber-mascot')) return;
      const type = el.getAttribute('data-mascot');
      const mood = el.getAttribute('data-mood') || 'neutral';
      const w = parseInt(el.getAttribute('data-width') || '65', 10);
      const h = parseInt(el.getAttribute('data-height') || '65', 10);

      if (type === 'detective') el.innerHTML = this.getDetective(mood, w, h);
      else if (type === 'alertBot') el.innerHTML = this.getAlertBot(mood, w, h);
      else if (type === 'guardian') el.innerHTML = this.getGuardian(mood, w, h);
      else if (type === 'impostor' || type === 'phishingImpostor') el.innerHTML = this.getPhishingImpostor(mood, w, h);
      else if (type === 'evidenceBot' || type === 'evidenceRobot') el.innerHTML = this.getEvidenceRobot(mood, w, h);
    });

    // 2. ID-based mounts for presentation slides & portal
    const idMap = {
      'mascot-title-detective': () => this.getDetective('neutral', 65, 65),
      'mascot-title-guardian': () => this.getGuardian('defending', 65, 65),
      'mascot-soc-alert': () => this.getAlertBot('alarm', 60, 60),
      'mascot-phish-impostor': () => this.getPhishingImpostor('luring', 55, 55),
      'mascot-evidence-bot': () => this.getEvidenceRobot('analyzing', 60, 60),
      'mascot-p1': () => this.getDetective('neutral', 70, 70),
      'mascot-p2': () => this.getAlertBot('calm', 60, 60),
      'mascot-p3': () => this.getGuardian('defending', 65, 65),
      'mascot-p4': () => this.getEvidenceRobot('analyzing', 60, 60)
    };

    for (const [id, getter] of Object.entries(idMap)) {
      const target = (root.querySelector ? root.querySelector('#' + id) : null) || document.getElementById(id);
      if (target && (!target.hasChildNodes() || !target.querySelector('.cyber-mascot'))) {
        target.innerHTML = getter();
      }
    }
  }
};

// Auto-run mount on DOM load
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => window.CyberCharacters && window.CyberCharacters.mountAll());
} else if (window.CyberCharacters) {
  window.CyberCharacters.mountAll();
}
