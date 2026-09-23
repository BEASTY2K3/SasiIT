"""
Unit 4 Data: Topics 50 to 70 (21 Topics)
Internet Architecture, Cloud Collaboration & Digital India
"""

unit4_topics = [
    # 50
    {
        "num": "50",
        "index": "01",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "Digital Infrastructure",
        "title": "The Internet & Global Undersea Fiber Mesh",
        "subtitle": "How billions of computers connect across oceans and continents through physical fiber optic cables and the client-server request-response model.",
        "analogy_title": "The Global Highway & Postal Network",
        "analogy_text": "Think of the <strong>Internet as the worldwide system of roads, bridges, and shipping lines</strong>. Just as delivery trucks transport physical packages between warehouses and your home, the Internet moves digital packets of information across undersea fiber cables directly to your screen.",
        "steps": [
            ("1", "Request Initiated", "When you open a website, your device (the Client) sends a structured digital request through your local router or cellular tower."),
            ("2", "Global Routing", "Your request travels through underground fiber and trans-oceanic submarine glass cables as pulses of laser light at over 200,000 km per second."),
            ("3", "Server Response", "A powerful data center computer (the Server) processes your request in milliseconds and transmits the requested web page back to your screen.")
        ],
        "rule": "Workplace Reality: Over 99% of international internet traffic travels through underwater ocean cables, not satellites! A damaged cable in the Red Sea can immediately slow down banking and video conferences.",
        "fig_title": "Figure 01 &bull; Global Internet Architecture",
        "takeaway": "Key Takeaway: The Internet is physical infrastructure; the Client asks, the Server answers.",
        "notes": "Emphasize to non-computer students that the Internet is not invisible magic in the air; it relies on hundreds of physical undersea fiber optic cables laid across ocean floors.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gOcean" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#F0F9FF"/><stop offset="100%" stop-color="#E0F2FE"/></linearGradient>
  </defs>
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Client Device -->
  <rect x="30" y="50" width="160" height="260" rx="10" fill="#FFFFFF" stroke="#BAE6FD" stroke-width="2"/>
  <rect x="45" y="65" width="130" height="28" rx="6" fill="#E0F2FE"/>
  <text x="110" y="83" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0369A1" text-anchor="middle">CLIENT DEVICE</text>
  <circle cx="110" cy="140" r="34" fill="#F0F9FF" stroke="#0284C7" stroke-width="2"/>
  <rect x="92" y="125" width="36" height="24" rx="3" fill="#0284C7"/>
  <rect x="100" y="152" width="20" height="4" rx="1" fill="#64748B"/>
  <text x="110" y="195" font-family="system-ui, sans-serif" font-size="11" font-weight="600" fill="#0F172A" text-anchor="middle">Laptop / Phone</text>
  <text x="110" y="212" font-family="system-ui, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">HTTP GET Request</text>
  <rect x="50" y="240" width="120" height="50" rx="6" fill="#F1F5F9" stroke="#E2E8F0"/>
  <text x="110" y="258" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#334155" text-anchor="middle">Local ISP Drop</text>
  <text x="110" y="274" font-family="system-ui, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Airtel / Jio / Fiber</text>
  <!-- Undersea Mesh -->
  <rect x="210" y="50" width="180" height="260" rx="10" fill="url(#gOcean)" stroke="#BAE6FD" stroke-width="1.5"/>
  <text x="300" y="80" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0284C7" text-anchor="middle">UNDERSEA CABLES</text>
  <path d="M 190 140 C 230 110, 270 170, 310 130 C 350 90, 370 150, 410 140" fill="none" stroke="#0284C7" stroke-width="4" stroke-dasharray="6,4"/>
  <path d="M 190 265 C 240 280, 280 240, 330 270 C 370 290, 380 260, 410 265" fill="none" stroke="#0EA5E9" stroke-width="3"/>
  <circle cx="300" cy="180" r="28" fill="#FFFFFF" stroke="#0284C7" stroke-width="2"/>
  <text x="300" y="176" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#0369A1" text-anchor="middle">550+</text>
  <text x="300" y="193" font-family="system-ui, sans-serif" font-size="9" font-weight="600" fill="#64748B" text-anchor="middle">Ocean Cables</text>
  <text x="300" y="225" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0284C7" text-anchor="middle">Speed: 200,000 km/s</text>
  <!-- Cloud Server -->
  <rect x="410" y="50" width="160" height="260" rx="10" fill="#FFFFFF" stroke="#BAE6FD" stroke-width="2"/>
  <rect x="425" y="65" width="130" height="28" rx="6" fill="#E0F2FE"/>
  <text x="490" y="83" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0369A1" text-anchor="middle">CLOUD SERVER</text>
  <rect x="450" y="115" width="80" height="65" rx="6" fill="#0369A1"/>
  <line x1="458" y1="130" x2="522" y2="130" stroke="#38BDF8" stroke-width="3"/>
  <line x1="458" y1="145" x2="522" y2="145" stroke="#38BDF8" stroke-width="3"/>
  <line x1="458" y1="160" x2="522" y2="160" stroke="#38BDF8" stroke-width="3"/>
  <circle cx="515" cy="130" r="2" fill="#22C55E"/>
  <circle cx="515" cy="145" r="2" fill="#22C55E"/>
  <circle cx="515" cy="160" r="2" fill="#22C55E"/>
  <text x="490" y="200" font-family="system-ui, sans-serif" font-size="11" font-weight="600" fill="#0F172A" text-anchor="middle">Host Data Center</text>
  <text x="490" y="216" font-family="system-ui, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Google / AWS / Cloud</text>
  <rect x="430" y="240" width="120" height="50" rx="6" fill="#F0FDF4" stroke="#BBF7D0"/>
  <text x="490" y="258" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#166534" text-anchor="middle">HTTP/200 OK</text>
  <text x="490" y="274" font-family="system-ui, sans-serif" font-size="9" fill="#15803D" text-anchor="middle">HTML, CSS, Video, Data</text>
</svg>"""
    },
    # 51
    {
        "num": "51",
        "index": "02",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "Web Fundamentals",
        "title": "World Wide Web (WWW) vs. Internet & URL Anatomy",
        "subtitle": "Understanding why the Web is just one application running on the Internet, and dissecting every segment of a web address.",
        "analogy_title": "City Stores vs. The Highway System",
        "analogy_text": "The <strong>Internet is the network of physical highways</strong>, while the <strong>World Wide Web is the collection of shops and libraries</strong> built alongside those highways. You can travel on highways without visiting a shop (e.g. sending an email or playing online games).",
        "steps": [
            ("1", "Protocol (The Language)", "`https://` dictates how browser and server converse securely using cryptographic encryption."),
            ("2", "Domain Name (The Location)", "`www.sasicollege.edu.in` translates via Domain Name System (DNS) into a numerical IP server address."),
            ("3", "Path & Parameters (The Specific File)", "`/courses/view?id=101` tells the server exactly which webpage document and student record to serve.")
        ],
        "rule": "Security Check: Always verify the protocol is `https://` (with a locked padlock icon) before entering passwords or college registration forms. `http://` sends your passwords in open readable text!",
        "fig_title": "Figure 02 &bull; Deconstructed URL Anatomy",
        "takeaway": "Key Takeaway: Protocol + Host Domain + Port + Path + Query Parameter = Precise Web Resource.",
        "notes": "Remind non-tech students that typing a URL is like writing an envelope with country, postal code, street, building number, and apartment unit.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Master URL Card -->
  <rect x="25" y="35" width="550" height="70" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="2"/>
  <text x="40" y="65" font-family="monospace" font-size="14" font-weight="700">
    <tspan fill="#0284C7">https://</tspan>
    <tspan fill="#0F172A">www.sasicollege.edu.in</tspan>
    <tspan fill="#D97706">:443</tspan>
    <tspan fill="#059669">/courses/view</tspan>
    <tspan fill="#9333EA">?id=101</tspan>
    <tspan fill="#DC2626">#syllabus</tspan>
  </text>
  <text x="40" y="90" font-family="system-ui, sans-serif" font-size="10" fill="#64748B">Uniform Resource Locator (URL) &bull; The Complete Web Address Blueprint</text>
  <!-- Dissection Grid -->
  <rect x="25" y="125" width="170" height="95" rx="8" fill="#F0F9FF" stroke="#BAE6FD" stroke-width="1.5"/>
  <rect x="35" y="135" width="70" height="20" rx="4" fill="#0284C7"/>
  <text x="70" y="149" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">PROTOCOL</text>
  <text x="35" y="175" font-family="monospace" font-size="13" font-weight="700" fill="#0369A1">https://</text>
  <text x="35" y="195" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">Hypertext Transfer Protocol Secure (TLS)</text>
  <rect x="210" y="125" width="220" height="95" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <rect x="220" y="135" width="90" height="20" rx="4" fill="#0F172A"/>
  <text x="265" y="149" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">DOMAIN NAME</text>
  <text x="220" y="175" font-family="monospace" font-size="12" font-weight="700" fill="#0F172A">www.sasicollege.edu.in</text>
  <text x="220" y="195" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">Mapped to server IP address via DNS</text>
  <rect x="445" y="125" width="130" height="95" rx="8" fill="#FFFBEB" stroke="#FDE68A" stroke-width="1.5"/>
  <rect x="455" y="135" width="50" height="20" rx="4" fill="#D97706"/>
  <text x="480" y="149" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">PORT</text>
  <text x="455" y="175" font-family="monospace" font-size="13" font-weight="700" fill="#B45309">:443</text>
  <text x="455" y="195" font-family="system-ui, sans-serif" font-size="9.5" fill="#78350F">Standard encrypted port</text>
  <rect x="25" y="235" width="180" height="95" rx="8" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1.5"/>
  <rect x="35" y="245" width="70" height="20" rx="4" fill="#059669"/>
  <text x="70" y="259" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">PATH</text>
  <text x="35" y="285" font-family="monospace" font-size="12" font-weight="700" fill="#047857">/courses/view</text>
  <text x="35" y="305" font-family="system-ui, sans-serif" font-size="9.5" fill="#065F46">Folder hierarchy on server disk</text>
  <rect x="220" y="235" width="180" height="95" rx="8" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="1.5"/>
  <rect x="230" y="245" width="80" height="20" rx="4" fill="#9333EA"/>
  <text x="270" y="259" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">QUERY (?)</text>
  <text x="230" y="285" font-family="monospace" font-size="12" font-weight="700" fill="#7E22CE">?id=101&amp;sem=3</text>
  <text x="230" y="305" font-family="system-ui, sans-serif" font-size="9.5" fill="#581C87">Dynamic database lookup keys</text>
  <rect x="415" y="235" width="160" height="95" rx="8" fill="#FEF2F2" stroke="#FECACA" stroke-width="1.5"/>
  <rect x="425" y="245" width="80" height="20" rx="4" fill="#DC2626"/>
  <text x="465" y="259" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">FRAGMENT</text>
  <text x="425" y="285" font-family="monospace" font-size="12" font-weight="700" fill="#B91C1C">#syllabus</text>
  <text x="425" y="305" font-family="system-ui, sans-serif" font-size="9.5" fill="#7F1D1D">Instant in-page scroll anchor</text>
</svg>"""
    },
    # 52
    {
        "num": "52",
        "index": "03",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "Client Applications",
        "title": "Web Browsers: Engines, Sandboxing & Hygiene",
        "subtitle": "How Chrome, Edge, Safari, and Firefox interpret web code, protect your operating system, and manage Cache vs. Cookies.",
        "analogy_title": "The Car Dashboard & Protective Windshield",
        "analogy_text": "A web browser is like the <strong>cabin of an automobile</strong>. The engine underneath converts raw fuel into movement (rendering HTML/CSS into a visible page), while the shatterproof windshield (Sandboxing) prevents external debris from hitting the driver (your laptop).",
        "steps": [
            ("1", "Rendering Engine", "Blink (Chrome/Edge), WebKit (Safari), and Gecko (Firefox) convert raw code into visual interactive graphics."),
            ("2", "Security Sandboxing", "Each browser tab runs in an isolated digital cell; if a website contains malicious scripts, it cannot escape to infect your C: drive."),
            ("3", "Cache vs. Cookies", "Cache stores heavy images locally for faster reload; Cookies store tiny text files keeping you logged into your email or college account.")
        ],
        "rule": "Incognito Myth: Private/Incognito mode ONLY stops your laptop from saving history locally. It DOES NOT hide your browsing from college network admins, Wi-Fi operators, or employers!",
        "fig_title": "Figure 03 &bull; Browser Architecture & Storage",
        "takeaway": "Key Takeaway: Cache stores static files for speed; Cookies preserve your identity; Sandboxing insulates your OS.",
        "notes": "Clarify that clearing Cache frees disk space and fixes broken web layouts, while clearing Cookies logs you out of all websites.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <rect x="30" y="30" width="540" height="300" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <path d="M 30 40 Q 30 30 40 30 L 560 30 Q 570 30 570 40 L 570 65 L 30 65 Z" fill="#F1F5F9"/>
  <circle cx="50" cy="48" r="5" fill="#EF4444"/>
  <circle cx="66" cy="48" r="5" fill="#F59E0B"/>
  <circle cx="82" cy="48" r="5" fill="#10B981"/>
  <rect x="110" y="38" width="340" height="20" rx="10" fill="#FFFFFF" stroke="#E2E8F0"/>
  <text x="280" y="52" font-family="system-ui, sans-serif" font-size="10" fill="#64748B" text-anchor="middle">https://portal.sasicollege.edu.in</text>
  <rect x="50" y="80" width="230" height="150" rx="8" fill="#F0F9FF" stroke="#BAE6FD"/>
  <text x="165" y="105" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0369A1" text-anchor="middle">RENDERING ENGINES</text>
  <rect x="65" y="120" width="200" height="28" rx="4" fill="#FFFFFF" stroke="#BAE6FD"/>
  <text x="75" y="138" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0284C7">Blink:</text>
  <text x="115" y="138" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">Chrome, Edge, Brave</text>
  <rect x="65" y="155" width="200" height="28" rx="4" fill="#FFFFFF" stroke="#BAE6FD"/>
  <text x="75" y="173" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#059669">WebKit:</text>
  <text x="125" y="173" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">Apple Safari, iOS</text>
  <rect x="65" y="190" width="200" height="28" rx="4" fill="#FFFFFF" stroke="#BAE6FD"/>
  <text x="75" y="208" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#D97706">Gecko:</text>
  <text x="120" y="208" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">Mozilla Firefox</text>
  <rect x="300" y="80" width="250" height="150" rx="8" fill="#FEF2F2" stroke="#FECACA"/>
  <text x="425" y="105" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#B91C1C" text-anchor="middle">PROCESS SANDBOXING</text>
  <rect x="315" y="120" width="220" height="42" rx="4" fill="#FFFFFF" stroke="#FECACA"/>
  <text x="325" y="137" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#DC2626">Tab Isolation</text>
  <text x="325" y="152" font-family="system-ui, sans-serif" font-size="9" fill="#475569">Malicious web scripts cannot access OS files</text>
  <rect x="315" y="170" width="220" height="48" rx="4" fill="#FFFBEB" stroke="#FDE68A"/>
  <text x="325" y="188" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#D97706">Incognito Myth</text>
  <text x="325" y="204" font-family="system-ui, sans-serif" font-size="9" fill="#78350F">No local history &bull; College network STILL logs traffic!</text>
  <rect x="50" y="245" width="230" height="70" rx="8" fill="#ECFDF5" stroke="#A7F3D0"/>
  <text x="65" y="268" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#047857">BROWSER CACHE</text>
  <text x="65" y="285" font-family="system-ui, sans-serif" font-size="9.5" fill="#065F46">Saves images &amp; logos for speed</text>
  <rect x="300" y="245" width="250" height="70" rx="8" fill="#F5F3FF" stroke="#DDD6FE"/>
  <text x="315" y="268" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#6D28D9">HTTP COOKIES</text>
  <text x="315" y="285" font-family="system-ui, sans-serif" font-size="9.5" fill="#5B21B6">Stores login session tokens</text>
</svg>"""
    },
    # 53
    {
        "num": "53",
        "index": "04",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "Information Retrieval",
        "title": "Search Engines: Crawlers, Indexing & Boolean Operators",
        "subtitle": "How Google scans billions of documents in 0.2 seconds, and how students can use targeted search syntax to find official papers.",
        "analogy_title": "The World's Fastest Universal Library Catalog",
        "analogy_text": "Imagine a university library with billions of books. Automated robotic librarians (<strong>Crawlers/Spiders</strong>) read every single page continuously, file the words in a massive card catalog (<strong>Index</strong>), and hand you the exact 3 best books in 0.2 seconds when you ask a question.",
        "steps": [
            ("1", "Crawling (Discovery)", "Automated software bots (Googlebot) follow hyperlinks 24/7 across every public server on Earth."),
            ("2", "Indexing (Organization)", "Text, images, and video metadata are parsed into an astronomical dictionary-like inverted index."),
            ("3", "Ranking (Algorithm)", "Over 200 signals (PageRank, relevancy, user location, speed) rank the most credible answer instantly.")
        ],
        "rule": "Power Search Formula: Type `\"cyber security syllabus\" site:gov.in filetype:pdf` in Google to instantly download verified government syllabus documents without commercial spam.",
        "fig_title": "Figure 04 &bull; Search Engine Pipeline & Query Modifiers",
        "takeaway": "Key Takeaway: Crawl &rarr; Index &rarr; Rank. Use quotes `\"\"`, `site:`, and `filetype:` to filter noise.",
        "notes": "Demonstrate the difference between a broad fuzzy query and a pinpoint Boolean query to save hours during undergraduate project research.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <rect x="25" y="40" width="165" height="120" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
  <rect x="35" y="50" width="60" height="20" rx="4" fill="#0284C7"/>
  <text x="65" y="64" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">STAGE 1</text>
  <text x="35" y="90" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0F172A">CRAWLING</text>
  <text x="35" y="110" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">Spiders traverse hyperlinks across 50+ billion web pages</text>
  <line x1="190" y1="100" x2="215" y2="100" stroke="#0284C7" stroke-width="3" stroke-linecap="round"/>
  <rect x="215" y="40" width="170" height="120" rx="10" fill="#FFFFFF" stroke="#0EA5E9" stroke-width="1.5"/>
  <rect x="225" y="50" width="60" height="20" rx="4" fill="#0EA5E9"/>
  <text x="255" y="64" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">STAGE 2</text>
  <text x="225" y="90" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0F172A">INDEXING</text>
  <text x="225" y="110" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">Giant dictionary maps words to URLs with semantic weights</text>
  <line x1="385" y1="100" x2="410" y2="100" stroke="#0EA5E9" stroke-width="3" stroke-linecap="round"/>
  <rect x="410" y="40" width="165" height="120" rx="10" fill="#FFFFFF" stroke="#059669" stroke-width="1.5"/>
  <rect x="420" y="50" width="60" height="20" rx="4" fill="#059669"/>
  <text x="450" y="64" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">STAGE 3</text>
  <text x="420" y="90" font-family="system-ui, sans-serif" font-size="14" font-weight="700" fill="#0F172A">RANKING</text>
  <text x="420" y="110" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">Calculates PageRank &amp; context in 0.2s for top results</text>
  <rect x="25" y="180" width="550" height="145" rx="10" fill="#F1F5F9" stroke="#E2E8F0"/>
  <text x="40" y="205" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F172A">BOOLEAN SEARCH MODIFIERS CHEATSHEET</text>
  <rect x="40" y="220" width="160" height="42" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="50" y="238" font-family="monospace" font-size="11" font-weight="700" fill="#0284C7">"exact phrase"</text>
  <text x="50" y="253" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B">Verbatim word order</text>
  <rect x="215" y="220" width="160" height="42" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="225" y="238" font-family="monospace" font-size="11" font-weight="700" fill="#059669">site:gov.in</text>
  <text x="225" y="253" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B">Official portals only</text>
  <rect x="390" y="220" width="170" height="42" rx="6" fill="#FFFFFF" stroke="#CBD5E1"/>
  <text x="400" y="238" font-family="monospace" font-size="11" font-weight="700" fill="#D97706">filetype:pdf</text>
  <text x="400" y="253" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B">Direct documents</text>
  <rect x="40" y="272" width="520" height="38" rx="6" fill="#E0F2FE" stroke="#BAE6FD"/>
  <text x="50" y="295" font-family="monospace" font-size="11" font-weight="700" fill="#0369A1">PRO-QUERY: "data protection act" site:meity.gov.in filetype:pdf</text>
</svg>"""
    },
    # 54
    {
        "num": "54",
        "index": "05",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "Messaging Infrastructure",
        "title": "Email Infrastructure: SMTP, IMAP & POP3 Protocols",
        "subtitle": "How corporate and institutional mail travels across servers, and why modern multi-device syncing relies on IMAP over legacy POP3.",
        "analogy_title": "Dropping Letters in a Box vs. Cloud PO Box",
        "analogy_text": "<strong>SMTP is the postman collecting outgoing letters</strong> from your local street box. <strong>POP3 is like physically taking letters home</strong> (they disappear from the post office). <strong>IMAP is like a digital post office locker</strong> that lets you view letters from your phone, laptop, and desktop simultaneously without deleting anything.",
        "steps": [
            ("1", "Outbound Relay (SMTP)", "Simple Mail Transfer Protocol sends your written draft from your client to your organization's outgoing mail relay."),
            ("2", "DNS MX Lookup", "Your server queries DNS for the recipient's Mail Exchange (MX) record to find their hosting server IP."),
            ("3", "Inbound Retrieval (IMAP)", "Internet Message Access Protocol keeps all folders, read flags, and replies synchronized in real time across phone and PC.")
        ],
        "rule": "Configuration Alert: Never configure a modern smartphone with POP3 unless instructed! POP3 downloads emails to one device and deletes them from the server, causing you to lose messages on your other devices.",
        "fig_title": "Figure 05 &bull; Mail Protocols Lifecycle (SMTP vs. IMAP vs. POP3)",
        "takeaway": "Key Takeaway: SMTP pushes outgoing mail; IMAP synchronizes incoming mail across all devices.",
        "notes": "Help non-technical students understand why an email sent from their smartphone immediately appears in the Sent folder of their college desktop computer.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <rect x="30" y="50" width="130" height="110" rx="8" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
  <text x="95" y="75" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A" text-anchor="middle">SENDER CLIENT</text>
  <rect x="50" y="90" width="90" height="26" rx="4" fill="#E0F2FE"/>
  <text x="95" y="107" font-family="monospace" font-size="10" font-weight="700" fill="#0369A1" text-anchor="middle">Draft Mail</text>
  <line x1="160" y1="105" x2="230" y2="105" stroke="#0284C7" stroke-width="3" stroke-linecap="round"/>
  <polygon points="230,100 240,105 230,110" fill="#0284C7"/>
  <text x="195" y="95" font-family="monospace" font-size="10" font-weight="700" fill="#0284C7" text-anchor="middle">SMTP:587</text>
  <rect x="240" y="50" width="140" height="110" rx="8" fill="#F0F9FF" stroke="#0284C7" stroke-width="1.5"/>
  <text x="310" y="75" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0369A1" text-anchor="middle">MAIL RELAY</text>
  <text x="310" y="105" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">Queries DNS MX</text>
  <line x1="380" y1="105" x2="430" y2="105" stroke="#059669" stroke-width="3" stroke-linecap="round"/>
  <polygon points="430,100 440,105 430,110" fill="#059669"/>
  <text x="405" y="95" font-family="monospace" font-size="10" font-weight="700" fill="#059669" text-anchor="middle">SMTP:25</text>
  <rect x="440" y="50" width="130" height="110" rx="8" fill="#ECFDF5" stroke="#059669" stroke-width="1.5"/>
  <text x="505" y="75" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#047857" text-anchor="middle">RECIPIENT SERVER</text>
  <text x="505" y="105" font-family="system-ui, sans-serif" font-size="9.5" fill="#065F46" text-anchor="middle">Stores inbox spool</text>
  <rect x="30" y="190" width="260" height="135" rx="8" fill="#FFFFFF" stroke="#059669" stroke-width="2"/>
  <rect x="45" y="200" width="80" height="22" rx="4" fill="#059669"/>
  <text x="85" y="215" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">IMAP (Port 993)</text>
  <text x="45" y="245" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Cloud Live Synchronization</text>
  <text x="45" y="265" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Keeps emails stored on server</text>
  <text x="45" y="280" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Synced on Phone, Laptop, Web</text>
  <rect x="310" y="190" width="260" height="135" rx="8" fill="#FFFBEB" stroke="#D97706" stroke-width="1.5"/>
  <rect x="325" y="200" width="80" height="22" rx="4" fill="#D97706"/>
  <text x="365" y="215" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">POP3 (Port 995)</text>
  <text x="325" y="245" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Legacy Single-PC Download</text>
  <text x="325" y="265" font-family="system-ui, sans-serif" font-size="9" fill="#78350F">&bull; Downloads to 1 computer only</text>
  <text x="325" y="280" font-family="system-ui, sans-serif" font-size="9" fill="#78350F">&bull; Deletes from mail server by default</text>
</svg>"""
    },
    # 55
    {
        "num": "55",
        "index": "06",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "Corporate Communication",
        "title": "Corporate Email Etiquette & Professional Anatomy",
        "subtitle": "Mastering the structural anatomy, subject lines, formal tone, and professional signature blocks required in modern workplaces.",
        "analogy_title": "The Formal Business Suit vs. Casual Streetwear",
        "analogy_text": "Writing an email to a professor, manager, or recruiter is like <strong>wearing formal attire to an interview</strong>. Casual slang, abbreviations like 'u r', and emojis look like attending a courtroom in pajamas. A crisp corporate structure commands immediate respect.",
        "steps": [
            ("1", "Subject Line Formula", "`[Action Required / Status Update] - Project Name - Your Name`. Recruiters decide whether to open your email in 3 seconds based on this."),
            ("2", "Salutation & Context", "Open with formal respect (`Dear Dr. Sharma:` or `Hello Team,`). The first sentence must state your purpose directly."),
            ("3", "Signature Block", "Include full name, degree/designation, institution, phone number, and professional LinkedIn hyperlink.")
        ],
        "rule": "The 24-Hour Rule: In professional environments, acknowledge emails within 24 business hours. If you need more time to gather data, reply: 'Acknowledging receipt; I am compiling the figures and will update you by 3:00 PM tomorrow.'",
        "fig_title": "Figure 06 &bull; Structural Anatomy of an Executive Email",
        "takeaway": "Key Takeaway: Clear Subject &rarr; Formal Salutation &rarr; Purpose in Line 1 &rarr; Bullets &rarr; Actionable Sign-off.",
        "notes": "Warn students against amateur usernames like cool_boy_99@gmail.com; professional job applications require firstname.lastname@gmail.com.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <rect x="30" y="30" width="540" height="300" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <rect x="45" y="45" width="510" height="30" rx="4" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="55" y="65" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#64748B">To:</text>
  <text x="85" y="65" font-family="system-ui, sans-serif" font-size="11" fill="#0F172A">recruitment@technovault.com</text>
  <rect x="45" y="80" width="510" height="30" rx="4" fill="#F0F9FF" stroke="#BAE6FD"/>
  <text x="55" y="100" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0284C7">Subject:</text>
  <text x="110" y="100" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0369A1">Application for Junior Systems Analyst &ndash; Vignesh Hari</text>
  <text x="55" y="135" font-family="system-ui, sans-serif" font-size="11" font-weight="600" fill="#0F172A">Dear Hiring Manager,</text>
  <text x="55" y="155" font-family="system-ui, sans-serif" font-size="10" fill="#334155">I am writing to formally submit my candidature for the Junior Systems Analyst position at TechnoVault.</text>
  <rect x="65" y="180" width="470" height="42" rx="4" fill="#F8FAFC"/>
  <text x="75" y="196" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; Financial data modeling and quantitative analytics in MS Excel</text>
  <text x="75" y="211" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; Cloud infrastructure hygiene, Google Workspace, and enterprise security</text>
  <text x="55" y="245" font-family="system-ui, sans-serif" font-size="10" fill="#334155">My resume is attached for your review. I look forward to discussing how my skills align with your objectives.</text>
  <line x1="55" y1="260" x2="250" y2="260" stroke="#CBD5E1" stroke-width="1"/>
  <text x="55" y="278" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Hari Vignesh</text>
  <text x="55" y="293" font-family="system-ui, sans-serif" font-size="9.5" fill="#64748B">B.Sc Computer Applications &bull; Sasi College</text>
  <text x="55" y="308" font-family="system-ui, sans-serif" font-size="9.5" fill="#0284C7">+91 98765 43210 | linkedin.com/in/harivignesh</text>
</svg>"""
    },
    # 56
    {
        "num": "56",
        "index": "07",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "File Optimization",
        "title": "Email Attachments: Limits, ZIP & Cloud Links",
        "subtitle": "Why video and massive PDFs bounce due to email file size limits, how Base64 adds 33% overhead, and when to send a Google Drive cloud link.",
        "analogy_title": "Luggage Weight Limits on an Airplane",
        "analogy_text": "An airline allows a <strong>maximum of 15 kg for check-in baggage</strong>; if your bag weighs 20 kg, you are turned away at the gate. Email systems enforce a strict <strong>25 MB ceiling</strong>. Trying to send a 40 MB video or presentation bounces immediately.",
        "steps": [
            ("1", "Base64 Encoding Overhead", "Email was built for text. Attaching a 20 MB binary file inflates it by ~33% to 27 MB, exceeding Gmail's 25 MB limit!"),
            ("2", "ZIP File Compression", "Bundles 20 scattered assignment sheets into 1 clean `.zip` archive while shrinking text size by up to 60%."),
            ("3", "Cloud Link Alternative", "Upload files over 25 MB to Google Drive or OneDrive, and insert the view/download link into the email body.")
        ],
        "rule": "Security Alert: Never attempt to send `.exe`, `.bat`, or `.vbs` files via email attachments. Gmail and Outlook automatically quarantine executable attachments to prevent ransomware infections.",
        "fig_title": "Figure 07 &bull; Attachment Optimization Matrix",
        "takeaway": "Key Takeaway: &le;25 MB = Direct Attachment or ZIP; &gt;25 MB = Google Drive Cloud Share Link.",
        "notes": "Demonstrate how to right-click a folder in Windows and choose 'Compress to ZIP file'.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- 25MB Gate Wall -->
  <rect x="250" y="35" width="100" height="290" rx="8" fill="#FEF2F2" stroke="#EF4444" stroke-width="2"/>
  <text x="300" y="65" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#DC2626" text-anchor="middle">25 MB GATE</text>
  <line x1="260" y1="80" x2="340" y2="80" stroke="#FECACA" stroke-width="2"/>
  <text x="300" y="120" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">EMAIL SERVER</text>
  <text x="300" y="138" font-family="system-ui, sans-serif" font-size="9" fill="#B91C1C" text-anchor="middle">SIZE LIMIT</text>
  <text x="300" y="180" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#DC2626" text-anchor="middle">Base64</text>
  <text x="300" y="196" font-family="system-ui, sans-serif" font-size="8.5" fill="#7F1D1D" text-anchor="middle">+33% Inflation</text>
  <rect x="260" y="220" width="80" height="85" rx="6" fill="#FFFFFF" stroke="#DC2626"/>
  <text x="300" y="245" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#B91C1C" text-anchor="middle">BLOCKED</text>
  <text x="300" y="265" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">.exe, .bat</text>
  <text x="300" y="280" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">&gt;25MB files</text>
  <!-- Left: Heavy Unoptimized File -->
  <rect x="30" y="60" width="190" height="240" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <rect x="45" y="75" width="160" height="30" rx="4" fill="#FEE2E2"/>
  <text x="125" y="94" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#991B1B" text-anchor="middle">HEAVY 45 MB VIDEO</text>
  <circle cx="125" cy="155" r="32" fill="#F8FAFC" stroke="#EF4444" stroke-width="2"/>
  <text x="125" y="160" font-family="system-ui, sans-serif" font-size="20" font-weight="800" fill="#DC2626" text-anchor="middle">&times;</text>
  <text x="125" y="210" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#DC2626" text-anchor="middle">Direct Send Bounces!</text>
  <text x="125" y="230" font-family="system-ui, sans-serif" font-size="9" fill="#64748B" text-anchor="middle">Error: "Message size exceeds fixed maximum limit"</text>
  <!-- Right: Optimized Solutions -->
  <rect x="380" y="60" width="190" height="110" rx="8" fill="#FFFFFF" stroke="#059669" stroke-width="1.5"/>
  <rect x="395" y="70" width="160" height="24" rx="4" fill="#ECFDF5"/>
  <text x="475" y="86" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">SOLUTION 1: ZIP ARCHIVE</text>
  <text x="475" y="115" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" fill="#065F46" text-anchor="middle">Compress Multi-Files</text>
  <text x="475" y="132" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">10 assignments &rarr; 1 tidy `.zip` file under 15 MB</text>
  <rect x="380" y="190" width="190" height="110" rx="8" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
  <rect x="395" y="200" width="160" height="24" rx="4" fill="#E0F2FE"/>
  <text x="475" y="216" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0369A1" text-anchor="middle">SOLUTION 2: CLOUD LINK</text>
  <text x="475" y="245" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" fill="#0284C7" text-anchor="middle">Google Drive / OneDrive</text>
  <text x="475" y="262" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Upload 500 MB video &amp; paste clean view link</text>
</svg>"""
    },
    # 57
    {
        "num": "57",
        "index": "08",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "Corporate Governance",
        "title": "Email Addressing: To vs. CC vs. BCC Rules",
        "subtitle": "Workplace governance of recipient fields: who takes action, who stays informed, and how to avoid privacy violations and 'Reply-All' storms.",
        "analogy_title": "Direct Speech vs. Keeping in Loop vs. Blind Copy",
        "analogy_text": "<strong>To:</strong> is speaking directly to someone across the desk ('You do this task'). <strong>CC (Carbon Copy):</strong> is letting your supervisor sit in the room for awareness. <strong>BCC (Blind Carbon Copy):</strong> is handing a sealed flyer to 500 people where none of them can see each other's contact details.",
        "steps": [
            ("1", "To Field (Action Required)", "Only put recipients who are expected to execute work or reply directly."),
            ("2", "CC Field (Courtesy Copy)", "Keep managers or teammates updated. Rule: People on CC should not feel obliged to reply."),
            ("3", "BCC Field (Privacy Protection)", "Mandatory when emailing student cohorts or external clients to conceal personal email addresses.")
        ],
        "rule": "Disaster Prevention: Never put 500 student emails in the 'To:' or 'CC:' line! If one person hits 'Reply All' with 'Thank you', it triggers a notification avalanche that crashes mail servers and leaks student contact data.",
        "fig_title": "Figure 08 &bull; Recipient Field Governance Matrix",
        "takeaway": "Key Takeaway: To = Do it; CC = Know it; BCC = Mass confidentiality & privacy.",
        "notes": "Emphasize how CCing a supervisor makes workplace accountability transparent without micromanagement.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- 3 Big Cards -->
  <!-- TO Card -->
  <rect x="25" y="40" width="170" height="280" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="2"/>
  <rect x="40" y="55" width="70" height="26" rx="4" fill="#0284C7"/>
  <text x="75" y="72" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">TO:</text>
  <text x="40" y="110" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#0F172A">PRIMARY ACTOR</text>
  <text x="40" y="130" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#0284C7">Action &amp; Reply Expected</text>
  <rect x="40" y="150" width="140" height="1" fill="#E2E8F0"/>
  <text x="40" y="175" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; The person directly responsible for the task</text>
  <text x="40" y="210" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; Should not exceed 1&ndash;3 people to prevent diffusion of responsibility</text>
  <rect x="40" y="250" width="140" height="50" rx="6" fill="#F0F9FF"/>
  <text x="110" y="270" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#0369A1" text-anchor="middle">"Please complete this audit report by 4 PM."</text>
  <!-- CC Card -->
  <rect x="215" y="40" width="170" height="280" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="2"/>
  <rect x="230" y="55" width="70" height="26" rx="4" fill="#475569"/>
  <text x="265" y="72" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">CC:</text>
  <text x="230" y="110" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#0F172A">CARBON COPY</text>
  <text x="230" y="130" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#475569">Awareness / FYIs Only</text>
  <rect x="230" y="150" width="140" height="1" fill="#E2E8F0"/>
  <text x="230" y="175" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; Supervisors and team members kept in the loop</text>
  <text x="230" y="210" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; No action required from CC recipients</text>
  <rect x="230" y="250" width="140" height="50" rx="6" fill="#F8FAFC"/>
  <text x="300" y="270" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#334155" text-anchor="middle">"Manager is CCed for visibility on progress."</text>
  <!-- BCC Card -->
  <rect x="405" y="40" width="170" height="280" rx="10" fill="#FFFFFF" stroke="#059669" stroke-width="2"/>
  <rect x="420" y="55" width="70" height="26" rx="4" fill="#059669"/>
  <text x="455" y="72" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">BCC:</text>
  <text x="420" y="110" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#0F172A">BLIND COPY</text>
  <text x="420" y="130" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#059669">Privacy &amp; Mass Mail</text>
  <rect x="420" y="150" width="140" height="1" fill="#E2E8F0"/>
  <text x="420" y="175" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; Recipients cannot see each other's addresses</text>
  <text x="420" y="210" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; Blocks Reply-All broadcast disasters</text>
  <rect x="420" y="250" width="140" height="50" rx="6" fill="#ECFDF5"/>
  <text x="490" y="270" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#047857" text-anchor="middle">"Sending notice to 500 college students safely."</text>
</svg>"""
    },
    # 58
    {
        "num": "58",
        "index": "09",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "Network Addressing",
        "title": "IP Addressing: IPv4 32-bit vs. IPv6 128-bit Architecture",
        "subtitle": "How devices obtain numerical addresses, why 4.3 billion IPv4 addresses were exhausted, and how India leads the world in IPv6 deployment.",
        "analogy_title": "Street Postal Address vs. Biometric Fingerprint",
        "analogy_text": "An <strong>IP Address is like your temporary mailing street address</strong> (it changes if you move from college Wi-Fi to a coffee shop). A <strong>MAC address is like your biometric fingerprint</strong> (permanently manufactured onto your phone's network chip).",
        "steps": [
            ("1", "IPv4 Architecture", "32 bits arranged in 4 decimal octets (`192.168.1.1`). Total capacity: 4.29 billion addresses, exhausted globally by 2011."),
            ("2", "NAT Workaround", "Network Address Translation lets 50 campus laptops share 1 single public IP on the internet."),
            ("3", "IPv6 Evolution", "128 bits in 8 hexadecimal blocks (`2405:201:...`). Provides 340 undecillion addresses (enough for every atom on Earth).")
        ],
        "rule": "National Milestone: India ranks #1 globally in IPv6 adoption (over 80% penetration), powered by Reliance Jio and Airtel fiber networks.",
        "fig_title": "Figure 09 &bull; IPv4 vs. IPv6 Structural Comparison",
        "takeaway": "Key Takeaway: IPv4 = 32-bit dotted-decimal (exhausted); IPv6 = 128-bit hexadecimal (infinite).",
        "notes": "Explain how students can open Command Prompt and type `ipconfig` to see their current IPv4 and IPv6 addresses.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- IPv4 Container -->
  <rect x="30" y="40" width="540" height="125" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
  <rect x="45" y="52" width="65" height="22" rx="4" fill="#0284C7"/>
  <text x="77" y="67" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">IPv4</text>
  <text x="125" y="68" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F172A">32-Bit Dotted Decimal Structure</text>
  <!-- Octet Boxes -->
  <rect x="45" y="85" width="80" height="36" rx="4" fill="#E0F2FE"/>
  <text x="85" y="107" font-family="monospace" font-size="13" font-weight="700" fill="#0369A1" text-anchor="middle">192</text>
  <circle cx="132" cy="103" r="3" fill="#0284C7"/>
  <rect x="140" y="85" width="80" height="36" rx="4" fill="#E0F2FE"/>
  <text x="180" y="107" font-family="monospace" font-size="13" font-weight="700" fill="#0369A1" text-anchor="middle">168</text>
  <circle cx="227" cy="103" r="3" fill="#0284C7"/>
  <rect x="235" y="85" width="80" height="36" rx="4" fill="#E0F2FE"/>
  <text x="275" y="107" font-family="monospace" font-size="13" font-weight="700" fill="#0369A1" text-anchor="middle">1</text>
  <circle cx="322" cy="103" r="3" fill="#0284C7"/>
  <rect x="330" y="85" width="80" height="36" rx="4" fill="#E0F2FE"/>
  <text x="370" y="107" font-family="monospace" font-size="13" font-weight="700" fill="#0369A1" text-anchor="middle">105</text>
  <rect x="430" y="85" width="125" height="36" rx="4" fill="#FEF2F2" stroke="#FECACA"/>
  <text x="492" y="100" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#B91C1C" text-anchor="middle">4.29 Billion Cap</text>
  <text x="492" y="113" font-family="system-ui, sans-serif" font-size="8" fill="#7F1D1D" text-anchor="middle">Exhausted Globally</text>
  <text x="45" y="145" font-family="system-ui, sans-serif" font-size="9.5" fill="#64748B">4 Octets &bull; 8 bits each = 32 bits total</text>
  <!-- IPv6 Container -->
  <rect x="30" y="180" width="540" height="145" rx="10" fill="#FFFFFF" stroke="#059669" stroke-width="1.5"/>
  <rect x="45" y="192" width="65" height="22" rx="4" fill="#059669"/>
  <text x="77" y="207" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#FFFFFF" text-anchor="middle">IPv6</text>
  <text x="125" y="208" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F172A">128-Bit Hexadecimal Structure</text>
  <rect x="45" y="225" width="510" height="40" rx="6" fill="#ECFDF5"/>
  <text x="300" y="250" font-family="monospace" font-size="12" font-weight="700" fill="#047857" text-anchor="middle">2405:201:2002:80c1:3d8e:9b44:f12a:0089</text>
  <rect x="45" y="275" width="160" height="36" rx="4" fill="#F0FDF4"/>
  <text x="125" y="297" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#166534" text-anchor="middle">340 Undecillion Space</text>
  <rect x="220" y="275" width="160" height="36" rx="4" fill="#F0FDF4"/>
  <text x="300" y="297" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#166534" text-anchor="middle">8 Hex Blocks &bull; 16 bits each</text>
  <rect x="395" y="275" width="160" height="36" rx="4" fill="#E0F2FE"/>
  <text x="475" y="297" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0369A1" text-anchor="middle">India #1 Worldwide</text>
</svg>"""
    },
    # 59
    {
        "num": "59",
        "index": "10",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "Performance Metrics",
        "title": "Internet Speed Metrics: Mbps vs. MB/s & Latency",
        "subtitle": "Demystifying ISP marketing: the 8-bit math difference between Megabits and Megabytes, ping latency, and jitter during video calls.",
        "analogy_title": "Pipe Diameter vs. Water Volume vs. Travel Delay",
        "analogy_text": "<strong>Bandwidth (Mbps) is the width of a water pipe</strong> (how much water can flow through at once). <strong>Download Speed (MB/s) is the bucket of water</strong> filled per second. <strong>Latency / Ping is the time delay</strong> between turning the faucet knob and seeing the first drop emerge.",
        "steps": [
            ("1", "The Divide-by-8 Rule", "ISPs advertise speed in MegaBITS (small 'b', Mbps). File size is measured in MegaBYTES (capital 'B', MB). 8 bits = 1 Byte."),
            ("2", "Real Speed Calculation", "A 100 Mbps broadband plan downloads files at a maximum theoretical rate of `100 / 8 = 12.5 MB/s`."),
            ("3", "Latency (Ping) & Jitter", "Ping measures round-trip time in milliseconds (ms). Under 20 ms = ideal; over 150 ms = choppy audio and lag.")
        ],
        "rule": "Troubleshooting Routine: When Zoom or Meet lags, don't just check speed; check Ping! High latency (ping &gt; 100ms) causes awkward speech overlaps even on a 300 Mbps connection.",
        "fig_title": "Figure 10 &bull; Telecommunications Math & Latency Visualizer",
        "takeaway": "Key Takeaway: 1 Byte = 8 bits. 100 Mbps Plan = 12.5 MB/s File Download. Ping = Real-time responsiveness.",
        "notes": "Help non-CS students calculate why downloading a 1 GB movie takes roughly 80 seconds on a true 100 Mbps line.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Divide by 8 Equation Banner -->
  <rect x="30" y="35" width="540" height="85" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="2"/>
  <text x="300" y="60" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0369A1" text-anchor="middle">THE GOLDEN ISP EQUATION (DIVIDE BY 8)</text>
  <text x="130" y="95" font-family="monospace" font-size="16" font-weight="800" fill="#0284C7" text-anchor="middle">100 Mbps</text>
  <text x="130" y="110" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">ISP Advertised Megabits</text>
  <text x="215" y="95" font-family="system-ui, sans-serif" font-size="18" font-weight="700" fill="#64748B" text-anchor="middle">&divide; 8 bits =</text>
  <text x="320" y="95" font-family="monospace" font-size="18" font-weight="800" fill="#059669" text-anchor="middle">12.5 MB/s</text>
  <text x="320" y="110" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Actual File Download Rate</text>
  <rect x="420" y="52" width="130" height="52" rx="6" fill="#F0FDF4" stroke="#BBF7D0"/>
  <text x="485" y="73" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#166534" text-anchor="middle">1 GB Movie</text>
  <text x="485" y="92" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#15803D" text-anchor="middle">&asymp; 82 Seconds</text>
  <!-- Latency vs Bandwidth Cards -->
  <rect x="30" y="140" width="255" height="180" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <rect x="45" y="155" width="120" height="24" rx="4" fill="#E0F2FE"/>
  <text x="105" y="171" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0369A1" text-anchor="middle">BANDWIDTH (Mbps)</text>
  <text x="45" y="202" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Volume Capacity</text>
  <text x="45" y="222" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; How wide the transmission pipe is</text>
  <text x="45" y="238" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; Essential for high-res 4K video streaming</text>
  <text x="45" y="254" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; Crucial for rapid multi-gigabyte downloads</text>
  <rect x="45" y="275" width="225" height="32" rx="4" fill="#F8FAFC"/>
  <text x="157" y="295" font-family="system-ui, sans-serif" font-size="9" font-weight="600" fill="#334155" text-anchor="middle">Truck carrying 10,000 hard disks</text>
  <rect x="315" y="140" width="255" height="180" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <rect x="330" y="155" width="120" height="24" rx="4" fill="#FEF3C7"/>
  <text x="390" y="171" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#B45309" text-anchor="middle">LATENCY / PING (ms)</text>
  <text x="330" y="202" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Time Delay / Responsiveness</text>
  <text x="330" y="222" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; Round-trip transmission time in ms</text>
  <text x="330" y="238" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; &lt;20 ms: Instant reaction, fluid Zoom call</text>
  <text x="330" y="254" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&bull; &gt;150 ms: Noticeable lag and awkward pauses</text>
  <rect x="330" y="275" width="225" height="32" rx="4" fill="#FEF2F2"/>
  <text x="442" y="295" font-family="system-ui, sans-serif" font-size="9" font-weight="600" fill="#B91C1C" text-anchor="middle">High ping ruins live conferencing</text>
</svg>"""
    }
]

print(f"data_unit4 part 1 initialized with {len(unit4_topics)} topics.")
