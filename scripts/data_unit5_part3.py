"""
Unit 5 Data Part 3: Topics 85 to 91 (7 Topics)
Spoofing, Cyber Ethics, Passkeys, IT Act 2000, DPDP Act 2023, 1930 Helpline & Capstone
"""

unit5_part3_topics = [
    # 85
    {
        "num": "85",
        "index": "36",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Identity Impersonation",
        "title": "Identity Spoofing, Caller ID & Deepfakes",
        "subtitle": "How VoIP software counterfeits official police numbers on Caller ID, the rampant 'Digital Arrest' scam in India, and AI voice cloning.",
        "analogy_title": "Wearing a Silicone Mask and Flashing a Forged Badge",
        "analogy_text": "Identity spoofing is like a criminal <strong>wearing a lifelike silicone face mask and flashing a counterfeit police badge</strong> at your door. On computer networks, legacy protocols like phone caller ID and email headers have no built-in verification, making it easy for scammers to pretend to be someone else.",
        "steps": [
            ("1", "VoIP Caller ID Spoofing", "Scammers use international internet phone services to make the display on your phone read 'CBI Headquarters' or '+91 100'."),
            ("2", "The 'Digital Arrest' Scam", "Scammers wear fake police uniforms on Skype or WhatsApp video calls, claiming you are under 'Digital Arrest' for money laundering."),
            ("3", "Verification Protocol", "Hang up immediately! Real police, CBI, and RBI NEVER conduct arrests or demand money transfers over video calls.")
        ],
        "rule": "Statutory Fact: Under Indian criminal law, there is NO legal concept called 'Digital Arrest'! Any caller demanding you stay on a Skype call or transfer money to 'verify funds' is a criminal.",
        "fig_title": "Figure 36 &bull; Caller ID Spoofing & 'Digital Arrest' Scam Anatomy",
        "takeaway": "Key Takeaway: Caller ID can be faked; 'Digital Arrest' does not exist legally; hang up and dial 1930.",
        "notes": "Discuss how deepfake AI voice cloning can imitate a family member's voice saying they were arrested and need bail money.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Left: Fake Caller ID Phone Display -->
  <rect x="30" y="45" width="250" height="270" rx="10" fill="#FFFFFF" stroke="#EF4444" stroke-width="2"/>
  <rect x="45" y="60" width="130" height="24" rx="4" fill="#FEE2E2"/>
  <text x="110" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">SPOOFED PHONE</text>
  <text x="45" y="105" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#B91C1C">VoIP Manipulation</text>
  <!-- Phone Screen Mockup -->
  <rect x="45" y="125" width="220" height="110" rx="8" fill="#1E293B"/>
  <text x="155" y="152" font-family="system-ui, sans-serif" font-size="10" fill="#94A3B8" text-anchor="middle">INCOMING CALL...</text>
  <text x="155" y="175" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#EF4444" text-anchor="middle">CBI HEADQUARTERS</text>
  <text x="155" y="195" font-family="monospace" font-size="10" fill="#F8FAFC" text-anchor="middle">+91 11 2436 0000</text>
  <text x="155" y="222" font-family="system-ui, sans-serif" font-size="8.5" fill="#F59E0B" text-anchor="middle">&cross; 100% Counterfeited via VoIP!</text>
  <rect x="45" y="245" width="220" height="50" rx="6" fill="#FEE2E2"/>
  <text x="155" y="268" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#B91C1C" text-anchor="middle">Lure: Fear &amp; Panic</text>
  <text x="155" y="284" font-family="system-ui, sans-serif" font-size="8.5" fill="#7F1D1D" text-anchor="middle">"You are under Digital Arrest for narcotics"</text>
  <!-- Right: Indian Legal Truth -->
  <rect x="320" y="45" width="250" height="270" rx="10" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
  <rect x="335" y="60" width="130" height="24" rx="4" fill="#D1FAE5"/>
  <text x="400" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#065F46" text-anchor="middle">INDIAN LAW REALITY</text>
  <text x="335" y="105" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#047857">The Golden Protocol</text>
  <rect x="335" y="125" width="220" height="110" rx="6" fill="#FFFFFF" stroke="#A7F3D0"/>
  <text x="345" y="148" font-family="system-ui, sans-serif" font-size="9.5" fill="#047857">&bull; No police arrests via Skype or WhatsApp</text>
  <text x="345" y="170" font-family="system-ui, sans-serif" font-size="9.5" fill="#047857">&bull; 'Digital Arrest' does NOT exist in law</text>
  <text x="345" y="192" font-family="system-ui, sans-serif" font-size="9.5" fill="#047857">&bull; Police never demand bank transfers</text>
  <text x="345" y="214" font-family="system-ui, sans-serif" font-size="9.5" fill="#047857">&bull; Never verify funds into 'RBI secure vault'</text>
  <rect x="335" y="245" width="220" height="50" rx="6" fill="#D1FAE5"/>
  <text x="445" y="268" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" fill="#065F46" text-anchor="middle">Action: Hang Up Instantly!</text>
  <text x="445" y="284" font-family="system-ui, sans-serif" font-size="8.5" fill="#047857" text-anchor="middle">Report number to 1930 &amp; cybercrime.gov.in</text>
</svg>"""
    },
    # 86
    {
        "num": "86",
        "index": "37",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Cyber Ethics",
        "title": "Cyber Ethics: Hackers vs. Crackers & Bug Bounties",
        "subtitle": "Distinguishing ethical White Hats from criminal Black Hats, and how students can legally earn rewards through global Bug Bounty platforms.",
        "analogy_title": "Locksmith Testing a Vault vs. Burglar Picking It",
        "analogy_text": "A <strong>White Hat Hacker is like a master locksmith hired by a bank</strong> to test whether the vault doors have flaws; when they find a weak bolt, they write a report so the bank can fix it. A <strong>Cracker (Black Hat) picks the same lock at midnight</strong> to steal the gold and run away.",
        "steps": [
            ("1", "White Hat (Ethical)", "100% authorized penetration testers who operate with strict legal permission and non-disclosure contracts."),
            ("2", "Black Hat (Cracker / Criminal)", "Unauthorized attackers who break into servers to steal data, extort ransoms, or sell credit card databases on the dark web."),
            ("3", "Bug Bounty Programs", "Global platforms (HackerOne, Bugcrowd) where companies like Google, Microsoft, and Zerodha pay cash rewards for reported vulnerabilities.")
        ],
        "rule": "Career Opportunity: College students with ethical hacking skills can legally earn lakhs of rupees from home participating in official bug bounties without breaking laws.",
        "fig_title": "Figure 37 &bull; The Hacker Taxonomy: White vs. Black vs. Grey Hat",
        "takeaway": "Key Takeaway: Permission is the dividing line between an Ethical Hacker and a Criminal Cracker.",
        "notes": "Remind students that probing college or government servers without written authorization violates IT Act Section 43/66.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- 3 Hat Pillars -->
  <!-- White Hat -->
  <rect x="25" y="40" width="170" height="280" rx="10" fill="#FFFFFF" stroke="#059669" stroke-width="2"/>
  <circle cx="110" cy="80" r="24" fill="#ECFDF5" stroke="#059669" stroke-width="2"/>
  <text x="110" y="85" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#047857" text-anchor="middle">WHITE</text>
  <text x="110" y="125" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#0F172A" text-anchor="middle">ETHICAL HACKER</text>
  <text x="110" y="142" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#059669" text-anchor="middle">100% Authorized</text>
  <rect x="35" y="155" width="150" height="1" fill="#E2E8F0"/>
  <text x="40" y="180" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Defends systems with permission</text>
  <text x="40" y="200" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Responsible disclosure</text>
  <text x="40" y="220" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Bug bounty rewards</text>
  <rect x="35" y="245" width="150" height="60" rx="6" fill="#F0FDF4"/>
  <text x="110" y="268" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#047857" text-anchor="middle">Status: Legal &amp; Respected</text>
  <text x="110" y="284" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Employed by banks &amp; govt</text>
  <!-- Grey Hat -->
  <rect x="215" y="40" width="170" height="280" rx="10" fill="#FFFFFF" stroke="#D97706" stroke-width="2"/>
  <circle cx="300" cy="80" r="24" fill="#FEF3C7" stroke="#D97706" stroke-width="2"/>
  <text x="300" y="85" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#B45309" text-anchor="middle">GREY</text>
  <text x="300" y="125" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#0F172A" text-anchor="middle">UNAUTHORIZED</text>
  <text x="300" y="142" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#D97706" text-anchor="middle">No Malicious Intent</text>
  <rect x="225" y="155" width="150" height="1" fill="#E2E8F0"/>
  <text x="230" y="180" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Hacks without permission</text>
  <text x="230" y="200" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Discloses bug to company</text>
  <text x="230" y="220" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; May demand fee or reward</text>
  <rect x="225" y="245" width="150" height="60" rx="6" fill="#FFFBEB"/>
  <text x="300" y="268" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#B45309" text-anchor="middle">Status: Legally Risky</text>
  <text x="300" y="284" font-family="system-ui, sans-serif" font-size="8.5" fill="#78350F" text-anchor="middle">Can still face IT Act charges</text>
  <!-- Black Hat -->
  <rect x="405" y="40" width="170" height="280" rx="10" fill="#FFFFFF" stroke="#EF4444" stroke-width="2"/>
  <circle cx="490" cy="80" r="24" fill="#FEE2E2" stroke="#EF4444" stroke-width="2"/>
  <text x="490" y="85" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#991B1B" text-anchor="middle">BLACK</text>
  <text x="490" y="125" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#0F172A" text-anchor="middle">CRACKER (CRIMINAL)</text>
  <text x="490" y="142" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#DC2626" text-anchor="middle">Malicious Motives</text>
  <rect x="415" y="155" width="150" height="1" fill="#E2E8F0"/>
  <text x="420" y="180" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Breaks in to steal or destroy</text>
  <text x="420" y="200" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Ransomware extortion</text>
  <text x="420" y="220" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Dark web data sales</text>
  <rect x="415" y="245" width="150" height="60" rx="6" fill="#FEE2E2"/>
  <text x="490" y="268" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#991B1B" text-anchor="middle">Status: Criminal Offense</text>
  <text x="490" y="284" font-family="system-ui, sans-serif" font-size="8.5" fill="#7F1D1D" text-anchor="middle">Jail time under Sec 66 IT Act</text>
</svg>"""
    },
    # 87
    {
        "num": "87",
        "index": "38",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Credential Security",
        "title": "Identity Theft, PII Protection & FIDO2 Passkeys",
        "subtitle": "How credential stuffing exploits password reuse, the transition from SMS OTP to Authenticator apps, and cryptographic Passkeys.",
        "analogy_title": "A House Key vs. Biometric Safe Scanner",
        "analogy_text": "Using a password like `Password123` across 15 websites is like <strong>using the exact same cheap padlock key for your front door, bicycle, bank locker, and car</strong>. If a thief finds that key anywhere, they unlock everything you own. <strong>A Passkey uses biometric thumbprint verification</strong> that cannot be phished.",
        "steps": [
            ("1", "Credential Stuffing", "When an obscure gaming site leaks your password, automated hacker bots test that same password on Amazon, SBI, and Gmail in seconds."),
            ("2", "Password Managers (Bitwarden)", "Generates 20-character random passwords (`x9#K2$vP!mQ1@z`) for every site; you only memorize one master password."),
            ("3", "FIDO2 Passkeys & Authenticator MFA", "Replaces SMS OTP (which can be intercepted via SIM-swapping) with cryptographic biometric passkeys.")
        ],
        "rule": "Password Mandate: Never use your name, birthday, or phone number in passwords! A 4-word passphrase (e.g. `ElephantCoffeeRocketBridge`) is 1000x harder for supercomputers to crack than `P@ssw0rd`.",
        "fig_title": "Figure 38 &bull; Password Reuse Vulnerability vs. FIDO2 Passkey Defense",
        "takeaway": "Key Takeaway: Unique password per website via Password Manager + App-based 2FA / Passkey.",
        "notes": "Demonstrate the website `haveibeenpwned.com` where students can safely check if their personal email was leaked in public breaches.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Credential Stuffing Hazard (Left) -->
  <rect x="30" y="45" width="250" height="270" rx="10" fill="#FFFFFF" stroke="#EF4444" stroke-width="2"/>
  <rect x="45" y="60" width="140" height="24" rx="4" fill="#FEE2E2"/>
  <text x="115" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">PASSWORD REUSE</text>
  <text x="45" y="105" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#B91C1C">Credential Stuffing</text>
  <rect x="45" y="125" width="220" height="95" rx="6" fill="#FEF2F2" stroke="#FECACA"/>
  <text x="55" y="148" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">1. Random forum hacked &rarr; Leaks password</text>
  <text x="55" y="168" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">2. Automated bot tests that exact password</text>
  <text x="55" y="188" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">3. Bot enters Amazon, Netflix, Gmail, SBI!</text>
  <text x="55" y="208" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" fill="#991B1B">Same password used across 15 accounts</text>
  <rect x="45" y="235" width="220" height="60" rx="6" fill="#FEE2E2"/>
  <text x="155" y="258" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#B91C1C" text-anchor="middle">Catastrophic Domino Collapse</text>
  <text x="155" y="275" font-family="system-ui, sans-serif" font-size="8.5" fill="#7F1D1D" text-anchor="middle">One minor leak compromises your entire identity</text>
  <!-- Modern Passkey Shield (Right) -->
  <rect x="320" y="45" width="250" height="270" rx="10" fill="#FFFFFF" stroke="#059669" stroke-width="2"/>
  <rect x="335" y="60" width="140" height="24" rx="4" fill="#ECFDF5"/>
  <text x="405" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">FIDO2 PASSKEYS</text>
  <text x="335" y="105" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#047857">Phishing-Resistant Auth</text>
  <rect x="335" y="125" width="220" height="95" rx="6" fill="#F0FDF4" stroke="#A7F3D0"/>
  <text x="345" y="148" font-family="system-ui, sans-serif" font-size="9" fill="#047857">&check; Zero typed passwords to steal or leak</text>
  <text x="345" y="168" font-family="system-ui, sans-serif" font-size="9" fill="#047857">&check; Public-key cryptography on device</text>
  <text x="345" y="188" font-family="system-ui, sans-serif" font-size="9" fill="#047857">&check; Biometric fingerprint / Face unlock</text>
  <text x="345" y="208" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" fill="#166534">Immune to fake phishing websites</text>
  <rect x="335" y="235" width="220" height="60" rx="6" fill="#ECFDF5"/>
  <text x="445" y="258" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#047857" text-anchor="middle">Modern Gold Standard</text>
  <text x="445" y="275" font-family="system-ui, sans-serif" font-size="8.5" fill="#065F46" text-anchor="middle">Google, Apple, Microsoft &amp; SBI Passkeys</text>
</svg>"""
    },
    # 88
    {
        "num": "88",
        "index": "39",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Indian Cyber Law",
        "title": "Indian Cyber Law: The IT Act, 2000 & PKI",
        "subtitle": "Core penal provisions (Sections 43, 65, 66, 66C, 66D, 66E, 67), asymmetric cryptography, and legal validity of digital signatures.",
        "analogy_title": "The Digital Penal Code & The Government Notary Stamp",
        "analogy_text": "Just as the Indian Penal Code (IPC) punishes physical theft and trespassing, the <strong>Information Technology Act, 2000 is India's legal penal code for cyberspace</strong>. It defines hacking, identity theft, and online harassment as criminal offenses with mandatory prison terms.",
        "steps": [
            ("1", "Key Penal Provisions", "Section 43 (unauthorized access), Section 66 (hacking), Section 66C (identity theft), Section 66D (impersonation fraud), Section 66E (privacy violation)."),
            ("2", "Public Key Infrastructure (PKI)", "Asymmetric key pairs: you sign documents using your secret Private Key; anyone verifies it with your Public Key."),
            ("3", "Legal Standing (Section 5)", "Digital signatures issued by licensed Certifying Authorities (CAs) have identical legal weight to physical pen-and-paper signatures in court.")
        ],
        "rule": "Statutory Severity: Committing cyber impersonation or UPI cheating under Section 66D of the IT Act carries up to 3 years of rigorous imprisonment and heavy financial penalties.",
        "fig_title": "Figure 39 &bull; IT Act Penal Sections & Asymmetric PKI Signing",
        "takeaway": "Key Takeaway: IT Act 2000 criminalizes cyber offenses; PKI asymmetric signatures are legally binding.",
        "notes": "Review the Certifying Authorities in India (eMudhra, (n)Code, NIC) licensed under the Controller of Certifying Authorities (CCA).",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Left: Core IT Act Sections -->
  <rect x="30" y="40" width="255" height="280" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
  <rect x="45" y="52" width="130" height="24" rx="4" fill="#E0F2FE"/>
  <text x="110" y="68" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0369A1" text-anchor="middle">IT ACT 2000 SECTIONS</text>
  <text x="45" y="98" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#0F172A">Key Penal Provisions</text>
  <rect x="45" y="112" width="225" height="26" rx="4" fill="#F8FAFC"/>
  <text x="55" y="129" font-family="monospace" font-size="9.5" font-weight="700" fill="#0369A1">Sec 43:</text>
  <text x="105" y="129" font-family="system-ui, sans-serif" font-size="9" fill="#334155">Unauthorized system access / damage</text>
  <rect x="45" y="142" width="225" height="26" rx="4" fill="#F8FAFC"/>
  <text x="55" y="159" font-family="monospace" font-size="9.5" font-weight="700" fill="#0369A1">Sec 66:</text>
  <text x="105" y="159" font-family="system-ui, sans-serif" font-size="9" fill="#334155">Hacking &amp; virus propagation (3 yrs jail)</text>
  <rect x="45" y="172" width="225" height="26" rx="4" fill="#F8FAFC"/>
  <text x="55" y="189" font-family="monospace" font-size="9.5" font-weight="700" fill="#0369A1">Sec 66C:</text>
  <text x="110" y="189" font-family="system-ui, sans-serif" font-size="9" fill="#334155">Identity theft / password stealing</text>
  <rect x="45" y="202" width="225" height="26" rx="4" fill="#F8FAFC"/>
  <text x="55" y="219" font-family="monospace" font-size="9.5" font-weight="700" fill="#0369A1">Sec 66D:</text>
  <text x="110" y="219" font-family="system-ui, sans-serif" font-size="9" fill="#334155">Cheating by personation (UPI fraud)</text>
  <rect x="45" y="232" width="225" height="26" rx="4" fill="#F8FAFC"/>
  <text x="55" y="249" font-family="monospace" font-size="9.5" font-weight="700" fill="#0369A1">Sec 66E:</text>
  <text x="110" y="249" font-family="system-ui, sans-serif" font-size="9" fill="#334155">Capturing / publishing private images</text>
  <rect x="45" y="262" width="225" height="42" rx="4" fill="#FEE2E2"/>
  <text x="55" y="278" font-family="monospace" font-size="9" font-weight="700" fill="#991B1B">Sec 67:</text>
  <text x="100" y="278" font-family="system-ui, sans-serif" font-size="8.5" fill="#7F1D1D">Publishing obscene material online</text>
  <text x="55" y="294" font-family="system-ui, sans-serif" font-size="8" font-weight="700" fill="#B91C1C">Mandatory 5-year imprisonment on repeat</text>
  <!-- Right: PKI Digital Signatures -->
  <rect x="315" y="40" width="255" height="280" rx="10" fill="#FFFFFF" stroke="#059669" stroke-width="1.5"/>
  <rect x="330" y="52" width="130" height="24" rx="4" fill="#ECFDF5"/>
  <text x="395" y="68" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">PKI ARCHITECTURE</text>
  <text x="330" y="98" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#0F172A">Asymmetric Cryptography</text>
  <!-- Document Signing Flow -->
  <rect x="330" y="115" width="225" height="50" rx="6" fill="#F8FAFC" stroke="#CBD5E1"/>
  <text x="442" y="135" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#0F172A" text-anchor="middle">Sender Signs with PRIVATE KEY</text>
  <text x="442" y="152" font-family="system-ui, sans-serif" font-size="8.5" fill="#DC2626" text-anchor="middle">Kept strictly confidential by signer</text>
  <line x1="442" y1="165" x2="442" y2="185" stroke="#059669" stroke-width="3" stroke-linecap="round"/>
  <rect x="330" y="185" width="225" height="50" rx="6" fill="#F0FDF4" stroke="#A7F3D0"/>
  <text x="442" y="205" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#047857" text-anchor="middle">Receiver Verifies with PUBLIC KEY</text>
  <text x="442" y="222" font-family="system-ui, sans-serif" font-size="8.5" fill="#15803D" text-anchor="middle">Freely distributed in public certificate</text>
  <rect x="330" y="245" width="225" height="60" rx="6" fill="#ECFDF5"/>
  <text x="442" y="268" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" fill="#065F46" text-anchor="middle">Legal Standing: Section 5</text>
  <text x="442" y="284" font-family="system-ui, sans-serif" font-size="8.5" fill="#047857" text-anchor="middle">100% equivalent to physical wet-ink signature</text>
  <text x="442" y="298" font-family="system-ui, sans-serif" font-size="8.5" fill="#047857" text-anchor="middle">Certified by Controller of Certifying Authorities</text>
</svg>"""
    },
    # 89
    {
        "num": "89",
        "index": "40",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Data Privacy",
        "title": "Data Governance: The DPDP Act 2023 & CERT-In",
        "subtitle": "Citizen privacy rights under the Digital Personal Data Protection Act, corporate compliance duties, and mandatory 6-hour CERT-In incident reporting.",
        "analogy_title": "The Citizen's Privacy Bill of Rights",
        "analogy_text": "Before the DPDP Act, apps and companies collected your phone number and sold it to telemarketers without consequences. The <strong>DPDP Act 2023 is your legal privacy shield</strong>: companies cannot touch your data without clear consent, and face fines up to &#8377;250 Crores if they leak it.",
        "steps": [
            ("1", "Data Principal Rights", "You (the citizen) have the legal right to know what data companies store, correct errors, and demand complete deletion."),
            ("2", "Data Fiduciary Duties", "Organizations (colleges, banks, tech firms) must implement strict security safeguards and purge data when no longer needed."),
            ("3", "CERT-In 6-Hour Reporting", "Under national cybersecurity guidelines, all corporations must report security breaches to CERT-In within 6 hours of discovery.")
        ],
        "rule": "Right to Erasure: If you stop using an online shopping app or gaming service, you can legally email their Grievance Officer demanding total erasure of your personal data under the DPDP Act.",
        "fig_title": "Figure 40 &bull; The DPDP Act 2023 Governance Ecosystem",
        "takeaway": "Key Takeaway: Clear Consent Required + Right to Erasure + Fines up to &#8377;250 Cr + 6-hour CERT-In notice.",
        "notes": "Explain CERT-In (Indian Computer Emergency Response Team) as India's national cyber emergency agency.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Central DPDP Act Shield -->
  <rect x="200" y="35" width="200" height="40" rx="8" fill="#059669"/>
  <text x="300" y="58" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#FFFFFF" text-anchor="middle">DPDP ACT 2023</text>
  <text x="300" y="70" font-family="system-ui, sans-serif" font-size="7.5" fill="#D1FAE5" text-anchor="middle">Digital Personal Data Protection Framework</text>
  <!-- 3 Strategic Pillars -->
  <!-- Pillar 1: Data Principal (Citizen) -->
  <rect x="30" y="95" width="165" height="230" rx="8" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
  <rect x="45" y="105" width="135" height="24" rx="4" fill="#E0F2FE"/>
  <text x="112" y="121" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#0369A1" text-anchor="middle">DATA PRINCIPAL (YOU)</text>
  <text x="112" y="150" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#0F172A" text-anchor="middle">Citizen Privacy Rights</text>
  <text x="45" y="175" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Right to clear consent</text>
  <text x="45" y="195" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Right to access summary</text>
  <text x="45" y="215" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Right to correct errors</text>
  <text x="45" y="235" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Right to complete erasure</text>
  <rect x="45" y="255" width="135" height="55" rx="4" fill="#F0F9FF"/>
  <text x="112" y="278" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" fill="#0369A1" text-anchor="middle">Right to Grievance</text>
  <text x="112" y="295" font-family="system-ui, sans-serif" font-size="8" fill="#64748B" text-anchor="middle">Direct appeal to Data Board</text>
  <!-- Pillar 2: Data Fiduciary (Company) -->
  <rect x="215" y="95" width="170" height="230" rx="8" fill="#FFFFFF" stroke="#059669" stroke-width="1.5"/>
  <rect x="230" y="105" width="140" height="24" rx="4" fill="#ECFDF5"/>
  <text x="300" y="121" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#047857" text-anchor="middle">DATA FIDUCIARY</text>
  <text x="300" y="150" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#0F172A" text-anchor="middle">Company Compliance</text>
  <text x="230" y="175" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Purpose limitation rule</text>
  <text x="230" y="195" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Reasonable security</text>
  <text x="230" y="215" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Delete data when done</text>
  <text x="230" y="235" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Appoint Grievance Officer</text>
  <rect x="230" y="255" width="140" height="55" rx="4" fill="#FEF2F2"/>
  <text x="300" y="278" font-family="system-ui, sans-serif" font-size="9" font-weight="800" fill="#DC2626" text-anchor="middle">Up to &#8377;250 Crores</text>
  <text x="300" y="295" font-family="system-ui, sans-serif" font-size="8" fill="#991B1B" text-anchor="middle">Heavy penalties for leaks</text>
  <!-- Pillar 3: CERT-In National Shield -->
  <rect x="405" y="95" width="165" height="230" rx="8" fill="#FFFFFF" stroke="#D97706" stroke-width="1.5"/>
  <rect x="420" y="105" width="135" height="24" rx="4" fill="#FEF3C7"/>
  <text x="487" y="121" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#B45309" text-anchor="middle">CERT-In MANDATE</text>
  <text x="487" y="150" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#0F172A" text-anchor="middle">National Defense</text>
  <circle cx="487" cy="190" r="26" fill="#FFFBEB" stroke="#D97706" stroke-width="2"/>
  <text x="487" y="195" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#B45309" text-anchor="middle">6 HRS</text>
  <text x="420" y="235" font-family="system-ui, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Mandatory incident reporting</text>
  <text x="420" y="250" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">All cyber attacks must be</text>
  <text x="420" y="265" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">reported to government</text>
  <rect x="420" y="275" width="135" height="35" rx="4" fill="#FFFBEB"/>
  <text x="487" y="297" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" fill="#B45309" text-anchor="middle">cert-in.org.in</text>
</svg>"""
    },
    # 90
    {
        "num": "90",
        "index": "41",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Incident Redressal",
        "title": "Incident Reporting: National 1930 Helpline",
        "subtitle": "How to freeze stolen money during the 'Golden Hour', filing complaints on cybercrime.gov.in, and evidence preservation standards.",
        "analogy_title": "Calling 100 for Burglary vs. 1930 for Cyber Crime",
        "analogy_text": "If a burglar breaks into your house, you call 100 for police response. If a cyber criminal tricks you into sharing an OTP and drains your bank balance, <strong>dialing 1930 immediately is your emergency lifeline</strong> &mdash; it alerts the national banking switch to freeze the stolen funds before the thief can withdraw them at an ATM.",
        "steps": [
            ("1", "The 'Golden Hour' Action", "The first 1 to 2 hours after a fraudulent transaction is critical. Calling 1930 triggers an automated freeze across recipient bank accounts."),
            ("2", "cybercrime.gov.in Portal", "File a formal legal complaint online. Upload screenshots of transaction SMS, sender phone numbers, UPI reference numbers, and URLs."),
            ("3", "Evidence Preservation", "Never delete transaction SMS, WhatsApp chats, or call records. These are legally recognized digital evidence under the Indian Evidence Act.")
        ],
        "rule": "Emergency Memory: Save 1930 into your phone contacts right now under 'Cyber Crime Emergency'. When financial fraud occurs, every single minute counts.",
        "fig_title": "Figure 41 &bull; The National 1930 Emergency Freeze Workflow",
        "takeaway": "Key Takeaway: Call 1930 in the Golden Hour; file on cybercrime.gov.in; preserve all digital evidence.",
        "notes": "Explain how the Citizen Financial Cyber Fraud Reporting System operates seamlessly across Indian commercial banks.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Emergency Step 1: Call 1930 -->
  <rect x="25" y="45" width="165" height="270" rx="10" fill="#FEF2F2" stroke="#EF4444" stroke-width="2"/>
  <rect x="40" y="60" width="70" height="24" rx="4" fill="#FEE2E2"/>
  <text x="75" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">STEP 1</text>
  <text x="40" y="110" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#B91C1C">DIAL 1930</text>
  <circle cx="107" cy="165" r="30" fill="#FFFFFF" stroke="#EF4444" stroke-width="2"/>
  <text x="107" y="172" font-family="system-ui, sans-serif" font-size="15" font-weight="800" fill="#DC2626" text-anchor="middle">1930</text>
  <text x="40" y="215" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#DC2626">Golden Hour Call</text>
  <text x="40" y="235" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569">&bull; Call within 1&ndash;2 hours</text>
  <text x="40" y="250" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569">&bull; State bank name &amp; UPI ID</text>
  <text x="40" y="265" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569">&bull; Provide transaction UTR</text>
  <!-- Arrow 1 -->
  <line x1="190" y1="170" x2="215" y2="170" stroke="#EF4444" stroke-width="3" stroke-linecap="round"/>
  <!-- Step 2: Automated Bank Freeze -->
  <rect x="215" y="45" width="170" height="270" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="2"/>
  <rect x="230" y="60" width="70" height="24" rx="4" fill="#E0F2FE"/>
  <text x="265" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0369A1" text-anchor="middle">STEP 2</text>
  <text x="230" y="110" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#0F172A">FUNDS FREEZE</text>
  <circle cx="300" cy="165" r="30" fill="#F0F9FF" stroke="#0284C7" stroke-width="2"/>
  <text x="300" y="172" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#0284C7" text-anchor="middle">FREEZE</text>
  <text x="230" y="215" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0284C7">National Switch Alert</text>
  <text x="230" y="235" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569">&bull; MHA system alerts banks</text>
  <text x="230" y="250" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569">&bull; Money frozen in scammer A/C</text>
  <text x="230" y="265" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569">&bull; Blocks ATM cash withdrawal</text>
  <!-- Arrow 2 -->
  <line x1="385" y1="170" x2="410" y2="170" stroke="#059669" stroke-width="3" stroke-linecap="round"/>
  <!-- Step 3: Formal Complaint -->
  <rect x="410" y="45" width="165" height="270" rx="10" fill="#ECFDF5" stroke="#059669" stroke-width="2"/>
  <rect x="425" y="60" width="70" height="24" rx="4" fill="#D1FAE5"/>
  <text x="460" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#065F46" text-anchor="middle">STEP 3</text>
  <text x="425" y="110" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#047857">cybercrime.gov.in</text>
  <circle cx="492" cy="165" r="30" fill="#FFFFFF" stroke="#059669" stroke-width="2"/>
  <text x="492" y="172" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#047857" text-anchor="middle">FIR</text>
  <text x="425" y="215" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#047857">Formal FIR Filed</text>
  <text x="425" y="235" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569">&bull; Upload SMS screenshots</text>
  <text x="425" y="250" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569">&bull; Upload bank statements</text>
  <text x="425" y="265" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569">&bull; Court order returns money</text>
</svg>"""
    },
    # 91
    {
        "num": "91",
        "index": "42",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Course Capstone",
        "title": "Career Capstone: Personal Cyber Defense Protocol",
        "subtitle": "Synthesizing all competencies from Units 4 and 5 into an actionable 7-layer daily security habit for workplace and career readiness.",
        "analogy_title": "Pre-Flight Pilot Checklist Before Every Journey",
        "analogy_text": "Commercial airline pilots do not rely on memory; before every flight, they walk through a <strong>rigorous multi-point safety checklist</strong>. As an undergraduate entering the digital workforce, following your personal cyber defense checklist guarantees you will never fall victim to online extortion or workplace data loss.",
        "steps": [
            ("1", "Authentication Shield", "Use unique 16+ character passwords via Bitwarden + Enable App-based 2FA (Google Authenticator) on all email and banking."),
            ("2", "System & Network Hygiene", "Keep Windows automatic updates ON + Never connect to public Wi-Fi without VPN + Use uBlock Origin on all browsers."),
            ("3", "Backup & Vigilance Habit", "Follow the 3-2-1 backup model (Cloud + USB) + Never click unverified email links + Never disclose OTPs to anyone.")
        ],
        "rule": "Graduate Readiness Certification: Mastering these practical skills transforms you from a vulnerable casual internet user into a trusted, cyber-literate corporate professional ready for 2026 employment.",
        "fig_title": "Figure 42 &bull; The 7-Layer Student Cyber Defense Shield",
        "takeaway": "Key Takeaway: Unique Passwords + 2FA + Windows Updates + 3-2-1 Backups + VPN + Vigilance = Invincible.",
        "notes": "Congratulate students on completing the course and emphasize that digital literacy is a continuous lifetime practice.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Master Capstone 7-Layer Shield -->
  <text x="300" y="45" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#0F172A" text-anchor="middle">THE 7-LAYER STUDENT DEFENSE SHIELD</text>
  <!-- Center Hexagon / Shield Badge -->
  <circle cx="300" cy="180" r="45" fill="#059669"/>
  <text x="300" y="176" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#FFFFFF" text-anchor="middle">CAREER</text>
  <text x="300" y="194" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#D1FAE5" text-anchor="middle">READY</text>
  <!-- Orbiting 6 Badges -->
  <!-- 1. Passwords (Top Left) -->
  <rect x="40" y="65" width="160" height="55" rx="6" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
  <text x="120" y="88" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#0284C7" text-anchor="middle">1. STRONG PASSWORDS</text>
  <text x="120" y="105" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Password Manager &bull; Passkeys</text>
  <!-- 2. 2FA (Top Right) -->
  <rect x="400" y="65" width="160" height="55" rx="6" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
  <text x="480" y="88" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#0284C7" text-anchor="middle">2. MULTI-FACTOR (MFA)</text>
  <text x="480" y="105" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Authenticator App &bull; No SMS</text>
  <!-- 3. Updates (Mid Left) -->
  <rect x="30" y="152" width="160" height="55" rx="6" fill="#FFFFFF" stroke="#059669" stroke-width="1.5"/>
  <text x="110" y="175" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#059669" text-anchor="middle">3. AUTO PATCHING</text>
  <text x="110" y="192" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Windows Updates &bull; Chrome</text>
  <!-- 4. 3-2-1 Backups (Mid Right) -->
  <rect x="410" y="152" width="160" height="55" rx="6" fill="#FFFFFF" stroke="#059669" stroke-width="1.5"/>
  <text x="490" y="175" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#059669" text-anchor="middle">4. 3-2-1 BACKUPS</text>
  <text x="490" y="192" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Cloud Drive + Offline USB</text>
  <!-- 5. Phishing Hover (Bottom Left) -->
  <rect x="40" y="240" width="160" height="55" rx="6" fill="#FFFFFF" stroke="#D97706" stroke-width="1.5"/>
  <text x="120" y="263" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#D97706" text-anchor="middle">5. URL HOVER CHECK</text>
  <text x="120" y="280" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Inspect links &bull; Never panic</text>
  <!-- 6. VPN on Public Wi-Fi (Bottom Right) -->
  <rect x="400" y="240" width="160" height="55" rx="6" fill="#FFFFFF" stroke="#D97706" stroke-width="1.5"/>
  <text x="480" y="263" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#D97706" text-anchor="middle">6. SECURE WI-FI &amp; VPN</text>
  <text x="480" y="280" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">AES Tunnel &bull; No evil twins</text>
  <!-- Bottom Banner -->
  <rect x="30" y="315" width="540" height="32" rx="6" fill="#0F172A"/>
  <text x="300" y="335" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#38BDF8" text-anchor="middle">7. EMERGENCY PREPAREDNESS: Save National 1930 &bull; File on cybercrime.gov.in</text>
</svg>"""
    }
]

print(f"data_unit5 part 3 initialized with {len(unit5_part3_topics)} topics.")
