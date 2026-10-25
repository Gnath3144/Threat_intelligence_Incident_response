/**
 * cyber-bg.js - Ambient Cybersecurity Telemetry Network Background
 * High-performance, lightweight HTML5 Canvas animation featuring moving telemetry nodes,
 * connecting cyber-lines, and subtle data packet pulses.
 * 
 * Performance & Resilience:
 * - < 50 nodes, low CPU footprint, 60fps requestAnimationFrame
 * - Automatic pause on tab blur (document.hidden)
 * - Safe fallback to CSS grid if canvas is unsupported
 * - Pointer-events: none (zero interference with slide navigation or clicks)
 */

(function() {
  function initCyberBackground() {
    if (document.getElementById('cyber-bg-canvas')) return;

    const canvas = document.createElement('canvas');
    canvas.id = 'cyber-bg-canvas';
    canvas.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:0;opacity:0.6;';
    document.body.insertBefore(canvas, document.body.firstChild);

    const ctx = canvas.getContext('2d');
    if (!ctx) return; // Fallback: CSS ambient grid in theme-cyber-soc.css remains active

    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    window.addEventListener('resize', () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    }, { passive: true });

    // Node generator
    const NODE_COUNT = Math.min(Math.floor((width * height) / 22000), 45);
    const nodes = [];
    const colors = ['#00F2FE', '#4FACFE', '#00E5FF', '#38BDF8'];

    for (let i = 0; i < NODE_COUNT; i++) {
      nodes.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.55,
        vy: (Math.random() - 0.5) * 0.55,
        radius: Math.random() * 1.8 + 1.2,
        color: colors[Math.floor(Math.random() * colors.length)],
        pulse: Math.random() * Math.PI
      });
    }

    let isVisible = true;
    document.addEventListener('visibilitychange', () => {
      isVisible = !document.hidden;
      if (isVisible) requestAnimationFrame(render);
    });

    let lastTime = 0;
    function render(time) {
      if (!isVisible) return;
      requestAnimationFrame(render);

      // Cap at ~60fps
      if (time - lastTime < 14) return;
      lastTime = time;

      ctx.clearRect(0, 0, width, height);

      // Update & Draw Nodes
      const maxDist = 125;
      const maxDistSq = maxDist * maxDist;

      for (let i = 0; i < nodes.length; i++) {
        const n = nodes[i];
        n.x += n.vx;
        n.y += n.vy;
        n.pulse += 0.03;

        if (n.x < 0) n.x = width;
        else if (n.x > width) n.x = 0;
        if (n.y < 0) n.y = height;
        else if (n.y > height) n.y = 0;

        // Draw connections
        for (let j = i + 1; j < nodes.length; j++) {
          const n2 = nodes[j];
          const dx = n.x - n2.x;
          const dy = n.y - n2.y;
          const distSq = dx * dx + dy * dy;

          if (distSq < maxDistSq) {
            const alpha = (1 - Math.sqrt(distSq) / maxDist) * 0.22;
            ctx.beginPath();
            ctx.strokeStyle = `rgba(0, 242, 254, ${alpha})`;
            ctx.lineWidth = 0.8;
            ctx.moveTo(n.x, n.y);
            ctx.lineTo(n2.x, n2.y);
            ctx.stroke();
          }
        }

        // Draw node
        const glow = Math.sin(n.pulse) * 0.4 + 0.6;
        ctx.beginPath();
        ctx.arc(n.x, n.y, n.radius * glow, 0, Math.PI * 2);
        ctx.fillStyle = n.color;
        ctx.shadowColor = n.color;
        ctx.shadowBlur = 6;
        ctx.fill();
        ctx.shadowBlur = 0;
      }
    }

    requestAnimationFrame(render);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCyberBackground);
  } else {
    initCyberBackground();
  }
})();
