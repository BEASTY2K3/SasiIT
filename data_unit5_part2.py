"""
Unit 5 Data Part 2: Topics 78 to 84 (7 Topics)
Adware, Spyware, Wi-Fi Traps, Antivirus, Firewalls, Phishing & Pharming
"""

unit5_part2_topics = [
    # 78
    {
        "num": "78",
        "index": "29",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Malware Threats",
        "title": "Adware & Browser Hijacking: Pop-ups & Defenses",
        "subtitle": "How bundled software installers sneak adware onto your PC, force malicious search redirects, and why uBlock Origin is the definitive defense.",
        "analogy_title": "Billboards Glued Over Your Car's Windshield",
        "analogy_text": "Imagine driving down a road and someone <strong>plasters advertising billboards directly across your front windshield</strong>, while simultaneously yanking the steering wheel so you take an exit towards a shady shopping mall. That is what browser hijackers do to Chrome.",
        "steps": [
            ("1", "Deceptive Bundled Installers", "Freeware installers pre-check hidden boxes to install toolbars and search engines alongside the real app."),
            ("2", "Search Engine Redirection", "Typing a query redirects you away from Google to shady ad-infested search portals that track your keystrokes."),
            ("3", "Open-Source Ad Blocking", "Installing uBlock Origin cuts out tracking scripts, malicious pop-under ads, and auto-playing video banners.")
        ],
        "rule": "Installation Discipline: Always choose 'Custom Installation' or 'Advanced Installation' when installing software, and uncheck all optional companion programs!",
        "fig_title": "Figure 29 &bull; Deceptive Bundler vs. Clean Custom Installation",
        "takeaway": "Key Takeaway: Never click 'Express Install'; uncheck sponsored bloatware; use uBlock Origin.",
        "notes": "Warn students against commercial ad blockers that accept payments from advertisers to whitelist ads.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Left: Deceptive Express Install -->
  <rect x="30" y="45" width="250" height="270" rx="10" fill="#FEF2F2" stroke="#EF4444" stroke-width="2"/>
  <rect x="45" y="60" width="130" height="24" rx="4" fill="#FEE2E2"/>
  <text x="110" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">&cross; EXPRESS INSTALL</text>
  <text x="45" y="105" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#B91C1C">The Adware Trap</text>
  <rect x="45" y="125" width="220" height="110" rx="6" fill="#FFFFFF" stroke="#FECACA"/>
  <text x="55" y="150" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">&check; Install Video Player (Wanted)</text>
  <text x="55" y="170" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">&check; [Pre-checked] Shady Search Toolbar</text>
  <text x="55" y="190" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">&check; [Pre-checked] PC Optimizer Cleaner</text>
  <text x="55" y="210" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">&check; [Pre-checked] Set homepage to AdSite</text>
  <rect x="45" y="245" width="220" height="50" rx="6" fill="#FEE2E2"/>
  <text x="155" y="268" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#B91C1C" text-anchor="middle">Result: Hijacked Chrome</text>
  <text x="155" y="284" font-family="system-ui, sans-serif" font-size="8.5" fill="#7F1D1D" text-anchor="middle">50 pop-up ads per hour &bull; Sluggish PC</text>
  <!-- Right: Clean Custom Installation -->
  <rect x="320" y="45" width="250" height="270" rx="10" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
  <rect x="335" y="60" width="130" height="24" rx="4" fill="#D1FAE5"/>
  <text x="400" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#065F46" text-anchor="middle">&check; CUSTOM SETUP</text>
  <text x="335" y="105" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#047857">The Smart Protocol</text>
  <rect x="335" y="125" width="220" height="110" rx="6" fill="#FFFFFF" stroke="#A7F3D0"/>
  <text x="345" y="150" font-family="system-ui, sans-serif" font-size="9" fill="#047857">&check; Install Video Player Only</text>
  <text x="345" y="170" font-family="system-ui, sans-serif" font-size="9" fill="#64748B">&square; [UNCHECKED] Shady Search Toolbar</text>
  <text x="345" y="190" font-family="system-ui, sans-serif" font-size="9" fill="#64748B">&square; [UNCHECKED] PC Optimizer Cleaner</text>
  <text x="345" y="210" font-family="system-ui, sans-serif" font-size="9" fill="#64748B">&square; [UNCHECKED] Change default homepage</text>
  <rect x="335" y="245" width="220" height="50" rx="6" fill="#D1FAE5"/>
  <text x="445" y="268" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#065F46" text-anchor="middle">Result: Clean &amp; Fast</text>
  <text x="445" y="284" font-family="system-ui, sans-serif" font-size="8.5" fill="#047857" text-anchor="middle">uBlock Origin blocks 100% of malicious scripts</text>
</svg>"""
    },
    # 79
    {
        "num": "79",
        "index": "30",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Surveillance Threats",
        "title": "Spyware & Keyloggers: Hardware vs. Software",
        "subtitle": "How invisible surveillance software intercepts passwords and credit cards, and how Pegasus demonstrates zero-click state surveillance.",
        "analogy_title": "A Hidden Micro-Camera Behind Your Bathroom Mirror",
        "analogy_text": "Unlike ransomware (which screams loudly for attention), <strong>spyware is designed to be 100% invisible</strong>. It is like an enemy planting a hidden micro-camera behind your mirror, watching every PIN you enter and recording every private conversation for months without your knowledge.",
        "steps": [
            ("1", "Hardware Keyloggers", "A tiny USB dongle plugged between keyboard and PC. Captures raw electrical signals &mdash; 100% invisible to antivirus!"),
            ("2", "Software Keyloggers", "Hooks into the operating system keyboard API, writing every keystroke into an encrypted log file uploaded to the hacker."),
            ("3", "Pegasus Zero-Click Spyware", "Transmitted via an invisible WhatsApp call. Requires zero clicking from the victim; silently weaponizes microphone and GPS.")
        ],
        "rule": "Lab PC Inspection: Whenever you use a public computer in a cyber cafe or bank, look behind the CPU case! If a strange black adapter is plugged between your keyboard cable and the USB port, do not type passwords.",
        "fig_title": "Figure 30 &bull; Hardware Keylogger Dongle vs. Software API Hook",
        "takeaway": "Key Takeaway: Check physical USB ports; use Password Managers (they auto-fill without typing keystrokes).",
        "notes": "Highlight that Password Managers defeat keyloggers because passwords are not manually typed on keyboards.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Hardware Keylogger (Left) -->
  <rect x="30" y="45" width="250" height="270" rx="10" fill="#FFFFFF" stroke="#D97706" stroke-width="2"/>
  <rect x="45" y="60" width="140" height="24" rx="4" fill="#FEF3C7"/>
  <text x="115" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#B45309" text-anchor="middle">HARDWARE KEYLOGGER</text>
  <text x="45" y="105" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#0F172A">Physical USB Adapter</text>
  <rect x="45" y="125" width="220" height="100" rx="6" fill="#F8FAFC" stroke="#FDE68A"/>
  <!-- Physical dongle diagram -->
  <rect x="65" y="145" width="60" height="25" rx="3" fill="#334155"/>
  <text x="95" y="161" font-family="monospace" font-size="8" fill="#FFFFFF" text-anchor="middle">KEYBOARD</text>
  <rect x="135" y="147" width="40" height="20" rx="2" fill="#D97706"/>
  <text x="155" y="160" font-family="monospace" font-size="7.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">DONGLE</text>
  <rect x="185" y="145" width="60" height="25" rx="3" fill="#0F172A"/>
  <text x="215" y="161" font-family="monospace" font-size="8" fill="#FFFFFF" text-anchor="middle">PC CASE</text>
  <text x="155" y="195" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#DC2626" text-anchor="middle">&cross; 100% Invisible to Antivirus!</text>
  <text x="155" y="210" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Captures raw physical electrical keystrokes</text>
  <rect x="45" y="240" width="220" height="55" rx="6" fill="#FFFBEB"/>
  <text x="155" y="262" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#B45309" text-anchor="middle">Defense: Physical Inspection</text>
  <text x="155" y="278" font-family="system-ui, sans-serif" font-size="8.5" fill="#78350F" text-anchor="middle">Check back of public computers before typing</text>
  <!-- Software Keylogger (Right) -->
  <rect x="320" y="45" width="250" height="270" rx="10" fill="#FFFFFF" stroke="#EF4444" stroke-width="2"/>
  <rect x="335" y="60" width="140" height="24" rx="4" fill="#FEE2E2"/>
  <text x="405" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">SOFTWARE KEYLOGGER</text>
  <text x="335" y="105" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#0F172A">OS Memory Hooks</text>
  <rect x="335" y="125" width="220" height="100" rx="6" fill="#F8FAFC" stroke="#FECACA"/>
  <text x="345" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">&bull; Hooks into Windows User32.dll API</text>
  <text x="345" y="165" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">&bull; Records bank passwords &amp; OTP entries</text>
  <text x="345" y="185" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">&bull; Takes silent screenshots of screen</text>
  <text x="345" y="205" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">&bull; Uploads logs to hacker every 10 mins</text>
  <rect x="335" y="240" width="220" height="55" rx="6" fill="#FEF2F2"/>
  <text x="445" y="262" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#991B1B" text-anchor="middle">Defense: Password Managers</text>
  <text x="445" y="278" font-family="system-ui, sans-serif" font-size="8.5" fill="#7F1D1D" text-anchor="middle">Auto-fill bypasses keyboard keystroke logging</text>
</svg>"""
    },
    # 80
    {
        "num": "80",
        "index": "31",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Network Snooping",
        "title": "Wi-Fi Snooping & Evil Twin Traps: VPN Shielding",
        "subtitle": "How hackers capture unencrypted packets in coffee shops using rogue Wi-Fi hotspots, and how a VPN creates an impenetrable cryptographic tunnel.",
        "analogy_title": "Megaphone in a Public Hall vs. Soundproof Tube",
        "analogy_text": "Using public Wi-Fi without protection is like <strong>shouting your bank passwords through a megaphone in a crowded bus stand</strong> &mdash; anyone holding a radio receiver can hear every word. <strong>A VPN is an impenetrable soundproof tube</strong> connecting you directly to your bank: outsiders see only scrambled static.",
        "steps": [
            ("1", "The Evil Twin Attack", "An attacker sets up a rogue hotspot named `Free_Airport_WiFi`. Devices connect automatically, routing traffic through the attacker's laptop."),
            ("2", "Packet Sniffing (Wireshark)", "The attacker captures unencrypted web credentials, visited URLs, and unencrypted session cookies."),
            ("3", "VPN Encrypted Tunnel", "A Virtual Private Network wraps all network packets in military-grade AES-256 encryption between you and the VPN gateway.")
        ],
        "rule": "Public Wi-Fi Protocol: Never perform banking transactions or log into university portals on open hotel/railway Wi-Fi unless your VPN is actively turned ON.",
        "fig_title": "Figure 31 &bull; Public Wi-Fi Sniffing vs. Encrypted VPN Tunnel",
        "takeaway": "Key Takeaway: Public Wi-Fi is open broadcast; a VPN wraps all data in an unbreakable cryptographic tunnel.",
        "notes": "Demonstrate the difference between HTTP (open text in Wireshark) and HTTPS / VPN (encrypted ciphertext).",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Top: Open Wi-Fi Trap -->
  <rect x="30" y="35" width="540" height="135" rx="10" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5"/>
  <rect x="45" y="45" width="150" height="20" rx="3" fill="#FEE2E2"/>
  <text x="120" y="59" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#991B1B" text-anchor="middle">&cross; UNPROTECTED PUBLIC WI-FI</text>
  <!-- Device -> Hacker Router -> Internet -->
  <circle cx="80" cy="105" r="22" fill="#FFFFFF" stroke="#0F172A"/>
  <text x="80" y="109" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Laptop</text>
  <line x1="105" y1="105" x2="260" y2="105" stroke="#DC2626" stroke-width="3" stroke-dasharray="4,4"/>
  <rect x="260" y="80" width="100" height="50" rx="6" fill="#DC2626"/>
  <text x="310" y="102" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#FFFFFF" text-anchor="middle">EVIL TWIN</text>
  <text x="310" y="117" font-family="system-ui, sans-serif" font-size="8" fill="#FEE2E2" text-anchor="middle">Hacker Snooper</text>
  <line x1="360" y1="105" x2="490" y2="105" stroke="#DC2626" stroke-width="3"/>
  <circle cx="515" cy="105" r="22" fill="#FFFFFF" stroke="#0F172A"/>
  <text x="515" y="109" font-family="system-ui, sans-serif" font-size="9" font-weight="700" text-anchor="middle">Internet</text>
  <text x="300" y="152" font-family="system-ui, sans-serif" font-size="9" font-weight="600" fill="#DC2626" text-anchor="middle">Packets Sniffed in Plaintext: Passwords &amp; Session Cookies Exposed!</text>
  <!-- Bottom: Encrypted VPN Tunnel -->
  <rect x="30" y="185" width="540" height="145" rx="10" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
  <rect x="45" y="195" width="150" height="20" rx="3" fill="#D1FAE5"/>
  <text x="120" y="209" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#065F46" text-anchor="middle">&check; ENCRYPTED VPN TUNNEL</text>
  <circle cx="80" cy="255" r="22" fill="#FFFFFF" stroke="#059669"/>
  <text x="80" y="259" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#059669" text-anchor="middle">Laptop</text>
  <!-- Solid Green Encrypted Pipe -->
  <rect x="110" y="242" width="370" height="26" rx="13" fill="#10B981"/>
  <text x="295" y="259" font-family="monospace" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">AES-256 ENCRYPTED MILITARY TUNNEL</text>
  <circle cx="515" cy="255" r="22" fill="#FFFFFF" stroke="#059669"/>
  <text x="515" y="259" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#059669" text-anchor="middle">Bank/Net</text>
  <text x="300" y="305" font-family="system-ui, sans-serif" font-size="9" font-weight="600" fill="#047857" text-anchor="middle">Outcome: External hackers see only scrambled, unbreakable mathematical noise!</text>
</svg>"""
    },
    # 81
    {
        "num": "81",
        "index": "32",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Endpoint Defense",
        "title": "Antivirus Defense: Signatures, Heuristics & Sandbox",
        "subtitle": "How modern antivirus suites detect threats, why running two antivirus engines freezes Windows, and how behavioral sandboxing isolates zero-day malware.",
        "analogy_title": "Airport Security with Threat Database & Quarantine Room",
        "analogy_text": "Antivirus software is like an <strong>airport security checkpoint</strong>. Signature scanning compares baggage against known terrorist mugshots. Heuristics notices suspicious nervous behavior. If an unknown substance is found, it is taken into an <strong>airtight explosion-proof chamber (Sandbox)</strong> to detonate safely away from passengers.",
        "steps": [
            ("1", "Signature Matching (Known Threats)", "Compares file hash against a cloud database of 500 million cataloged malware signatures in milliseconds."),
            ("2", "Heuristic Behavioral Analysis", "Looks for suspicious code actions (e.g. attempting to modify the Windows Master Boot Record or inject into explorer.exe)."),
            ("3", "Virtual Sandbox Detonation", "Executes suspicious programs inside an isolated virtual bubble to observe what they try to do before letting them touch your real files.")
        ],
        "rule": "System Hygiene Warning: NEVER install two antivirus suites simultaneously (e.g. McAfee + Norton)! They conflict over the same Windows kernel memory hooks, causing severe system freezes and crashes.",
        "fig_title": "Figure 32 &bull; Three-Stage Antivirus Inspection Funnel",
        "takeaway": "Key Takeaway: Microsoft Defender + uBlock Origin is sufficient; never install dual conflicting antivirus software.",
        "notes": "Explain why built-in Microsoft Defender on Windows 10/11 is ranked among the world's best enterprise antivirus engines.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- 3 Stages of Defense Funnel -->
  <!-- Stage 1 -->
  <rect x="25" y="45" width="165" height="270" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
  <rect x="40" y="60" width="70" height="24" rx="4" fill="#E0F2FE"/>
  <text x="75" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0369A1" text-anchor="middle">TIER 1</text>
  <text x="40" y="110" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#0F172A">SIGNATURES</text>
  <text x="40" y="128" font-family="system-ui, sans-serif" font-size="9" fill="#64748B">Known Threat Hash</text>
  <circle cx="107" cy="180" r="32" fill="#F0F9FF" stroke="#0284C7" stroke-width="2"/>
  <text x="107" y="177" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#0369A1" text-anchor="middle">SHA-256</text>
  <text x="107" y="193" font-family="system-ui, sans-serif" font-size="8" fill="#64748B" text-anchor="middle">Instant Match</text>
  <text x="40" y="245" font-family="system-ui, sans-serif" font-size="9" fill="#475569">Scans 500M known virus fingerprints in 0.05 seconds</text>
  <!-- Arrow 1 -->
  <line x1="190" y1="180" x2="215" y2="180" stroke="#0284C7" stroke-width="3" stroke-linecap="round"/>
  <!-- Stage 2 -->
  <rect x="215" y="45" width="170" height="270" rx="10" fill="#FFFFFF" stroke="#D97706" stroke-width="1.5"/>
  <rect x="230" y="60" width="70" height="24" rx="4" fill="#FEF3C7"/>
  <text x="265" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#B45309" text-anchor="middle">TIER 2</text>
  <text x="230" y="110" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#0F172A">HEURISTICS</text>
  <text x="230" y="128" font-family="system-ui, sans-serif" font-size="9" fill="#64748B">Behavioral Analysis</text>
  <circle cx="300" cy="180" r="32" fill="#FFFBEB" stroke="#D97706" stroke-width="2"/>
  <text x="300" y="177" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#B45309" text-anchor="middle">AI RULES</text>
  <text x="300" y="193" font-family="system-ui, sans-serif" font-size="8" fill="#78350F" text-anchor="middle">Pattern Detect</text>
  <text x="230" y="245" font-family="system-ui, sans-serif" font-size="9" fill="#475569">Detects brand-new modified variants exhibiting suspicious behavior</text>
  <!-- Arrow 2 -->
  <line x1="385" y1="180" x2="410" y2="180" stroke="#D97706" stroke-width="3" stroke-linecap="round"/>
  <!-- Stage 3 -->
  <rect x="410" y="45" width="165" height="270" rx="10" fill="#FFFFFF" stroke="#059669" stroke-width="1.5"/>
  <rect x="425" y="60" width="70" height="24" rx="4" fill="#ECFDF5"/>
  <text x="460" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">TIER 3</text>
  <text x="425" y="110" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#0F172A">SANDBOXING</text>
  <text x="425" y="128" font-family="system-ui, sans-serif" font-size="9" fill="#64748B">Virtual Chamber</text>
  <circle cx="492" cy="180" r="32" fill="#F0FDF4" stroke="#059669" stroke-width="2"/>
  <text x="492" y="177" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#047857" text-anchor="middle">DETONATE</text>
  <text x="492" y="193" font-family="system-ui, sans-serif" font-size="8" fill="#15803D" text-anchor="middle">Isolated Bubble</text>
  <text x="425" y="245" font-family="system-ui, sans-serif" font-size="9" fill="#475569">Executes unknown files safely in cloud VM before real PC</text>
</svg>"""
    },
    # 82
    {
        "num": "82",
        "index": "33",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Perimeter Defense",
        "title": "Network Firewalls & The Demilitarized Zone (DMZ)",
        "subtitle": "Stateful packet inspection, isolating public web servers from private databases, and configuring Windows Defender Firewall.",
        "analogy_title": "The Gated Compound with Guardhouse & Visitor Lobby",
        "analogy_text": "A firewall is like the <strong>security checkpoint and barrier gate outside an army base</strong>. Visitors are stopped at the gatehouse (<strong>DMZ</strong>) to show identification; nobody is allowed into the private headquarters vault (<strong>Internal Database</strong>) directly.",
        "steps": [
            ("1", "Stateful Packet Inspection", "The firewall checks whether incoming traffic is a requested response to a website YOU opened, or an unsolicited hack attempt."),
            ("2", "Demilitarized Zone (DMZ)", "Public web servers sit in a semi-isolated zone; if a hacker breaches the web server, the inner firewall stops them from reaching the student database."),
            ("3", "Windows Firewall Profiles", "Private Profile allows printer and file sharing at home; Public Profile locks all sharing when on coffee shop Wi-Fi.")
        ],
        "rule": "Firewall Rule: If a pop-up asks 'Allow this unknown app through Windows Firewall on Public Networks?', ALWAYS CLICK CANCEL unless you personally downloaded the tool.",
        "fig_title": "Figure 33 &bull; DMZ Dual-Firewall Enterprise Architecture",
        "takeaway": "Key Takeaway: Firewalls inspect stateful traffic; DMZ isolates public servers from private crown jewels.",
        "notes": "Show how to type `wf.msc` into Windows Run dialog to view the Advanced Security firewall rules.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Untrusted Internet -->
  <rect x="25" y="50" width="105" height="260" rx="8" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5"/>
  <text x="77" y="80" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#991B1B" text-anchor="middle">UNTRUSTED</text>
  <text x="77" y="98" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#DC2626" text-anchor="middle">INTERNET</text>
  <circle cx="77" cy="160" r="24" fill="#FFFFFF" stroke="#EF4444"/>
  <text x="77" y="165" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#DC2626" text-anchor="middle">&cross;</text>
  <text x="77" y="225" font-family="system-ui, sans-serif" font-size="8.5" fill="#7F1D1D" text-anchor="middle">Public Traffic</text>
  <text x="77" y="240" font-family="system-ui, sans-serif" font-size="8.5" fill="#7F1D1D" text-anchor="middle">Port Scans</text>
  <!-- Firewall 1 -->
  <rect x="145" y="80" width="24" height="200" rx="4" fill="#EF4444"/>
  <text x="157" y="185" font-family="system-ui, sans-serif" font-size="9" font-weight="800" fill="#FFFFFF" text-anchor="middle" transform="rotate(-90 157 185)">PERIMETER FIREWALL</text>
  <!-- DMZ Subnet -->
  <rect x="185" y="50" width="170" height="260" rx="8" fill="#FFFBEB" stroke="#D97706" stroke-width="1.5"/>
  <text x="270" y="80" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#B45309" text-anchor="middle">DMZ ZONE</text>
  <text x="270" y="98" font-family="system-ui, sans-serif" font-size="9" fill="#78350F" text-anchor="middle">Demilitarized Buffer</text>
  <rect x="200" y="120" width="140" height="60" rx="6" fill="#FFFFFF" stroke="#FDE68A"/>
  <text x="270" y="145" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0F172A" text-anchor="middle">Web / Mail Server</text>
  <text x="270" y="162" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Port 80/443 Public Access</text>
  <rect x="200" y="195" width="140" height="95" rx="6" fill="#FEF3C7"/>
  <text x="270" y="220" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#B45309" text-anchor="middle">Buffer Protection</text>
  <text x="270" y="238" font-family="system-ui, sans-serif" font-size="8" fill="#78350F" text-anchor="middle">Even if Web Server is hacked,</text>
  <text x="270" y="252" font-family="system-ui, sans-serif" font-size="8" fill="#78350F" text-anchor="middle">Internal Firewall blocks</text>
  <text x="270" y="266" font-family="system-ui, sans-serif" font-size="8" fill="#78350F" text-anchor="middle">access to student data!</text>
  <!-- Firewall 2 -->
  <rect x="370" y="80" width="24" height="200" rx="4" fill="#059669"/>
  <text x="382" y="185" font-family="system-ui, sans-serif" font-size="9" font-weight="800" fill="#FFFFFF" text-anchor="middle" transform="rotate(-90 382 185)">INTERNAL FIREWALL</text>
  <!-- Private Database Subnet -->
  <rect x="410" y="50" width="165" height="260" rx="8" fill="#ECFDF5" stroke="#059669" stroke-width="1.5"/>
  <text x="492" y="80" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">SECURE VAULT</text>
  <text x="492" y="98" font-family="system-ui, sans-serif" font-size="9" fill="#065F46" text-anchor="middle">Internal LAN Network</text>
  <rect x="425" y="120" width="135" height="75" rx="6" fill="#FFFFFF" stroke="#A7F3D0"/>
  <text x="492" y="145" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">Student DB &amp; Marks</text>
  <text x="492" y="162" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Financial Payroll</text>
  <text x="492" y="177" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">100% Isolated from Web</text>
  <rect x="425" y="210" width="135" height="80" rx="6" fill="#F0FDF4"/>
  <text x="492" y="235" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#166534" text-anchor="middle">&check; Zero Direct Access</text>
  <text x="492" y="255" font-family="system-ui, sans-serif" font-size="8" fill="#15803D" text-anchor="middle">Internal staff only via VPN</text>
</svg>"""
    },
    # 83
    {
        "num": "83",
        "index": "34",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Social Engineering",
        "title": "Phishing & Social Engineering: Forensic Email Anatomy",
        "subtitle": "Dissecting spear-phishing lures, fake urgent deadlines, typosquatted sender domains, and the mandatory URL hover inspection technique.",
        "analogy_title": "A Fake Fisherman Casting Shiny Bait",
        "analogy_text": "In regular fishing, the fisherman puts bait on a hook hoping a fish bites. In <strong>phishing, a cyber criminal sends you an email pretending to be your bank or college principal</strong> ('Account suspended in 24 hours!'), panicking you into entering your password into their fake login page.",
        "steps": [
            ("1", "Artificial Urgency & Fear", "Subject line screams 'Account Locked' or 'Income Tax Refund Waiting' to stop you from thinking rationally."),
            ("2", "Typosquatted Sender Domain", "Sender displays 'State Bank', but the actual email address is `support@sbi-security-verify.xyz`."),
            ("3", "The URL Hover Technique", "Hover your mouse pointer over the button without clicking! The real destination URL appears in the browser corner.")
        ],
        "rule": "The Golden Rule of Links: Before clicking any link in an SMS or email, hover your mouse over it! If the text says 'onlinesbi.com' but the actual link points to 'sbi-update.xyz', IT IS 100% FRAUD.",
        "fig_title": "Figure 34 &bull; Forensic Anatomy of a Spear-Phishing Email",
        "takeaway": "Key Takeaway: Never trust sender display names; always hover before clicking; banks NEVER ask for PIN via email.",
        "notes": "Demonstrate the hover technique live: hovering reveals the true destination URL in the bottom-left status bar.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Phishing Email Frame -->
  <rect x="30" y="30" width="540" height="300" rx="10" fill="#FFFFFF" stroke="#EF4444" stroke-width="2"/>
  <!-- Warning Banner -->
  <rect x="30" y="30" width="540" height="32" rx="10 10 0 0" fill="#EF4444"/>
  <text x="300" y="51" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#FFFFFF" text-anchor="middle">FORENSIC PHISHING ANATOMY: 4 RED FLAGS</text>
  <!-- Red Flag 1: Fake Sender -->
  <rect x="45" y="70" width="510" height="36" rx="4" fill="#FEF2F2" stroke="#FECACA"/>
  <text x="55" y="86" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#991B1B">From: State Bank Customer Care &lt;alert@onlinesbi-verification.xyz&gt;</text>
  <text x="55" y="100" font-family="system-ui, sans-serif" font-size="8" fill="#DC2626">RED FLAG 1: Typosquatted domain (.xyz instead of sbi.co.in)</text>
  <!-- Red Flag 2: Panic Subject -->
  <rect x="45" y="112" width="510" height="36" rx="4" fill="#FEF2F2" stroke="#FECACA"/>
  <text x="55" y="128" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#991B1B">Subject: URGENT: Your Debit Card will be Permanently BLOCKED in 2 Hours!</text>
  <text x="55" y="142" font-family="system-ui, sans-serif" font-size="8" fill="#DC2626">RED FLAG 2: Artificial urgency designed to trigger panic and bypass critical thinking</text>
  <!-- Red Flag 3: Generic Salutation -->
  <text x="55" y="170" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#0F172A">Dear Customer, (RED FLAG 3: Real banks address you by your real full name!)</text>
  <text x="55" y="190" font-family="system-ui, sans-serif" font-size="9.5" fill="#334155">We detected unauthorized activity on your account. Please update your KYC immediately to avoid penalties.</text>
  <!-- Red Flag 4: Deceptive Link with Hover Reveal -->
  <rect x="180" y="215" width="240" height="36" rx="6" fill="#DC2626"/>
  <text x="300" y="238" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">UPDATE KYC NOW</text>
  <!-- Hover Status Bar (The Smoking Gun) -->
  <rect x="45" y="265" width="510" height="50" rx="4" fill="#1E293B"/>
  <text x="55" y="283" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#F59E0B">HOVER INSPECTION REVEALS TRUE DESTINATION (BOTTOM-LEFT CORNER):</text>
  <text x="55" y="303" font-family="monospace" font-size="11" font-weight="700" fill="#38BDF8">http://185.220.101.5/hacker/fake-sbi-login.php</text>
</svg>"""
    },
    # 84
    {
        "num": "84",
        "index": "35",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "DNS Threats",
        "title": "Pharming Attacks: Poisoning the Digital Road Signs",
        "subtitle": "How DNS cache poisoning redirects legitimate web traffic to clone servers without clicking bad links, and how SSL/TLS certificates prevent disaster.",
        "analogy_title": "Silently Replacing Highway Direction Signs at Night",
        "analogy_text": "In Phishing, a criminal hands you a fake map. In <strong>Pharming, criminals secretly sneak out at night and physically repaint the highway road signs</strong>! Even though you drove towards the sign saying 'Airport', the repainted sign leads your car straight into an abandoned warehouse.",
        "steps": [
            ("1", "DNS Poisoning", "Hacker injects false IP mappings into a vulnerable ISP DNS server or alters your local Windows `hosts` file."),
            ("2", "Silent Redirection", "You type the 100% correct URL (`onlinesbi.sbi`), but your computer is silently routed to the hacker's clone server."),
            ("3", "The SSL/TLS Warning", "The hacker's fake server does NOT have the bank's cryptographic SSL certificate. Your browser flashes a bright red security warning!")
        ],
        "rule": "Browser Warning Commandment: If your browser ever flashes: 'Your connection is not private' or 'Security Certificate Invalid', NEVER CLICK 'Proceed Anyway'! It means you are likely on a Pharming clone server.",
        "fig_title": "Figure 35 &bull; DNS Poisoning vs. SSL Certificate Defense",
        "takeaway": "Key Takeaway: Pharming redirects correct URLs via DNS poisoning; SSL certificate warnings are your last line of defense.",
        "notes": "Demonstrate the Windows hosts file located at C:\\Windows\\System32\\drivers\\etc\\hosts.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- User Types Correct URL -->
  <rect x="30" y="45" width="160" height="270" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
  <rect x="45" y="60" width="130" height="24" rx="4" fill="#E0F2FE"/>
  <text x="110" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0369A1" text-anchor="middle">USER CLIENT</text>
  <rect x="45" y="100" width="130" height="70" rx="6" fill="#F0F9FF" stroke="#BAE6FD"/>
  <text x="110" y="125" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0F172A" text-anchor="middle">Types 100% Correct</text>
  <text x="110" y="145" font-family="monospace" font-size="9.5" font-weight="700" fill="#0284C7" text-anchor="middle">https://sbi.co.in</text>
  <text x="110" y="195" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569" text-anchor="middle">User made ZERO typo</text>
  <text x="110" y="210" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569" text-anchor="middle">Did not click bad email</text>
  <!-- Poisoned DNS (Middle) -->
  <rect x="225" y="45" width="150" height="270" rx="10" fill="#FEF2F2" stroke="#EF4444" stroke-width="2"/>
  <rect x="235" y="60" width="130" height="24" rx="4" fill="#FEE2E2"/>
  <text x="300" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#991B1B" text-anchor="middle">POISONED DNS</text>
  <circle cx="300" cy="130" r="28" fill="#FFFFFF" stroke="#EF4444" stroke-width="2"/>
  <text x="300" y="128" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#DC2626" text-anchor="middle">DNS</text>
  <text x="300" y="142" font-family="system-ui, sans-serif" font-size="8" fill="#7F1D1D" text-anchor="middle">POISONED</text>
  <rect x="235" y="180" width="130" height="110" rx="6" fill="#FFFFFF" stroke="#FECACA"/>
  <text x="300" y="202" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" fill="#B91C1C" text-anchor="middle">Fake IP Injected:</text>
  <text x="300" y="222" font-family="monospace" font-size="9" fill="#DC2626" text-anchor="middle">sbi.co.in &rarr; 198.51.100.2</text>
  <text x="300" y="245" font-family="system-ui, sans-serif" font-size="8" fill="#7F1D1D" text-anchor="middle">Silently re-routes traffic to attacker's server</text>
  <!-- Browser Warning Defense (Right) -->
  <rect x="410" y="45" width="160" height="270" rx="10" fill="#FFFFFF" stroke="#EF4444" stroke-width="1.5"/>
  <rect x="425" y="60" width="130" height="24" rx="4" fill="#FEE2E2"/>
  <text x="490" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#B91C1C" text-anchor="middle">BROWSER SHIELD</text>
  <rect x="425" y="100" width="130" height="85" rx="6" fill="#FEF2F2" stroke="#EF4444"/>
  <text x="490" y="122" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#DC2626" text-anchor="middle">SSL ERROR!</text>
  <text x="490" y="140" font-family="system-ui, sans-serif" font-size="8.5" fill="#7F1D1D" text-anchor="middle">"Certificate Invalid"</text>
  <text x="490" y="155" font-family="system-ui, sans-serif" font-size="8" fill="#991B1B" text-anchor="middle">Hacker lacks bank's SSL keys</text>
  <rect x="425" y="200" width="130" height="95" rx="6" fill="#FEE2E2"/>
  <text x="490" y="225" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#B91C1C" text-anchor="middle">LIFESAVING RULE:</text>
  <text x="490" y="245" font-family="system-ui, sans-serif" font-size="8.5" font-weight="800" fill="#DC2626" text-anchor="middle">NEVER BYPASS</text>
  <text x="490" y="260" font-family="system-ui, sans-serif" font-size="8" fill="#7F1D1D" text-anchor="middle">Turn around immediately</text>
</svg>"""
    }
]

print(f"data_unit5 part 2 initialized with {len(unit5_part2_topics)} topics.")
