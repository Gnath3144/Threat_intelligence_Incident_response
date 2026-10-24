/**
 * cyber-3d.js - Lightweight Three.js Experiences for Cybersecurity Keynote
 * Upgraded Interactive Version with Node Raycasting, Explicit Play/Pause Controls,
 * and Full Reveal.js Event Isolation (stopPropagation).
 * 
 * Scenes:
 * 1. Global Threat Intel Globe (Day 1 & Master Portal) - Clickable nodes & C2 telemetry
 * 2. 3D Interconnected Attack Surface Mesh (Day 2 & Day 4) - Clickable enterprise systems
 * 3. 3D Rotating Cryptographic Defense Shield (Day 5 & Day 6) - Clickable containment pulse
 */

window.Cyber3D = {
  scenes: {},

  // 1. Interactive 3D Cyber Threat Globe
  renderThreatGlobe: function(containerId) {
    const container = document.getElementById(containerId);
    if (!container || typeof THREE === 'undefined') return;

    // Avoid duplicate initialization
    if (this.scenes[containerId]) return;

    const width = container.clientWidth || 380;
    const height = container.clientHeight || 320;

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
    camera.position.z = 210;

    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    container.innerHTML = '';
    container.appendChild(renderer.domElement);

    // Prevent any clicks or drags inside container from propagating to Reveal.js
    container.addEventListener('click', (e) => e.stopPropagation());

    // Globe Group
    const globeGroup = new THREE.Group();
    scene.add(globeGroup);

    // Wireframe Sphere
    const sphereGeo = new THREE.SphereGeometry(75, 24, 24);
    const sphereMat = new THREE.MeshBasicMaterial({
      color: 0x00F2FE,
      wireframe: true,
      transparent: true,
      opacity: 0.18
    });
    const sphere = new THREE.Mesh(sphereGeo, sphereMat);
    globeGroup.add(sphere);

    // Inner Core Glow
    const coreGeo = new THREE.SphereGeometry(70, 16, 16);
    const coreMat = new THREE.MeshBasicMaterial({
      color: 0x0A1128,
      transparent: true,
      opacity: 0.85
    });
    const core = new THREE.Mesh(coreGeo, coreMat);
    globeGroup.add(core);

    // Threat Nodes (Coordinates mapped to sphere)
    const nodeCoords = [
      { lat: 12.9716, lon: 77.5946, label: 'Bangalore SOC (Target Infrastructure)', role: 'SOC Pod Telemetry Collector', ip: '10.20.4.15', status: 'Active Ingestion (Healthy)' },
      { lat: 50.1109, lon: 8.6821, label: 'Frankfurt C2 Pivot Node', role: 'Fast-Flux Proxy (Bulletproof Hosting)', ip: '198.51.100.45', status: 'Flagged by NATO B2 Advisory' },
      { lat: 38.9072, lon: -77.0369, label: 'Virginia Cloud Relay', role: 'Staging Bucket (AWS S3 Proxy)', ip: '203.0.113.88', status: 'Exfiltration Relay' },
      { lat: 1.3521, lon: 103.8198, label: 'Singapore Relay Node', role: 'Secondary Fallback C2', ip: '192.0.2.77', status: 'Heartbeat Monitored' },
      { lat: 55.7558, lon: 37.6173, label: 'Adversary Origin (UNC-PHOENIX)', role: 'Threat Actor Primary Operator', ip: '203.0.113.12', status: 'Diamond Model: Adversary Vertex' }
    ];

    function latLonToVector3(lat, lon, radius) {
      const phi = (90 - lat) * (Math.PI / 180);
      const theta = (lon + 180) * (Math.PI / 180);
      const x = -(radius * Math.sin(phi) * Math.cos(theta));
      const z = radius * Math.sin(phi) * Math.sin(theta);
      const y = radius * Math.cos(phi);
      return new THREE.Vector3(x, y, z);
    }

    const nodeMeshes = [];
    nodeCoords.forEach((coord, i) => {
      const pos = latLonToVector3(coord.lat, coord.lon, 75);

      // Node Marker
      const nodeGeo = new THREE.SphereGeometry(3.5, 12, 12);
      const nodeMat = new THREE.MeshBasicMaterial({
        color: i === 4 ? 0xFF4B4B : (i === 0 ? 0x00E676 : 0xFFB300)
      });
      const nodeMesh = new THREE.Mesh(nodeGeo, nodeMat);
      nodeMesh.position.copy(pos);
      nodeMesh.userData = coord;
      globeGroup.add(nodeMesh);
      nodeMeshes.push(nodeMesh);
    });

    // Threat Attack Arc Lines
    for (let i = 1; i < nodeMeshes.length; i++) {
      const p1 = nodeMeshes[i].position;
      const p2 = nodeMeshes[0].position; // Connecting into Bangalore SOC
      const mid = new THREE.Vector3().addVectors(p1, p2).multiplyScalar(0.5);
      mid.normalize().multiplyScalar(98); // Elevate curve above sphere

      const curve = new THREE.QuadraticBezierCurve3(p1, mid, p2);
      const curveGeo = new THREE.BufferGeometry().setFromPoints(curve.getPoints(30));
      const curveMat = new THREE.LineBasicMaterial({
        color: i === 4 ? 0xFF4B4B : 0x00F2FE,
        transparent: true,
        opacity: 0.65
      });
      const arc = new THREE.Line(curveGeo, curveMat);
      globeGroup.add(arc);
    }

    // Add Overlay Controls Bar
    const controlsBar = document.createElement('div');
    controlsBar.className = 'three-controls-bar';
    controlsBar.innerHTML = `
      <button class="three-ctrl-btn" id="${containerId}-toggle-btn" title="Pause or Resume Orbital Rotation">⏸ PAUSE</button>
      <button class="three-ctrl-btn" id="${containerId}-reset-btn" title="Reset Viewport Perspective">↺ RESET</button>
    `;
    container.appendChild(controlsBar);

    // Detail Callout Card
    const detailCard = document.createElement('div');
    detailCard.className = 'three-node-detail-card';
    detailCard.id = `${containerId}-detail`;
    detailCard.innerHTML = `
      <div>
        <strong style="color: #00F2FE;">🌐 3D Threat Telemetry:</strong> Click any node or drag globe to inspect offshore C2 infrastructure.
      </div>
      <span style="color: var(--text-muted); font-size: 10px;">Drag: Rotate | Click Node: Inspect</span>
    `;
    container.appendChild(detailCard);

    // Play/Pause State
    let isPaused = false;
    let isDragging = false;
    let prevMousePos = { x: 0, y: 0 };
    let dragDistance = 0;

    const toggleBtn = document.getElementById(`${containerId}-toggle-btn`);
    if (toggleBtn) {
      toggleBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        isPaused = !isPaused;
        toggleBtn.textContent = isPaused ? '▶ ROTATE' : '⏸ PAUSE';
      });
    }

    const resetBtn = document.getElementById(`${containerId}-reset-btn`);
    if (resetBtn) {
      resetBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        globeGroup.rotation.set(0, 0, 0);
      });
    }

    // Raycaster for Node Clicking
    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();

    container.addEventListener('mousedown', e => {
      e.stopPropagation();
      isDragging = true;
      dragDistance = 0;
      prevMousePos = { x: e.clientX, y: e.clientY };
    });

    window.addEventListener('mouseup', (e) => {
      if (!isDragging) return;
      isDragging = false;

      // If mouse moved less than 6px, treat as click for Raycasting
      if (dragDistance < 6) {
        const rect = container.getBoundingClientRect();
        mouse.x = ((e.clientX - rect.left) / container.clientWidth) * 2 - 1;
        mouse.y = -((e.clientY - rect.top) / container.clientHeight) * 2 + 1;

        raycaster.setFromCamera(mouse, camera);
        const intersects = raycaster.intersectObjects(nodeMeshes);

        if (intersects.length > 0) {
          const clickedNode = intersects[0].object;
          const data = clickedNode.userData;
          detailCard.innerHTML = `
            <div>
              <strong style="color: #00E676;">📍 ${data.label}</strong> [IP: <code>${data.ip}</code>]<br>
              <span style="color: #CBD5E1;">${data.role} — <em>${data.status}</em></span>
            </div>
            <button class="three-ctrl-btn" onclick="document.getElementById('${containerId}-detail').innerHTML='<div><strong style=\"color: #00F2FE;\">🌐 3D Threat Telemetry:</strong> Click any node to inspect.</div>'; event.stopPropagation();">✕</button>
          `;
          
          // Animate node pulse
          clickedNode.scale.set(1.8, 1.8, 1.8);
          setTimeout(() => clickedNode.scale.set(1, 1, 1), 400);
        }
      }
    });

    window.addEventListener('mousemove', e => {
      if (!isDragging) return;
      const deltaX = e.clientX - prevMousePos.x;
      const deltaY = e.clientY - prevMousePos.y;
      dragDistance += Math.abs(deltaX) + Math.abs(deltaY);

      globeGroup.rotation.y += deltaX * 0.008;
      globeGroup.rotation.x += deltaY * 0.008;
      prevMousePos = { x: e.clientX, y: e.clientY };
    });

    let reqId;
    function animate() {
      reqId = requestAnimationFrame(animate);
      if (!isPaused && !isDragging) {
        globeGroup.rotation.y += 0.004;
      }
      renderer.render(scene, camera);
    }
    animate();

    this.scenes[containerId] = { renderer, reqId, container };
  },

  // 2. 3D Interconnected Attack Surface Mesh
  renderDefenseMesh: function(containerId) {
    const container = document.getElementById(containerId);
    if (!container || typeof THREE === 'undefined') return;
    if (this.scenes[containerId]) return;

    const width = container.clientWidth || 400;
    const height = container.clientHeight || 300;

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(50, width / height, 0.1, 1000);
    camera.position.set(0, 0, 160);

    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    container.innerHTML = '';
    container.appendChild(renderer.domElement);

    container.addEventListener('click', (e) => e.stopPropagation());

    const meshGroup = new THREE.Group();
    scene.add(meshGroup);

    // Nodes representing Enterprise Systems
    const nodes = [
      { name: 'Edge Gateway', pos: [-55, 30, 0], color: 0x00F2FE, ip: '10.0.1.1', zone: 'Perimeter DMZ', mitigation: 'M1037: Filter Network Traffic' },
      { name: 'Core Firewall', pos: [-20, 10, 20], color: 0x4FACFE, ip: '10.0.2.1', zone: 'Internal Segment Boundary', mitigation: 'M1030: Network Segmentation' },
      { name: 'Active Directory DC', pos: [25, 35, -15], color: 0xFFB300, ip: '10.0.10.5', zone: 'Tier 0 Identity Root', mitigation: 'M1026: Privileged Account Management' },
      { name: 'SOC Analyst Host', pos: [50, -10, 10], color: 0x00E676, ip: '10.0.4.12', zone: 'Tier 2 Administrative Pod', mitigation: 'M1047: Audit & Sysmon Event 1' },
      { name: 'AeroGrid SCADA PLC', pos: [-10, -35, -10], color: 0xFF4B4B, ip: '192.168.100.22', zone: 'OT Substation Network', mitigation: 'M1035: Limit Hardware Installation (Air-Gap)' }
    ];

    const nodeMeshes = [];
    nodes.forEach(n => {
      const geo = new THREE.IcosahedronGeometry(7, 1);
      const mat = new THREE.MeshBasicMaterial({ color: n.color, wireframe: true });
      const mesh = new THREE.Mesh(geo, mat);
      mesh.position.set(n.pos[0], n.pos[1], n.pos[2]);
      mesh.userData = n;
      meshGroup.add(mesh);
      nodeMeshes.push(mesh);
    });

    // Connecting Telemetry Links
    const links = [
      [0, 1], [1, 2], [1, 3], [1, 4], [2, 3], [3, 4]
    ];
    links.forEach(pair => {
      const p1 = nodeMeshes[pair[0]].position;
      const p2 = nodeMeshes[pair[1]].position;
      const lineGeo = new THREE.BufferGeometry().setFromPoints([p1, p2]);
      const lineMat = new THREE.LineBasicMaterial({ color: 0x38BDF8, transparent: true, opacity: 0.4 });
      const line = new THREE.Line(lineGeo, lineMat);
      meshGroup.add(line);
    });

    // Controls bar & detail card
    const controlsBar = document.createElement('div');
    controlsBar.className = 'three-controls-bar';
    controlsBar.innerHTML = `
      <button class="three-ctrl-btn" id="${containerId}-toggle-btn">⏸ PAUSE</button>
      <button class="three-ctrl-btn" id="${containerId}-reset-btn">↺ RESET</button>
    `;
    container.appendChild(controlsBar);

    const detailCard = document.createElement('div');
    detailCard.className = 'three-node-detail-card';
    detailCard.id = `${containerId}-detail`;
    detailCard.innerHTML = `
      <div>
        <strong style="color: #4FACFE;">🛡️ Enterprise Topology:</strong> Click systems to inspect trust boundaries and MITRE mitigations.
      </div>
      <span style="color: var(--text-muted); font-size: 10px;">Click Node: Inspect</span>
    `;
    container.appendChild(detailCard);

    let isPaused = false;
    let isDragging = false;
    let prevMousePos = { x: 0, y: 0 };
    let dragDist = 0;

    const toggleBtn = document.getElementById(`${containerId}-toggle-btn`);
    if (toggleBtn) {
      toggleBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        isPaused = !isPaused;
        toggleBtn.textContent = isPaused ? '▶ ROTATE' : '⏸ PAUSE';
      });
    }

    const resetBtn = document.getElementById(`${containerId}-reset-btn`);
    if (resetBtn) {
      resetBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        meshGroup.rotation.set(0, 0, 0);
      });
    }

    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();

    container.addEventListener('mousedown', e => {
      e.stopPropagation();
      isDragging = true;
      dragDist = 0;
      prevMousePos = { x: e.clientX, y: e.clientY };
    });

    window.addEventListener('mouseup', e => {
      if (!isDragging) return;
      isDragging = false;

      if (dragDist < 6) {
        const rect = container.getBoundingClientRect();
        mouse.x = ((e.clientX - rect.left) / container.clientWidth) * 2 - 1;
        mouse.y = -((e.clientY - rect.top) / container.clientHeight) * 2 + 1;

        raycaster.setFromCamera(mouse, camera);
        const intersects = raycaster.intersectObjects(nodeMeshes);

        if (intersects.length > 0) {
          const data = intersects[0].object.userData;
          detailCard.innerHTML = `
            <div>
              <strong style="color: #FFB300;">💻 ${data.name}</strong> [<code>${data.ip}</code> | Zone: ${data.zone}]<br>
              <span style="color: #69F0AE;">Mitigation: ${data.mitigation}</span>
            </div>
            <button class="three-ctrl-btn" onclick="document.getElementById('${containerId}-detail').innerHTML='<div><strong style=\"color: #4FACFE;\">🛡️ Enterprise Topology:</strong> Click systems to inspect.</div>'; event.stopPropagation();">✕</button>
          `;
          intersects[0].object.scale.set(1.5, 1.5, 1.5);
          setTimeout(() => intersects[0].object.scale.set(1, 1, 1), 350);
        }
      }
    });

    window.addEventListener('mousemove', e => {
      if (!isDragging) return;
      const deltaX = e.clientX - prevMousePos.x;
      const deltaY = e.clientY - prevMousePos.y;
      dragDist += Math.abs(deltaX) + Math.abs(deltaY);

      meshGroup.rotation.y += deltaX * 0.008;
      meshGroup.rotation.x += deltaY * 0.008;
      prevMousePos = { x: e.clientX, y: e.clientY };
    });

    let reqId;
    function animate() {
      reqId = requestAnimationFrame(animate);
      if (!isPaused && !isDragging) {
        meshGroup.rotation.y += 0.006;
        meshGroup.rotation.x += 0.002;
      }
      renderer.render(scene, camera);
    }
    animate();

    this.scenes[containerId] = { renderer, reqId, container };
  },

  // 3. 3D Rotating Cryptographic Defense Shield
  renderSecurityShield: function(containerId) {
    const container = document.getElementById(containerId);
    if (!container || typeof THREE === 'undefined') return;
    if (this.scenes[containerId]) return;

    const width = container.clientWidth || 360;
    const height = container.clientHeight || 280;

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
    camera.position.z = 120;

    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    container.innerHTML = '';
    container.appendChild(renderer.domElement);

    container.addEventListener('click', (e) => e.stopPropagation());

    const shieldGroup = new THREE.Group();
    scene.add(shieldGroup);

    // Faceted 3D Shield Mesh
    const shieldShape = new THREE.Shape();
    shieldShape.moveTo(0, 35);
    shieldShape.lineTo(30, 25);
    shieldShape.lineTo(24, -15);
    shieldShape.lineTo(0, -38);
    shieldShape.lineTo(-24, -15);
    shieldShape.lineTo(-30, 25);
    shieldShape.closePath();

    const extrudeSettings = { depth: 6, bevelEnabled: true, bevelSegments: 3, steps: 1, bevelSize: 2, bevelThickness: 2 };
    const shieldGeo = new THREE.ExtrudeGeometry(shieldShape, extrudeSettings);
    const shieldMat = new THREE.MeshBasicMaterial({
      color: 0x00F2FE,
      wireframe: true,
      transparent: true,
      opacity: 0.75
    });
    const shieldMesh = new THREE.Mesh(shieldGeo, shieldMat);
    shieldGroup.add(shieldMesh);

    // Central Core Orb
    const orbGeo = new THREE.SphereGeometry(8, 16, 16);
    const orbMat = new THREE.MeshBasicMaterial({ color: 0xFFB300 });
    const orb = new THREE.Mesh(orbGeo, orbMat);
    shieldGroup.add(orb);

    // Controls bar & detail card
    const controlsBar = document.createElement('div');
    controlsBar.className = 'three-controls-bar';
    controlsBar.innerHTML = `
      <button class="three-ctrl-btn" id="${containerId}-toggle-btn">⏸ PAUSE</button>
      <button class="three-ctrl-btn" id="${containerId}-pulse-btn">⚡ PULSE SHIELD</button>
    `;
    container.appendChild(controlsBar);

    const detailCard = document.createElement('div');
    detailCard.className = 'three-node-detail-card';
    detailCard.innerHTML = `
      <div>
        <strong style="color: #00E676;">🛡️ Cryptographic Perimeter:</strong> AES-256-GCM Active | Zero-Trust Enforced
      </div>
      <span style="color: var(--text-muted); font-size: 10px;">Click Shield to Pulse</span>
    `;
    container.appendChild(detailCard);

    let isPaused = false;
    const toggleBtn = document.getElementById(`${containerId}-toggle-btn`);
    if (toggleBtn) {
      toggleBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        isPaused = !isPaused;
        toggleBtn.textContent = isPaused ? '▶ ROTATE' : '⏸ PAUSE';
      });
    }

    function triggerPulse() {
      shieldMat.color.setHex(0x00E676);
      orb.scale.set(2.2, 2.2, 2.2);
      detailCard.innerHTML = `
        <div>
          <strong style="color: #00E676;">⚡ SHIELD PULSE ACTIVATED:</strong> Incident containment verified across Tier 0 Active Directory!
        </div>
      `;
      setTimeout(() => {
        shieldMat.color.setHex(0x00F2FE);
        orb.scale.set(1, 1, 1);
      }, 600);
    }

    const pulseBtn = document.getElementById(`${containerId}-pulse-btn`);
    if (pulseBtn) {
      pulseBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        triggerPulse();
      });
    }

    container.addEventListener('click', (e) => {
      e.stopPropagation();
      triggerPulse();
    });

    let reqId;
    function animate() {
      reqId = requestAnimationFrame(animate);
      if (!isPaused) {
        shieldGroup.rotation.y += 0.015;
      }
      orb.scale.setScalar(1 + Math.sin(Date.now() * 0.004) * 0.15);
      renderer.render(scene, camera);
    }
    animate();

    this.scenes[containerId] = { renderer, reqId, container };
  },

  // Cleanup helper
  destroyScene: function(containerId) {
    if (this.scenes[containerId]) {
      cancelAnimationFrame(this.scenes[containerId].reqId);
      this.scenes[containerId].renderer.dispose();
      this.scenes[containerId].container.innerHTML = '';
      delete this.scenes[containerId];
    }
  }
};
