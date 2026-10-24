# Slides Data: Act 4 (Day 4 - Telemetry & Sigma) & Act 5 (Day 5 - Triage & Forensics)
# Slides 37 to 58

ACT4_ACT5_SLIDES = [
    # SLIDE 37: Day 4 Launch
    {
        "title": "Day 4 Launch & Objectives",
        "day": "DAY 04",
        "day_start": 4,
        "module": "MOD-04: TELEMETRY & SIEM",
        "session": "SES-04 (1:00–5:00 PM)",
        "ref": "Handbook Module 4",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">MODULE 04 LAUNCH</div>
            <h2>Multi-Source Telemetry, SIEM Correlation & Sigma Detection Rules</h2>
            <p>Session ID: SES-04 | Scheduled Net Teaching: 220 Minutes | Refreshment Break: 3:00 PM (20 min)</p>
            
            <div class="grid-2" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 15px;">Target Learning Outcomes (PLO-4)</strong>
                <ul style="font-size: 13px; color: var(--text-secondary); margin-top: 10px; line-height: 1.7;">
                  <li><strong>Telemetry Architecture:</strong> Integrate Host, Network, and Cloud sensor logs.</li>
                  <li><strong>Windows Auditing:</strong> Decipher Event ID 4624 (Logon Types) and 4688 (Process Lineage).</li>
                  <li><strong>Sysmon Deep-Dive:</strong> Master Event IDs 1 (Process), 3 (Network), 10 (Injection), 22 (DNS).</li>
                  <li><strong>Network Sensors:</strong> Correlate Zeek <code>conn.log</code>, <code>dns.log</code>, and Suricata EVE.json.</li>
                  <li><strong>Cross-Source Pivoting:</strong> Map local host process execution directly to network flow UIDs.</li>
                  <li><strong>Sigma Rule Engineering:</strong> Author portable detection logic and transpile via <code>pySigma</code>.</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--electric-blue); font-size: 15px;">Hands-On Milestone: LAB-04</strong>
                <p style="font-size: 13px; margin-top: 10px;">
                  Every analyst will analyze multi-source telemetry logs, pivot from a suspicious Windows Sysmon Event ID 1 process tree to Zeek network flow records, author a custom Sigma YAML detection rule for <strong>UNC-PHOENIX</strong> Certutil staging, and transpile it to Splunk and Elasticsearch formats.
                </p>
                <div style="margin-top: 16px; padding: 10px; background: rgba(0, 242, 254, 0.08); border-radius: 6px; border: 1px dashed var(--cyber-cyan); font-family: var(--font-mono); font-size: 12px; color: var(--cyber-cyan);">
                  TARGET FILE: sigma_certutil_staging.yml // LAB-04 COMPLETE
                </div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Good afternoon, colleagues, and welcome to Day 4. Today we enter the engine room: Windows internals, Sysmon, and network packet telemetry. If you enjoy staring at pretty vendor dashboards with green pie charts, today will cure you of that habit! Real threat detection happens down in the raw event logs.",
        "notes_pedagogy": "HUMOR ANCHOR: Vendor dashboards with green pie charts vs. raw engine-room logs. Set the technical stage for deep telemetry analysis."
    },

    # SLIDE 38: Multi-Source Telemetry Architecture
    {
        "title": "Multi-Source Telemetry Architecture",
        "day": "DAY 04",
        "module": "MOD-04: TELEMETRY & SIEM",
        "session": "CON-01",
        "ref": "Handbook Day 4 Concept 1",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-blue">TELEMETRY CORRELATION</div>
            <h2>Multi-Source Telemetry: The Triad of Visibility</h2>
            <p>No single sensor sees the entire attack. True visibility requires multi-source correlation.</p>
            
            <div class="grid-3" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan);">1. HOST TELEMETRY</strong>
                <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 6px;">Windows Events, Sysmon, EDR</div>
                <p style="font-size: 13px;">What executed? Process trees, command lines, loaded DLLs, memory injections, registry modifications. <em>Strength: Exact process and user attribution.</em></p>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--electric-blue);">2. NETWORK TELEMETRY</strong>
                <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 6px;">Zeek, Suricata, NetFlow, PCAP</div>
                <p style="font-size: 13px;">Where did it communicate? Byte volumes, TCP flags, DNS queries, TLS certificates, HTTP headers. <em>Strength: Unforgeable wire truth.</em></p>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--neon-amber);">3. CLOUD / IDENTITY</strong>
                <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 6px;">Entra ID, AWS CloudTrail, Okta</div>
                <p style="font-size: 13px;">Who authenticated? MFA tokens, token theft, service principal activity, abnormal geolocations. <em>Strength: Identity plane tracking.</em></p>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Correlating host and network telemetry is like checking both the college main gate security register and the hostel warden's sign-in sheet. If a student says they were in the hostel studying at 10 PM, but the main gate register shows their bike leaving at 9:45 PM, the discrepancy tells you the truth. In cyber defense, an attacker can modify their command line, but they cannot erase the firewall connection record and the Zeek conn.log simultaneously.",
        "notes_pedagogy": "HUMOR ANCHOR: Hostel warden's sign-in sheet vs. main gate security register. Explains why combining host and wire data defeats adversary evasion."
    },

    # SLIDE 39: Windows Security Event Telemetry
    {
        "title": "Windows Security Event Telemetry",
        "day": "DAY 04",
        "module": "MOD-04: TELEMETRY & SIEM",
        "session": "CON-02",
        "ref": "Handbook Day 4 Concept 2",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">HOST INTERNALS</div>
            <h2>Windows Security Auditing: Essential Event IDs</h2>
            <p>The standard Windows Event Log security baseline for detection engineers.</p>
            
            <div class="grid-2" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 15px;">EVENT ID 4624: LOGON TYPES</strong>
                <table class="lab-steps-compact" style="margin-top: 8px;">
                  <tr><th>Type</th><th>Logon Mechanism & Operational Context</th></tr>
                  <tr><td><strong>Type 2</strong></td><td>Interactive Logon (Physical keyboard & screen)</td></tr>
                  <tr><td><strong>Type 3</strong></td><td>Network Logon (SMB, PsExec, Pass-the-Hash!)</td></tr>
                  <tr><td><strong>Type 7</strong></td><td>Unlock Workstation (Screen unlock)</td></tr>
                  <tr><td><strong>Type 10</strong></td><td>RemoteInteractive (Remote Desktop Protocol / RDP)</td></tr>
                </table>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--neon-amber); font-size: 15px;">EVENT ID 4688: PROCESS CREATION</strong>
                <p style="font-size: 13px; margin-top: 8px;">
                  Records every binary executed on the system. Requires GPO policy <em>"Include command line in process creation events"</em> enabled.
                </p>
                <div class="terminal-buffer" style="margin-top: 10px; font-size: 11px;">
                  <div class="terminal-body">
<span class="terminal-cmd">Creator Process:</span> C:\Windows\explorer.exe
<span class="terminal-cmd">New Process Name:</span> C:\Windows\System32\cmd.exe
<span class="terminal-cmd">Process Command Line:</span> cmd.exe /c whoami /priv
                  </div>
                </div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Memorize Logon Type 3. When an attacker executes Pass-the-Hash or moves laterally using PsExec, Windows records Logon Type 3 (Network). If you see an administrative account logging in via Type 3 at 3:00 AM from a DMZ workstation, sound the alarm.",
        "notes_pedagogy": "Emphasize Logon Type 3 and Type 10 as the core indicators of lateral movement."
    },

    # SLIDE 40: Sysmon Internal Telemetry
    {
        "title": "Sysmon Telemetry Deep-Dive",
        "day": "DAY 04",
        "module": "MOD-04: TELEMETRY & SIEM",
        "session": "CON-03",
        "ref": "Handbook Day 4 Concept 3",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-amber">SYSINTERNALS SYSMON</div>
            <h2>Microsoft Sysmon: The High-Fidelity Endpoint Sensor</h2>
            <p>System Monitor bridges the gap between basic event logs and commercial EDR agents.</p>
            
            <div class="grid-4" style="margin-top: 20px; font-size: 12px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan);">EVENT ID 1</strong>
                <div style="font-weight: 700; color: #FFF; margin: 6px 0;">Process Create</div>
                <p>Captures full command line, parent process lineage, image hashes (MD5, SHA-256), and original file name.</p>
              </div>
              <div class="cyber-card">
                <strong style="color: var(--electric-blue);">EVENT ID 3</strong>
                <div style="font-weight: 700; color: #FFF; margin: 6px 0;">Network Connect</div>
                <p>Binds the exact process ID and binary image to an outbound destination IP, port, and protocol.</p>
              </div>
              <div class="cyber-card">
                <strong style="color: var(--alert-crimson);">EVENT ID 10</strong>
                <div style="font-weight: 700; color: #FFF; margin: 6px 0;">Process Access</div>
                <p>Detects process injection (T1055) and LSASS memory dumping (Mimikatz accessing lsass.exe).</p>
              </div>
              <div class="cyber-card">
                <strong style="color: var(--neon-amber);">EVENT ID 22</strong>
                <div style="font-weight: 700; color: #FFF; margin: 6px 0;">DNS Query</div>
                <p>Logs the exact query string, resolved IP, and originating process ID (detects C2 domain resolution).</p>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Look at Sysmon Event ID 1: Process Creation. We look at the parent-child relationship. If Word launches PowerShell, which launches CMD, which launches Certutil... colleagues, that is not Microsoft Word doing document formatting! That is like your younger brother borrowing your motorcycle at 2:00 AM wearing a helmet and carrying a crowbar! You don't need an audit committee to know something suspicious is taking place.",
        "notes_pedagogy": "HUMOR ANCHOR: The younger brother borrowing your bike at 2:00 AM with a crowbar! Memorable analogy for malicious process trees."
    },

    # SLIDE 41: Zeek Protocol Telemetry
    {
        "title": "Zeek Protocol Brokering Telemetry",
        "day": "DAY 04",
        "module": "MOD-04: TELEMETRY & SIEM",
        "session": "CON-04",
        "ref": "Handbook Day 4 Concept 4",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-blue">WIRE TELEMETRY</div>
            <h2>Zeek (formerly Bro): Structured Protocol Brokering</h2>
            <p>Zeek converts unstructured network packet chaos into clean, structured tab-delimited logs.</p>
            
            <div class="grid-3" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 15px;">conn.log (Connections)</strong>
                <p style="font-size: 12px; margin-top: 6px;">Every TCP/UDP session. Tracks originating/responding IPs, ports, duration, byte counts, and connection state (e.g., <code>SF</code> for normal, <code>S0</code> for scan).</p>
                <div style="font-family: var(--font-mono); font-size: 11px; color: var(--text-highlight);">UID: Unique flow identifier</div>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--electric-blue); font-size: 15px;">dns.log (DNS Queries)</strong>
                <p style="font-size: 12px; margin-top: 6px;">Every domain query and response. Logs QTYPE (A, AAAA, TXT), resolved IPs, and TTL values. Detects DNS tunneling and DGA algorithms.</p>
                <div style="font-family: var(--font-mono); font-size: 11px; color: var(--text-highlight);">Linked by UID to conn.log!</div>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--neon-amber); font-size: 15px;">ssl.log (TLS Sessions)</strong>
                <p style="font-size: 12px; margin-top: 6px;">Server Name Indication (SNI), certificate subject, issuer, SHA-1 fingerprint, and JA3/JA3S client/server fingerprints.</p>
                <div style="font-family: var(--font-mono); font-size: 11px; color: var(--text-highlight);">Exposes C2 despite encryption!</div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Zeek is pure gold for SOC analysts. Notice the UID field. In Zeek, every single network conversation gets a unique connection ID—like CHhAvV31uWRrAc8oj6. If you see that UID in conn.log, you can grep that exact UID in dns.log, ssl.log, and http.log to reassemble the entire conversation.",
        "notes_pedagogy": "Explain how Zeek's UID field ties disparate protocol logs into a unified investigation stream."
    },

    # SLIDE 42: Suricata NIDS & EVE.json
    {
        "title": "Suricata NIDS & EVE.json Telemetry",
        "day": "DAY 04",
        "module": "MOD-04: TELEMETRY & SIEM",
        "session": "SURICATA",
        "ref": "Handbook Day 4 Section 4.3",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-crimson">SIGNATURE INSPECTION</div>
            <h2>Suricata Network IDS & EVE.json Telemetry</h2>
            <p>High-performance, multi-threaded signature-based network threat detection.</p>
            
            <div class="terminal-buffer" style="margin-top: 18px;">
              <div class="terminal-header">
                <div class="terminal-dots"><span class="dot dot-red"></span><span class="dot dot-yellow"></span><span class="dot dot-green"></span></div>
                <span>SURICATA RULE STRUCTURE & EVE JSON OUTPUT</span>
              </div>
              <div class="terminal-body" style="font-size: 12px;">
<span style="color: #64748B;"># Suricata Signature Syntax:</span>
<span class="terminal-cmd">alert http $HOME_NET any -> $EXTERNAL_NET any</span> (
  msg:<span style="color: #A5D6A7;">"ET MALWARE UNC-PHOENIX Certutil Staging Download"</span>;
  flow:established,to_server;
  http.uri; content:<span style="color: #A5D6A7;">"/internal-sync.txt"</span>;
  http.user_agent; content:<span style="color: #A5D6A7;">"Certutil"</span>;
  classtype:trojan-activity; sid:2045910; rev:1;
)

<span style="color: #64748B;"># Resulting EVE.json Telemetry:</span>
{"timestamp":"2026-10-29T02:14:15.120Z","event_type":"alert","src_ip":"10.0.4.12","src_port":49820,
 "dest_ip":"198.51.100.45","dest_port":80,"alert":{"action":"allowed","signature_id":2045910,
 "signature":"ET MALWARE UNC-PHOENIX Certutil Staging Download","category":"Trojan Activity"}}
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Look at the Suricata rule. We inspect both the URI and the User-Agent header for 'Certutil'. When an attacker executes certutil to download a stager, Suricata triggers SID 2045910 and outputs a clean JSON record in eve.json.",
        "notes_pedagogy": "Deconstruct the Suricata rule syntax: Action, Protocol, Network, Flow, Content matching, SID."
    },

    # SLIDE 43: Cross-Source Pivot Mechanics
    {
        "title": "Cross-Source Telemetry Pivoting",
        "day": "DAY 04",
        "module": "MOD-04: TELEMETRY & SIEM",
        "session": "CON-05",
        "ref": "Handbook Day 4 Concept 5",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">SOC PIVOTING WORKFLOW</div>
            <h2>The Cross-Source Pivot: From Host Lineage to Wire Flow</h2>
            <p>How tier-2 analysts correlate host artifacts with unforgeable network evidence.</p>
            
            <div class="grid-3" style="margin-top: 24px;">
              <div class="cyber-card" style="border-color: var(--alert-crimson);">
                <span class="cyber-badge badge-crimson">STEP 1: SYSMON EID 1</span>
                <div style="font-weight: 700; color: #FFF; margin: 10px 0 4px 0;">Host Execution</div>
                <p style="font-size: 12px;">Alert fires on <code>cmd.exe</code> launching <code>certutil.exe -urlcache</code> on Host 10.0.4.12. Process ID: <strong>4820</strong>.</p>
              </div>
              <div class="cyber-card" style="border-color: var(--electric-blue);">
                <span class="cyber-badge badge-blue">STEP 2: SYSMON EID 3</span>
                <div style="font-weight: 700; color: #FFF; margin: 10px 0 4px 0;">Socket Binding</div>
                <p style="font-size: 12px;">Process ID <strong>4820</strong> opens outbound socket: <code>10.0.4.12:49820 ➔ 198.51.100.45:80</code> at 02:14:14 IST.</p>
              </div>
              <div class="cyber-card" style="border-color: var(--cyber-cyan);">
                <span class="cyber-badge badge-cyan">STEP 3: ZEEK conn.log</span>
                <div style="font-weight: 700; color: #FFF; margin: 10px 0 4px 0;">Wire Corroboration</div>
                <p style="font-size: 12px;">Search 5-tuple in Zeek: UID <code>CHhAvV31uWRrAc8oj6</code> proves 45 KB transferred. HTTP log confirms payload hash!</p>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "This three-step pivot is the bedrock of threat investigation. Step 1: Sysmon Event 1 gives you the PID and command line. Step 2: Sysmon Event 3 binds that PID to an outbound socket. Step 3: Zeek conn.log confirms the exact bytes on the wire. The adversary cannot escape this correlation.",
        "notes_pedagogy": "Walk students through the 3-step pivot sequence. Key concept for Lab 4."
    },

    # SLIDE 44: Sigma Rule Specification
    {
        "title": "Sigma Rule Specification",
        "day": "DAY 04",
        "module": "MOD-04: TELEMETRY & SIEM",
        "session": "CON-06",
        "ref": "Handbook Day 4 Concept 6",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-amber">GENERIC DETECTION</div>
            <h2>Sigma: The 'Write Once, Detect Everywhere' Standard</h2>
            <p>Open-source, generic YAML detection signatures transpiled to any SIEM query language.</p>
            
            <div class="terminal-buffer" style="margin-top: 18px;">
              <div class="terminal-header">
                <div class="terminal-dots"><span class="dot dot-red"></span><span class="dot dot-yellow"></span><span class="dot dot-green"></span></div>
                <span>proc_creation_win_certutil_staging.yml // SIGMA SPECIFICATION</span>
              </div>
              <div class="terminal-body" style="font-size: 12px;">
<span class="terminal-cmd">title:</span> UNC-PHOENIX Certutil Remote File Download
<span class="terminal-cmd">id:</span> a8b4c2e1-4501-4921-9921-091248591234
<span class="terminal-cmd">status:</span> production
<span class="terminal-cmd">logsource:</span>
    category: process_creation
    product: windows
<span class="terminal-cmd">detection:</span>
    selection_cmd:
        Image|endswith: <span style="color: #A5D6A7;">'\\certutil.exe'</span>
        CommandLine|contains|all:
            - <span style="color: #A5D6A7;">'-urlcache'</span>
            - <span style="color: #A5D6A7;">'http'</span>
    condition: selection_cmd
<span class="terminal-cmd">level:</span> high
<span class="terminal-cmd">tags:</span>
    - attack.defense_evasion
    - attack.t1059.001
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Sigma is the 'write once, detect everywhere' language. It's like writing an algorithm on the blackboard that works in C, Java, and Python. Unlike student assignments where four people copy the same code from GitHub and forget to change the original author's name in the header comment, Sigma rules are clean, standardized, and portable across Splunk, QRadar, and Elasticsearch.",
        "notes_pedagogy": "HUMOR ANCHOR: Copying GitHub code and forgetting to change the roll number! Explain how pySigma converts Sigma into native SIEM queries."
    },

    # SLIDE 45: Demonstration 4 Walkthrough
    {
        "title": "Demonstration 4: Telemetry Pivot & Sigma Transpilation",
        "day": "DAY 04",
        "module": "MOD-04: TELEMETRY & SIEM",
        "session": "DEMO-04",
        "ref": "Handbook Demonstration 4",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">TRAINER DEMONSTRATION</div>
            <h2>Demo 4: Cross-Source Pivot & pySigma Transpilation</h2>
            <p>From raw event logs to production Splunk and Elasticsearch detection queries.</p>
            
            <div class="grid-2" style="margin-top: 16px;">
              <div class="terminal-buffer">
                <div class="terminal-header">
                  <div class="terminal-dots"><span class="dot dot-red"></span><span class="dot dot-yellow"></span><span class="dot dot-green"></span></div>
                  <span>TRANSPILING TO SPLUNK SPL</span>
                </div>
                <div class="terminal-body" style="font-size: 11px;">
<span class="terminal-cmd"># Transpile with pySigma:</span>
sigma convert -t splunk -p sysmon proc_creation_win_certutil_staging.yml
<br><span style="color: var(--cyber-cyan);">// GENERATED SPLUNK QUERY:</span>
index=windows_sysmon EventCode=1 
Image="*\\certutil.exe" 
CommandLine="*-urlcache*" CommandLine="*http*"
                </div>
              </div>
              
              <div class="terminal-buffer">
                <div class="terminal-header">
                  <div class="terminal-dots"><span class="dot dot-red"></span><span class="dot dot-yellow"></span><span class="dot dot-green"></span></div>
                  <span>TRANSPILING TO ELASTICSEARCH KQL</span>
                </div>
                <div class="terminal-body" style="font-size: 11px;">
<span class="terminal-cmd"># Transpile with pySigma:</span>
sigma convert -t elasticsearch -p ecs proc_creation_win_certutil_staging.yml
<br><span style="color: var(--neon-amber);">// GENERATED ELASTIC KQL:</span>
event.code:"1" and 
process.executable:*\\certutil.exe and 
process.command_line:*urlcache* and 
process.command_line:*http*
                </div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Watch pySigma in action. One generic Sigma YAML file transpiles into production-ready Splunk SPL on the left, and Elastic KQL on the right. Write your detection once; deploy it across any SIEM platform in the world.",
        "notes_pedagogy": "Demonstrate the command line execution of pySigma. Emphasize why vendor independence matters."
    },

    # SLIDE 46: Guided Lab 4 Walkthrough
    {
        "title": "Guided Lab 4: Multi-Source Telemetry & Sigma",
        "day": "DAY 04",
        "module": "MOD-04: TELEMETRY & SIEM",
        "session": "LAB-04",
        "ref": "Handbook Lab Manual 4",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-blue">HANDS-ON LABORATORY</div>
            <h2>Lab 4: Telemetry Correlation & Custom Sigma Engineering</h2>
            <p>Workstation Target: <code>C:\\ThreatIntel_Labs\\Lab04_Telemetry\\</code> | Time Allocated: 60 Minutes</p>
            
            <div class="grid-2" style="margin-top: 16px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 14px;">20-Step Lab Milestones</strong>
                <ul style="font-size: 12px; color: var(--text-secondary); margin-top: 8px; line-height: 1.8;">
                  <li><strong>Steps 1–5:</strong> Open <code>sysmon_evtx.evtx</code> in Event Viewer, locate Event ID 1.</li>
                  <li><strong>Steps 6–10:</strong> Extract PID and destination IP from Event ID 3 network connect.</li>
                  <li><strong>Steps 11–15:</strong> Grep Zeek <code>conn.log</code> for IP <code>198.51.100.45</code>, extract UID.</li>
                  <li><strong>Steps 16–20:</strong> Author Sigma rule for Certutil staging, transpile via <code>pySigma</code>.</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--neon-amber); font-size: 14px;">Lab Troubleshooting & Fallbacks</strong>
                <p style="font-size: 12px; margin-top: 8px;">
                  If <code>sigma convert</code> throws <code>BackendNotFoundError: splunk</code>, ensure the pySigma Splunk plugin is installed in your local venv:
                </p>
                <div class="terminal-buffer" style="margin: 8px 0; font-size: 11px;">
                  <div class="terminal-body">
<span class="terminal-cmd"># Local Plugin Verification:</span>
pip install pySigma-backend-splunk pySigma-backend-elasticsearch
                  </div>
                </div>
                <div style="font-size: 11px; color: var(--text-muted);">Pass Criterion: Valid Sigma YAML and transpiled SPL query submitted.</div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Turn to your workstations. Open Lab 4. Follow the 20 milestones to correlate the Sysmon EVTX trace with the Zeek conn.log, and transpile your Sigma rule. You have 60 minutes.",
        "notes_pedagogy": "Guide students through the EVTX to Zeek pivot. Remind them to check pySigma plugin packages."
    },

    # SLIDE 47: Day 4 Knowledge Check
    {
        "title": "Day 4 Knowledge Check",
        "day": "DAY 04",
        "module": "MOD-04: TELEMETRY & SIEM",
        "session": "CHECKPOINT",
        "ref": "Trainer Handbook Section 4.7",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-amber">END-OF-DAY CHECKPOINT</div>
            <h2>Day 4 Knowledge Check: Telemetry Mastery</h2>
            <p>Verify your understanding of cross-source correlation before we move to digital forensics.</p>
            
            <div class="interactive-decision-box" style="margin-top: 20px;">
              <strong style="color: #FFF; font-size: 15px;">Question for Pod 3 & Pod 4:</strong>
              <p style="font-size: 13px; color: var(--text-secondary); margin: 8px 0 14px 0;">
                An attacker compromises an internal server and executes a living-off-the-land command. To evade detection, they use an unmanaged script that modifies the local Windows command-line string. Which network sensor guarantees unforgeable visibility of the outbound connection, and why?
              </p>
              <div class="decision-options">
                <button class="decision-btn" onclick="selectDecision(this, false, 'Endpoint logs can be manipulated if the adversary achieves SYSTEM privileges.')">
                  <span>A) Windows Security Event ID 4688, because endpoint operating systems can never be bypassed.</span>
                  <span>➔</span>
                </button>
                <button class="decision-btn" onclick="selectDecision(this, true, 'Correct! Zeek inspects the raw physical network packets on the wire (out-of-band). Even if an adversary compromises the host kernel, they cannot forge the TCP 3-way handshake recorded by the network tap.')">
                  <span>B) Zeek conn.log, because out-of-band network packet capture records wire truth independent of compromised host OS state.</span>
                  <span>➔</span>
                </button>
              </div>
              <div class="decision-explanation" style="margin-top: 12px; font-size: 13px; font-family: var(--font-mono);"></div>
            </div>
          </div>
        ''',
        "notes_say": "Pod 3 and Pod 4, review the question. Why is Zeek unforgeable? Exactly! The wire doesn't lie. Even if an attacker has root on a server, the network switch tap records the raw TCP packets. That is wire truth.",
        "notes_pedagogy": "Reinforce the principle of out-of-band wire truth. Bridge to Day 5: forensic triage."
    },

    # SLIDE 48: Day 5 Launch
    {
        "title": "Day 5 Launch & Objectives",
        "day": "DAY 05",
        "day_start": 5,
        "module": "MOD-05: TRIAGE & FORENSICS",
        "session": "SES-05 (2:00–5:00 PM)",
        "ref": "Handbook Module 5",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-crimson">MODULE 05 LAUNCH</div>
            <h2>Incident Triage, Digital Forensics & Volatile Evidence Acquisition</h2>
            <p>Session ID: SES-05 | Scheduled Net Teaching: 165 Minutes | Friday Schedule (2:00–5:00 PM)</p>
            
            <div class="grid-2" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 15px;">Target Learning Outcomes (PLO-5)</strong>
                <ul style="font-size: 13px; color: var(--text-secondary); margin-top: 10px; line-height: 1.7;">
                  <li><strong>NIST SP 800-61r3:</strong> Navigate the 4-phase incident response lifecycle.</li>
                  <li><strong>CSIRT Roles & Severity:</strong> Classify P1 Critical to P4 Low enterprise incidents.</li>
                  <li><strong>RFC 3227 Volatility:</strong> Execute the order of volatile evidence preservation.</li>
                  <li><strong>The Golden Rule:</strong> Prevent forensic contamination—never reboot live victim hosts!</li>
                  <li><strong>KAPE Triage:</strong> Execute target and module collections for rapid artifact extraction.</li>
                  <li><strong>Master Timelines:</strong> Detect timestomping across $STANDARD_INFO vs. $FILE_NAME.</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--alert-crimson); font-size: 15px;">Hands-On Milestone: LAB-06</strong>
                <p style="font-size: 13px; margin-top: 10px;">
                  Every analyst will execute a KAPE triage collection on a compromised host image, parse extracted MFT artifacts using Timeline Explorer, isolate timestomped binaries, and construct a verified forensic incident timeline for <strong>UNC-PHOENIX</strong>.
                </p>
                <div style="margin-top: 16px; padding: 10px; background: rgba(255, 75, 75, 0.08); border-radius: 6px; border: 1px dashed var(--alert-crimson); font-family: var(--font-mono); font-size: 12px; color: var(--alert-crimson);">
                  TARGET FILE: forensic_triage_timeline.csv // LAB-06 COMPLETE
                </div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Good afternoon, colleagues, and welcome to Day 5. Today is Friday, and we start at 2:00 PM. In enterprise security, Friday afternoon is the exact hour when adversaries love to strike—because they know the security team is dreaming about the weekend, traffic on the highway is building up, and the SOC is handing over to the skeleton weekend shift!",
        "notes_pedagogy": "HUMOR ANCHOR: Friday afternoon adversary strikes while everyone thinks of the weekend. Emphasize why rigor cannot slacken on Fridays."
    },

    # SLIDE 49: NIST SP 800-61r3 Lifecycle
    {
        "title": "NIST SP 800-61r3 Lifecycle",
        "day": "DAY 05",
        "module": "MOD-05: TRIAGE & FORENSICS",
        "session": "CON-01",
        "ref": "Handbook Day 5 Concept 1",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">INCIDENT FRAMEWORK</div>
            <h2>NIST SP 800-61r3: The Incident Response Lifecycle</h2>
            <p>The definitive global standard for structured enterprise incident handling.</p>
            
            <div class="grid-4" style="margin-top: 24px; font-size: 13px;">
              <div class="cyber-card">
                <span class="cyber-badge badge-blue">PHASE 1: PREPARATION</span>
                <div style="font-weight: 700; color: #FFF; margin: 10px 0 4px 0;">Readiness Baseline</div>
                <p style="font-size: 12px;">CSIRT contact lists, out-of-band comms, pre-deployed KAPE tools, retainers, and tabletop drills.</p>
              </div>
              <div class="cyber-card" style="border-color: var(--cyber-cyan);">
                <span class="cyber-badge badge-cyan">PHASE 2: DETECTION</span>
                <div style="font-weight: 700; color: #FFF; margin: 10px 0 4px 0;">Triage & Scoping</div>
                <p style="font-size: 12px;">Validate precursors vs. indicators. Classify severity (P1–P4). Isolate patient zero and attack blast radius.</p>
              </div>
              <div class="cyber-card" style="border-color: var(--alert-crimson);">
                <span class="cyber-badge badge-crimson">PHASE 3: CONTAINMENT</span>
                <div style="font-weight: 700; color: #FFF; margin: 10px 0 4px 0;">Eradication & Recovery</div>
                <p style="font-size: 12px;">Short-term network isolation, KRBTGT double-reset, wipe persistence, restore from clean golden backups.</p>
              </div>
              <div class="cyber-card" style="border-color: var(--neon-amber);">
                <span class="cyber-badge badge-amber">PHASE 4: POST-INCIDENT</span>
                <div style="font-weight: 700; color: #FFF; margin: 10px 0 4px 0;">Lessons Learned</div>
                <p style="font-size: 12px;">Post-mortem RCA meeting within 72 hours. Update detection rules, patch architectural gaps.</p>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "NIST SP 800-61r3 gives us our incident battle plan. Notice Phase 1: Preparation. You do not install forensic tools during a ransomware outbreak! You have them pre-staged in your forensic toolkit.",
        "notes_pedagogy": "Deconstruct the 4 phases of NIST SP 800-61r3."
    },

    # SLIDE 50: CSIRT Roles & Severity Matrix
    {
        "title": "CSIRT Roles & Severity Matrix",
        "day": "DAY 05",
        "module": "MOD-05: TRIAGE & FORENSICS",
        "session": "CON-02",
        "ref": "Handbook Day 5 Concept 2",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-amber">INCIDENT GOVERNANCE</div>
            <h2>CSIRT Operational Roles & Enterprise Severity Matrix</h2>
            <p>Clear role boundaries prevent panic during high-stakes enterprise incidents.</p>
            
            <div class="grid-2" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 15px;">CSIRT Role Hierarchy:</strong>
                <ul style="font-size: 13px; color: var(--text-secondary); margin-top: 8px; line-height: 1.7;">
                  <li><strong>Incident Commander (IC):</strong> Holds absolute authority over containment decisions. Shields technical analysts from executive interference.</li>
                  <li><strong>Lead Investigator / DFIR:</strong> Directs forensic triage, memory dumps, and timeline analysis.</li>
                  <li><strong>Containment Engineer:</strong> Executes firewall null-routes, AD account lockouts, and host network isolation.</li>
                  <li><strong>Communications Lead:</strong> Manages legal counsel, regulatory disclosures (CERT-In), and customer PR.</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--alert-crimson); font-size: 15px;">Severity Classification:</strong>
                <table class="lab-steps-compact" style="margin-top: 8px;">
                  <tr><th>Level</th><th>Impact & SLA</th></tr>
                  <tr><td><strong style="color: var(--alert-crimson);">P1 - Critical</strong></td><td>Active ransomware, domain controller breach (SLA: 15m)</td></tr>
                  <tr><td><strong style="color: var(--neon-amber);">P2 - High</strong></td><td>Lateral movement, customer database compromised (SLA: 1h)</td></tr>
                  <tr><td><strong style="color: var(--electric-blue);">P3 - Medium</strong></td><td>Single workstation malware, isolated C2 beacon (SLA: 4h)</td></tr>
                  <tr><td><strong style="color: var(--cyber-cyan);">P4 - Low</strong></td><td>Phishing email blocked by filter, port scan (SLA: 24h)</td></tr>
                </table>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "The Incident Commander has one primary job: protect the technical analysts from panicking executives so the analysts can do their work! If the CEO walks in demanding answers every ten minutes, the IC steps in and manages the briefing.",
        "notes_pedagogy": "Emphasize the role of the Incident Commander as the operational shield."
    },

    # SLIDE 51: RFC 3227 Order of Volatility
    {
        "title": "RFC 3227 Order of Volatility",
        "day": "DAY 05",
        "module": "MOD-05: TRIAGE & FORENSICS",
        "session": "CON-03",
        "ref": "Handbook Day 5 Concept 3",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-crimson">EVIDENCE PRESERVATION</div>
            <h2>RFC 3227: Order of Volatility & Legal Chain of Custody</h2>
            <p>Evidence disappears at different rates. Capture the most volatile artifacts first.</p>
            
            <div style="max-width: 800px; margin: 20px auto 0 auto;">
              <div class="cyber-card" style="margin-bottom: 8px; border-color: var(--alert-crimson); background: rgba(255,75,75,0.12);">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="color: var(--alert-crimson);">1. CPU Registers & Cache</strong>
                  <span class="cyber-badge badge-crimson">NANOSECONDS</span>
                </div>
                <div style="font-size: 12px; color: var(--text-secondary); margin-top: 4px;">Vanishes instantly on context switch. Rarely captured in standard enterprise triage.</div>
              </div>
              <div class="cyber-card" style="margin-bottom: 8px; border-color: var(--neon-amber); background: rgba(255,179,0,0.1);">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="color: var(--neon-amber);">2. Routing Tables, ARP Cache, Process Table, Kernel Memory (RAM)</strong>
                  <span class="cyber-badge badge-amber">SECONDS TO MINUTES</span>
                </div>
                <div style="font-size: 12px; color: var(--text-secondary); margin-top: 4px;">Decrypted malware binaries, active C2 network sockets, injected DLLs, unencrypted keys. <em>Vulnerable to power loss!</em></div>
              </div>
              <div class="cyber-card" style="margin-bottom: 8px; border-color: var(--electric-blue); background: rgba(79,172,254,0.1);">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="color: var(--electric-blue);">3. Temporary File Systems & Swap Space</strong>
                  <span class="cyber-badge badge-blue">MINUTES TO HOURS</span>
                </div>
                <div style="font-size: 12px; color: var(--text-secondary); margin-top: 4px;">Virtual memory pagefile.sys, hiberfil.sys, staging folders (C:\\Windows\\Temp).</div>
              </div>
              <div class="cyber-card" style="border-color: var(--cyber-cyan); background: rgba(0,242,254,0.06);">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <strong style="color: var(--cyber-cyan);">4. Non-Volatile Storage (Hard Disks, SSDs) & Remote Logging</strong>
                  <span class="cyber-badge badge-cyan">DAYS TO YEARS</span>
                </div>
                <div style="font-size: 12px; color: var(--text-secondary); margin-top: 4px;">NTFS $MFT, Event Log EVTX files, prefetch, Amcache. Stable across power cycles.</div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "RFC 3227 dictates our preservation sequence. Notice RAM sits at Level 2. If you turn off the power, volatile RAM vanishes forever. Always capture memory before touching the hard drive.",
        "notes_pedagogy": "Drill the RFC 3227 order of volatility into memory. Direct bridge to the Golden Rule."
    },

    # SLIDE 52: The Golden Rule: "Do Not Reboot!"
    {
        "title": "The Golden Rule: Do Not Reboot!",
        "day": "DAY 05",
        "module": "MOD-05: TRIAGE & FORENSICS",
        "session": "CON-04",
        "ref": "Handbook Day 5 Concept 4",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-crimson">FORENSIC CARDINAL SIN</div>
            <h2>The Golden Rule of Incident Response: Do Not Reboot!</h2>
            <p>Rebooting an infected system destroys the most critical evidence required for attribution.</p>
            
            <div class="grid-2" style="margin-top: 24px;">
              <div class="cyber-card alert-card">
                <strong style="color: var(--alert-crimson); font-size: 15px;">WHAT REBOOTING DESTROYS FOREVER:</strong>
                <ul style="font-size: 13px; color: var(--text-secondary); margin-top: 10px; line-height: 1.8;">
                  <li><strong>Volatile RAM:</strong> Injected fileless malware DLLs running in memory.</li>
                  <li><strong>Decrypted Payloads:</strong> Ransomware keys stored in memory buffers.</li>
                  <li><strong>Active Network Sockets:</strong> Live TCP connections to adversary C2 IP nodes.</li>
                  <li><strong>Running Process Tree:</strong> Parent-child process IDs and command lines.</li>
                  <li><strong>Logged-in Session Tokens:</strong> Stolen Kerberos tickets and NTLM hashes.</li>
                </ul>
              </div>
              
              <div class="cyber-card intel-card">
                <strong style="color: var(--cyber-cyan); font-size: 15px;">CORRECT TRIAGE PROTOCOL:</strong>
                <ul style="font-size: 13px; color: var(--text-secondary); margin-top: 10px; line-height: 1.8;">
                  <li><strong>1. Network Isolation:</strong> Disconnect Ethernet or apply host firewall null-route.</li>
                  <li><strong>2. Keep Power On:</strong> Prevent system shutdown or sleep mode.</li>
                  <li><strong>3. Live Memory Dump:</strong> Execute WinPmem, DumpIt, or LiME memory acquisition.</li>
                  <li><strong>4. Triage Collection:</strong> Run KAPE to extract $MFT, Prefetch, and Event Logs.</li>
                  <li><strong>5. Chain of Custody:</strong> Calculate SHA-256 hash immediately on extraction!</li>
                </ul>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "When your laptop starts behaving strangely, the common campus instinct is: 'Sir, just restart it and hope the problem has graduated and left!' In incident response, restarting the machine is an unforgivable forensic crime! Rebooting dumps volatile RAM instantly—which is where the malware's decrypted payload and active C2 sockets live. It is like a detective arriving at a crime scene with a mop and disinfectant and washing the floor before taking fingerprints!",
        "notes_pedagogy": "HUMOR ANCHOR: The detective arriving at a crime scene with a mop and disinfectant! The classic 'problem graduated' joke. Unforgettable forensic lesson."
    },

    # SLIDE 53: Live Memory Acquisition
    {
        "title": "Live Memory Acquisition Concepts",
        "day": "DAY 05",
        "module": "MOD-05: TRIAGE & FORENSICS",
        "session": "MEMORY",
        "ref": "Handbook Day 5 Section 5.3",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-blue">VOLATILITY ANALYSIS</div>
            <h2>Live Memory Acquisition & Volatility 3 Analysis</h2>
            <p>Extracting kernel memory to uncover stealth process injection and unencrypted payloads.</p>
            
            <div class="terminal-buffer" style="margin-top: 18px;">
              <div class="terminal-header">
                <div class="terminal-dots"><span class="dot dot-red"></span><span class="dot dot-yellow"></span><span class="dot dot-green"></span></div>
                <span>VOLATILITY 3 COMMAND LINE SUITE</span>
              </div>
              <div class="terminal-body" style="font-size: 12px;">
<span style="color: #64748B;"># 1. Process Tree Inspection:</span>
<span class="terminal-cmd">python3 vol.py -f memdump.raw windows.pstree</span>
* Identifies hidden processes unlinked from the ActiveProcessLinks double-linked list.

<span style="color: #64748B;"># 2. Injected Code Detection (Malfind):</span>
<span class="terminal-cmd">python3 vol.py -f memdump.raw windows.malfind</span>
* Scans VAD tree for memory pages marked PAGE_EXECUTE_READWRITE containing MZ/PE headers.

<span style="color: #64748B;"># 3. Active Network Sockets:</span>
<span class="terminal-cmd">python3 vol.py -f memdump.raw windows.netscan</span>
* Recovers closed and active TCP connections, binding PID 4820 to C2 IP 198.51.100.45.
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Volatility 3 allows you to inspect the memory dump as if the operating system were still alive. Notice malfind: it looks for memory pages marked PAGE_EXECUTE_READWRITE. Legitimate software rarely needs write and execute permissions on the same memory page—that is the signature of process injection.",
        "notes_pedagogy": "Explain the concept of memory protections (W^X) and how malfind catches stealth injected threads."
    },

    # SLIDE 54: KAPE Forensic Triage Acquisition
    {
        "title": "KAPE Forensic Triage Acquisition",
        "day": "DAY 05",
        "module": "MOD-05: TRIAGE & FORENSICS",
        "session": "CON-05",
        "ref": "Handbook Day 5 Concept 5",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">RAPID TRIAGE</div>
            <h2>KAPE: Kroll Artifact Parser and Extractor</h2>
            <p>Eric Zimmerman's triage tool acquires 95% of forensic value in under 5 minutes.</p>
            
            <div class="grid-2" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 15px;">TARGETS (--targets)</strong>
                <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 6px;">Specifies WHAT files to copy</p>
                <ul style="font-size: 12px; color: var(--text-secondary); line-height: 1.6;">
                  <li><code>KapeTriage</code>: Compound target collection</li>
                  <li><code>$MFT</code>: Master File Table metadata</li>
                  <li><code>RegistryHives</code>: SYSTEM, SOFTWARE, SAM, NTUSER.dat</li>
                  <li><code>EventLogs</code>: All *.evtx operational logs</li>
                  <li><code>Prefetch</code>: Evidence of program execution</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--electric-blue); font-size: 15px;">MODULES (--modules)</strong>
                <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 6px;">Specifies HOW to parse artifacts</p>
                <ul style="font-size: 12px; color: var(--text-secondary); line-height: 1.6;">
                  <li><code>MFTECmd</code>: Parses $MFT into CSV timeline</li>
                  <li><code>PECmd</code>: Parses Prefetch execution run counts</li>
                  <li><code>EvtxECmd</code>: Parses and normalizes Event Logs</li>
                  <li><code>RECmd</code>: Extracts registry persistence keys</li>
                  <li><em>Outputs normalized CSV for Timeline Explorer!</em></li>
                </ul>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "In the old days of forensics, capturing an image of a 2 TB hard drive took 14 hours. In incident response, you don't have 14 hours! KAPE copies only the forensic crown jewels: the MFT, prefetch, registry, and event logs. It finishes in 4 minutes and gives you 95% of the evidence.",
        "notes_pedagogy": "Contrast full physical bitstream imaging with surgical forensic triage via KAPE."
    },

    # SLIDE 55: Timestomping Analysis
    {
        "title": "Timestomping & $MFT Anomaly Analysis",
        "day": "DAY 05",
        "module": "MOD-05: TRIAGE & FORENSICS",
        "session": "CON-06",
        "ref": "Handbook Day 5 Concept 6",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-amber">ANTI-FORENSICS EXPOSED</div>
            <h2>Timestomping: $STANDARD_INFORMATION vs. $FILE_NAME</h2>
            <p>Adversaries modify file timestamps to blend in with legitimate system software.</p>
            
            <div class="grid-2" style="margin-top: 20px;">
              <div class="cyber-card">
                <strong style="color: var(--neon-amber); font-size: 15px;">The NTFS Dual-Timestamp Mechanism:</strong>
                <div style="font-size: 13px; color: var(--text-secondary); margin-top: 8px; line-height: 1.7;">
                  • <strong>$STANDARD_INFORMATION ($SI):</strong> The timestamp shown in Windows Explorer. User-mode APIs can freely backdate this attribute.<br>
                  • <strong>$FILE_NAME ($FN):</strong> The kernel-level timestamp recorded when the file name is created/renamed. Only the Windows operating system kernel can update this attribute!
                </div>
              </div>
              
              <div class="terminal-buffer" style="font-size: 11px;">
                <div class="terminal-header">
                  <div class="terminal-dots"><span class="dot dot-red"></span><span class="dot dot-yellow"></span><span class="dot dot-green"></span></div>
                  <span>TIMELINE EXPLORER // ANOMALY EXPOSED</span>
                </div>
                <div class="terminal-body">
<span class="terminal-cmd">File Name:</span> C:\Windows\Temp\calc_updater.exe
<span class="terminal-cmd">$SI Created:</span> 2021-04-12 08:14:02 (Falsified!)
<span class="terminal-cmd">$FN Created:</span> 2026-10-30 02:14:15 (REAL KERNEL RECEIPT!)
<br><span style="color: var(--alert-crimson); font-weight: 700;">VERDICT: TIMESTOMPED MALWARE (UNC-PHOENIX)</span>
                </div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Adversaries try to hide by modifying file timestamps—timestomping. They take their malware and change its creation date to match calc.exe from 2021. It's like a student who forgot to submit an assignment on Monday, so they change the date on the front page to 'Last Friday' and hope the professor doesn't notice! But NTFS keeps two receipts: $STANDARD_INFORMATION and $FILE_NAME. When we compare them in Timeline Explorer, the lie is exposed instantly!",
        "notes_pedagogy": "HUMOR ANCHOR: Backdating an assignment submission to last Friday! Explains why $FILE_NAME kernel timestamps catch anti-forensics."
    },

    # SLIDE 56: Demonstration 5 Walkthrough
    {
        "title": "Demonstration 5: KAPE & Timeline Explorer",
        "day": "DAY 05",
        "module": "MOD-05: TRIAGE & FORENSICS",
        "session": "DEMO-05",
        "ref": "Handbook Demonstration 5",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">TRAINER DEMONSTRATION</div>
            <h2>Demo 5: Live Triage Acquisition & MFT Parsing</h2>
            <p>Extracting artifacts via KAPE CLI and isolating timestomping in Timeline Explorer.</p>
            
            <div class="terminal-buffer" style="margin-top: 18px;">
              <div class="terminal-header">
                <div class="terminal-dots"><span class="dot dot-red"></span><span class="dot dot-yellow"></span><span class="dot dot-green"></span></div>
                <span>KAPE TRIAGE EXECUTION SYNTAX</span>
              </div>
              <div class="terminal-body" style="font-size: 12px;">
<span class="terminal-cmd"># Execute KAPE Compound Triage Extraction:</span>
kape.exe --tsource C: --target KapeTriage --tdest E:\Triage\Target --vhdx TriageEvidence
<br><span class="terminal-cmd"># Parse Extracted $MFT into Normalized CSV Timeline:</span>
MFTECmd.exe -f "E:\Triage\Target\C\$MFT" --csv "E:\Triage\Parsed" --csvf mft_timeline.csv
<br><span style="color: var(--emerald-pass);">// Extraction finished in 3m 42s. 14,820 artifacts parsed into mft_timeline.csv.</span>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Watch the speed of KAPE on screen. In less than four minutes, it mounted the volume shadow copy, extracted the MFT, prefetch, and registry hives, and MFTECmd generated our master timeline CSV.",
        "notes_pedagogy": "Demonstrate the KAPE CLI command syntax. Show that forensic triage is fast and automated."
    },

    # SLIDE 57: Guided Lab 6 Walkthrough
    {
        "title": "Guided Lab 6: Forensic Triage Acquisition",
        "day": "DAY 05",
        "module": "MOD-05: TRIAGE & FORENSICS",
        "session": "LAB-06",
        "ref": "Handbook Lab Manual 6",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-blue">HANDS-ON LABORATORY</div>
            <h2>Lab 6: Triage Acquisition & Timestomp Anomaly Detection</h2>
            <p>Workstation Target: <code>C:\\ThreatIntel_Labs\\Lab06_Forensics\\</code> | Time Allocated: 60 Minutes</p>
            
            <div class="grid-2" style="margin-top: 16px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 14px;">20-Step Lab Milestones</strong>
                <ul style="font-size: 12px; color: var(--text-secondary); margin-top: 8px; line-height: 1.8;">
                  <li><strong>Steps 1–5:</strong> Mount <code>evidence_disk.vhdx</code>, verify read-only write blocker.</li>
                  <li><strong>Steps 6–10:</strong> Execute KAPE CLI targeting <code>KapeTriage</code> compound target.</li>
                  <li><strong>Steps 11–15:</strong> Open <code>mft_timeline.csv</code> in Timeline Explorer, filter by <code>C:\\Windows\\Temp</code>.</li>
                  <li><strong>Steps 16–20:</strong> Locate timestomped binary, compare $SI vs $FN, export evidence hash.</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--neon-amber); font-size: 14px;">Lab Troubleshooting & Fallbacks</strong>
                <p style="font-size: 12px; margin-top: 8px;">
                  If Timeline Explorer crashes on 2-million-row CSV files, apply an initial memory filter via PowerShell:
                </p>
                <div class="terminal-buffer" style="margin: 8px 0; font-size: 11px;">
                  <div class="terminal-body">
<span class="terminal-cmd"># Filter CSV to Staging Folder Before Opening:</span>
Import-Csv mft_timeline.csv | Where-Object {$_.ParentPath -like "*Temp*"} | Export-Csv temp_filtered.csv -NoType
                  </div>
                </div>
                <div style="font-size: 11px; color: var(--text-muted);">Pass Criterion: Identified timestomped binary with $FN proof submitted.</div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Turn to your workstations. Open Lab 6. You have 60 minutes to extract the triage image and isolate the timestomped binary in Timeline Explorer. If the CSV is too large, use the PowerShell filter script.",
        "notes_pedagogy": "Guide students through Timeline Explorer column sorting ($SI vs $FN created times)."
    },

    # SLIDE 58: Day 5 Knowledge Check
    {
        "title": "Day 5 Knowledge Check",
        "day": "DAY 05",
        "module": "MOD-05: TRIAGE & FORENSICS",
        "session": "CHECKPOINT",
        "ref": "Trainer Handbook Section 5.7",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-amber">END-OF-DAY CHECKPOINT</div>
            <h2>Day 5 Knowledge Check: Forensic Integrity</h2>
            <p>Verify your understanding before our marathon Saturday Capstone.</p>
            
            <div class="interactive-decision-box" style="margin-top: 20px;">
              <strong style="color: #FFF; font-size: 15px;">Question for Pod 5 & Pod 6:</strong>
              <p style="font-size: 13px; color: var(--text-secondary); margin: 8px 0 14px 0;">
                During an active intrusion, a junior system administrator notices suspicious network activity and immediately pulls the power cord from the wall to stop the attack. What catastrophic forensic consequence just occurred?
              </p>
              <div class="decision-options">
                <button class="decision-btn" onclick="selectDecision(this, false, 'The hard drive remains intact, but the critical volatile evidence is lost.')">
                  <span>A) The hard drive was physically damaged and all non-volatile files are now permanently corrupted.</span>
                  <span>➔</span>
                </button>
                <button class="decision-btn" onclick="selectDecision(this, true, 'Correct! Pulling the power dumps volatile memory (RAM) instantly, permanently destroying running process trees, unencrypted ransomware keys, injected fileless malware DLLs, and live C2 network sockets.')">
                  <span>B) Volatile RAM was completely wiped, destroying running process trees, unencrypted keys, injected DLLs, and live C2 socket evidence.</span>
                  <span>➔</span>
                </button>
              </div>
              <div class="decision-explanation" style="margin-top: 12px; font-size: 13px; font-family: var(--font-mono);"></div>
            </div>
          </div>
        ''',
        "notes_say": "Pod 5 and Pod 6, what happened when the admin pulled the power cord? Exactly! Volatile RAM was wiped clean. Never pull the plug unless you are facing destructive disk wiper malware with zero other options.",
        "notes_pedagogy": "Reinforce the volatile memory destruction principle. Bridge to Day 6: the Saturday Capstone."
    }
]
