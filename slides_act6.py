# Slides Data: Act 6 (Day 6 - Phishing, Containment, SOAR & AeroGrid Capstone Simulation)
# Slides 59 to 72

ACT6_SLIDES = [
    # SLIDE 59: Day 6 Launch & Overview
    {
        "title": "Day 6 Launch & Capstone Marathon",
        "day": "DAY 06",
        "day_start": 6,
        "module": "MOD-06: CAPSTONE MARATHON",
        "session": "SES-06A / 06B / 06C (08:30 - 17:00)",
        "ref": "Course Syllabus Day 6; Handbook Chapter 7",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-red animate-pulse">DAY 06 CAPSTONE CRUCIBLE</div>
            <h2>Day 6: Advanced Triage, Containment, SOAR & AeroGrid APT Crisis</h2>
            <p>Saturday Marathon | Scheduled Net Teaching: 390 Minutes | 3 Sessions, 3 Guided Labs, 1 Enterprise Crisis</p>
            
            <div class="grid-3" style="margin-top: 16px;">
              <div class="cyber-card" style="border-top: 2px solid var(--cyber-cyan);">
                <div style="color: var(--cyber-cyan); font-family: var(--font-mono); font-size: 11px; font-weight: 700;">08:30 – 11:00 (150 MIN)</div>
                <div style="font-size: 15px; font-weight: 700; color: #FFF; margin: 6px 0;">SES-06A: Phishing Triage</div>
                <p style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
                  Dissecting email headers under RFC 5322, bypassing spoofing with SPF/DKIM/DMARC analysis, and weaponized CyberChef recipe pipelines.
                </p>
                <div style="margin-top: 10px; padding: 6px 10px; background: rgba(0,242,254,0.08); border-radius: 4px; font-family: var(--font-mono); font-size: 11px; color: var(--cyber-cyan);">
                  LAB-05: RFC 5322 & CyberChef
                </div>
              </div>
              
              <div class="cyber-card" style="border-top: 2px solid var(--neon-amber);">
                <div style="color: var(--neon-amber); font-family: var(--font-mono); font-size: 11px; font-weight: 700;">11:15 – 13:45 (150 MIN)</div>
                <div style="font-size: 15px; font-weight: 700; color: #FFF; margin: 6px 0;">SES-06B: Containment & SOAR</div>
                <p style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
                  Active Directory forest isolation, the delicate 10-hour KRBTGT double reset dance, and automated orchestration via Shuffle SOAR.
                </p>
                <div style="margin-top: 10px; padding: 6px 10px; background: rgba(255,179,0,0.08); border-radius: 4px; font-family: var(--font-mono); font-size: 11px; color: var(--neon-amber);">
                  LAB-07: Shuffle SOAR Playbooks
                </div>
              </div>
              
              <div class="cyber-card" style="border-top: 2px solid var(--alert-crimson);">
                <div style="color: var(--alert-crimson); font-family: var(--font-mono); font-size: 11px; font-weight: 700;">14:30 – 17:00 (150 MIN)</div>
                <div style="font-size: 15px; font-weight: 700; color: #FFF; margin: 6px 0;">SES-06C: AeroGrid Crisis</div>
                <p style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
                  Live tabletop crisis: State-sponsored APT infiltration of a regional power grid SCADA telemetry network. Triage under extreme operational pressure.
                </p>
                <div style="margin-top: 10px; padding: 6px 10px; background: rgba(255,75,75,0.08); border-radius: 4px; font-family: var(--font-mono); font-size: 11px; color: var(--alert-crimson);">
                  LAB-08: AeroGrid APT Defense
                </div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Welcome to Day 6 — Saturday morning in LH3. If you look around the room, nobody is yawning because today is what you have trained for all week. Today is the SOC Crucible. 450 minutes of pure operational execution. No theoretical introductions, no generic slides. We start with weaponized email triage, advance into Active Directory forest recovery and SOAR automation, and conclude with the AeroGrid APT tabletop crisis simulation. By 17:00 today, you are no longer students; you are certified operational defenders.",
        "notes_pedagogy": "Outline the strict time gates and high energy expectations for the Saturday marathon session."
    },

    # SLIDE 60: SES-06A Phishing Triage & RFC 5322
    {
        "title": "RFC 5322 Email Telemetry & Header Analysis",
        "day": "DAY 06",
        "module": "SES-06A: PHISHING TRIAGE",
        "session": "SES-06A (08:30 - 11:00)",
        "ref": "RFC 5322; RFC 7208; RFC 7489; Handbook Section 7.2",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">EMAIL TELEMETRY</div>
            <h2>SES-06A: Deconstructing RFC 5322 Email Telemetry</h2>
            <p>Never Trust the Display Name: Dissecting Mail Transfer Agent (MTA) Hops & Authentication Records</p>
            
            <div class="grid-2" style="margin-top: 16px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 14px;">MTA Hop Dissection: Received: Headers (Bottom-to-Top)</strong>
                <div class="terminal-buffer" style="margin-top: 8px; font-size: 11px;">
                  <div class="terminal-body" style="line-height: 1.4;">
<span style="color: var(--neon-amber);">Received:</span> from mail.attacker-infra.xyz (198.51.100.44)
  by mx.recipient-corp.com with ESMTP id ABC12345
  for &lt;cfo@recipient-corp.com&gt;; Sat, 31 Oct 2026 08:32:11 +0530
<span style="color: var(--cyber-cyan);">Authentication-Results:</span> mx.recipient-corp.com;
  spf=<span style="color: var(--alert-crimson); font-weight: bold;">fail</span> (sender IP is 198.51.100.44) smtp.mailfrom=executive-urgent.com;
  dkim=<span style="color: var(--alert-crimson); font-weight: bold;">none</span> (message not signed);
  dmarc=<span style="color: var(--alert-crimson); font-weight: bold;">fail</span> action=none header.from=recipient-corp.com;
<span style="color: var(--neon-amber);">From:</span> "Dr. K. Narayanan, Director" &lt;director@recipient-corp.com&gt;
<span style="color: var(--neon-amber);">Reply-To:</span> &lt;offboarding-payroll@attacker-infra.xyz&gt;
<span style="color: var(--neon-amber);">Subject:</span> URGENT: Q3 Executive Compensation Review & Policy Update
                  </div>
                </div>
                <div style="font-size: 11px; color: var(--text-muted); margin-top: 6px;">Key takeaway: Header analysis begins at the bottom-most <code>Received</code> line, establishing true originating MTA IP.</div>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--electric-blue); font-size: 14px;">The Authentication Triage Triad</strong>
                <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 10px;">
                  <div style="background: rgba(0,242,254,0.05); padding: 8px; border-left: 3px solid var(--cyber-cyan); border-radius: 4px;">
                    <strong style="color: var(--cyber-cyan); font-size: 12px;">SPF (Sender Policy Framework - RFC 7208)</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin: 2px 0;">DNS TXT record validating whether sending MTA IP is authorized to emit mail for envelope Return-Path.</p>
                  </div>
                  <div style="background: rgba(255,179,0,0.05); padding: 8px; border-left: 3px solid var(--neon-amber); border-radius: 4px;">
                    <strong style="color: var(--neon-amber); font-size: 12px;">DKIM (DomainKeys Identified Mail - RFC 6376)</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin: 2px 0;">Asymmetric cryptographic signature attached to email headers/body, verified against sender's public DNS key.</p>
                  </div>
                  <div style="background: rgba(255,75,75,0.05); padding: 8px; border-left: 3px solid var(--alert-crimson); border-radius: 4px;">
                    <strong style="color: var(--alert-crimson); font-size: 12px;">DMARC (Domain-based Auth & Conformance - RFC 7489)</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin: 2px 0;">Enforces alignment between Header-From and envelope domains, mandating policy action (<code>none</code>, <code>quarantine</code>, <code>reject</code>).</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Notice the email on screen. The display name says Dr. K. Narayanan, Director. To a distracted college employee or department head, this looks completely authentic. But look at the Received headers from bottom to top. The sending IP is 198.51.100.44, originating from attacker-infra.xyz. Look at Authentication-Results: SPF fail, DKIM none, DMARC fail! The Reply-To address redirects replies to offboarding-payroll@attacker-infra.xyz. Attackers exploit cognitive load; defenders rely on mathematical telemetry.",
        "notes_pedagogy": "Walk through the difference between RFC 5321 (Envelope From) and RFC 5322 (Header From) spoofing vulnerabilities."
    },

    # SLIDE 61: CyberChef Extraction Recipes
    {
        "title": "Weaponized CyberChef Pipelines for Phishing Triage",
        "day": "DAY 06",
        "module": "SES-06A: PHISHING TRIAGE",
        "session": "SES-06A (08:30 - 11:00)",
        "ref": "GCHQ CyberChef Documentation; Handbook Section 7.3",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-purple">INVESTIGATIVE TOOLKIT</div>
            <h2>Weaponized CyberChef Pipelines for Phishing Triage</h2>
            <p>Safe Defanging, Multilayer URL Decoding, Base64 Extraction, and XOR De-obfuscation</p>
            
            <div class="grid-2" style="margin-top: 16px;">
              <div class="cyber-card">
                <strong style="color: var(--purple-intel); font-size: 14px;">The Essential 4-Stage Defanging Pipeline</strong>
                <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 10px;">
                  <div style="background: rgba(0,242,254,0.05); padding: 8px; border-radius: 4px;">
                    <strong style="color: var(--cyber-cyan); font-size: 12px;">1. URL Decode (Multi-Pass)</strong>
                    <div style="font-size: 11px; color: var(--text-secondary);">Strips URL percent-encoding (<code>%68%74%74%70</code> &rarr; <code>http</code>) to expose raw obfuscated targets.</div>
                  </div>
                  <div style="background: rgba(79,172,254,0.05); padding: 8px; border-radius: 4px;">
                    <strong style="color: var(--electric-blue); font-size: 12px;">2. From Base64 (RFC 4648)</strong>
                    <div style="font-size: 11px; color: var(--text-secondary);">Decodes embedded Base64 strings hiding secondary payloads or hidden HTTP redirects.</div>
                  </div>
                  <div style="background: rgba(255,179,0,0.05); padding: 8px; border-radius: 4px;">
                    <strong style="color: var(--neon-amber); font-size: 12px;">3. Extract URLs / Extract IP Addresses</strong>
                    <div style="font-size: 11px; color: var(--text-secondary);">Uses RegEx parsers to isolate fully qualified domain names (FQDNs), IPv4 addresses, and URIs.</div>
                  </div>
                  <div style="background: rgba(0,230,118,0.05); padding: 8px; border-radius: 4px;">
                    <strong style="color: var(--emerald-pass); font-size: 12px;">4. Defang URL (Safety Guarantee)</strong>
                    <div style="font-size: 11px; color: var(--text-secondary);">Converts active links into safe tokens (<code>hxxps[://]evil[.]com/login</code>) preventing accidental clicks in tickets.</div>
                  </div>
                </div>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 14px;">Live Pipeline Demonstration (Input &rarr; Output)</strong>
                <div class="terminal-buffer" style="margin-top: 10px; font-size: 11px;">
                  <div class="terminal-body">
<span style="color: var(--text-muted);">// INPUT OBFUSCATED STRING:</span>
<span style="color: var(--neon-amber);">aHR0cHM6Ly9hdHRhY2tlci1pbmZyYS54eXovcGF5bG9hZC5leGU=</span>

<span style="color: var(--cyber-cyan);">&gt; CyberChef Recipe: From_Base64('A-Za-z0-9+/=',true,false)</span>
<span style="color: var(--cyber-cyan);">&gt; CyberChef Recipe: Defang_URL(true,true,true,'Valid domains and full URLs')</span>

<span style="color: var(--text-muted);">// OUTPUT DEFANGED IOC:</span>
<span style="color: var(--emerald-pass); font-weight: bold;">hxxps[://]attacker-infra[.]xyz/payload[.]exe</span>
                  </div>
                </div>
                <div style="margin-top: 10px; padding: 8px; background: rgba(255,75,75,0.08); border-left: 3px solid var(--alert-crimson); border-radius: 4px;">
                  <strong style="color: var(--alert-crimson); font-size: 11px;">Golden Safety Rule:</strong>
                  <div style="font-size: 11px; color: var(--text-secondary); margin-top: 2px;">Never share an un-defanged URL in Slack, Teams, or an incident ticket. One accidental misclick turns an investigation into an active breach.</div>
                </div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "CyberChef is the Swiss Army knife of every SOC analyst. When an attacker sends a phishing link, they do not just send http://evil.com. They embed it in SafeLinks, wrap it in percent encoding, Base64 encode the parameter, and append tracking tokens. In CyberChef, we construct multi-step processing pipelines. And notice Step 4: Defanging. If you post a raw malicious URL in your team chat, someone will accidentally click it while looking for coffee. Always defang before documenting!",
        "notes_pedagogy": "Emphasize the defensive habit of defanging IOCs in incident management ticketing systems."
    },

    # SLIDE 62: Guided Lab 5 Walkthrough
    {
        "title": "Guided Lab 5: Advanced Phishing Analysis",
        "day": "DAY 06",
        "module": "SES-06A: PHISHING TRIAGE",
        "session": "SES-06A (08:30 - 11:00)",
        "ref": "Lab 5 Manual; Handbook Section 7.4",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-blue">HANDS-ON LABORATORY</div>
            <h2>Lab 5: Advanced Phishing Triage & RFC 5322 Analysis</h2>
            <p>Workstation Target: <code>C:\\ThreatIntel_Labs\\Lab05_Phishing\\</code> | Time Allocated: 45 Minutes</p>
            
            <div class="grid-2" style="margin-top: 16px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 14px;">Lab Execution Protocol</strong>
                <ul style="font-size: 12px; color: var(--text-secondary); margin-top: 8px; line-height: 1.8;">
                  <li><strong>1. Dataset Acquisition:</strong> Open <code>phishing_sample_q3_bonus.eml</code> inside the REMnux analysis container.</li>
                  <li><strong>2. Header Parsing:</strong> Extract all <code>Received</code> hops, <code>Message-ID</code>, and SPF/DKIM verification tags using text editor.</li>
                  <li><strong>3. CyberChef Decoding:</strong> Load the HTML body parameter into CyberChef. Construct recipe: <em>URL Decode &rarr; From Base64 &rarr; Extract URLs</em>.</li>
                  <li><strong>4. OSINT Enrichment:</strong> Pivot discovered C2 domain into VirusTotal and URLhaus to confirm threat actor clustering.</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--emerald-pass); font-size: 14px;">Expected Deliverables & Evidence</strong>
                <div class="terminal-buffer" style="margin-top: 8px; font-size: 11px;">
                  <div class="terminal-body" style="line-height: 1.4;">
[+] Extracted Originating IP: 198.51.100.44 (AS9808 - Bulletproof Host)
[+] DMARC Policy Status: 'none' (Permitted Spoofed From-Header)
[+] Obfuscated Attachment Hash (SHA256):
    e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
[+] Extracted Credential Harvesting URI:
    hxxps[://]auth-portal-secure-update[.]com/login/redirect.php
[+] Recommended SOC Action: Immediate Firewall Block + Purge Inbox via M365 PowerShell
                  </div>
                </div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Lab 5 is your proving ground for email security. You have 45 minutes to analyze the phishing_sample_q3_bonus.eml file located on your lab desktop. Do not open the EML file in Outlook or an active mail client! Open it in a text editor or REMnux environment. Locate the true originating IP, build your CyberChef recipe, defang the target credential harvesting link, and produce your incident record. Time begins now.",
        "notes_pedagogy": "Supervise students to ensure no one double-clicks the attachment natively in Windows."
    },

    # SLIDE 63: SES-06B Containment Strategies
    {
        "title": "Strategic Containment & Blast Radius Mitigation",
        "day": "DAY 06",
        "module": "SES-06B: CONTAINMENT & SOAR",
        "session": "SES-06B (11:15 - 13:45)",
        "ref": "NIST SP 800-61r3 Section 3.3.1; Handbook Section 7.5",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-amber">INCIDENT CONTAINMENT</div>
            <h2>SES-06B: Strategic Containment & Blast Radius Mitigation</h2>
            <p>Balancing Operational Continuity vs. Threat Isolation Under NIST SP 800-61 Criteria</p>
            
            <div class="grid-3" style="margin-top: 16px;">
              <div class="cyber-card" style="border-top: 2px solid var(--cyber-cyan);">
                <div style="color: var(--cyber-cyan); font-weight: 700; font-size: 14px;">1. Network Isolation</div>
                <p style="font-size: 12px; color: var(--text-secondary); margin-top: 6px; line-height: 1.5;">
                  Severing IP connectivity at switch ports (802.1X quarantine VLAN) or host-based firewall isolation via EDR sensor.
                </p>
                <div style="font-size: 11px; color: var(--text-muted); margin-top: 8px;">
                  <strong>Trade-off:</strong> Preserves volatile memory forensics while severing active C2 command channels.
                </div>
              </div>
              
              <div class="cyber-card" style="border-top: 2px solid var(--neon-amber);">
                <div style="color: var(--neon-amber); font-weight: 700; font-size: 14px;">2. Identity Revocation</div>
                <p style="font-size: 12px; color: var(--text-secondary); margin-top: 6px; line-height: 1.5;">
                  Disabling compromised Active Directory accounts, revoking Kerberos TGT tickets, terminating active OAuth tokens, and forcing MFA resets.
                </p>
                <div style="font-size: 11px; color: var(--text-muted); margin-top: 8px;">
                  <strong>Trade-off:</strong> May alert adversary to SOC awareness; timing must be coordinated.
                </div>
              </div>
              
              <div class="cyber-card" style="border-top: 2px solid var(--alert-crimson);">
                <div style="color: var(--alert-crimson); font-weight: 700; font-size: 14px;">3. Endpoint Nullification</div>
                <p style="font-size: 12px; color: var(--text-secondary); margin-top: 6px; line-height: 1.5;">
                  Process suspension (freezing ransomware encryption threads without terminating memory space) and host-level null-routing.
                </p>
                <div style="font-size: 11px; color: var(--text-muted); margin-top: 8px;">
                  <strong>Trade-off:</strong> Prevents catastrophic data wiping while preserving volatile artifacts for forensic inspection.
                </div>
              </div>
            </div>
            
            <div class="cyber-card" style="margin-top: 14px; border-left: 3px solid var(--cyber-cyan);">
              <strong style="color: var(--cyber-cyan); font-size: 13px;">NIST SP 800-61 Section 3.3 Containment Criteria:</strong>
              <div style="font-size: 12px; color: var(--text-secondary); margin-top: 4px;">
                Before pulling any network cable, evaluate: (1) Potential damage/theft of assets, (2) Evidence preservation requirements, (3) Service availability impact, (4) Time and resources required, (5) Effectiveness of containment solution.
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Containment is the supreme balancing act in cybersecurity. If an attacker breaches the payroll database on the 31st of the month, and you immediately disconnect the servers, 10,000 employees do not get paid. The business executive will be at your SOC desk asking why you shut down operations without authorization. On the other hand, if you wait, the attacker exfiltrates all banking records. NIST SP 800-61 Section 3.3 mandates a structured containment strategy based on business impact, evidence preservation, and blast radius control.",
        "notes_pedagogy": "Contrast naive containment (pulling the plug) with professional defensive containment (EDR isolation, token revocation, process suspension)."
    },

    # SLIDE 64: Active Directory Forest Recovery: KRBTGT
    {
        "title": "Active Directory Recovery: The KRBTGT Double Reset",
        "day": "DAY 06",
        "module": "SES-06B: CONTAINMENT & SOAR",
        "session": "SES-06B (11:15 - 13:45)",
        "ref": "Microsoft Active Directory Forest Recovery Guide; Handbook Section 7.6",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-red">KERBEROS DEFENSE</div>
            <h2>Active Directory Recovery: The KRBTGT Double Reset</h2>
            <p>Eradicating Golden Ticket Persistence Without Inducing Enterprise Kerberos Outages</p>
            
            <div class="grid-2" style="margin-top: 16px;">
              <div class="cyber-card">
                <strong style="color: var(--alert-crimson); font-size: 14px;">The Golden Ticket Vulnerability (T1558.001)</strong>
                <p style="font-size: 12px; color: var(--text-secondary); margin-top: 6px; line-height: 1.5;">
                  When an adversary extracts the NTLM hash or AES-256 key of the <code>krbtgt</code> account (via DCSync / Mimikatz), they can forge arbitrary Kerberos Ticket Granting Tickets (TGTs) granting unlimited Domain Admin rights for up to 10 years.
                </p>
                <div class="terminal-buffer" style="margin-top: 8px; font-size: 11px;">
                  <div class="terminal-body">
<span style="color: var(--alert-crimson);">// Mimikatz DCSync Attack:</span>
lsadump::dcsync /domain:corp.local /user:krbtgt
<span style="color: var(--neon-amber);">Hash NTLM:</span> b28c413e3fa041b80d7c71d6438a2e05
<span style="color: var(--cyber-cyan);">Forged Golden Ticket Valid Until:</span> 2036-10-31
                  </div>
                </div>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--neon-amber); font-size: 14px;">The Mandatory 10-Hour Two-Phase Protocol</strong>
                <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 10px;">
                  <div style="background: rgba(255,179,0,0.05); padding: 8px; border-left: 3px solid var(--neon-amber); border-radius: 4px;">
                    <strong style="color: var(--neon-amber); font-size: 12px;">Step 1: First Reset & Forest Replication</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin: 2px 0;">Reset KRBTGT password once using Microsoft PowerShell script. Replicate across all Domain Controllers. Wait maximum Kerberos ticket lifetime (default: 10 hours) so legitimate tickets expire naturally.</p>
                  </div>
                  <div style="background: rgba(0,230,118,0.05); padding: 8px; border-left: 3px solid var(--emerald-pass); border-radius: 4px;">
                    <strong style="color: var(--emerald-pass); font-size: 12px;">Step 2: Second Reset & Complete Purge</strong>
                    <p style="font-size: 11px; color: var(--text-secondary); margin: 2px 0;">Reset KRBTGT password a second time. This invalidates the previous password history, permanently severing all adversary-forged Golden Tickets while preserving domain service continuity.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Why must we reset the KRBTGT password TWICE? This is a favorite question in senior cybersecurity interviews. Active Directory stores the current password and the previous password of the krbtgt account. If you reset it once, the attacker can still authenticate using their forged ticket because AD accepts tickets signed with the previous key! But if you reset it twice back-to-back immediately, all valid Kerberos tickets in your entire company become invalid instantly — users cannot log in, services fail, and the CEO cannot access email. You reset it once, wait 10 hours for replication and ticket expiry, and then reset it the second time. Precision engineering under pressure.",
        "notes_pedagogy": "Demystify the Kerberos authentication architecture and highlight why incident recovery requires rigorous scheduling."
    },

    # SLIDE 65: Shuffle SOAR Playbook Architecture
    {
        "title": "Shuffle SOAR: Orchestrating Automated Threat Response",
        "day": "DAY 06",
        "module": "SES-06B: CONTAINMENT & SOAR",
        "session": "SES-06B (11:15 - 13:45)",
        "ref": "Shuffle SOAR Documentation; Handbook Section 7.7",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-teal">SOAR AUTOMATION</div>
            <h2>Shuffle SOAR: Orchestrating Automated Threat Response</h2>
            <p>From Alert Webhook to Automated Firewall Null-Route in Under 850 Milliseconds</p>
            
            <div class="grid-2" style="margin-top: 16px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 14px;">Event-Driven SOAR Execution Flow (Sub-Second Response)</strong>
                <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 8px;">
                  <div style="background: rgba(0,242,254,0.05); padding: 6px 10px; border-left: 3px solid var(--cyber-cyan); font-size: 11px;">
                    <strong>1. Webhook Ingestion:</strong> Suricata alerts trigger an HTTP POST webhook containing EVE.json alert payload to Shuffle.
                  </div>
                  <div style="background: rgba(79,172,254,0.05); padding: 6px 10px; border-left: 3px solid var(--electric-blue); font-size: 11px;">
                    <strong>2. Threat Intel Query:</strong> Shuffle queries VirusTotal and MISP APIs concurrently to extract reputation score and malicious tags.
                  </div>
                  <div style="background: rgba(255,179,0,0.05); padding: 6px 10px; border-left: 3px solid var(--neon-amber); font-size: 11px;">
                    <strong>3. Conditional Logic:</strong> If VT Malicious &gt; 15 AND Confidence &gt; 80%, branch to containment workflow; else log to ticket queue.
                  </div>
                  <div style="background: rgba(255,75,75,0.05); padding: 6px 10px; border-left: 3px solid var(--alert-crimson); font-size: 11px;">
                    <strong>4. Automated Action:</strong> Dispatch API call to Edge Firewall to null-route C2 IP and isolate infected workstation via Wazuh EDR.
                  </div>
                </div>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--electric-blue); font-size: 14px;">Shuffle Execution Node Architecture</strong>
                <div class="terminal-buffer" style="margin-top: 8px; font-size: 11px;">
                  <div class="terminal-body">
<span style="color: var(--cyber-cyan);">{</span>
  <span style="color: var(--neon-amber);">"workflow_id"</span>: "wf-phish-contain-001",
  <span style="color: var(--neon-amber);">"execution_state"</span>: "SUCCESS",
  <span style="color: var(--neon-amber);">"execution_time_ms"</span>: 742,
  <span style="color: var(--neon-amber);">"nodes_executed"</span>: [
    {"node": "Webhook_Receiver", "status": "200 OK"},
    {"node": "MISP_Attribute_Lookup", "status": "MATCH_FOUND"},
    {"node": "Wazuh_Host_Quarantine", "status": "AGENT_ISOLATED"},
    {"node": "TheHive_Alert_Create", "status": "TICKET_#4891"}
  ]
<span style="color: var(--cyber-cyan);">}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "In modern SOC operations, human analysts cannot manually type firewall commands for 500 alerts an hour. If a human analyst takes 15 minutes to respond, ransomware encrypts 5,000 servers in that time. Shuffle is an open-source SOAR platform that connects your SIEM, threat intelligence, and endpoints through automated API execution nodes. An alert arrives, intel is checked, threshold is verified, and the endpoint is quarantined in 742 milliseconds. The analyst reviews the completed containment rather than scrambling to execute it.",
        "notes_pedagogy": "Explain the difference between manual SOC triage and Automated SOAR Playbooks."
    },

    # SLIDE 66: Guided Lab 7 Walkthrough
    {
        "title": "Guided Lab 7: Automated Threat Containment with Shuffle SOAR",
        "day": "DAY 06",
        "module": "SES-06B: CONTAINMENT & SOAR",
        "session": "SES-06B (11:15 - 13:45)",
        "ref": "Lab 7 Manual; Handbook Section 7.8",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-blue">HANDS-ON LABORATORY</div>
            <h2>Lab 7: Automated Threat Containment with Shuffle SOAR</h2>
            <p>Workstation Target: <code>http://localhost:3001</code> | Time Allocated: 45 Minutes</p>
            
            <div class="grid-2" style="margin-top: 16px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 14px;">Lab Workflow Milestones</strong>
                <ul style="font-size: 12px; color: var(--text-secondary); margin-top: 8px; line-height: 1.8;">
                  <li><strong>1. Access Shuffle UI:</strong> Navigate to <code>http://localhost:3001</code> in Chrome. Log in using training credentials.</li>
                  <li><strong>2. Build Playbook Nodes:</strong> Drag-and-drop Webhook node &rarr; Python Code Node (Payload Parse) &rarr; HTTP Request Node (Wazuh Isolation API).</li>
                  <li><strong>3. Test Execution:</strong> Transmit synthetic alert JSON using <code>curl -X POST http://localhost:3001/api/v1/hooks/...</code>.</li>
                  <li><strong>4. Verify Isolation:</strong> Confirm target workstation drops ping connectivity while agent maintains management heartbeat.</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--emerald-pass); font-size: 14px;">Lab Verification Script</strong>
                <div class="terminal-buffer" style="margin-top: 8px; font-size: 11px;">
                  <div class="terminal-body">
<span class="terminal-cmd"># Transmit synthetic C2 beacon alert to Shuffle Webhook:</span>
curl.exe -X POST http://localhost:3001/api/v1/hooks/webhook_c2_alert `
  -H "Content-Type: application/json" `
  -d '{"src_ip": "10.0.4.15", "alert": "Cobalt Strike Beacon", "severity": 1}'

<span class="terminal-cmd"># Expected Output from Wazuh Agent Check:</span>
<span style="color: var(--emerald-pass);">Agent 004 (WS-ACCOUNTING-02): Status [ISOLATED]</span>
<span style="color: var(--cyber-cyan);">Firewall Rule: Block Inbound/Outbound ALL except Manager (10.0.1.50)</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Lab 7 demonstrates automated containment. You will log into Shuffle SOAR at port 3001, configure an execution workflow, and send a synthetic Cobalt Strike beacon alert. Observe how Shuffle executes the nodes, parses the source IP, and calls the Wazuh API to isolate WS-ACCOUNTING-02 in real time. You have 45 minutes.",
        "notes_pedagogy": "Assist students in debugging JSON path parameters inside Shuffle node inputs (e.g., $exec.src_ip)."
    },

    # SLIDE 67: SES-06C AeroGrid Critical Infrastructure APT Simulation
    {
        "title": "SES-06C: AeroGrid Critical Infrastructure Tabletop Crisis",
        "day": "DAY 06",
        "module": "SES-06C: CAPSTONE CRISIS",
        "session": "SES-06C (14:30 - 17:00)",
        "ref": "AeroGrid Simulation Briefing; Handbook Section 7.9",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-red animate-pulse">CRISIS SIMULATION</div>
            <h2>SES-06C: AeroGrid Critical Infrastructure Tabletop Crisis</h2>
            <p>150 Minutes of High-Stakes Incident Response: Regional Power Grid SCADA Network Breach</p>
            
            <div class="grid-3" style="margin-top: 16px;">
              <div class="cyber-card" style="border-top: 2px solid var(--alert-crimson);">
                <div style="color: var(--alert-crimson); font-family: var(--font-mono); font-size: 11px; font-weight: 700;">PHASE 1 (14:30 - 15:15)</div>
                <div style="font-size: 14px; font-weight: 700; color: #FFF; margin: 4px 0;">Alert Triage & Incursion</div>
                <p style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
                  Multiple telemetry spikes from Substation 4 OT gateway. Abnormal Modbus TCP function codes and unauthorized VPN sessions from foreign ASNs.
                </p>
              </div>
              
              <div class="cyber-card" style="border-top: 2px solid var(--neon-amber);">
                <div style="color: var(--neon-amber); font-family: var(--font-mono); font-size: 11px; font-weight: 700;">PHASE 2 (15:15 - 16:00)</div>
                <div style="font-size: 14px; font-weight: 700; color: #FFF; margin: 4px 0;">Lateral Movement & Containment</div>
                <p style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
                  Adversary pivots from IT corporate network into OT engineering workstation. Mimikatz DCSync detected. Rapid containment decisions required.
                </p>
              </div>
              
              <div class="cyber-card" style="border-top: 2px solid var(--cyber-cyan);">
                <div style="color: var(--cyber-cyan); font-family: var(--font-mono); font-size: 11px; font-weight: 700;">PHASE 3 (16:00 - 17:00)</div>
                <div style="font-size: 14px; font-weight: 700; color: #FFF; margin: 4px 0;">Post-Mortem & Debrief</div>
                <p style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
                  Reconstructing full intrusion kill chain, compiling CERT-In mandatory reporting documentation, and presenting defense findings to Executive Board.
                </p>
              </div>
            </div>
            
            <div class="cyber-card" style="margin-top: 14px; border-left: 3px solid var(--alert-crimson);">
              <div style="display: flex; justify-content: space-between; align-items: center;">
                <strong style="color: var(--alert-crimson); font-size: 13px;">CRISIS RULES OF ENGAGEMENT:</strong>
                <span class="cyber-badge badge-red" style="font-size: 10px;">REAL-TIME PRESSURE</span>
              </div>
              <div style="font-size: 12px; color: var(--text-secondary); margin-top: 4px;">
                Every 20 minutes, new injects (simulated executive calls, press inquiries, and anomalous OT sensor alarms) will be introduced. Teams must maintain an immutable Master Incident Log.
              </div>
            </div>
          </div>
        ''',
        "notes_say": "It is 14:30. This is the ultimate crucible of our 6-day program: The AeroGrid Critical Infrastructure Tabletop Crisis. You are no longer students in LH3; you are the elite Incident Response Taskforce for AeroGrid Power Corporation, managing the electrical distribution network for southern India. At 14:12, automated alarms triggered in Substation 4. Turbine telemetry sensors are reporting abnormal Modbus command sequences. The attacker is inside the perimeter. Your mission: Triage, Contain, Eradicate, and Report. Let us begin.",
        "notes_pedagogy": "Set a serious, high-intensity operational tone to simulate a Tier-3 SOC emergency room."
    },

    # SLIDE 68: AeroGrid Scenario Briefing & Timeline
    {
        "title": "AeroGrid Breach Timeline: 72-Hour Infiltration Sequence",
        "day": "DAY 06",
        "module": "SES-06C: CAPSTONE CRISIS",
        "session": "SES-06C (14:30 - 17:00)",
        "ref": "MITRE ATT&CK for ICS; Handbook Section 7.10",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-cyan">ATTACK TIMELINE</div>
            <h2>AeroGrid Breach Timeline: 72-Hour Infiltration Sequence</h2>
            <p>Chronological Reconstruction of State-Sponsored APT Incursion via Spear-Phishing to SCADA Gateway</p>
            
            <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 14px;">
              <div class="cyber-card" style="border-left: 3px solid var(--cyber-cyan); padding: 8px 14px;">
                <div style="display: flex; justify-content: space-between;">
                  <strong style="color: var(--cyber-cyan); font-size: 13px;">T-72h (Wednesday 10:14) — Initial Access [T1566.001]</strong>
                  <span style="font-size: 11px; color: var(--text-muted); font-family: var(--font-mono);">SPEAR-PHISHING ATTACHMENT</span>
                </div>
                <p style="font-size: 12px; color: var(--text-secondary); margin: 2px 0;">Engineering contractor opens <code>Turbine_Spec_Update.xlsx</code> containing malicious macro executing Certutil download.</p>
              </div>
              
              <div class="cyber-card" style="border-left: 3px solid var(--electric-blue); padding: 8px 14px;">
                <div style="display: flex; justify-content: space-between;">
                  <strong style="color: var(--electric-blue); font-size: 13px;">T-48h (Thursday 16:30) — Credential Access & Discovery [T1003.001 / T1087]</strong>
                  <span style="font-size: 11px; color: var(--text-muted); font-family: var(--font-mono);">LSASS DUMP & AD ENUMERATION</span>
                </div>
                <p style="font-size: 12px; color: var(--text-secondary); margin: 2px 0;">Procdump invoked against <code>lsass.exe</code>. Service account credentials harvested; BloodHound run to map domain trusts.</p>
              </div>
              
              <div class="cyber-card" style="border-left: 3px solid var(--neon-amber); padding: 8px 14px;">
                <div style="display: flex; justify-content: space-between;">
                  <strong style="color: var(--neon-amber); font-size: 13px;">T-12h (Friday 22:15) — Lateral Movement to Dual-Homed Jump Box [T1021.001]</strong>
                  <span style="font-size: 11px; color: var(--text-muted); font-family: var(--font-mono);">RDP PIVOT TO OT JUMP HOST</span>
                </div>
                <p style="font-size: 12px; color: var(--text-secondary); margin: 2px 0;">Adversary uses stolen OT-Admin credentials to establish RDP session into Dual-Homed Jump Host bridging IT (10.0.1.0/24) and SCADA OT (192.168.100.0/24).</p>
              </div>
              
              <div class="cyber-card" style="border-left: 3px solid var(--alert-crimson); padding: 8px 14px;">
                <div style="display: flex; justify-content: space-between;">
                  <strong style="color: var(--alert-crimson); font-size: 13px;">T-0 (Saturday 14:12) — ICS/SCADA Manipulation [T0855]</strong>
                  <span style="font-size: 11px; color: var(--text-muted); font-family: var(--font-mono);">UNAUTHORIZED MODBUS COMMANDS</span>
                </div>
                <p style="font-size: 12px; color: var(--text-secondary); margin: 2px 0;">Adversary issues unauthorized Modbus Function Code 05 (Write Single Coil) attempting to trip distribution breakers.</p>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Examine this attack timeline carefully. Notice how the adversary operated over 72 hours. Initial compromise happened on Wednesday via a spear-phishing spreadsheet. Thursday night, they dumped LSASS. Friday night, when IT staff was off-duty, they pivoted through the dual-homed jump host into the OT network. And today, Saturday afternoon, they attempted to trigger Modbus commands to trip electrical breakers. This is not a random script kiddie; this is a patient, structured Advanced Persistent Threat.",
        "notes_pedagogy": "Walk through the Purdue Model of ICS/SCADA networks to show how attackers cross from Level 3 (IT) to Level 2/1 (OT)."
    },

    # SLIDE 69: Attack Path Analysis & Diamond Model
    {
        "title": "AeroGrid Attack Graph: Diamond Model & Attack Path Synthesis",
        "day": "DAY 06",
        "module": "SES-06C: CAPSTONE CRISIS",
        "session": "SES-06C (14:30 - 17:00)",
        "ref": "Handbook Section 7.11; CISA ICS Defense Guidelines",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-purple">INTELLIGENCE SYNTHESIS</div>
            <h2>AeroGrid Attack Graph: Diamond Model & Attack Path Synthesis</h2>
            <p>Synthesizing Adversary Infrastructure, Capabilities, Victims, and Systemic Vulnerabilities</p>
            
            <div class="grid-2" style="margin-top: 16px;">
              <div class="cyber-card">
                <strong style="color: var(--purple-intel); font-size: 14px;">Diamond Model Synthesis for AeroGrid Incursion</strong>
                <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 10px;">
                  <div style="background: rgba(255,75,75,0.05); padding: 8px; border-left: 3px solid var(--alert-crimson); border-radius: 4px;">
                    <strong style="color: var(--alert-crimson); font-size: 12px;">ADVERSARY:</strong>
                    <div style="font-size: 11px; color: var(--text-secondary);">UNC3886 / APT41 Hybrid Nexus (State-Sponsored Espionage)</div>
                  </div>
                  <div style="background: rgba(0,242,254,0.05); padding: 8px; border-left: 3px solid var(--cyber-cyan); border-radius: 4px;">
                    <strong style="color: var(--cyber-cyan); font-size: 12px;">CAPABILITY:</strong>
                    <div style="font-size: 11px; color: var(--text-secondary);">Certutil LOLBin, Cobalt Strike Beacon, Custom Modbus Scraper</div>
                  </div>
                  <div style="background: rgba(255,179,0,0.05); padding: 8px; border-left: 3px solid var(--neon-amber); border-radius: 4px;">
                    <strong style="color: var(--neon-amber); font-size: 12px;">INFRASTRUCTURE:</strong>
                    <div style="font-size: 11px; color: var(--text-secondary);">Compromised WordPress C2 Proxy &rarr; Bulletproof Fast-Flux IPs</div>
                  </div>
                  <div style="background: rgba(0,230,118,0.05); padding: 8px; border-left: 3px solid var(--emerald-pass); border-radius: 4px;">
                    <strong style="color: var(--emerald-pass); font-size: 12px;">VICTIM:</strong>
                    <div style="font-size: 11px; color: var(--text-secondary);">AeroGrid Substation 4 SCADA Telemetry & Power Distribution Network</div>
                  </div>
                </div>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--electric-blue); font-size: 14px;">Purdue Model Zone Breakdown</strong>
                <div style="font-size: 12px; line-height: 1.7; margin-top: 8px;">
                  <p><strong style="color: var(--cyber-cyan);">Level 4 (Enterprise IT):</strong> Email gateway, Active Directory, Workstations (Compromised T-72h).</p>
                  <p><strong style="color: var(--electric-blue);">Level 3.5 (DMZ):</strong> Dual-Homed Jump Box, Remote Access Gateway (Pivoted T-12h).</p>
                  <p><strong style="color: var(--neon-amber);">Level 3 (OT Operations):</strong> SCADA HMI, Historian, Engineering Workstation (Breached T-4h).</p>
                  <p><strong style="color: var(--alert-crimson);">Level 1/0 (Field Devices):</strong> PLCs, RTUs, Circuit Breakers (Target of T-0 Modbus attack).</p>
                </div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Notice how the Diamond Model we learned on Day 1 now perfectly organizes our Day 6 crisis findings. The adversary is an APT espionage nexus. Their capability combines Windows Living-off-the-Land binaries with custom OT Modbus manipulation tools. Their infrastructure relies on fast-flux proxy nodes. And our victim is Substation 4. As an incident commander, this structured view allows you to brief both technical responders and executive directors with complete clarity.",
        "notes_pedagogy": "Reinforce the Purdue Model layers and show how IT-OT convergence increases attack surfaces."
    },

    # SLIDE 70: Guided Lab 8 Walkthrough
    {
        "title": "Guided Lab 8: AeroGrid Enterprise Containment",
        "day": "DAY 06",
        "module": "SES-06C: CAPSTONE CRISIS",
        "session": "SES-06C (14:30 - 17:00)",
        "ref": "Lab 8 Manual; Handbook Section 7.12",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-blue">HANDS-ON LABORATORY</div>
            <h2>Lab 8: AeroGrid Enterprise Multi-Stage Containment</h2>
            <p>Workstation Target: <code>C:\\ThreatIntel_Labs\\Lab08_AeroGrid\\</code> | Time Allocated: 60 Minutes</p>
            
            <div class="grid-2" style="margin-top: 16px;">
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 14px;">Emergency Response Checklist</strong>
                <ul style="font-size: 12px; color: var(--text-secondary); margin-top: 8px; line-height: 1.8;">
                  <li><strong>1. OT Air-Gap Severance:</strong> Issue emergency firewall rule blocking all traffic crossing IT-OT DMZ (Port 502 Modbus & Port 3389 RDP).</li>
                  <li><strong>2. Memory Capture:</strong> Run winpmem against Dual-Homed Jump Host before terminating connections.</li>
                  <li><strong>3. Identity Lockout:</strong> Disable compromised contractor accounts; initiate Phase 1 of KRBTGT 10-hour reset.</li>
                  <li><strong>4. Evidence Preservation:</strong> Package KAPE triage containers and upload to secure incident storage with cryptographic hash verification.</li>
                </ul>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--emerald-pass); font-size: 14px;">Live Triage Verification Command</strong>
                <div class="terminal-buffer" style="margin-top: 8px; font-size: 11px;">
                  <div class="terminal-body">
<span class="terminal-cmd"># 1. Emergency OT Severance Rule:</span>
New-NetFirewallRule -DisplayName "EMERGENCY_OT_ISOLATE" `
  -Direction Outbound -RemoteAddress 192.168.100.0/24 -Action Block

<span class="terminal-cmd"># 2. Verify OT Modbus Gateway Ping Drops:</span>
Test-NetConnection -ComputerName 192.168.100.10 -Port 502
<span style="color: var(--alert-crimson);">TcpTestSucceeded : False (BLOCKED BY FIREWALL RULE)</span>

<span class="terminal-cmd"># 3. Verify Active Directory KRBTGT Password Age:</span>
(Get-ADUser krbtgt -Properties PasswordLastSet).PasswordLastSet
<span style="color: var(--emerald-pass);">Output: 31-Oct-2026 15:42:19 (RESET PHASE 1 ACTIVE)</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Lab 8 is your final practical exam. You have 60 minutes. Execute the emergency containment protocol: block the DMZ bridge, freeze the jump host, initiate KRBTGT reset phase 1, and verify that Modbus command execution ceases. If your firewall rule fails, the simulated turbine simulator will trip and the scoreboard will log a simulated grid blackout. Coordinate with your team partners. Go!",
        "notes_pedagogy": "Create controlled tension in the room while providing technical guidance on firewall and Active Directory PowerShell cmdlets."
    },

    # SLIDE 71: Executive Incident Briefing: The Post-Mortem
    {
        "title": "The Post-Mortem Defense Plan & Executive Briefing",
        "day": "DAY 06",
        "module": "SES-06C: CAPSTONE CRISIS",
        "session": "SES-06C (14:30 - 17:00)",
        "ref": "CERT-In Cyber Security Directions 2022; Handbook Section 7.13",
        "content": '''
          <div style="text-align: left;">
            <div class="cyber-badge badge-amber">EXECUTIVE GOVERNANCE</div>
            <h2>The Post-Mortem Defense Plan & Executive Briefing</h2>
            <p>Translating Raw Telemetry into Business Impact, Root Causes, and CERT-In Regulatory Filings</p>
            
            <div class="grid-2" style="margin-top: 16px;">
              <div class="cyber-card">
                <strong style="color: var(--neon-amber); font-size: 14px;">Executive 1-Page Briefing Structure</strong>
                <div style="font-size: 12px; line-height: 1.6; margin-top: 8px;">
                  <p><strong>1. Executive Summary:</strong> What happened, when detected, operational status (Grid operational; zero physical damage sustained).</p>
                  <p><strong>2. Root Cause Analysis (RCA):</strong> Spear-phishing macro on unmanaged contractor laptop; absence of MFA on internal IT-OT jump host.</p>
                  <p><strong>3. Business & Financial Impact:</strong> Containment completed within 142 minutes; customer outage averted; zero regulatory penalties.</p>
                  <p><strong>4. Strategic Remediation:</strong> Enforce FIDO2 hardware keys, micro-segment OT subnet with unidirectional data diodes, deploy SOAR playbooks.</p>
                </div>
              </div>
              
              <div class="cyber-card">
                <strong style="color: var(--cyber-cyan); font-size: 14px;">CERT-In Mandatory Reporting Compliance</strong>
                <div class="terminal-buffer" style="margin-top: 8px; font-size: 11px;">
                  <div class="terminal-body">
<span style="color: var(--cyber-cyan);">// CERT-In 6-Hour Incident Notification Summary:</span>
Incident Ref: CERT-IN-2026-AEROGRID-0891
Reporting Entity: AeroGrid Power Distribution Ltd.
Incident Category: Unauthorized Access to Critical Infrastructure / ICS
Time of Detection: 31-Oct-2026 14:12 IST
Time of Reporting: 31-Oct-2026 16:30 IST (Within 6-hour statutory window)
Containment Status: Full Network Severance & Account Revocation Completed
Impact Assessment: Distribution Telemetry Secured; No Blackout Incurred
                  </div>
                </div>
              </div>
            </div>
          </div>
        ''',
        "notes_say": "Technical skill without the ability to communicate with leadership is useless. The Board of Directors does not care what Sysmon Event ID 10 is. They want to know: Did the lights go out? Was customer data stolen? Are we in legal compliance with CERT-In 6-hour mandatory reporting regulations? And what will prevent this from happening again on Monday? Presenting your post-mortem with clarity and confidence establishes your authority as a cybersecurity professional.",
        "notes_pedagogy": "Emphasize the Indian regulatory landscape, including CERT-In cyber crisis management rules."
    },

    # SLIDE 72: Course Graduation & SOC Transition
    {
        "title": "Mission Accomplished: Operational SOC Transition",
        "day": "DAY 06",
        "module": "COURSE GRADUATION",
        "session": "FINAL COMMENCEMENT (17:00)",
        "ref": "Handbook Epilogue; Course Evaluation Protocol",
        "content": '''
          <div style="text-align: center; padding: 20px 10px;">
            <div class="cyber-badge badge-teal animate-pulse" style="margin-bottom: 14px;">PROGRAM STATUS: 100% COMPLETED (LH3 - 4TH FLOOR)</div>
            <h1 style="font-size: 2.4em; margin-bottom: 10px;">From Classroom to Cyber Defense Operations</h1>
            <p style="font-size: 1.1em; color: var(--text-secondary); max-width: 820px; margin: 0 auto 24px auto;">
              You have mastered the entire operational lifecycle: Threat Intelligence, Indicator Engineering, ATT&CK TTP Mapping, Telemetry Correlation, Forensic Volatility, Automated Containment, and Executive Governance.
            </p>
            
            <div class="grid-3" style="max-width: 920px; margin: 0 auto; text-align: left;">
              <div class="cyber-card" style="border-top: 2px solid var(--cyber-cyan);">
                <strong style="color: var(--cyber-cyan); font-size: 14px;">Continuous Curiosity</strong>
                <p style="font-size: 12px; color: var(--text-secondary); margin-top: 6px; line-height: 1.5;">
                  Tools change every 18 months; foundational principles (RFC protocols, volatility, telemetry correlation) last a lifetime.
                </p>
              </div>
              
              <div class="cyber-card" style="border-top: 2px solid var(--neon-amber);">
                <strong style="color: var(--neon-amber); font-size: 14px;">Rigorous Evidence</strong>
                <p style="font-size: 12px; color: var(--text-secondary); margin-top: 6px; line-height: 1.5;">
                  Never guess. Verify every hypothesis with raw event logs, cryptographic hashes, and structured analysis.
                </p>
              </div>
              
              <div class="cyber-card" style="border-top: 2px solid var(--emerald-pass);">
                <strong style="color: var(--emerald-pass); font-size: 14px;">Defenders Unite</strong>
                <p style="font-size: 12px; color: var(--text-secondary); margin-top: 6px; line-height: 1.5;">
                  Attackers share infrastructure and exploits; defenders must share intelligence, playbooks, and solidarity.
                </p>
              </div>
            </div>
            
            <div style="margin-top: 28px; font-family: var(--font-mono); font-size: 13px; color: var(--text-muted);">
              "In cybersecurity, we don't rise to the level of our hopes; we fall to the level of our training."
            </div>
          </div>
        ''',
        "notes_say": "Please give yourselves a massive round of applause. In 6 days, you have covered 26.5 hours of rigorous technical training. You configured STIX/TAXII graphs, mapped ATT&CK Navigator layers, authored Sigma rules, extracted volatile memory with KAPE, built automated SOAR playbooks, and defended a critical infrastructure power grid from an advanced threat actor. Remember: the tools will evolve, but your disciplined mindset — verifying evidence, understanding protocols, and standing guard — will define your career. It has been an absolute honor being your trainer this week. Thank you, and welcome to the ranks of operational defenders!",
        "notes_pedagogy": "Conclude with high encouragement, congratulate students individually, and open the floor for final feedback and certificate distribution."
    }
]
