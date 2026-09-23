"""
Unit 5 Data Part 1: Topics 71 to 77 (7 Topics)
Cyber Threat Landscape, Taxonomy, Viruses, Worms, Trojans, Spam & Ransomware
"""

unit5_part1_topics = [
    # 71
    {
        "num": "71",
        "index": "22",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Threat Landscape",
        "title": "Cyber Threat Landscape & Digital Footprints",
        "subtitle": "Understanding what the internet remembers about you: passive vs. active footprints, canvas fingerprinting, and pre-employment audits.",
        "analogy_title": "Footprints in Wet Cement That Never Wash Away",
        "analogy_text": "Walking on a sandy beach leaves footprints that ocean waves wash away. The <strong>internet is not sand; it is wet cement</strong>. Every social media comment, late-night search, and leaked password sets into stone permanently &mdash; even if you click 'delete' on your phone.",
        "steps": [
            ("1", "Active Footprint", "Data you intentionally share online: photos on Instagram, resumes on job portals, comments on YouTube."),
            ("2", "Passive Footprint", "Data harvested invisibly: your exact IP location, device model, battery percentage, screen resolution, and browsing speed."),
            ("3", "Browser Fingerprinting", "Websites draw an invisible canvas graphic to identify your unique graphics card, tracking you even without cookies!")
        ],
        "rule": "Pre-Placement Audit: Search your full name in quotes inside an Incognito window: `\"Hari Vignesh\"`. If old forgotten social profiles or inappropriate images appear, delete them before recruiters search your name.",
        "fig_title": "Figure 22 &bull; Active vs. Passive Digital Footprint",
        "takeaway": "Key Takeaway: The internet never forgets. Audit privacy settings and minimize public PII.",
        "notes": "Explain to students that recruiters at top tech firms routinely check social media histories of final candidates.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Active Footprint Card -->
  <rect x="30" y="45" width="255" height="270" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="2"/>
  <rect x="45" y="60" width="130" height="24" rx="4" fill="#E0F2FE"/>
  <text x="110" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0369A1" text-anchor="middle">ACTIVE FOOTPRINT</text>
  <text x="45" y="105" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#0F172A">You Knowingly Share</text>
  <rect x="45" y="120" width="225" height="110" rx="6" fill="#F8FAFC" stroke="#BAE6FD"/>
  <text x="55" y="145" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; Photos uploaded to social media</text>
  <text x="55" y="165" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; Resumes submitted to job portals</text>
  <text x="55" y="185" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; Blog posts, tweets &amp; forum replies</text>
  <text x="55" y="205" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; Online survey &amp; contest entries</text>
  <rect x="45" y="245" width="225" height="50" rx="6" fill="#F0F9FF"/>
  <text x="157" y="268" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#0369A1" text-anchor="middle">Control: High</text>
  <text x="157" y="284" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">You choose what to upload and when to stop</text>
  <!-- Passive Footprint Card -->
  <rect x="315" y="45" width="255" height="270" rx="10" fill="#FFFFFF" stroke="#D97706" stroke-width="2"/>
  <rect x="330" y="60" width="130" height="24" rx="4" fill="#FEF3C7"/>
  <text x="395" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#B45309" text-anchor="middle">PASSIVE FOOTPRINT</text>
  <text x="330" y="105" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#0F172A">Harvested Invisibly</text>
  <rect x="330" y="120" width="225" height="110" rx="6" fill="#F8FAFC" stroke="#FDE68A"/>
  <text x="340" y="145" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; IP address &amp; geo-location tracking</text>
  <text x="340" y="165" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; Browser canvas hardware fingerprint</text>
  <text x="340" y="185" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; Device battery &amp; screen dimensions</text>
  <text x="340" y="205" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; Click heatmaps &amp; time spent per page</text>
  <rect x="330" y="245" width="225" height="50" rx="6" fill="#FFFBEB"/>
  <text x="442" y="268" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#B45309" text-anchor="middle">Control: Low to Moderate</text>
  <text x="442" y="284" font-family="system-ui, sans-serif" font-size="8.5" fill="#78350F" text-anchor="middle">Requires privacy extensions, VPNs &amp; ad-blockers</text>
</svg>"""
    },
    # 72
    {
        "num": "72",
        "index": "23",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Threat Taxonomy",
        "title": "Threat Anatomy: Vulnerabilities, Exploits & Attackers",
        "subtitle": "The foundational triad of cyber defense: understanding the critical difference between a security flaw, a hacker tool, and an adversary.",
        "analogy_title": "An Unlocked Window, a Crowbar, and a Burglar",
        "analogy_text": "A <strong>Vulnerability</strong> is leaving your ground-floor window unlocked by accident. An <strong>Exploit</strong> is the crowbar a criminal buys from the hardware store to pry the window open. A <strong>Threat Actor</strong> is the burglar walking down the street looking for open windows.",
        "steps": [
            ("1", "Vulnerability (Software Flaw)", "A bug or configuration mistake in Windows, Chrome, or your home router that hackers can target."),
            ("2", "Exploit (Weaponized Code)", "A specialized program engineered by hackers that takes advantage of the vulnerability to break into the PC."),
            ("3", "Threat Actor Spectrum", "Ranges from amateur teenagers ('Script Kiddies') to billion-dollar cybercrime syndicates and military intelligence units.")
        ],
        "rule": "The Patching Defense: When Microsoft releases a security update on 'Patch Tuesday', install it immediately! Updates lock the window so the hacker's crowbar bounces off harmlessly.",
        "fig_title": "Figure 23 &bull; The Cyber Threat Triad",
        "takeaway": "Key Takeaway: Vulnerability (The Hole) + Exploit (The Tool) + Threat Actor (The Hacker) = Cyber Breach.",
        "notes": "Ensure non-CS students do not confuse vulnerabilities with viruses; vulnerabilities are weaknesses, viruses are malware.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- The Threat Triangle -->
  <circle cx="300" cy="180" r="110" fill="none" stroke="#E2E8F0" stroke-width="2" stroke-dasharray="6,4"/>
  <!-- Node 1: Vulnerability (Top) -->
  <rect x="210" y="30" width="180" height="85" rx="8" fill="#FFFFFF" stroke="#EF4444" stroke-width="2"/>
  <rect x="225" y="42" width="150" height="20" rx="3" fill="#FEE2E2"/>
  <text x="300" y="56" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#991B1B" text-anchor="middle">VULNERABILITY (THE FLAW)</text>
  <text x="300" y="80" font-family="system-ui, sans-serif" font-size="9" fill="#0F172A" text-anchor="middle">Software bug / unpatched OS</text>
  <text x="300" y="95" font-family="system-ui, sans-serif" font-size="8" fill="#DC2626" text-anchor="middle">Analogy: The Unlocked Window</text>
  <!-- Node 2: Exploit (Bottom Left) -->
  <rect x="30" y="225" width="180" height="85" rx="8" fill="#FFFFFF" stroke="#D97706" stroke-width="2"/>
  <rect x="45" y="237" width="150" height="20" rx="3" fill="#FEF3C7"/>
  <text x="120" y="251" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#B45309" text-anchor="middle">EXPLOIT (THE TOOL)</text>
  <text x="120" y="275" font-family="system-ui, sans-serif" font-size="9" fill="#0F172A" text-anchor="middle">Script or malware payload</text>
  <text x="120" y="290" font-family="system-ui, sans-serif" font-size="8" fill="#B45309" text-anchor="middle">Analogy: The Burglar's Crowbar</text>
  <!-- Node 3: Threat Actor (Bottom Right) -->
  <rect x="390" y="225" width="180" height="85" rx="8" fill="#FFFFFF" stroke="#7C3AED" stroke-width="2"/>
  <rect x="405" y="237" width="150" height="20" rx="3" fill="#EDE9FE"/>
  <text x="480" y="251" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#6D28D9" text-anchor="middle">THREAT ACTOR (THE PERSON)</text>
  <text x="480" y="275" font-family="system-ui, sans-serif" font-size="9" fill="#0F172A" text-anchor="middle">Criminal syndicate / Hacker</text>
  <text x="480" y="290" font-family="system-ui, sans-serif" font-size="8" fill="#6D28D9" text-anchor="middle">Analogy: The Burglar Outside</text>
  <!-- Center Breach Result -->
  <circle cx="300" cy="180" r="38" fill="#FEF2F2" stroke="#EF4444" stroke-width="2"/>
  <text x="300" y="176" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#DC2626" text-anchor="middle">DATA</text>
  <text x="300" y="192" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#DC2626" text-anchor="middle">BREACH</text>
</svg>"""
    },
    # 73
    {
        "num": "73",
        "index": "24",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Malware Taxonomy",
        "title": "Computer Viruses: Parasites & Macro Infection",
        "subtitle": "Why a computer virus cannot replicate without human help, how macro viruses infect Word and Excel documents, and how to disinfect your PC.",
        "analogy_title": "A Biological Flu Virus Needing a Human Sneeze",
        "analogy_text": "A biological influenza virus cannot fly across a room on its own; it needs a human host to cough or sneeze. Similarly, a <strong>computer virus is parasitic</strong>: it injects itself into a clean application (like a game or Word doc) and <strong>requires human clicking</strong> to wake up and spread.",
        "steps": [
            ("1", "Host File Attachment", "The virus attaches its malicious code to legitimate executable files (`.exe`) or document templates (`.docm`)."),
            ("2", "Execution Trigger", "When a student double-clicks the infected file, the host program runs, but the virus executes first in memory."),
            ("3", "Replication & Payload", "The virus searches your hard drive for other `.exe` files, corrupts them, and damages your operating system.")
        ],
        "rule": "Office Security Rule: NEVER click 'Enable Content' or 'Enable Macros' on a downloaded Word or Excel file from the internet! Macro viruses use this button to bypass Windows defenses.",
        "fig_title": "Figure 24 &bull; Parasitic Virus Injection Lifecycle",
        "takeaway": "Key Takeaway: A virus requires a host file and human execution; never enable macros on unverified docs.",
        "notes": "Contrast viruses with worms; viruses need a human to double-click, whereas worms spread autonomously.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Clean Host Program -->
  <rect x="30" y="45" width="160" height="270" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
  <rect x="45" y="60" width="130" height="24" rx="4" fill="#E0F2FE"/>
  <text x="110" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0369A1" text-anchor="middle">CLEAN PROGRAM</text>
  <rect x="45" y="100" width="130" height="90" rx="6" fill="#F8FAFC" stroke="#CBD5E1"/>
  <text x="110" y="130" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">Resume.docx</text>
  <text x="110" y="150" font-family="system-ui, sans-serif" font-size="9" fill="#059669" text-anchor="middle">&check; Uninfected File</text>
  <text x="110" y="165" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Clean legitimate code</text>
  <rect x="45" y="210" width="130" height="85" rx="6" fill="#F0FDF4"/>
  <text x="110" y="235" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#166534" text-anchor="middle">Harmless State</text>
  <text x="110" y="255" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">No damage while inert on drive</text>
  <!-- Arrow 1: Infection Injection -->
  <line x1="190" y1="145" x2="225" y2="145" stroke="#EF4444" stroke-width="3" stroke-linecap="round"/>
  <!-- Parasitic Injection (Middle) -->
  <rect x="225" y="45" width="150" height="270" rx="10" fill="#FEF2F2" stroke="#EF4444" stroke-width="2"/>
  <rect x="235" y="60" width="130" height="24" rx="4" fill="#FEE2E2"/>
  <text x="300" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#991B1B" text-anchor="middle">PARASITIC VIRUS</text>
  <circle cx="300" cy="130" r="30" fill="#FFFFFF" stroke="#EF4444" stroke-width="2"/>
  <text x="300" y="126" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#DC2626" text-anchor="middle">VIRUS</text>
  <text x="300" y="142" font-family="system-ui, sans-serif" font-size="8" fill="#7F1D1D" text-anchor="middle">CODE</text>
  <rect x="235" y="180" width="130" height="115" rx="6" fill="#FFFFFF" stroke="#FECACA"/>
  <text x="300" y="200" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#B91C1C" text-anchor="middle">Infection Vector</text>
  <text x="300" y="220" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569" text-anchor="middle">Injected into macro / header</text>
  <text x="300" y="240" font-family="system-ui, sans-serif" font-size="8.5" fill="#DC2626" text-anchor="middle">Requires User Click!</text>
  <text x="300" y="260" font-family="system-ui, sans-serif" font-size="8" fill="#64748B" text-anchor="middle">Cannot spread on its own</text>
  <!-- Arrow 2: Execution -->
  <line x1="375" y1="145" x2="410" y2="145" stroke="#EF4444" stroke-width="3" stroke-linecap="round"/>
  <!-- Infected System (Right) -->
  <rect x="410" y="45" width="160" height="270" rx="10" fill="#FFFFFF" stroke="#EF4444" stroke-width="1.5"/>
  <rect x="425" y="60" width="130" height="24" rx="4" fill="#FEE2E2"/>
  <text x="490" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#B91C1C" text-anchor="middle">INFECTED HOST</text>
  <rect x="425" y="100" width="130" height="90" rx="6" fill="#FEF2F2" stroke="#FECACA"/>
  <text x="490" y="130" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#991B1B" text-anchor="middle">User Double Clicks!</text>
  <text x="490" y="150" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626" text-anchor="middle">Virus Awakens in RAM</text>
  <text x="490" y="168" font-family="system-ui, sans-serif" font-size="8.5" fill="#7F1D1D" text-anchor="middle">Infects all other .exe files</text>
  <rect x="425" y="210" width="130" height="85" rx="6" fill="#FEE2E2"/>
  <text x="490" y="235" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#991B1B" text-anchor="middle">Payload Triggered</text>
  <text x="490" y="255" font-family="system-ui, sans-serif" font-size="8.5" fill="#7F1D1D" text-anchor="middle">Corrupts boot sectors, files</text>
  <text x="490" y="270" font-family="system-ui, sans-serif" font-size="8.5" fill="#B91C1C" text-anchor="middle">Steals login credentials</text>
</svg>"""
    },
    # 74
    {
        "num": "74",
        "index": "25",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Malware Taxonomy",
        "title": "Computer Worms: Autonomous Network Spread",
        "subtitle": "How worms like Morris, ILOVEYOU, and Stuxnet propagate across network cables without human action or host files.",
        "analogy_title": "An Uninvited Pest Crawling Through Open Pipes",
        "analogy_text": "Unlike a virus (which needs you to click it), a <strong>computer worm is like a robotic pest crawling through open plumbing pipes</strong> into your apartment. If your computer is connected to the network without a firewall, the worm enters automatically without you touching a single key.",
        "steps": [
            ("1", "Port Scanning", "The worm scans the local Wi-Fi or internet for computers with open unpatched network ports (e.g. SMB port 445)."),
            ("2", "Zero-Click Exploitation", "It transmits an exploit packet that triggers a buffer overflow, granting remote system access."),
            ("3", "Autonomous Self-Replication", "It downloads a copy of itself onto the victim PC and immediately starts scanning for the next victim.")
        ],
        "rule": "Primary Worm Defense: Keep Windows Automatic Updates switched ON! Worms exploit known security holes. If your system is patched, the worm cannot enter.",
        "fig_title": "Figure 25 &bull; Autonomous Network Worm Propagation",
        "takeaway": "Key Takeaway: Worms are standalone (no host file needed) and spread with ZERO human interaction.",
        "notes": "Discuss Stuxnet (2010), the first military-grade cyber worm that physically destroyed Iranian nuclear centrifuges.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Central Network Cable (The Pipe) -->
  <line x1="50" y1="180" x2="550" y2="180" stroke="#0284C7" stroke-width="8" stroke-linecap="round"/>
  <text x="300" y="165" font-family="monospace" font-size="11" font-weight="700" fill="#0369A1" text-anchor="middle">LOCAL AREA NETWORK (LAN / WI-FI CABLE)</text>
  <!-- Computer 1 (Patient Zero) -->
  <rect x="50" y="40" width="130" height="95" rx="8" fill="#FEE2E2" stroke="#EF4444" stroke-width="2"/>
  <text x="115" y="65" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">PC A (INFECTED)</text>
  <circle cx="115" cy="95" r="16" fill="#DC2626"/>
  <text x="115" y="100" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#FFFFFF" text-anchor="middle">WORM</text>
  <line x1="115" y1="135" x2="115" y2="176" stroke="#EF4444" stroke-width="3"/>
  <!-- Computer 2 (Target 1) -->
  <rect x="235" y="220" width="130" height="95" rx="8" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5"/>
  <text x="300" y="245" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">PC B (INFECTED)</text>
  <text x="300" y="270" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569" text-anchor="middle">No human touched it!</text>
  <text x="300" y="285" font-family="system-ui, sans-serif" font-size="8.5" fill="#DC2626" text-anchor="middle">Auto-infected via port 445</text>
  <line x1="300" y1="184" x2="300" y2="220" stroke="#EF4444" stroke-width="3"/>
  <!-- Computer 3 (Target 2) -->
  <rect x="420" y="40" width="130" height="95" rx="8" fill="#FEF2F2" stroke="#EF4444" stroke-width="1.5"/>
  <text x="485" y="65" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">PC C (INFECTED)</text>
  <text x="485" y="90" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569" text-anchor="middle">Worm replicates again</text>
  <text x="485" y="105" font-family="system-ui, sans-serif" font-size="8.5" fill="#DC2626" text-anchor="middle">Scans 100 new PCs</text>
  <line x1="485" y1="135" x2="485" y2="176" stroke="#EF4444" stroke-width="3"/>
  <!-- Bottom Banner: Contrast Virus vs Worm -->
  <rect x="50" y="325" width="500" height="25" rx="4" fill="#E0F2FE"/>
  <text x="300" y="342" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#0369A1" text-anchor="middle">CRITICAL DISTINCTION: A Virus needs Human Action; A Worm crawls by itself!</text>
</svg>"""
    },
    # 75
    {
        "num": "75",
        "index": "26",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Malware Taxonomy",
        "title": "Trojan Horses: Masquerading Software & RATs",
        "subtitle": "How malware disguises itself inside free utilities, games, or PDFs, and how Remote Access Trojans (RATs) give hackers complete webcam and file control.",
        "analogy_title": "The Mythological Wooden Horse of Ancient Troy",
        "analogy_text": "In ancient history, Greek soldiers hid inside a giant decorative wooden horse. The Trojans wheeled it inside their fortress gates as a gift; at night, soldiers emerged and seized the city. <strong>A digital Trojan pretends to be a free video game or PDF reader</strong>, but sneaks a hacker inside your laptop.",
        "steps": [
            ("1", "Deceptive Camouflage", "Malware is disguised as a pirate game, free movie player, or fake PDF invoice (`invoice.pdf.exe`)."),
            ("2", "Voluntary Installation", "The user willingly runs the installer, granting administrator permission past security dialogs."),
            ("3", "Remote Access Trojan (RAT)", "The hidden payload establishes an encrypted reverse shell to the attacker, giving them total control over your webcam, mic, and files.")
        ],
        "rule": "Extension Audit: Always enable 'File name extensions' in Windows File Explorer! Attackers disguise Trojans as `syllabus.pdf.exe` &mdash; Windows hides `.exe` by default, tricking you into double-clicking!",
        "fig_title": "Figure 26 &bull; The Anatomy of a Trojan Horse Masquerade",
        "takeaway": "Key Takeaway: Trojans disguise malware as useful apps; RATs give attackers total remote control.",
        "notes": "Teach students how to inspect Task Manager Publisher column to check if background processes are legitimately signed.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- The Trojan Package (Exterior) -->
  <rect x="30" y="45" width="250" height="270" rx="10" fill="#FFFFFF" stroke="#059669" stroke-width="2"/>
  <rect x="45" y="60" width="130" height="24" rx="4" fill="#ECFDF5"/>
  <text x="110" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">OUTSIDE APPEARANCE</text>
  <text x="45" y="105" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#0F172A">"Free Game / PDF Tool"</text>
  <rect x="45" y="125" width="220" height="95" rx="6" fill="#F8FAFC" stroke="#A7F3D0"/>
  <text x="155" y="150" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#059669" text-anchor="middle">&check; Looks 100% Genuine</text>
  <text x="155" y="170" font-family="system-ui, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Attractive icon, clean interface</text>
  <text x="155" y="190" font-family="system-ui, sans-serif" font-size="9" fill="#475569" text-anchor="middle">Promises free cracked software</text>
  <rect x="45" y="235" width="220" height="60" rx="6" fill="#F0FDF4"/>
  <text x="155" y="258" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#047857" text-anchor="middle">User installs willingly</text>
  <text x="155" y="275" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Bypasses firewall because YOU clicked 'Yes'</text>
  <!-- Arrow: Hidden Interior -->
  <line x1="280" y1="180" x2="320" y2="180" stroke="#EF4444" stroke-width="4" stroke-linecap="round"/>
  <!-- The Hidden Payload (Interior RAT) -->
  <rect x="320" y="45" width="250" height="270" rx="10" fill="#FEF2F2" stroke="#EF4444" stroke-width="2"/>
  <rect x="335" y="60" width="130" height="24" rx="4" fill="#FEE2E2"/>
  <text x="400" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">HIDDEN REALITY</text>
  <text x="335" y="105" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#B91C1C">Remote Access Trojan</text>
  <rect x="335" y="125" width="220" height="95" rx="6" fill="#FFFFFF" stroke="#FECACA"/>
  <text x="345" y="150" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">&bull; Secret backdoor reverse connection</text>
  <text x="345" y="170" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">&bull; Silently switches on your webcam</text>
  <text x="345" y="190" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">&bull; Logs bank passwords &amp; keypresses</text>
  <text x="345" y="210" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">&bull; Hacker downloads all private photos</text>
  <rect x="335" y="235" width="220" height="60" rx="6" fill="#FEE2E2"/>
  <text x="445" y="258" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#991B1B" text-anchor="middle">Outcome: Total PC Takeover</text>
  <text x="445" y="275" font-family="system-ui, sans-serif" font-size="8.5" fill="#7F1D1D" text-anchor="middle">Hacker has administrator control of your PC</text>
</svg>"""
    },
    # 76
    {
        "num": "76",
        "index": "27",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Threat Vectors",
        "title": "Email Spam: Botnet Infrastructure & Bayesian Filters",
        "subtitle": "The economics of mass unsolicited email, zombie botnets, statistical Bayesian filtering, and why clicking 'Unsubscribe' on spam is dangerous.",
        "analogy_title": "Billions of Junk Paper Flyers Dropped on Every Porch",
        "analogy_text": "Printing 100 million physical paper advertisements and mailing them to homes costs millions of rupees. Sending 100 million digital spam emails costs virtually nothing ($50). Even if only <strong>1 person in 100,000 falls for a scam, the criminal makes massive profit</strong>.",
        "steps": [
            ("1", "Zombie Botnets", "Attackers infect 50,000 vulnerable home routers and laptops to blast billions of spam emails without using their own servers."),
            ("2", "Bayesian Probability Scoring", "Spam filters analyze words ('lottery', 'winner', 'claim funds', 'wire') to calculate the mathematical likelihood of spam."),
            ("3", "The 'Unsubscribe' Trap", "Clicking 'Unsubscribe' on criminal spam alerts the attacker that your email address is active, multiplying your spam 10-fold!")
        ],
        "rule": "Inbox Hygiene: Never click 'Unsubscribe' on a spam email from an unknown sender. Simply click 'Report Spam' or 'Block Sender' inside Gmail/Outlook.",
        "fig_title": "Figure 27 &bull; Botnet Spam Flooding & Bayesian Filter Gate",
        "takeaway": "Key Takeaway: Spam is driven by zero sending costs; Naive Bayes filters score spam probability; Report Spam, don't Unsubscribe.",
        "notes": "Explain why college mail servers aggressively block IP ranges known for hosting zombie botnets.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Botnet Zombie Army (Left) -->
  <rect x="30" y="45" width="160" height="270" rx="10" fill="#FFFFFF" stroke="#EF4444" stroke-width="1.5"/>
  <rect x="45" y="60" width="130" height="24" rx="4" fill="#FEE2E2"/>
  <text x="110" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">ZOMBIE BOTNET</text>
  <rect x="45" y="95" width="130" height="50" rx="6" fill="#F8FAFC" stroke="#FECACA"/>
  <text x="110" y="115" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#B91C1C" text-anchor="middle">50,000 Infected PCs</text>
  <text x="110" y="130" font-family="system-ui, sans-serif" font-size="8" fill="#64748B" text-anchor="middle">Compromised routers &amp; laptops</text>
  <line x1="110" y1="150" x2="110" y2="190" stroke="#EF4444" stroke-width="3" stroke-dasharray="4,4"/>
  <rect x="45" y="195" width="130" height="105" rx="6" fill="#FEF2F2"/>
  <text x="110" y="215" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#DC2626" text-anchor="middle">100M Spam Blast</text>
  <text x="110" y="235" font-family="system-ui, sans-serif" font-size="8" fill="#7F1D1D" text-anchor="middle">Fake lottery notifications</text>
  <text x="110" y="250" font-family="system-ui, sans-serif" font-size="8" fill="#7F1D1D" text-anchor="middle">Phishing banking links</text>
  <text x="110" y="265" font-family="system-ui, sans-serif" font-size="8" fill="#7F1D1D" text-anchor="middle">Fake crypto investments</text>
  <!-- Arrow: Inbound Blast -->
  <line x1="190" y1="180" x2="230" y2="180" stroke="#EF4444" stroke-width="3" stroke-linecap="round"/>
  <!-- Bayesian Filter (Middle) -->
  <rect x="230" y="45" width="150" height="270" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="2"/>
  <rect x="240" y="60" width="130" height="24" rx="4" fill="#E0F2FE"/>
  <text x="305" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0369A1" text-anchor="middle">BAYESIAN FILTER</text>
  <text x="305" y="115" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0F172A" text-anchor="middle">Word Probability</text>
  <rect x="240" y="130" width="130" height="30" rx="4" fill="#F8FAFC"/>
  <text x="305" y="150" font-family="monospace" font-size="8.5" fill="#DC2626" text-anchor="middle">"winner" &rarr; 98% spam</text>
  <rect x="240" y="165" width="130" height="30" rx="4" fill="#F8FAFC"/>
  <text x="305" y="185" font-family="monospace" font-size="8.5" fill="#DC2626" text-anchor="middle">"urgent PIN" &rarr; 99% spam</text>
  <circle cx="305" cy="235" r="28" fill="#F0F9FF" stroke="#0284C7" stroke-width="2"/>
  <text x="305" y="238" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#0284C7" text-anchor="middle">P(S|W)</text>
  <text x="305" y="250" font-family="system-ui, sans-serif" font-size="8" fill="#64748B" text-anchor="middle">Naive Bayes</text>
  <text x="305" y="295" font-family="system-ui, sans-serif" font-size="8.5" font-weight="600" fill="#0369A1" text-anchor="middle">Calculates Risk</text>
  <!-- Forking Destinations (Right) -->
  <!-- Top: Junk Folder -->
  <rect x="420" y="45" width="150" height="120" rx="8" fill="#FEE2E2" stroke="#EF4444" stroke-width="1.5"/>
  <text x="495" y="70" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#B91C1C" text-anchor="middle">SPAM FOLDER</text>
  <text x="495" y="90" font-family="system-ui, sans-serif" font-size="8.5" fill="#7F1D1D" text-anchor="middle">99.7% of junk filtered</text>
  <text x="495" y="105" font-family="system-ui, sans-serif" font-size="8.5" fill="#7F1D1D" text-anchor="middle">Auto-deleted after 30 days</text>
  <rect x="435" y="120" width="120" height="30" rx="4" fill="#FFFFFF"/>
  <text x="495" y="139" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#DC2626" text-anchor="middle">Never Unsubscribe!</text>
  <!-- Bottom: Clean Inbox -->
  <rect x="420" y="195" width="150" height="120" rx="8" fill="#ECFDF5" stroke="#10B981" stroke-width="1.5"/>
  <text x="495" y="220" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">CLEAN INBOX</text>
  <text x="495" y="240" font-family="system-ui, sans-serif" font-size="8.5" fill="#065F46" text-anchor="middle">Legitimate emails arrive</text>
  <text x="495" y="255" font-family="system-ui, sans-serif" font-size="8.5" fill="#065F46" text-anchor="middle">College &amp; work messages safe</text>
  <rect x="435" y="270" width="120" height="30" rx="4" fill="#FFFFFF"/>
  <text x="495" y="289" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#059669" text-anchor="middle">&check; Verified Delivery</text>
</svg>"""
    },
    # 77
    {
        "num": "77",
        "index": "28",
        "unit": "Unit 5",
        "unit_full": "Unit 5 &bull; Cyber Defense & Law",
        "category": "Malware Threats",
        "title": "Ransomware Extortion & The 3-2-1 Backup Shield",
        "subtitle": "How military-grade AES encryption kidnaps files, the 2017 WannaCry crisis, why ransoms must never be paid, and the 3-2-1 backup protocol.",
        "analogy_title": "A Padlock Snapped on Your File Cabinet",
        "analogy_text": "Imagine a burglar breaks into your office, does not steal your paper files, but <strong>snaps an unbreakable titanium padlock onto your file cabinet</strong> and leaves a note: 'Pay $5,000 in Bitcoin or you will never open your files again.' That is digital ransomware.",
        "steps": [
            ("1", "Silent File Encryption", "Ransomware invisibly encrypts PDFs, Word docs, photos, and databases with unbreakable AES-256 encryption."),
            ("2", "The Extortion Note", "Your desktop wallpaper changes into a red warning screen demanding cryptocurrency within 72 hours."),
            ("3", "The 3-2-1 Backup Shield", "If you have clean offline backups, ransomware has ZERO power over you &mdash; simply wipe the laptop and restore in 20 minutes!")
        ],
        "rule": "Law Enforcement Rule: Police, FBI, and CERT-In advise: NEVER PAY THE RANSOM! In over 50% of cases where victims pay, the criminals take the money and never send the decryption key.",
        "fig_title": "Figure 28 &bull; The 3-2-1 Immutable Backup Architecture",
        "takeaway": "Key Takeaway: 3 copies of data, on 2 different media types, with 1 copy offsite/cloud (3-2-1).",
        "notes": "Discuss WannaCry (2017) which paralyzed 200,000 computers across NHS hospitals in the UK and Indian police stations.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- 3-2-1 Pillars -->
  <!-- 3 Copies -->
  <rect x="30" y="50" width="165" height="240" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="2"/>
  <circle cx="112" cy="95" r="28" fill="#E0F2FE"/>
  <text x="112" y="103" font-family="system-ui, sans-serif" font-size="22" font-weight="800" fill="#0284C7" text-anchor="middle">3</text>
  <text x="112" y="145" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#0F172A" text-anchor="middle">TOTAL COPIES</text>
  <text x="112" y="165" font-family="system-ui, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Never rely on single drive</text>
  <rect x="45" y="185" width="135" height="85" rx="6" fill="#F8FAFC"/>
  <text x="112" y="205" font-family="system-ui, sans-serif" font-size="9" fill="#334155" text-anchor="middle">&bull; 1 Primary working file</text>
  <text x="112" y="225" font-family="system-ui, sans-serif" font-size="9" fill="#334155" text-anchor="middle">&bull; 2 Independent backups</text>
  <text x="112" y="245" font-family="system-ui, sans-serif" font-size="8.5" fill="#0284C7" text-anchor="middle">Reduces loss risk to 0.01%</text>
  <!-- 2 Media Types -->
  <rect x="215" y="50" width="170" height="240" rx="10" fill="#FFFFFF" stroke="#059669" stroke-width="2"/>
  <circle cx="300" cy="95" r="28" fill="#ECFDF5"/>
  <text x="300" y="103" font-family="system-ui, sans-serif" font-size="22" font-weight="800" fill="#059669" text-anchor="middle">2</text>
  <text x="300" y="145" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#0F172A" text-anchor="middle">DIFFERENT MEDIA</text>
  <text x="300" y="165" font-family="system-ui, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Protect against media failure</text>
  <rect x="230" y="185" width="140" height="85" rx="6" fill="#F8FAFC"/>
  <text x="300" y="205" font-family="system-ui, sans-serif" font-size="9" fill="#334155" text-anchor="middle">&bull; Media A: Internal PC SSD</text>
  <text x="300" y="225" font-family="system-ui, sans-serif" font-size="9" fill="#334155" text-anchor="middle">&bull; Media B: External USB HDD</text>
  <text x="300" y="245" font-family="system-ui, sans-serif" font-size="8.5" fill="#059669" text-anchor="middle">Hardware fault isolated</text>
  <!-- 1 Offsite Cloud -->
  <rect x="405" y="50" width="165" height="240" rx="10" fill="#FFFFFF" stroke="#D97706" stroke-width="2"/>
  <circle cx="487" cy="95" r="28" fill="#FEF3C7"/>
  <text x="487" y="103" font-family="system-ui, sans-serif" font-size="22" font-weight="800" fill="#D97706" text-anchor="middle">1</text>
  <text x="487" y="145" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#0F172A" text-anchor="middle">OFFSITE / CLOUD</text>
  <text x="487" y="165" font-family="system-ui, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Geographically separated</text>
  <rect x="420" y="185" width="135" height="85" rx="6" fill="#F8FAFC"/>
  <text x="487" y="205" font-family="system-ui, sans-serif" font-size="9" fill="#334155" text-anchor="middle">&bull; Google Drive / OneDrive</text>
  <text x="487" y="225" font-family="system-ui, sans-serif" font-size="9" fill="#334155" text-anchor="middle">&bull; Immutable cloud vault</text>
  <text x="487" y="245" font-family="system-ui, sans-serif" font-size="8.5" fill="#D97706" text-anchor="middle">Immune to fire, theft &amp; ransomware</text>
  <!-- Bottom Verdict Banner -->
  <rect x="30" y="305" width="540" height="35" rx="6" fill="#1E293B"/>
  <text x="300" y="327" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">RANSOMWARE RESILIENCE: Clean Offsite Backups Render Extortion 100% Worthless!</text>
</svg>"""
    }
]

print(f"data_unit5 part 1 initialized with {len(unit5_part1_topics)} topics.")
