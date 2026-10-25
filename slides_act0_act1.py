# Slides Data: Act 0 (Orientation) & Act 1 (Day 1 - CTI Fundamentals & Diamond Model)
# Slides 1 to 16

ACT0_ACT1_SLIDES = [
    # SLIDE 01: Title Slide
    {
        "title": "Title Keynote",
        "day": "WELCOME",
        "module": "COURSE LAUNCH",
        "session": "LH3 – 4TH FLOOR",
        "ref": "Course Overview & Persona",
        "content": '''
          <div style="text-align: center; padding: 40px 20px;">
            <div class="cyber-badge badge-cyan animate-fade-up" style="margin-bottom: 20px;">OPERATIONAL CYBERSECURITY IMMERSION</div>
            <h1 class="animate-fade-up delay-1" style="font-size: 2.8em; margin-bottom: 12px;">Threat Intelligence &<br><span style="color: var(--cyber-cyan);">Incident Response</span></h1>
            <p class="animate-fade-up delay-2" style="font-size: 1.15em; color: var(--text-secondary); max-width: 800px; margin: 0 auto 30px auto;">
              Transforming Alert Janitors into Adversary-Centric Defenders Across Multi-Source Enterprise Telemetry
            </p>
            
            <div class="grid-3 animate-fade-up delay-3" style="max-width: 900px; margin: 0 auto; text-align: left;">
              <div class="cyber-card">
                <div style="color: var(--cyber-cyan); font-family: var(--font-mono); font-size: 11px;">TRAINING VENUE</div>
                <div style="font-size: 16px; font-weight: 700; color: #FFF; margin-top: 4px;">LH3 – 4th Floor</div>
                <div style="color: var(--text-muted); font-size: 12px;">SOC Pod Setup (24 Workstations)</div>
              </div>
              <div class="cyber-card">
                <div style="color: var(--electric-blue); font-family: var(--font-mono); font-size: 11px;">SCHEDULE & VOLUME</div>
                <div style="font-size: 16px; font-weight: 700; color: #FFF; margin-top: 4px;">26–31 October 2026</div>
                <div style="color: var(--text-muted); font-size: 12px;">26.5h Gross / 23.4h Net (6 Days)</div>
              </div>
              <div class="cyber-card">
                <div style="color: var(--neon-amber); font-family: var(--font-mono); font-size: 11px;">LEAD INSTRUCTOR</div>
                <div style="font-size: 16px; font-weight: 700; color: #FFF; margin-top: 4px;">Gopinath A</div>
                <div style="color: var(--text-muted); font-size: 12px;">Chief AI Knowledge Architect</div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Good afternoon, colleagues, and welcome to Venue LH3 on the 4th Floor. My name is Gopinath, and over the next six days, we will be working together on an intensive, operational immersion into Threat Intelligence and Incident Response. Whether you are working as a SOC analyst, a threat researcher, a security engineer, or academic faculty, this program is engineered to build battle-tested capabilities.",
        "notes_pedagogy": "Establish instructor credibility immediately. Acknowledge the room's energy and set an authoritative, encouraging tone."
    },

    # SLIDE 02: Alert Janitor vs Threat Hunter
    {
        "title": "Alert Janitors vs. Threat Hunters",
        "day": "ORIENTATION",
        "module": "COURSE PHILOSOPHY",
        "session": "OPERATIONAL DILEMMA",
        "ref": "Trainer Handbook Section 1.2",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-crimson">OPERATIONAL REALITY CHECK</div>
            <h2>The Enterprise Dilemma: Alert Janitor vs. Threat Hunter</h2>
            <p>Every single day, an enterprise SOC ingests millions of events. How your team responds defines your security posture.</p>
            
            <div class="grid-2" style="margin-top: 24px;">
              <div class="cyber-card alert-card">
                <div style="color: var(--alert-crimson); font-family: var(--font-mono); font-weight: 700; font-size: 13px;">❌ THE ALERT JANITOR (REACTIVE TRAP)</div>
                <ul style="font-size: 14px; color: var(--text-secondary); margin-top: 12px; line-height: 1.7;">
                  <li>Treats every IP address as an isolated emergency.</li>
                  <li>Blindly copies indicators into perimeter blocklists.</li>
                  <li>Measures success by tickets closed per hour.</li>
                  <li>Leaves the SOC completely blind when the adversary switches IPs.</li>
                  <li><em>Adversary cost to bypass: 15 seconds and four cents.</em></li>
                </ul>
              </div>
              
              <div class="cyber-card intel-card">
                <div style="color: var(--cyber-cyan); font-family: var(--font-mono); font-weight: 700; font-size: 13px;">✅ THE ADVERSARY-CENTRIC DEFENDER</div>
                <ul style="font-size: 14px; color: var(--text-secondary); margin-top: 12px; line-height: 1.7;">
                  <li>Uncovers the human operator behind the terminal.</li>
                  <li>Maps adversary intent, infrastructure, and capabilities.</li>
                  <li>Breaks adversary TTPs using MITRE ATT&CK and D3FEND.</li>
                  <li>Preserves forensic evidence without destroying volatile memory.</li>
                  <li><em>Adversary cost to bypass: complete campaign rebuilding.</em></li>
                </ul>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "An alert sounds, an IP address flashes crimson on a monitor, a dashboard announces that 50,000 bad indicators were ingested today. And what does the average tier-1 analyst do? They copy the IP into a perimeter blocklist, close the ticket, and move to the next alert. Colleagues, that is not cybersecurity. That is alert janitorial work. Real defense begins when you understand the human adversary.",
        "notes_pedagogy": "Contrast reactive alert janitorial work with strategic threat hunting. Disarm the misconception that closing alerts equals true security."
    },

    # SLIDE 03: Master Course Roadmap
    {
        "title": "Master Course Delivery Roadmap",
        "day": "ORIENTATION",
        "module": "COURSE ROADMAP",
        "session": "TIMETABLE",
        "ref": "Trainer Handbook Section 1.3",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-blue">SIX-DAY IMMERSION ROADMAP</div>
            <h2>Master Course Delivery Roadmap & Hands-on Labs</h2>
            <p>26.50 Gross Hours | 23.42 Net Instructional Hours (1,405 Net Minutes) across 8 Core Modules.</p>
            
            <div class="grid-3" style="font-size: 12px; margin-top: 18px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan);">DAY 1 (26 OCT) • 1:00–5:00 PM</strong>
                <div style="color: #FFF; font-weight: 600; margin-top: 4px;">CTI Fundamentals & Diamond Model</div>
                <div style="color: var(--text-muted); margin-top: 4px;">LAB-01: Admiralty Scoring & AlienVault OTX</div>
              </div>
              <div class="cyber-card">
                <strong style="color: var(--electric-blue);">DAY 2 (27 OCT) • 1:00–5:00 PM</strong>
                <div style="color: #FFF; font-weight: 600; margin-top: 4px;">Threat Modeling & ATT&CK Matrix</div>
                <div style="color: var(--text-muted); margin-top: 4px;">LAB-03: ATT&CK Navigator Layer Algebra</div>
              </div>
              <div class="cyber-card">
                <strong style="color: var(--matrix-teal);">DAY 3 (28 OCT) • 1:00–5:00 PM</strong>
                <div style="color: #FFF; font-weight: 600; margin-top: 4px;">Defensive OSINT & STIX/TAXII</div>
                <div style="color: var(--text-muted); margin-top: 4px;">LAB-02: STIX 2.1 Bundle Construction</div>
              </div>
              <div class="cyber-card">
                <strong style="color: var(--neon-amber);">DAY 4 (29 OCT) • 1:00–5:00 PM</strong>
                <div style="color: #FFF; font-weight: 600; margin-top: 4px;">Multi-Source Telemetry & Sigma</div>
                <div style="color: var(--text-muted); margin-top: 4px;">LAB-04: Sysmon, Zeek & pySigma Rules</div>
              </div>
              <div class="cyber-card">
                <strong style="color: var(--alert-crimson);">DAY 5 (30 OCT) • 2:00–5:00 PM</strong>
                <div style="color: #FFF; font-weight: 600; margin-top: 4px;">Incident Triage & Forensics</div>
                <div style="color: var(--text-muted); margin-top: 4px;">LAB-06: KAPE Triage & Timestomp Forensics</div>
              </div>
              <div class="cyber-card" style="border: 1px solid var(--cyber-cyan);">
                <strong style="color: var(--purple-intel);">DAY 6 (31 OCT) • 9:30 AM–5:00 PM</strong>
                <div style="color: #FFF; font-weight: 600; margin-top: 4px;">Saturday Capstone Intensive</div>
                <div style="color: var(--text-muted); margin-top: 4px;">LAB-05/07/08: Phishing, SOAR & AeroGrid APT</div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Here is our flight plan for the week. Notice the progression: we start with intelligence fundamentals on Day 1, move to behavioral frameworks on Day 2, standards on Day 3, engine-room telemetry on Day 4, forensic triage on Day 5, and culminate in our 7.5-hour Saturday Capstone intensive.",
        "notes_pedagogy": "Set clear trajectory expectations. Highlight that Saturday is a marathon capstone bringing every skill together."
    },

    # SLIDE 04: Classroom Culture & Indian College Context
    {
        "title": "Classroom Operating Rules & Culture",
        "day": "ORIENTATION",
        "module": "CLASSROOM NORMS",
        "session": "LH3 PROTOCOLS",
        "ref": "Trainer Delivery Script - Section C",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-amber">CAMPUS LAB REALITY</div>
            <h2>Classroom Ground Rules: Collaboration Over Competition</h2>
            <p>Welcome to LH3 – 4th Floor. We are operating as a unified Security Operations Center.</p>
            
            <div class="grid-3" style="margin-top: 20px;">
              <div class="cyber-card">
                <div style="font-size: 24px; margin-bottom: 8px;">🔋</div>
                <strong style="color: #FFF;">The Power Rule</strong>
                <p style="font-size: 13px; margin-top: 6px;">Your laptop battery will show 98% in the hostel and drop to 3% the moment the trainer speaks! Verified power sockets are live at all 6 pods. Keep plugged in.</p>
              </div>
              <div class="cyber-card">
                <div style="font-size: 24px; margin-bottom: 8px;">🤝</div>
                <strong style="color: #FFF;">Pod Collaboration</strong>
                <p style="font-size: 13px; margin-top: 6px;">No group-project syndromes here! Unlike college projects where one person writes code and four people contribute roll numbers, every analyst executes their own labs.</p>
              </div>
              <div class="cyber-card">
                <div style="font-size: 24px; margin-bottom: 8px;">☕</div>
                <strong style="color: #FFF;">The Chai/Coffee Protocol</strong>
                <p style="font-size: 13px; margin-top: 6px;">Filter coffee or canteen tea? Both are acceptable threat-hunting fuel. Scheduled 20-minute refreshment breaks are strictly respected to keep minds sharp.</p>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "I see everyone has found their pods, laptops are booted, and chargers are plugged in. We all know the universal law of campus labs: your laptop battery will show 98% in the hostel, and the moment the external examiner or trainer walks in, it drops to 3% with a critical warning! Rest assured, LH3 has verified power sockets at every desk. We are here to build real-world capability.",
        "notes_pedagogy": "HUMOR ANCHOR: Disarm classroom stiffness with light, culturally relatable campus observations (hostel batteries, group projects, canteen coffee). Encourages collaborative bonding."
    },

    # SLIDE 05: The 40/60 Rule & Pod Model
    {
        "title": "The 40/60 Pedagogical Rule",
        "day": "ORIENTATION",
        "module": "METHODOLOGY",
        "session": "HANDS-ON STANDARD",
        "ref": "Trainer Handbook Section 1.4",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">SOC POD PEDAGOGY</div>
            <h2>The 40/60 Execution Standard</h2>
            <p>You will not sit and passively listen to lectures. In LH3, theory immediately transforms into hands-on keyboard action.</p>
            
            <div class="grid-2" style="margin-top: 24px;">
              <div class="cyber-card" style="text-align: center; padding: 30px;">
                <div style="font-family: var(--font-heading); font-size: 54px; font-weight: 700; color: var(--electric-blue);">40%</div>
                <strong style="color: #FFF; font-size: 16px;">Architectural Framing & Live Demonstrations</strong>
                <p style="font-size: 13px; margin-top: 8px;">First-principles theory, adversary tradecraft mechanics, whiteboard modeling, and step-by-step instructor demonstrations on the dual projection screens.</p>
              </div>
              <div class="cyber-card" style="text-align: center; padding: 30px; border-color: var(--cyber-cyan);">
                <div style="font-family: var(--font-heading); font-size: 54px; font-weight: 700; color: var(--cyber-cyan);">60%</div>
                <strong style="color: #FFF; font-size: 16px;">Hands-On Pod Investigation & Guided Labs</strong>
                <p style="font-size: 13px; margin-top: 8px;">20-step structured execution on student workstations, real tool navigation, log queries, Sigma rule testing, forensic artifact triage, and peer review.</p>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "In LH3, we adhere strictly to the 40/60 rule: 40% architectural framing and live demonstrations, and 60% hands-on investigation on your lab machines. You will not sit and passively listen to lectures. You will be at the keyboard querying repositories, scoring source credibility, and dissecting authentic adversary infrastructure.",
        "notes_pedagogy": "Commit to the 40/60 rule early so students understand they are active investigators, not passive listeners."
    },

    # SLIDE 06: Opening Challenge Scenario
    {
        "title": "Opening Engagement Scenario",
        "day": "ORIENTATION",
        "module": "ICEBREAKER SCENARIO",
        "session": "POD CHALLENGE",
        "ref": "Verbatim Script Opening Scenario",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-crimson">CLASSROOM OPENING CHALLENGE</div>
            <h2>Scenario: The 2:00 AM Eastern European Port Scan</h2>
            <p>Consider this real-world operational event reported by your perimeter firewall:</p>
            
            <div class="terminal-buffer" style="margin: 18px 0;">
              <div class="terminal-header">
                <div class="terminal-dots"><span class="dot dot-red"></span><span class="dot dot-yellow"></span><span class="dot dot-green"></span></div>
                <span>EDGE-FW-01.SOC.CORP // ALERT ID: 884192</span>
              </div>
              <div class="terminal-body">
<span class="terminal-cmd">SRC_IP:</span> 185.220.101.42 (AS44050 - Eastern Europe)
<span class="terminal-cmd">DST_IP:</span> 198.51.100.10 (Portal DMZ) // DST_PORT: 443 (TLS)
<span class="terminal-cmd">EVENT:</span> 3 TCP SYN packets detected within 450ms at 02:14:02 IST
<span class="terminal-cmd">ACTION:</span> ALLOWED (Standard Web Traffic Rule)
              </div>
            </div>
            
            <div class="interactive-decision-box">
              <strong style="color: #FFF; font-size: 15px;">SOC Question for Pod 1 & Pod 2:</strong>
              <div class="decision-options">
                <button class="decision-btn" onclick="selectDecision(this, false, 'Premature blocking fills firewall state tables and provides zero insight into whether this was an automated benign research crawler or a targeted adversary.')">
                  <span>A) Immediately block 185.220.101.42 at the border router and page the Incident Commander.</span>
                  <span>➔</span>
                </button>
                <button class="decision-btn" onclick="selectDecision(this, true, 'Correct! Port scans occur constantly across IPv4 space from benign bots (Shodan, Censys) and automated scanners. It is raw data/information, not yet actionable threat intelligence.')">
                  <span>B) It is raw data/information. Enrich with passive DNS and threat feeds before drawing conclusions.</span>
                  <span>➔</span>
                </button>
              </div>
              <div class="decision-explanation" style="margin-top: 12px; font-size: 13px; font-family: var(--font-mono);"></div>
            </div>
          </div>
        ''',
        "notes_say": "Let me begin with a challenge for Pod 1 and Pod 2: If our firewall reports that an external IP address in Eastern Europe scanned port 443 on our corporate portal three times at 2:00 AM, is that a cyber threat, a security incident, or raw data? And should we immediately block it? Review the options and let's see your decision.",
        "notes_pedagogy": "Socratic Icebreaker: Engage students actively with a clickable choice. Shows why contextual enrichment is the difference between knee-jerk panic and professional threat intelligence."
    },

    # SLIDE 07: Day 1 Launch & Objectives
    {
        "title": "Day 1 Launch & Objectives",
        "day": "DAY 01",
        "day_start": 1,
        "module": "MOD-01: CTI FUNDAMENTALS",
        "session": "SES-01 (1:00–5:00 PM)",
        "ref": "Handbook Module 1",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">MODULE 01 LAUNCH</div>
            <h2>Cyber Threat Intelligence Fundamentals & Diamond Modeling</h2>
            <p>Session ID: SES-01 | Scheduled Net Teaching: 220 Minutes | Refreshment Break: 3:00 PM (20 min)</p>
            
            <div class="grid-2" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 15px;">Target Learning Outcomes (PLO-1)</strong>
                <ul style="font-size: 13px; color: var(--text-secondary); margin-top: 10px; line-height: 1.7;">
                  <li><strong>DIKW Hierarchy:</strong> Transform raw telemetry numbers into executive intelligence.</li>
                  <li><strong>Four CTI Tiers:</strong> Map Strategic, Operational, Tactical, and Technical consumers.</li>
                  <li><strong>Threat Actor Profiling:</strong> Contrast nation-state APTs, RaaS, Hacktivists, and Insiders.</li>
                  <li><strong>Intelligence Cycle:</strong> Execute the 6-phase cycle from Planning to Feedback.</li>
                  <li><strong>NATO Admiralty Code:</strong> Objectively score source reliability and credibility.</li>
                  <li><strong>Diamond Model:</strong> Deconstruct intrusions across 4 mathematical vertices.</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--electric-blue); font-size: 15px;">Hands-On Milestone: LAB-01</strong>
                <p style="font-size: 13px; margin-top: 10px;">
                  Every analyst will evaluate unverified threat bulletins using the NATO Admiralty Rubric, query Certificate Transparency via <code>crt.sh</code>, ingest indicators via AlienVault OTX, and construct a verified 4-vertex Diamond Model artifact for threat actor <strong>UNC-PHOENIX</strong>.
                </p>
                <div style="margin-top: 16px; padding: 10px; background: rgba(0, 242, 254, 0.08); border-radius: 6px; border: 1px dashed var(--cyber-cyan); font-family: var(--font-mono); font-size: 12px; color: var(--cyber-cyan);">
                  TARGET FILE: evaluation_worksheet.docx // LAB-01 COMPLETE
                </div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Our objective this afternoon in Module 1 is to build our foundational analytical toolkit. By 5:00 PM today, you will transform raw data into actionable intelligence, classify consumers across the four tiers, score unverified threat bulletins with the Admiralty Code, and deconstruct attacks using the Diamond Model.",
        "notes_pedagogy": "State clear, measurable session objectives. Highlight the concrete deliverable for Lab 1."
    },

    # SLIDE 08: The DIKW Hierarchy in Cybersecurity
    {
        "title": "The DIKW Hierarchy in Cybersecurity",
        "day": "DAY 01",
        "module": "MOD-01: CTI FUNDAMENTALS",
        "session": "CON-01",
        "ref": "Handbook Concept 1",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">ANALYTICAL FOUNDATION</div>
            <h2>The DIKW Hierarchy: Raw Data to Actionable CTI</h2>
            <p>Intelligence is not just more data—it is data refined through context, analysis, and decision enablement.</p>
            
            <div class="grid-4" style="margin-top: 24px;">
              <div class="cyber-card">
                <span class="cyber-badge badge-blue">LEVEL 1: DATA</span>
                <div style="font-size: 20px; font-weight: 700; color: #FFF; margin: 12px 0 6px 0;">198.51.100.45</div>
                <p style="font-size: 12px;">Raw, discrete 32-bit integer. No context, no timestamp, no meaning. Cannot justify security action.</p>
              </div>
              <div class="cyber-card">
                <span class="cyber-badge badge-cyan">LEVEL 2: INFORMATION</span>
                <div style="font-size: 14px; font-weight: 700; color: #FFF; margin: 12px 0 6px 0;">Outbound TLS at 02:14 AM</div>
                <p style="font-size: 12px;">Data processed with context: Who, What, When. 45 MB payload from internal Host 10.0.4.12.</p>
              </div>
              <div class="cyber-card">
                <span class="cyber-badge badge-amber">LEVEL 3: KNOWLEDGE</span>
                <div style="font-size: 14px; font-weight: 700; color: #FFF; margin: 12px 0 6px 0;">Correlated Baseline</div>
                <p style="font-size: 12px;">Host 10.0.4.12 is an unpatched staging server; 198.51.100.45 was registered 4 hours ago via crt.sh.</p>
              </div>
              <div class="cyber-card" style="border-color: var(--cyber-cyan);">
                <span class="cyber-badge badge-crimson">LEVEL 4: INTELLIGENCE</span>
                <div style="font-size: 14px; font-weight: 700; color: #FFF; margin: 12px 0 6px 0;">UNC-PHOENIX C2 Node</div>
                <p style="font-size: 12px;">Actionable: isolate host, null-route IP, revoke Kerberos cache. Directly enables decision advantage.</p>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "What is this string of numbers: 198.51.100.45? You cannot tell me if it is malicious. Right now, it is raw data—like your raw internal assessment marks before moderation! When we add timestamp and port, it becomes Information. When we correlate with baseline host roles, it becomes Knowledge. When we tie it to UNC-PHOENIX and know we must isolate Host 10.0.4.12, that is actionable Cyber Threat Intelligence.",
        "notes_pedagogy": "HUMOR ANCHOR: Raw numbers are like raw marks before moderation—meaningless without the class average! Highlight the decision enablement standard of intelligence."
    },

    # SLIDE 09: The 4 Tiers of CTI
    {
        "title": "The Four Tiers of CTI",
        "day": "DAY 01",
        "module": "MOD-01: CTI FUNDAMENTALS",
        "session": "CON-02",
        "ref": "Handbook Concept 2",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-blue">TARGET AUDIENCE ALIGNMENT</div>
            <h2>The Four Tiers of Cyber Threat Intelligence</h2>
            <p>Intelligence is not one-size-fits-all. Tailor the message to the exact decision-maker consuming it.</p>
            
            <div class="grid-2" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--purple-intel);">STRATEGIC INTELLIGENCE</strong>
                <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 6px;">Audience: Board, CEO, CISO | Lifespan: Months to Years</div>
                <p style="font-size: 13px;">Executive briefings, geopolitical risk trends, loss models. Answers: <em>"Are competitors in our sector being hit by BlackCat? Do we need $2M for cloud defense?"</em></p>
                <div style="font-family: var(--font-mono); font-size: 11px; color: var(--text-highlight);">Metric: Financial risk exposure & regulatory compliance</div>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--neon-amber);">OPERATIONAL INTELLIGENCE</strong>
                <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 6px;">Audience: SOC Managers, Incident Commanders | Lifespan: Weeks to Months</div>
                <p style="font-size: 13px;">Adversary profiling, campaign staging, infrastructure shifts. Answers: <em>"Which threat groups are actively scanning our supply chain this quarter?"</em></p>
                <div style="font-family: var(--font-mono); font-size: 11px; color: var(--text-highlight);">Metric: Campaign tracking & defensive resource allocation</div>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--electric-blue);">TACTICAL INTELLIGENCE</strong>
                <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 6px;">Audience: SOC Tier-2/3, Threat Hunters | Lifespan: Days to Weeks</div>
                <p style="font-size: 13px;">Adversary TTPs, MITRE ATT&CK techniques, Sigma rules. Answers: <em>"How does UNC-PHOENIX achieve lateral movement? Pass-the-Hash and WMI execution."</em></p>
                <div style="font-family: var(--font-mono); font-size: 11px; color: var(--text-highlight);">Metric: Detection rule coverage & hunting hypothesis success</div>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan);">TECHNICAL INTELLIGENCE</strong>
                <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 6px;">Audience: SIEM parsers, Firewalls, SOAR | Lifespan: Hours to Days</div>
                <p style="font-size: 13px;">Raw IoCs: SHA-256 hashes, IP addresses, domains, STIX JSON. Answers: <em>"Is this specific file hash present on any workstation in subnet 10.0.4.0/24?"</em></p>
                <div style="font-family: var(--font-mono); font-size: 11px; color: var(--text-highlight);">Metric: Automated ingestion rate, blocklist precision & false-positive ratio</div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Imagine you walk into the boardroom of your Chief Information Security Officer and hand them a printout of 10,000 MD5 hashes. What will happen? The CISO will politely show you the door! The CISO manages business risk and capital budgets, not hash tables. Notice the inverse relationship: as you go UP, technical detail drops, but lifespan and business value soar.",
        "notes_pedagogy": "Emphasize audience alignment. Never hand an executive a list of hashes, and never hand a tier-1 analyst a 40-page policy whitepaper."
    },

    # SLIDE 10: Threat Actor Categorization
    {
        "title": "Threat Actor Categorization",
        "day": "DAY 01",
        "module": "MOD-01: CTI FUNDAMENTALS",
        "session": "CON-03",
        "ref": "Handbook Concept 3",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-amber">ADVERSARY PROFILING</div>
            <h2>Threat Actor Categorization: Intent, Capability & Opportunity</h2>
            <p>Treating every threat with identical defensive playbooks leads to SOC operational collapse.</p>
            
            <table class="lab-steps-compact" style="margin-top: 20px; font-size: 13px;">
              <thead>
                <tr>
                  <th>Actor Category</th>
                  <th>Primary Motivation</th>
                  <th>Sponsorship & Resources</th>
                  <th>Tradecraft & Operational Tempo</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong style="color: var(--alert-crimson);">Nation-State (APTs)</strong></td>
                  <td>Geopolitical espionage, IP theft, critical infra disruption</td>
                  <td>National intelligence/military agencies; unlimited funding</td>
                  <td>Custom zero-days, multi-year stealth persistence, Living-off-the-Land (LOLBins)</td>
                </tr>
                <tr>
                  <td><strong style="color: var(--neon-amber);">Organized Cybercrime (RaaS)</strong></td>
                  <td>Direct financial extortion, cryptocurrency ransom</td>
                  <td>Commercial affiliate syndicates (LockBit, BlackCat)</td>
                  <td>Rapid multi-extortion, double-dipping leaks, automated affiliate staging</td>
                </tr>
                <tr>
                  <td><strong style="color: var(--electric-blue);">Hacktivists</strong></td>
                  <td>Ideological, political, religious, environmental publicity</td>
                  <td>Loose collectives, volunteer forums</td>
                  <td>DDoS, website defacements, sensationalized Telegram/Pastebin data dumps</td>
                </tr>
                <tr>
                  <td><strong style="color: var(--purple-intel);">Insiders (Malicious / Negligent)</strong></td>
                  <td>Greed, workplace grievance, sabotage, accidental leak</td>
                  <td>Authorized internal employees, contractors</td>
                  <td>Legitimate credentials, perimeter bypass, data exfiltration via legitimate cloud tools</td>
                </tr>
              </tbody>
            </table>
          </div>
        ''',
        "notes_say": "Not all adversaries are created equal. If you treat a teenage script kiddie with the same defensive response model as a foreign military cyber unit, your SOC will collapse under operational exhaustion. Notice APTs use Living-off-the-Land tools like Certutil and PowerShell so their commands blend right in with your system administrators.",
        "notes_pedagogy": "Explain the three pillars: Intent, Capability, and Opportunity. Emphasize why APTs love Living-off-the-Land Binaries."
    },

    # SLIDE 11: The Traditional Intelligence Cycle
    {
        "title": "The Traditional Intelligence Cycle",
        "day": "DAY 01",
        "module": "MOD-01: CTI FUNDAMENTALS",
        "session": "CON-04",
        "ref": "Handbook Concept 4",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">OPERATIONAL WORKFLOW</div>
            <h2>The 6-Phase Traditional Intelligence Cycle</h2>
            <p>Intelligence is not an event—it is a continuous, closed-loop feedback lifecycle.</p>
            
            <div class="grid-3" style="margin-top: 20px;">
              <div class="cyber-card">
                <span style="color: var(--cyber-cyan); font-family: var(--font-mono); font-size: 12px; font-weight: 700;">PHASE 1: PLANNING & DIRECTION</span>
                <p style="font-size: 13px; margin-top: 6px;">Establish formalized Priority Intelligence Requirements (PIRs). Without PIRs, teams collect indiscriminate junk and drown in noise.</p>
              </div>
              <div class="cyber-card">
                <span style="color: var(--cyber-cyan); font-family: var(--font-mono); font-size: 12px; font-weight: 700;">PHASE 2: COLLECTION</span>
                <p style="font-size: 13px; margin-top: 6px;">Gather raw artifacts from OSINT, commercial feeds, honeypots, dark web forums, and internal firewall/EDR telemetry.</p>
              </div>
              <div class="cyber-card">
                <span style="color: var(--cyber-cyan); font-family: var(--font-mono); font-size: 12px; font-weight: 700;">PHASE 3: PROCESSING</span>
                <p style="font-size: 13px; margin-top: 6px;">Normalize disparate data formats: parse JSON, de-duplicate IPs, extract IOCs from PDF reports, translate foreign language posts.</p>
              </div>
              <div class="cyber-card">
                <span style="color: var(--electric-blue); font-family: var(--font-mono); font-size: 12px; font-weight: 700;">PHASE 4: ANALYSIS & PRODUCTION</span>
                <p style="font-size: 13px; margin-top: 6px;">Synthesize evidence into actionable intelligence using structured techniques: Admiralty scoring, Diamond modeling, hypothesis testing.</p>
              </div>
              <div class="cyber-card">
                <span style="color: var(--electric-blue); font-family: var(--font-mono); font-size: 12px; font-weight: 700;">PHASE 5: DISSEMINATION</span>
                <p style="font-size: 13px; margin-top: 6px;">Distribute timely, tailored deliverables: STIX 2.1 feeds to firewalls, Sigma rules to SIEM, executive threat briefs to CISO.</p>
              </div>
              <div class="cyber-card" style="border-color: var(--neon-amber);">
                <span style="color: var(--neon-amber); font-family: var(--font-mono); font-size: 12px; font-weight: 700;">PHASE 6: FEEDBACK & EVALUATION</span>
                <p style="font-size: 13px; margin-top: 6px;">Review efficacy: did the rule prevent compromise? Decommission stale signatures. <em>The most neglected phase in modern SOCs!</em></p>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "The 6-Phase Intelligence Cycle is our operational rhythm. Notice Phase 6: Feedback. In most enterprise SOCs, Phase 6 is completely abandoned! Teams write an emergency detection rule, and two years later it is still running, generating 400 useless alerts every weekend because nobody completed the cycle to decommission it.",
        "notes_pedagogy": "Highlight Phase 1 (PIRs) and Phase 6 (Feedback) as the two areas where security teams either succeed or fail."
    },

    # SLIDE 12: NATO Admiralty Code
    {
        "title": "NATO Admiralty Code Source Scoring",
        "day": "DAY 01",
        "module": "MOD-01: CTI FUNDAMENTALS",
        "session": "CON-05",
        "ref": "Handbook Concept 5",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-amber">OBJECTIVE EVALUATION</div>
            <h2>NATO Admiralty Code: Source Reliability × Information Credibility</h2>
            <p>Never panic over rumors. Score source pedigree independently from technical evidence.</p>
            
            <div class="grid-2" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan);">SOURCE RELIABILITY (A to F)</strong>
                <table class="lab-steps-compact" style="margin-top: 8px;">
                  <tr><th>Code</th><th>Assessment Standard</th></tr>
                  <tr><td><strong>A</strong></td><td>Completely Reliable (No doubt of authenticity or competence)</td></tr>
                  <tr><td><strong>B</strong></td><td>Usually Reliable (Past reports consistently verified)</td></tr>
                  <tr><td><strong>C</strong></td><td>Fairly Reliable (Past track record mostly accurate)</td></tr>
                  <tr><td><strong>D</strong></td><td>Not Usually Reliable (Past history of inaccuracies)</td></tr>
                  <tr><td><strong>E</strong></td><td>Unreliable (Past reports routinely false or manipulated)</td></tr>
                  <tr><td><strong>F</strong></td><td>Reliability Cannot Be Judged (Brand-new source, unverified)</td></tr>
                </table>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--neon-amber);">INFORMATION CREDIBILITY (1 to 6)</strong>
                <table class="lab-steps-compact" style="margin-top: 8px;">
                  <tr><th>Code</th><th>Assessment Standard</th></tr>
                  <tr><td><strong>1</strong></td><td>Confirmed by other independent sources (Empirical proof)</td></tr>
                  <tr><td><strong>2</strong></td><td>Probably True (Matches known adversary TTPs)</td></tr>
                  <tr><td><strong>3</strong></td><td>Possibly True (Plausible but uncorroborated)</td></tr>
                  <tr><td><strong>4</strong></td><td>Doubtful (Inconsistent with known baselines)</td></tr>
                  <tr><td><strong>5</strong></td><td>Improbable (Defies physical/technical possibility)</td></tr>
                  <tr><td><strong>6</strong></td><td>Truth Cannot Be Judged (Zero corroborating evidence)</td></tr>
                </table>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "When an unverified post on Telegram claims your bank has been breached, what is its Admiralty rating? The source is F: unknown. The credibility is 6: unverified. You do not wake up your CEO for an F6! But if your internal proxy logs corroborate traffic to that exact C2 domain, credibility leaps to 1, giving you an actionable F1 rating.",
        "notes_pedagogy": "Teach the separation of Source (pedigree) and Information (empirical evidence). Crucial foundation for Lab 1."
    },

    # SLIDE 13: The Diamond Model
    {
        "title": "The Diamond Model of Intrusion Analysis",
        "day": "DAY 01",
        "module": "MOD-01: CTI FUNDAMENTALS",
        "session": "CON-06",
        "ref": "Handbook Concept 6",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">MATHEMATICAL MODELING</div>
            <h2>The Diamond Model: 4 Core Vertices & Meta-Features</h2>
            <p>Sergio Caltagirone's model deconstructs every malicious event into four interrelated vertices.</p>
            
            <div class="grid-2" style="margin-top: 14px; align-items: stretch;">
              <!-- Left: Interactive Diamond SVG + Control Surface -->
              <div class="diamond-interactive-stage" id="diamond-model-stage">
                <svg class="diamond-svg-canvas" viewBox="0 0 480 330">
                  <!-- Diamond Outer Perimeter Lines -->
                  <line x1="240" y1="36" x2="80" y2="165" stroke="rgba(79, 172, 254, 0.4)" stroke-width="2" stroke-dasharray="4,4" id="line-adv-cap"/>
                  <line x1="80" y1="165" x2="240" y2="294" stroke="rgba(0, 242, 254, 0.4)" stroke-width="2" stroke-dasharray="4,4" id="line-cap-vic"/>
                  <line x1="240" y1="294" x2="400" y2="165" stroke="rgba(255, 179, 0, 0.4)" stroke-width="2" stroke-dasharray="4,4" id="line-vic-inf"/>
                  <line x1="400" y1="165" x2="240" y2="36" stroke="rgba(255, 75, 75, 0.4)" stroke-width="2" stroke-dasharray="4,4" id="line-inf-adv"/>

                  <!-- Internal Cross Axes -->
                  <line x1="240" y1="50" x2="240" y2="280" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1.5" stroke-dasharray="6,4"/>
                  <line x1="95" y1="165" x2="385" y2="165" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1.5" stroke-dasharray="6,4"/>

                  <!-- Meta-Feature Axis Labels -->
                  <text x="245" y="105" fill="#64748B" font-family="monospace" font-size="9" letter-spacing="1">SOCIOPOLITICAL AXIS</text>
                  <text x="245" y="235" fill="#64748B" font-family="monospace" font-size="9" letter-spacing="1">INTENT & IMPACT</text>
                  <text x="100" y="152" fill="#64748B" font-family="monospace" font-size="9" letter-spacing="1">TECHNICAL AXIS</text>
                </svg>

                <!-- Interactive Vertex Nodes -->
                <button type="button" class="diamond-vertex-btn diamond-vertex-adversary" data-vertex="Adversary" onclick="inspectDiamondVertex('Adversary', event)">
                  <span style="font-size: 13px;">🎯</span> ADVERSARY
                </button>

                <button type="button" class="diamond-vertex-btn diamond-vertex-capability" data-vertex="Capability" onclick="inspectDiamondVertex('Capability', event)">
                  <span style="font-size: 13px;">⚡</span> CAPABILITY
                </button>

                <button type="button" class="diamond-vertex-btn diamond-vertex-infrastructure" data-vertex="Infrastructure" onclick="inspectDiamondVertex('Infrastructure', event)">
                  <span style="font-size: 13px;">📡</span> INFRASTRUCTURE
                </button>

                <button type="button" class="diamond-vertex-btn diamond-vertex-victim" data-vertex="Victim" onclick="inspectDiamondVertex('Victim', event)">
                  <span style="font-size: 13px;">🛡️</span> VICTIM
                </button>

                <!-- Center Intrusion Hub -->
                <button type="button" class="diamond-hub-btn" data-vertex="Event" onclick="inspectDiamondVertex('Event', event)" title="Click to inspect the Intrusion Event Hub">
                  <span style="font-size: 14px; margin-bottom: 2px;">⚡</span>
                  <span>EVENT</span>
                  <span style="font-size: 8px; opacity: 0.8;">HUB</span>
                </button>
              </div>
              
              <!-- Right: Detailed Forensic Telemetry Panel -->
              <div class="cyber-card" style="display: flex; flex-direction: column; justify-content: space-between; padding: 18px 20px;">
                <div>
                  <strong style="color: #FFF; font-size: 14px;">Vertex Telemetry & Operational Pivots:</strong>
                  <div id="diamond-vertex-desc" style="margin-top: 10px; font-size: 12px; color: var(--text-secondary); min-height: 140px; padding: 12px 14px; background: rgba(5,8,20,0.6); border-radius: 8px; border: 1px solid var(--border-subtle); transition: border-color 0.3s ease;">
                    <span style="color: var(--cyber-cyan); font-weight: 600;">Click any vertex (Adversary, Capability, Infrastructure, Victim) or the center Event Hub</span> to explore its investigative telemetry, NATO Admiralty rating, and pivoting pathways.
                  </div>
                </div>
                
                <div style="margin-top: 10px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 8px;">
                  <strong style="color: var(--neon-amber); font-size: 11px;">Intrusion Meta-Features:</strong>
                  <div style="font-size: 11px; color: var(--text-muted); margin-top: 4px; line-height: 1.5;">
                    • <strong>Timestamp:</strong> Execution start/end window &nbsp;|&nbsp; • <strong>Phase:</strong> Cyber Kill Chain step<br>
                    • <strong>Result:</strong> Success / Defeated / Denied &nbsp;|&nbsp; • <strong>Direction:</strong> Adversary-to-Victim / C2 Transit
                  </div>
                </div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "The Diamond Model treats an intrusion as a mathematical event. If an attacker changes their IP address, you don't panic. You pivot from the Infrastructure vertex to the Capability vertex to identify their staging tools, and then pivot to the Adversary vertex to determine their campaign objective.",
        "notes_pedagogy": "Demonstrate the interactive Diamond Model widget. Show how pivoting across vertices exposes adversary infrastructure."
    },

    # SLIDE 14: Demonstration 1 Walkthrough
    {
        "title": "Demonstration 1: Admiralty Source Scoring",
        "day": "DAY 01",
        "module": "MOD-01: CTI FUNDAMENTALS",
        "session": "DEMO-01",
        "ref": "Handbook Demonstration 1",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">TRAINER DEMONSTRATION</div>
            <h2>Demo 1: Evaluating Threat Advisory UNC-PHOENIX</h2>
            <p>Comparing an anonymous Telegram dump (F6) against an authenticated DFIR bulletin (B2).</p>
            
            <div class="grid-2" style="margin-top: 16px;">
              <div class="terminal-buffer">
                <div class="terminal-header">
                  <div class="terminal-dots"><span class="dot dot-red"></span><span class="dot dot-yellow"></span><span class="dot dot-green"></span></div>
                  <span>SOURCE A: TELEGRAM DUMP @DarkLeaks</span>
                </div>
                <div class="terminal-body" style="font-size: 12px;">
"CRITICAL ZERO-DAY! BlackCat Ransomware group 
UNC-PHOENIX is attacking energy portals right now! 
IP: 198.51.100.45 // Domain: internal-sync[.]com 
Cert issued via crt.sh! All SOCs must block!"
<br><span style="color: var(--alert-crimson); font-weight: 700;">ADMIRALTY RATING: F6 (Unverified rumor)</span>
                </div>
              </div>
              
              <div class="terminal-buffer">
                <div class="terminal-header">
                  <div class="terminal-dots"><span class="dot dot-red"></span><span class="dot dot-yellow"></span><span class="dot dot-green"></span></div>
                  <span>SOURCE B: CISA / MANDIANT ADVISORY</span>
                </div>
                <div class="terminal-body" style="font-size: 12px;">
"Advisory: UNC-PHOENIX actively targeting power grids. 
Observed Certutil downloads from 198.51.100.45 
matching SHA-256 hash e3b0c44298fc1c149afbf4... 
Corroborated by 3 energy sector incident teams."
<br><span style="color: var(--emerald-pass); font-weight: 700;">ADMIRALTY RATING: B2 (Usually reliable, probably true)</span>
                </div>
              </div>
            </div>
            
            <div class="cyber-card" style="margin-top: 14px; font-size: 13px;">
              <strong style="color: var(--cyber-cyan);">Instructor Demonstration Takeaway:</strong>
              Never assign an 'A' rating to an external vendor unless you have verified empirical packet captures inside your own network. Source B receives B2—high confidence, actionable, but still requires internal sensor verification.
            </div>
          </div>
        ''',
        "notes_say": "Notice the stark difference on screen. Source A is noisy, emotional, and completely unverified—an F6 rating. Source B gives us hashes, command-line staging, and corroboration—a B2 rating. Watch how we pivot into crt.sh to verify the certificate SANs.",
        "notes_pedagogy": "Guide students to observe technical differences between hype and actionable intelligence."
    },

    # SLIDE 15: Guided Lab 1 Walkthrough
    {
        "title": "Guided Lab 1: OTX & crt.sh Reconnaissance",
        "day": "DAY 01",
        "module": "MOD-01: CTI FUNDAMENTALS",
        "session": "LAB-01",
        "ref": "Handbook Lab Manual 1",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-blue">HANDS-ON LABORATORY</div>
            <h2>Lab 1: AlienVault OTX & crt.sh Threat Reconnaissance</h2>
            <p>Workstation Target: <code>C:\\ThreatIntel_Labs\\Lab01_OSINT\\</code> | Time Allocated: 60 Minutes</p>
            
            <div class="grid-2" style="margin-top: 16px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 14px;">20-Step Lab Milestones</strong>
                <ul style="font-size: 12px; color: var(--text-secondary); margin-top: 8px; line-height: 1.8;">
                  <li><strong>Steps 1–5:</strong> Verify venv, open <code>https://crt.sh</code>, search <code>internal-sync.com</code>.</li>
                  <li><strong>Steps 6–10:</strong> Extract Subject Alternative Names (SANs) and certificate serial numbers.</li>
                  <li><strong>Steps 11–15:</strong> Log in to AlienVault OTX, query pulse <code>UNC-PHOENIX Energy Staging</code>.</li>
                  <li><strong>Steps 16–20:</strong> Export CSV indicators, score advisory to B2, complete Diamond Model.</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--neon-amber); font-size: 14px;">Lab Troubleshooting & Fallbacks</strong>
                <p style="font-size: 12px; margin-top: 8px;">
                  If <code>crt.sh</code> returns 502/504 Gateway Timeout due to global query load, do not stop your investigation!
                </p>
                <div class="terminal-buffer" style="margin: 8px 0; font-size: 11px;">
                  <div class="terminal-body">
<span class="terminal-cmd"># Classroom Offline Fallback:</span>
cat C:\\ThreatIntel_Labs\\Lab01_OSINT\\offline_cache\\crt_sh_internal_sync.json | jq .
                  </div>
                </div>
                <div style="font-size: 11px; color: var(--text-muted);">Pass Criterion: Verified Admiralty worksheet & Diamond Model submitted.</div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Turn to your lab workstations. Navigate to C:\\ThreatIntel_Labs\\Lab01_OSINT. If crt.sh hangs, remember your troubleshooting training: use the pre-cached JSON fallback. You have 60 minutes to complete the 20 milestones. I will be circulating across all 6 pods.",
        "notes_pedagogy": "Emphasize self-reliance and the offline fallback. Walk the floor actively during student execution."
    },

    # SLIDE 16: Day 1 Knowledge Check
    {
        "title": "Day 1 Knowledge Check",
        "day": "DAY 01",
        "module": "MOD-01: CTI FUNDAMENTALS",
        "session": "CHECKPOINT",
        "ref": "Trainer Handbook Section 1.7",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-amber">END-OF-DAY CHECKPOINT</div>
            <h2>Day 1 Knowledge Check: Analytical Verification</h2>
            <p>Test your understanding before we bridge into Day 2 behavioral modeling.</p>
            
            <div class="interactive-decision-box" style="margin-top: 20px;">
              <strong style="color: #FFF; font-size: 15px;">Question for Pod 3 & Pod 4:</strong>
              <p style="font-size: 13px; color: var(--text-secondary); margin: 8px 0 14px 0;">
                A threat intelligence vendor bulletin claims that an IP address is malicious with 99% confidence. However, passive DNS reveals that this same IP currently hosts 600 distinct legitimate corporate customer domains on a multi-tenant cloud CDN. What action should the SOC take?
              </p>
              <div class="decision-options">
                <button class="decision-btn" onclick="selectDecision(this, false, 'Blocking this IP would inadvertently block hundreds of legitimate customer applications and cause major business disruption.')">
                  <span>A) Add the IP to the perimeter firewall blocklist immediately because vendor confidence is 99%.</span>
                  <span>➔</span>
                </button>
                <button class="decision-btn" onclick="selectDecision(this, true, 'Correct! On shared cloud infrastructure, blocking the IP causes massive collateral damage. Analysts must filter by domain/Host header or inspect endpoint process execution.')">
                  <span>B) Do not block the IP. Pivot to domain/URL filtering and inspect local host process execution.</span>
                  <span>➔</span>
                </button>
              </div>
              <div class="decision-explanation" style="margin-top: 12px; font-size: 13px; font-family: var(--font-mono);"></div>
            </div>
          </div>
        ''',
        "notes_say": "Look at the question on screen. A vendor says 99% confidence, but passive DNS reveals 600 domains on that IP. What do you do? Pod 3, what's your verdict? Exactly! If you block that IP, you take down your own customer portals. Context prevents defense from destroying business operations.",
        "notes_pedagogy": "Reinforce the multi-tenant cloud IP dilemma. Bridge cleanly to Day 2: moving beyond fragile IP addresses to behavioral modeling."
    }
]
