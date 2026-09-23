"""
Unit 4 Data Part 3: Topics 64 to 70 (7 Topics)
Video Conferencing, LinkedIn, SWAYAM, Citizen e-Portals & UPI
"""

unit4_part3_topics = [
    # 64
    {
        "num": "64",
        "index": "15",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "Remote Work Fluency",
        "title": "Video Conferencing: Meeting Etiquette & Screen Sharing",
        "subtitle": "Audio/video hygiene, browser WebRTC protocols, avoiding privacy disasters during screen sharing, and meeting security controls.",
        "analogy_title": "Entering a Corporate Boardroom vs. Casual Living Room",
        "analogy_text": "Joining a corporate video call is like <strong>stepping into an executive conference room</strong>. Leaving your microphone unmuted while family members talk in the background is like having random people shouting through the boardroom window. Professional hygiene builds immediate trust.",
        "steps": [
            ("1", "Screen Sharing Hygiene", "CRITICAL: Never share 'Entire Screen' during client calls! WhatsApp notifications or banking alerts pop up visibly. Share a specific 'Window' or 'Chrome Tab' only."),
            ("2", "Audio & Mute Discipline", "Default to Mute upon joining. Use a headset to cancel ambient echoes; un-mute only when actively presenting."),
            ("3", "Lighting & Virtual Background", "Position light in front of your face (not behind you like a dark silhouette), and use a subtle blurred background to hide dorm clutter.")
        ],
        "rule": "Meeting Gatekeeping: Always enable 'Waiting Room' and require host approval. This prevents unauthorized internet trolls from hijacking your class presentation.",
        "fig_title": "Figure 15 &bull; Screen Sharing Privacy: Tab vs. Entire Desktop",
        "takeaway": "Key Takeaway: Share single Tab/Window, never full screen; Mute by default; Light from front.",
        "notes": "Remind students that job interviews conducted on Google Meet or Zoom assess professional setting and camera eye contact.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Bad vs Good Screen Sharing Comparison -->
  <!-- Left: Dangerous Full Screen -->
  <rect x="25" y="40" width="260" height="280" rx="10" fill="#FEF2F2" stroke="#EF4444" stroke-width="2"/>
  <rect x="40" y="55" width="130" height="24" rx="4" fill="#FEE2E2"/>
  <text x="105" y="71" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">&cross; ENTIRE SCREEN</text>
  <text x="40" y="105" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#B91C1C">High Privacy Hazard</text>
  <rect x="40" y="125" width="230" height="110" rx="6" fill="#FFFFFF" stroke="#FECACA"/>
  <text x="50" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">&bull; Private WhatsApp message pops up</text>
  <text x="50" y="165" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">&bull; Bank balance notification displayed</text>
  <text x="50" y="185" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">&bull; Unrelated browser tabs visible to boss</text>
  <text x="50" y="205" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">&bull; Family photos on desktop exposed</text>
  <rect x="40" y="250" width="230" height="50" rx="6" fill="#FFFFFF"/>
  <text x="155" y="272" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#B91C1C" text-anchor="middle">Verdict: Extreme Embarrassment</text>
  <text x="155" y="288" font-family="system-ui, sans-serif" font-size="8.5" fill="#7F1D1D" text-anchor="middle">May violate corporate NDA agreements</text>
  <!-- Right: Safe Tab Sharing -->
  <rect x="315" y="40" width="260" height="280" rx="10" fill="#ECFDF5" stroke="#10B981" stroke-width="2"/>
  <rect x="330" y="55" width="130" height="24" rx="4" fill="#D1FAE5"/>
  <text x="395" y="71" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#065F46" text-anchor="middle">&check; SINGLE TAB / WINDOW</text>
  <text x="330" y="105" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#047857">Executive Best Practice</text>
  <rect x="330" y="125" width="230" height="110" rx="6" fill="#FFFFFF" stroke="#A7F3D0"/>
  <text x="340" y="145" font-family="system-ui, sans-serif" font-size="9" fill="#047857">&bull; Only presentation slides are shared</text>
  <text x="340" y="165" font-family="system-ui, sans-serif" font-size="9" fill="#047857">&bull; Background desktop completely hidden</text>
  <text x="340" y="185" font-family="system-ui, sans-serif" font-size="9" fill="#047857">&bull; Incoming chat alerts blocked automatically</text>
  <text x="340" y="205" font-family="system-ui, sans-serif" font-size="9" fill="#047857">&bull; Audio tab sharing preserves video sound</text>
  <rect x="330" y="250" width="230" height="50" rx="6" fill="#FFFFFF"/>
  <text x="445" y="272" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#047857" text-anchor="middle">Verdict: Professional &amp; Secure</text>
  <text x="445" y="288" font-family="system-ui, sans-serif" font-size="8.5" fill="#065F46" text-anchor="middle">Maintains strict focus and executive polish</text>
</svg>"""
    },
    # 65
    {
        "num": "65",
        "index": "16",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "Career Networking",
        "title": "Professional Networking: LinkedIn Personal Branding",
        "subtitle": "Optimizing headlines, showcasing verified technical projects, navigating the hidden job market, and passing HR social media screening.",
        "analogy_title": "A 24/7 Digital Career Billboard That Works While You Sleep",
        "analogy_text": "A paper resume stays buried in a drawer until you hand it to someone. A <strong>LinkedIn profile is a high-visibility digital storefront on the busiest avenue in the world</strong>: corporate recruiters and hiring managers browse your portfolio, certifications, and recommendations 24 hours a day.",
        "steps": [
            ("1", "Action-Driven Headline", "Never write just 'Student at Sasi College'. Write: 'Aspiring Systems Analyst | B.Sc | Skilled in Python, Financial Modeling & Cloud Tools'."),
            ("2", "The Hidden Job Market", "Up to 70% of professional jobs are never publicly posted on boards; they are filled through alumni referrals and direct LinkedIn networking."),
            ("3", "Featured Project Section", "Attach live PDF certificates, GitHub repositories, and capstone presentation links to prove competence visually.")
        ],
        "rule": "Pre-Hiring Audit: Over 75% of employers screen candidates' social profiles before issuing job offers! Delete unprofessional memes or aggressive comments before starting your job search.",
        "fig_title": "Figure 16 &bull; LinkedIn Profile Anatomy for High-Impact Hiring",
        "takeaway": "Key Takeaway: Professional Headshot + Skill-Based Headline + Featured Projects = Recruiter Inbound.",
        "notes": "Guide undergraduate students on how to connect with Sasi College alumni working in Bangalore, Chennai, and Hyderabad.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- LinkedIn Profile Blueprint Card -->
  <rect x="30" y="30" width="540" height="300" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <!-- Top Banner -->
  <rect x="30" y="30" width="540" height="70" rx="10 10 0 0" fill="#0077B5"/>
  <text x="300" y="70" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">EXECUTIVE LINKEDIN PROFILE BLUEPRINT</text>
  <!-- Avatar (Circle) -->
  <circle cx="85" cy="100" r="32" fill="#FFFFFF" stroke="#0077B5" stroke-width="3"/>
  <circle cx="85" cy="100" r="28" fill="#E0F2FE"/>
  <text x="85" y="105" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#0369A1" text-anchor="middle">HV</text>
  <!-- Name & Professional Headline -->
  <text x="135" y="115" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#0F172A">Hari Vignesh</text>
  <text x="135" y="132" font-family="system-ui, sans-serif" font-size="10.5" font-weight="600" fill="#0077B5">Aspiring Systems Analyst | B.Sc | Excel Modeling &bull; Cloud Governance &bull; Cyber Defense</text>
  <text x="135" y="148" font-family="system-ui, sans-serif" font-size="9" fill="#64748B">Sasi College &bull; Chennai, Tamil Nadu &bull; 500+ Connections</text>
  <!-- 3 Profile Building Blocks -->
  <rect x="45" y="165" width="160" height="145" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
  <rect x="55" y="175" width="80" height="20" rx="4" fill="#0077B5"/>
  <text x="95" y="189" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">ABOUT SECTION</text>
  <text x="55" y="212" font-family="system-ui, sans-serif" font-size="9" fill="#475569">First person summary:</text>
  <text x="55" y="228" font-family="system-ui, sans-serif" font-size="8.5" fill="#0F172A">"Undergraduate focused on enterprise IT systems, data hygiene, and practical automation."</text>
  <rect x="220" y="165" width="160" height="145" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
  <rect x="230" y="175" width="80" height="20" rx="4" fill="#059669"/>
  <text x="270" y="189" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">FEATURED WORK</text>
  <text x="230" y="212" font-family="system-ui, sans-serif" font-size="9" fill="#475569">Visual Evidence:</text>
  <text x="230" y="228" font-family="system-ui, sans-serif" font-size="8.5" fill="#0F172A">&bull; ATS Resume PDF</text>
  <text x="230" y="244" font-family="system-ui, sans-serif" font-size="8.5" fill="#0F172A">&bull; Capstone Project Link</text>
  <text x="230" y="260" font-family="system-ui, sans-serif" font-size="8.5" fill="#0F172A">&bull; NPTEL Gold Badge</text>
  <rect x="395" y="165" width="160" height="145" rx="8" fill="#F8FAFC" stroke="#E2E8F0"/>
  <rect x="405" y="175" width="80" height="20" rx="4" fill="#D97706"/>
  <text x="445" y="189" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">ENDORSES</text>
  <text x="405" y="212" font-family="system-ui, sans-serif" font-size="9" fill="#475569">Social Proof:</text>
  <text x="405" y="228" font-family="system-ui, sans-serif" font-size="8.5" fill="#0F172A">&bull; 15 Professor Endorsements</text>
  <text x="405" y="244" font-family="system-ui, sans-serif" font-size="8.5" fill="#0F172A">&bull; Peer recommendations</text>
  <text x="405" y="260" font-family="system-ui, sans-serif" font-size="8.5" fill="#0F172A">&bull; Verified Skill Badges</text>
</svg>"""
    },
    # 66
    {
        "num": "66",
        "index": "17",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "Digital Education",
        "title": "National Online Learning: SWAYAM Central & NPTEL",
        "subtitle": "Accessing world-class courses designed by IITs and IISc, understanding UGC credit transfer rules, and boosting college transcripts for free.",
        "analogy_title": "Free Admission to Premier IIT Lecture Halls",
        "analogy_text": "Before national MOOC portals, only students who passed the grueling JEE could attend lectures by IIT professors. <strong>SWAYAM and NPTEL open the digital gates of IIT Madras, IIT Bombay, and IISc to any student in India for free</strong>, from the comfort of their home.",
        "steps": [
            ("1", "Enrollment & 4 Quadrants", "Access video lectures, downloadable reading materials, weekly self-assessment quizzes, and active discussion forums."),
            ("2", "Proctored Exam Certification", "After 8 or 12 weeks of self-study, sit for an offline proctored exam at a local center for an authentic IIT-verified certificate."),
            ("3", "UGC Credit Transfer", "Under University Grants Commission regulations, students can transfer up to 40% of their semester degree credits through SWAYAM!")
        ],
        "rule": "Transcript Superpower: An NPTEL certificate signed by an IIT professor on your resume immediately separates you from thousands of other job applicants.",
        "fig_title": "Figure 17 &bull; The SWAYAM 4-Quadrant Instructional Model",
        "takeaway": "Key Takeaway: 4 Quadrants (Video, Reading, Quizzes, Forums) + Proctored Exam = UGC Credit Transfer.",
        "notes": "Encourage students to enroll in at least one NPTEL course per academic year to build specialized industry skills.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Central SWAYAM Hub -->
  <rect x="220" y="35" width="160" height="40" rx="6" fill="#0284C7"/>
  <text x="300" y="58" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#FFFFFF" text-anchor="middle">SWAYAM / NPTEL</text>
  <text x="300" y="70" font-family="system-ui, sans-serif" font-size="7.5" fill="#E0F2FE" text-anchor="middle">IITs &bull; IISc &bull; MHRD &bull; UGC</text>
  <!-- 4 Quadrants Grid -->
  <!-- Quadrant 1 -->
  <rect x="30" y="95" width="250" height="105" rx="8" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
  <rect x="45" y="105" width="80" height="20" rx="3" fill="#E0F2FE"/>
  <text x="85" y="119" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#0369A1" text-anchor="middle">QUADRANT 1</text>
  <text x="45" y="142" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">e-Tutorial (Video Lectures)</text>
  <text x="45" y="160" font-family="system-ui, sans-serif" font-size="9" fill="#475569">High-definition modular videos taught by IIT &amp; IISc faculty</text>
  <text x="45" y="175" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B">Animation, laboratory demos, real-world case studies</text>
  <!-- Quadrant 2 -->
  <rect x="320" y="95" width="250" height="105" rx="8" fill="#FFFFFF" stroke="#059669" stroke-width="1.5"/>
  <rect x="335" y="105" width="80" height="20" rx="3" fill="#ECFDF5"/>
  <text x="375" y="119" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#047857" text-anchor="middle">QUADRANT 2</text>
  <text x="335" y="142" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">e-Content (Reading Material)</text>
  <text x="335" y="160" font-family="system-ui, sans-serif" font-size="9" fill="#475569">Downloadable PDF eBooks, lecture transcripts, summaries</text>
  <text x="335" y="175" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B">Curated references and textbook chapters for deep study</text>
  <!-- Quadrant 3 -->
  <rect x="30" y="215" width="250" height="105" rx="8" fill="#FFFFFF" stroke="#D97706" stroke-width="1.5"/>
  <rect x="45" y="225" width="80" height="20" rx="3" fill="#FEF3C7"/>
  <text x="85" y="239" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#B45309" text-anchor="middle">QUADRANT 3</text>
  <text x="45" y="262" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Self-Assessment (Quizzes)</text>
  <text x="45" y="280" font-family="system-ui, sans-serif" font-size="9" fill="#475569">Weekly graded multiple-choice questions &amp; coding tests</text>
  <text x="45" y="295" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B">Instant performance feedback and solution explanations</text>
  <!-- Quadrant 4 -->
  <rect x="320" y="215" width="250" height="105" rx="8" fill="#FFFFFF" stroke="#9333EA" stroke-width="1.5"/>
  <rect x="335" y="225" width="80" height="20" rx="3" fill="#FAF5FF"/>
  <text x="375" y="239" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#7E22CE" text-anchor="middle">QUADRANT 4</text>
  <text x="335" y="262" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0F172A">Discussion Forum (Clearing Doubts)</text>
  <text x="335" y="280" font-family="system-ui, sans-serif" font-size="9" fill="#475569">Dedicated teaching assistants answering technical questions</text>
  <text x="335" y="295" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B">Peer networking with students across 1,000+ colleges</text>
</svg>"""
    },
    # 67
    {
        "num": "67",
        "index": "18",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "Learning Methodology",
        "title": "Smart Self-Paced Learning: Documentation & Active Recall",
        "subtitle": "Why passively binge-watching tutorial videos causes an illusion of competence, and how hands-on documentation reading builds true mastery.",
        "analogy_title": "Watching Cooking Shows vs. Actually Cooking a Dish",
        "analogy_text": "Watching 5 hours of cooking tutorials on YouTube makes you feel like a chef, but you cannot cook until you <strong>physically enter the kitchen, cut vegetables, and handle the heat</strong>. Watching programming or Excel videos without typing formulas is passive entertainment, not learning.",
        "steps": [
            ("1", "The Illusion of Competence", "Nodding along with a video tutorial gives false confidence. You only know a tool when you can use it on a blank screen with no assistance."),
            ("2", "Official Documentation First", "YouTube videos get outdated quickly. Learning to read official docs (`support.microsoft.com` or `python.org`) teaches self-reliance."),
            ("3", "Active Recall & Spaced Repetition", "Test yourself 24 hours later. Build mini-projects rather than memorizing definitions.")
        ],
        "rule": "The Blank Screen Test: After watching any software tutorial, close the video, open a blank document, and recreate the exercise from scratch without looking. If you get stuck, that is where real learning begins.",
        "fig_title": "Figure 18 &bull; The Learning Retention Pyramid",
        "takeaway": "Key Takeaway: Passive Lecture = 10% retention; Hands-on Practice & Teaching Others = 90% retention.",
        "notes": "Guide students to overcome tutorial paralysis by building their own small projects (e.g. personal budget in Excel).",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- The Retention Pyramid -->
  <text x="300" y="45" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#0F172A" text-anchor="middle">THE LEARNING RETENTION PYRAMID</text>
  <!-- Tier 1 (Passive) -->
  <polygon points="260,65 340,65 370,105 230,105" fill="#FEE2E2" stroke="#EF4444" stroke-width="1.5"/>
  <text x="300" y="85" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#B91C1C" text-anchor="middle">Passive Video Watching (10%)</text>
  <text x="300" y="98" font-family="system-ui, sans-serif" font-size="8" fill="#7F1D1D" text-anchor="middle">Illusion of competence &bull; Forgotten in 48 hrs</text>
  <!-- Tier 2 -->
  <polygon points="230,110 370,110 410,165 190,165" fill="#FEF3C7" stroke="#F59E0B" stroke-width="1.5"/>
  <text x="300" y="135" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#B45309" text-anchor="middle">Reading Official Docs &amp; Books (30%)</text>
  <text x="300" y="150" font-family="system-ui, sans-serif" font-size="8.5" fill="#78350F" text-anchor="middle">Direct source material &bull; Independent problem solving</text>
  <!-- Tier 3 -->
  <polygon points="190,170 410,170 460,235 140,235" fill="#E0F2FE" stroke="#0284C7" stroke-width="1.5"/>
  <text x="300" y="198" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#0369A1" text-anchor="middle">Hands-On Practice by Doing (75%)</text>
  <text x="300" y="215" font-family="system-ui, sans-serif" font-size="9" fill="#0C4A6E" text-anchor="middle">Building personal spreadsheets, typing code, fixing errors</text>
  <!-- Tier 4 (Mastery) -->
  <polygon points="140,240 460,240 510,315 90,315" fill="#DCFCE7" stroke="#10B981" stroke-width="2"/>
  <text x="300" y="272" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#166534" text-anchor="middle">Active Recall &amp; Teaching Others (90%)</text>
  <text x="300" y="292" font-family="system-ui, sans-serif" font-size="9.5" fill="#14532D" text-anchor="middle">Explain concept to classmate &bull; Build capstone project from scratch</text>
</svg>"""
    },
    # 68
    {
        "num": "68",
        "index": "19",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "Digital Governance",
        "title": "Citizen Services: UIDAI Aadhaar & Masked Aadhaar",
        "subtitle": "Understanding national identity infrastructure, biometric authentication, DigiLocker, and why Masked Aadhaar protects against fraud.",
        "analogy_title": "National ID Card with a Privacy Shutter",
        "analogy_text": "Sharing your full 12-digit Aadhaar card at a hotel or photocopy shop is like <strong>handing a stranger your house keys and password list</strong>. <strong>Masked Aadhaar is like an ID card with a shutter</strong>: it displays your verified photo and government seal, but covers the first 8 digits so nobody can steal your identity.",
        "steps": [
            ("1", "Aadhaar Microarchitecture", "12-digit random identifier linked to 10 fingerprints, 2 iris scans, and facial biometrics managed by UIDAI."),
            ("2", "Masked Aadhaar (`xxxx-xxxx-1234`)", "Downloadable from `myaadhaar.uidai.gov.in`. Conceals first 8 digits while remaining 100% legally valid for hotel check-ins and SIM cards."),
            ("3", "DigiLocker Integration", "Government cloud repository issuing legally recognized digital driving licenses, marksheets, and voter IDs under IT Act 2000 Rule 9A.")
        ],
        "rule": "Statutory Protection: The Reserve Bank of India (RBI) and UIDAI explicitly state that private entities (hotels, cinemas, gyms) CANNOT demand your full unmasked Aadhaar number. Always provide Masked Aadhaar!",
        "fig_title": "Figure 19 &bull; Regular Aadhaar vs. Secure Masked Aadhaar",
        "takeaway": "Key Takeaway: Masked Aadhaar hides first 8 digits; biometric lock prevents fraudulent SIM cards.",
        "notes": "Demonstrate the 'Lock Biometrics' feature on the mAadhaar smartphone app to lock fingerprint scanners.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Regular Aadhaar (Vulnerable) -->
  <rect x="30" y="45" width="255" height="270" rx="10" fill="#FFFFFF" stroke="#EF4444" stroke-width="2"/>
  <rect x="45" y="60" width="130" height="24" rx="4" fill="#FEE2E2"/>
  <text x="110" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#991B1B" text-anchor="middle">REGULAR AADHAAR</text>
  <text x="45" y="105" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#B91C1C">Exposed 12 Digits</text>
  <!-- Card Mockup -->
  <rect x="45" y="120" width="225" height="110" rx="6" fill="#F8FAFC" stroke="#FECACA"/>
  <rect x="55" y="132" width="35" height="42" rx="3" fill="#CBD5E1"/>
  <text x="100" y="145" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#0F172A">Govt of India</text>
  <text x="100" y="160" font-family="system-ui, sans-serif" font-size="8" fill="#64748B">DOB: 15/08/2003</text>
  <!-- Full numbers visible -->
  <rect x="55" y="185" width="205" height="30" rx="4" fill="#FEE2E2"/>
  <text x="157" y="205" font-family="monospace" font-size="12" font-weight="800" fill="#DC2626" text-anchor="middle">9876 5432 1098</text>
  <text x="45" y="250" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">&bull; Left behind at local photocopy xerox shops</text>
  <text x="45" y="265" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">&bull; Vulnerable to illegal SIM card issuance</text>
  <text x="45" y="280" font-family="system-ui, sans-serif" font-size="9" fill="#DC2626">&bull; High risk of banking impersonation</text>
  <!-- Masked Aadhaar (Secure) -->
  <rect x="315" y="45" width="255" height="270" rx="10" fill="#FFFFFF" stroke="#10B981" stroke-width="2"/>
  <rect x="330" y="60" width="130" height="24" rx="4" fill="#D1FAE5"/>
  <text x="395" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#065F46" text-anchor="middle">MASKED AADHAAR</text>
  <text x="330" y="105" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#047857">Legally Protected</text>
  <!-- Card Mockup -->
  <rect x="330" y="120" width="225" height="110" rx="6" fill="#F8FAFC" stroke="#A7F3D0"/>
  <rect x="340" y="132" width="35" height="42" rx="3" fill="#A7F3D0"/>
  <text x="385" y="145" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#0F172A">Govt of India</text>
  <text x="385" y="160" font-family="system-ui, sans-serif" font-size="8" fill="#64748B">DOB: 15/08/2003</text>
  <!-- Masked numbers -->
  <rect x="340" y="185" width="205" height="30" rx="4" fill="#D1FAE5"/>
  <text x="442" y="205" font-family="monospace" font-size="12" font-weight="800" fill="#047857" text-anchor="middle">XXXX XXXX 1098</text>
  <text x="330" y="250" font-family="system-ui, sans-serif" font-size="9" fill="#047857">&bull; 100% valid for hotel check-ins &amp; trains</text>
  <text x="330" y="265" font-family="system-ui, sans-serif" font-size="9" fill="#047857">&bull; First 8 digits completely concealed</text>
  <text x="330" y="280" font-family="system-ui, sans-serif" font-size="9" fill="#047857">&bull; QR code retains cryptographically signed proof</text>
</svg>"""
    },
    # 69
    {
        "num": "69",
        "index": "20",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "State e-Governance",
        "title": "State e-Governance: Land Records & Certificates",
        "subtitle": "How Tamil Nadu e-Services empower citizens to extract Patta, Chitta, Encumbrance Certificates (EC), and revenue certificates without middlemen.",
        "analogy_title": "Digital Land Ownership Deeds at Your Fingertips",
        "analogy_text": "Historically, verifying whether a plot of land had debts required <strong>standing in lines at government registrar offices for weeks</strong>. Today, state e-Governance portals let any citizen verify authentic government property records from a smartphone in 60 seconds.",
        "steps": [
            ("1", "Patta / Chitta Extraction", "Visit `eservices.tn.gov.in`. Enter District, Taluk, Village, and Survey number to generate digitally verified ownership records."),
            ("2", "Encumbrance Certificate (EC)", "Inspects registered sales, mortgages, or bank debt against a property over the last 30 years via the Inspector General of Registration (TNREGINET)."),
            ("3", "QR Code Verification", "Every digital certificate contains an asymmetric QR code that police, banks, and registrars can scan to verify authenticity.")
        ],
        "rule": "Real Estate Safety: Never buy a house or plot of land without extracting an online Encumbrance Certificate (EC). If the owner secretly mortgaged the property to a bank, the EC will expose it immediately!",
        "fig_title": "Figure 20 &bull; Tamil Nadu e-Services Architecture",
        "takeaway": "Key Takeaway: e-Services eliminate bribes and middlemen; QR codes ensure cryptographic authenticity.",
        "notes": "Show non-CS students how knowing how to pull Patta/Chitta makes them invaluable problem solvers for their families.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Process Workflow Steps -->
  <!-- Step 1: Citizen Portal -->
  <rect x="25" y="45" width="165" height="270" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
  <rect x="40" y="60" width="70" height="24" rx="4" fill="#E0F2FE"/>
  <text x="75" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0369A1" text-anchor="middle">STEP 1</text>
  <text x="40" y="110" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#0F172A">INPUT DATA</text>
  <text x="40" y="128" font-family="system-ui, sans-serif" font-size="9" fill="#64748B">eservices.tn.gov.in</text>
  <rect x="40" y="150" width="135" height="110" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="50" y="172" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; District: Coimbatore</text>
  <text x="50" y="192" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Taluk: Pollachi</text>
  <text x="50" y="212" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Village / Ward</text>
  <text x="50" y="232" font-family="system-ui, sans-serif" font-size="9" fill="#475569">&bull; Survey No / Sub-div</text>
  <!-- Arrow 1 -->
  <line x1="190" y1="180" x2="215" y2="180" stroke="#0284C7" stroke-width="3" stroke-linecap="round"/>
  <!-- Step 2: Database Registry -->
  <rect x="215" y="45" width="170" height="270" rx="10" fill="#FFFFFF" stroke="#059669" stroke-width="1.5"/>
  <rect x="230" y="60" width="70" height="24" rx="4" fill="#ECFDF5"/>
  <text x="265" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">STEP 2</text>
  <text x="230" y="110" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#0F172A">STATE REVENUE</text>
  <text x="230" y="128" font-family="system-ui, sans-serif" font-size="9" fill="#64748B">Centralized Database</text>
  <rect x="230" y="150" width="140" height="110" rx="6" fill="#F0FDF4" stroke="#BBF7D0"/>
  <text x="300" y="175" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#166534" text-anchor="middle">TNREGINET</text>
  <text x="300" y="195" font-family="system-ui, sans-serif" font-size="8.5" fill="#15803D" text-anchor="middle">Land Records &amp; Deeds</text>
  <text x="300" y="215" font-family="system-ui, sans-serif" font-size="8.5" fill="#15803D" text-anchor="middle">Mortgage History</text>
  <text x="300" y="235" font-family="system-ui, sans-serif" font-size="8.5" fill="#15803D" text-anchor="middle">Court Attachments Check</text>
  <!-- Arrow 2 -->
  <line x1="385" y1="180" x2="410" y2="180" stroke="#059669" stroke-width="3" stroke-linecap="round"/>
  <!-- Step 3: Instant Verified PDF -->
  <rect x="410" y="45" width="165" height="270" rx="10" fill="#FFFFFF" stroke="#9333EA" stroke-width="1.5"/>
  <rect x="425" y="60" width="70" height="24" rx="4" fill="#FAF5FF"/>
  <text x="460" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#7E22CE" text-anchor="middle">STEP 3</text>
  <text x="425" y="110" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#0F172A">VERIFIED PDF</text>
  <text x="425" y="128" font-family="system-ui, sans-serif" font-size="9" fill="#64748B">Instant Legal Download</text>
  <rect x="425" y="150" width="135" height="110" rx="6" fill="#FAF5FF" stroke="#E9D5FF"/>
  <text x="492" y="175" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#7E22CE" text-anchor="middle">Patta / Chitta / EC</text>
  <!-- QR Code representation -->
  <rect x="472" y="190" width="40" height="40" rx="3" fill="#7E22CE"/>
  <rect x="480" y="198" width="24" height="24" rx="2" fill="#FFFFFF"/>
  <text x="492" y="250" font-family="system-ui, sans-serif" font-size="8" fill="#64748B" text-anchor="middle">Digital Signature QR</text>
</svg>"""
    },
    # 70
    {
        "num": "70",
        "index": "21",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "Fintech Infrastructure",
        "title": "National Career Service & NPCI UPI Architecture",
        "subtitle": "How the National Payments Corporation of India (NPCI) clears bank-to-bank UPI transfers in under 2 seconds without exposing bank account numbers.",
        "analogy_title": "Direct Bank-to-Bank Wire via a Digital Nickname",
        "analogy_text": "In older banking systems, sending money required memorizing a 16-digit account number, branch address, and IFSC code. <strong>UPI is like having a single universal digital nickname (VPA)</strong>: money zips directly from your bank vault into the merchant's vault instantly, with no middlemen holding your cash.",
        "steps": [
            ("1", "VPA & Dynamic QR Code", "Virtual Payment Address (`username@okaxis` or phone number) masks your sensitive account number."),
            ("2", "NPCI Central Switch", "National Payments Corporation of India verifies cryptographic credentials and coordinates the real-time settlement."),
            ("3", "Immediate Gross Settlement", "Payer's bank debits funds; Payee's bank credits funds; confirmation SMS arrives on both smartphones in under 1.8 seconds.")
        ],
        "rule": "UPI Golden Rule: You NEVER need to enter your UPI PIN to RECEIVE money! If a buyer on OLX or Facebook Marketplace asks you to 'scan a QR code and enter your PIN to claim money', it is 100% FRAUD.",
        "fig_title": "Figure 21 &bull; NPCI UPI Instant Clearing Architecture",
        "takeaway": "Key Takeaway: PIN is ONLY for paying; VPA masks account numbers; NPCI routes in &lt;2 seconds.",
        "notes": "Remind students that UPI fraud is the #1 cyber scam affecting undergraduate students in India today.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Payer Bank (Left) -->
  <rect x="30" y="45" width="160" height="270" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
  <rect x="45" y="60" width="130" height="24" rx="4" fill="#E0F2FE"/>
  <text x="110" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0369A1" text-anchor="middle">PAYER (STUDENT)</text>
  <rect x="45" y="100" width="130" height="85" rx="6" fill="#F0F9FF" stroke="#BAE6FD"/>
  <text x="110" y="125" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0F172A" text-anchor="middle">UPI App (GPay / PhonePe)</text>
  <text x="110" y="145" font-family="monospace" font-size="9" fill="#0284C7" text-anchor="middle">Scans QR / Enters VPA</text>
  <rect x="65" y="155" width="90" height="20" rx="3" fill="#0284C7"/>
  <text x="110" y="169" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">Enters UPI PIN</text>
  <rect x="45" y="200" width="130" height="50" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="110" y="222" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#0F172A" text-anchor="middle">Remitter Bank (SBI)</text>
  <text x="110" y="238" font-family="system-ui, sans-serif" font-size="8.5" fill="#DC2626" text-anchor="middle">Debits &#8377;500</text>
  <!-- NPCI Central Switch (Middle) -->
  <rect x="220" y="45" width="160" height="270" rx="10" fill="#F0FDF4" stroke="#059669" stroke-width="2"/>
  <rect x="235" y="60" width="130" height="26" rx="4" fill="#059669"/>
  <text x="300" y="77" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#FFFFFF" text-anchor="middle">NPCI SWITCH</text>
  <text x="300" y="115" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">National Switch Engine</text>
  <circle cx="300" cy="170" r="34" fill="#FFFFFF" stroke="#059669" stroke-width="2"/>
  <text x="300" y="166" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#047857" text-anchor="middle">&lt;1.8s</text>
  <text x="300" y="182" font-family="system-ui, sans-serif" font-size="8" fill="#64748B" text-anchor="middle">Instant Settlement</text>
  <rect x="235" y="225" width="130" height="70" rx="6" fill="#FFFFFF" stroke="#A7F3D0"/>
  <text x="300" y="245" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" fill="#0F172A" text-anchor="middle">13+ Billion</text>
  <text x="300" y="260" font-family="system-ui, sans-serif" font-size="8" fill="#64748B" text-anchor="middle">Monthly Transactions</text>
  <text x="300" y="278" font-family="system-ui, sans-serif" font-size="8" font-weight="600" fill="#059669" text-anchor="middle">World Leader in Fintech</text>
  <!-- Payee Bank (Right) -->
  <rect x="410" y="45" width="160" height="270" rx="10" fill="#FFFFFF" stroke="#059669" stroke-width="1.5"/>
  <rect x="425" y="60" width="130" height="24" rx="4" fill="#ECFDF5"/>
  <text x="490" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">PAYEE (MERCHANT)</text>
  <rect x="425" y="100" width="130" height="85" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="490" y="125" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0F172A" text-anchor="middle">Merchant Account</text>
  <text x="490" y="145" font-family="monospace" font-size="9" fill="#059669" text-anchor="middle">VPA: bookstore@upi</text>
  <rect x="445" y="155" width="90" height="20" rx="3" fill="#059669"/>
  <text x="490" y="169" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">No PIN needed</text>
  <rect x="425" y="200" width="130" height="50" rx="6" fill="#F0FDF4" stroke="#BBF7D0"/>
  <text x="490" y="222" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#166534" text-anchor="middle">Beneficiary Bank (HDFC)</text>
  <text x="490" y="238" font-family="system-ui, sans-serif" font-size="8.5" fill="#15803D" text-anchor="middle">Credits &#8377;500</text>
</svg>"""
    }
]

print(f"data_unit4 part 3 initialized with {len(unit4_part3_topics)} topics.")
