"""
Unit 4 Data Part 2: Topics 60 to 70 (11 Topics)
Cloud Collaboration, Digital India & UPI Payments
"""

unit4_part2_topics = [
    # 60
    {
        "num": "60",
        "index": "11",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "Cloud Collaboration",
        "title": "Cloud Storage Architecture: Google Drive & File Sync",
        "subtitle": "How files are replicated across hyperscale data centers, freeing your laptop storage while ensuring 99.99% availability.",
        "analogy_title": "Bank Safety Deposit Box in the Sky",
        "analogy_text": "Saving a file to your laptop hard disk is like <strong>keeping cash inside your physical wallet</strong>; if your laptop is stolen or dropped in water, the cash is gone. <strong>Cloud storage is like depositing money into a secure national bank</strong> &mdash; accessible from any ATM or smartphone anywhere in the world.",
        "steps": [
            ("1", "Local File Ingestion", "You drag an assignment file into your Google Drive folder; the desktop agent calculates a cryptographic hash."),
            ("2", "Multi-Region Replication", "Google automatically splits the file into encrypted chunks and clones it across at least 3 geographically separated data centers."),
            ("3", "Instant Delta Sync", "If you modify slide 3, only the altered bytes are synced, conserving internet bandwidth.")
        ],
        "rule": "15 GB Storage Hygiene: When your free 15 GB Google storage fills up, Gmail stops receiving incoming emails! Use 'Clean up storage' to delete large forgotten video files rather than panicking.",
        "fig_title": "Figure 11 &bull; Cloud Storage vs. Local Hard Disk",
        "takeaway": "Key Takeaway: Cloud storage provides multi-device accessibility, automatic backup, and cross-continent replication.",
        "notes": "Demonstrate the Google Drive web interface: how to use search chips to find PDFs modified in the last 7 days.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- User Devices (Left) -->
  <rect x="30" y="45" width="180" height="270" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
  <rect x="45" y="60" width="150" height="24" rx="4" fill="#E0F2FE"/>
  <text x="120" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0369A1" text-anchor="middle">USER CLIENT DEVICES</text>
  <rect x="50" y="100" width="140" height="45" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="120" y="120" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0F172A" text-anchor="middle">Laptop (Workstation)</text>
  <text x="120" y="135" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Local Drive Client Active</text>
  <rect x="50" y="155" width="140" height="45" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="120" y="175" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0F172A" text-anchor="middle">Smartphone (Mobile)</text>
  <text x="120" y="190" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Instant Photo &amp; Doc Access</text>
  <rect x="50" y="210" width="140" height="45" rx="6" fill="#F8FAFC" stroke="#E2E8F0"/>
  <text x="120" y="230" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0F172A" text-anchor="middle">College Lab PC</text>
  <text x="120" y="245" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Web Browser Portal Session</text>
  <text x="120" y="295" font-family="system-ui, sans-serif" font-size="9" font-weight="600" fill="#0284C7" text-anchor="middle">Anywhere, Any Device Access</text>
  <!-- Bi-directional Sync Arrows -->
  <line x1="210" y1="180" x2="270" y2="180" stroke="#0284C7" stroke-width="4" stroke-linecap="round"/>
  <polygon points="270,174 282,180 270,186" fill="#0284C7"/>
  <polygon points="222,174 210,180 222,186" fill="#0284C7"/>
  <text x="246" y="165" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#0284C7" text-anchor="middle">Encrypted TLS</text>
  <text x="246" y="200" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Delta Sync</text>
  <!-- Cloud Hyperscale Center (Right) -->
  <rect x="290" y="45" width="280" height="270" rx="10" fill="#F0F9FF" stroke="#0284C7" stroke-width="2"/>
  <rect x="310" y="60" width="240" height="26" rx="4" fill="#0369A1"/>
  <text x="430" y="77" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#FFFFFF" text-anchor="middle">HYPERSCALE CLOUD DATA CENTER</text>
  <!-- 3 Replicated Nodes -->
  <rect x="310" y="100" width="240" height="48" rx="6" fill="#FFFFFF" stroke="#BAE6FD"/>
  <circle cx="330" cy="124" r="8" fill="#22C55E"/>
  <text x="350" y="120" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0F172A">Primary Node &bull; Mumbai Center</text>
  <text x="350" y="135" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B">Active Master Copy &bull; Immediate Low Latency</text>
  <rect x="310" y="155" width="240" height="48" rx="6" fill="#FFFFFF" stroke="#BAE6FD"/>
  <circle cx="330" cy="179" r="8" fill="#22C55E"/>
  <text x="350" y="175" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0F172A">Replica Node &bull; Hyderabad Center</text>
  <text x="350" y="190" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B">Real-time geo-redundancy backup clone</text>
  <rect x="310" y="210" width="240" height="48" rx="6" fill="#FFFFFF" stroke="#BAE6FD"/>
  <circle cx="330" cy="234" r="8" fill="#22C55E"/>
  <text x="350" y="230" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0F172A">Cold Storage Archive &bull; Singapore</text>
  <text x="350" y="245" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B">Immutable disaster recovery failover copy</text>
  <rect x="310" y="270" width="240" height="30" rx="4" fill="#E0F2FE"/>
  <text x="430" y="289" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0369A1" text-anchor="middle">99.999999999% (11 9's) Data Durability</text>
</svg>"""
    },
    # 61
    {
        "num": "61",
        "index": "12",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "Cloud Governance",
        "title": "Cloud File Permissions: Viewer, Commenter & Editor",
        "subtitle": "The 3-tier access control matrix, link sharing hazards, and how to prevent unauthorized downloads of confidential documents.",
        "analogy_title": "Glass Display Case vs. Sticky Notes vs. Room Keys",
        "analogy_text": "<strong>Viewer:</strong> is looking at a precious diamond inside a bulletproof museum glass case (you can look, but cannot touch). <strong>Commenter:</strong> is putting yellow sticky-notes on a notice board without altering the text. <strong>Editor:</strong> is handing someone the physical master keys and a permanent marker to rewrite everything.",
        "steps": [
            ("1", "Viewer (Read-Only)", "Recipient can read the document. Pro tip: Disable 'Viewers can download, print, and copy' in advanced settings for exams."),
            ("2", "Commenter (Feedback)", "Perfect for professors grading essays: can highlight paragraphs and propose changes without altering original sentences."),
            ("3", "Editor (Full Control)", "Can rewrite sentences, delete paragraphs, and share permissions with others. Reserve strictly for trusted team members.")
        ],
        "rule": "Security Red Flag: Never set a confidential project folder to 'Anyone with the link can Edit'! Anyone who gets the link can anonymously delete every file in your Google Drive without leaving a trace.",
        "fig_title": "Figure 12 &bull; Three-Tier Cloud Permission Hierarchy",
        "takeaway": "Key Takeaway: Restrict link sharing; assign minimum privilege (Viewer by default, Editor only when needed).",
        "notes": "Show students how to click the Gear icon in the Google Drive share modal to uncheck download and print permissions for viewers.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- 3 Permission Tiers Grid -->
  <!-- Viewer -->
  <rect x="25" y="40" width="170" height="280" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="2"/>
  <rect x="40" y="55" width="80" height="26" rx="4" fill="#E0F2FE"/>
  <text x="80" y="72" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#0369A1" text-anchor="middle">VIEWER</text>
  <text x="40" y="110" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#0F172A">READ-ONLY</text>
  <text x="40" y="130" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#0284C7">Safest Sharing Tier</text>
  <rect x="40" y="145" width="140" height="1" fill="#E2E8F0"/>
  <text x="40" y="170" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&check; Can read file on screen</text>
  <text x="40" y="195" font-family="system-ui, sans-serif" font-size="9.5" fill="#DC2626">&cross; Cannot change a single letter</text>
  <text x="40" y="220" font-family="system-ui, sans-serif" font-size="9.5" fill="#DC2626">&cross; Cannot leave margin comments</text>
  <rect x="35" y="245" width="150" height="60" rx="6" fill="#F0F9FF"/>
  <text x="110" y="268" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#0369A1" text-anchor="middle">Best for: Distributing</text>
  <text x="110" y="284" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Syllabus, Exam Hall Tickets, Handouts</text>
  <!-- Commenter -->
  <rect x="215" y="40" width="170" height="280" rx="10" fill="#FFFFFF" stroke="#059669" stroke-width="2"/>
  <rect x="230" y="55" width="100" height="26" rx="4" fill="#ECFDF5"/>
  <text x="280" y="72" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#047857" text-anchor="middle">COMMENTER</text>
  <text x="230" y="110" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#0F172A">FEEDBACK TIER</text>
  <text x="230" y="130" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#059669">Collaborative Review</text>
  <rect x="230" y="145" width="140" height="1" fill="#E2E8F0"/>
  <text x="230" y="170" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&check; Can read full document</text>
  <text x="230" y="195" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&check; Can highlight &amp; leave notes</text>
  <text x="230" y="220" font-family="system-ui, sans-serif" font-size="9.5" fill="#DC2626">&cross; Original sentences stay intact</text>
  <rect x="225" y="245" width="150" height="60" rx="6" fill="#F0FDF4"/>
  <text x="300" y="268" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#047857" text-anchor="middle">Best for: Professors</text>
  <text x="300" y="284" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Reviewing Draft Theses &amp; Resumes</text>
  <!-- Editor -->
  <rect x="405" y="40" width="170" height="280" rx="10" fill="#FFFFFF" stroke="#DC2626" stroke-width="2"/>
  <rect x="420" y="55" width="70" height="26" rx="4" fill="#FEE2E2"/>
  <text x="455" y="72" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#991B1B" text-anchor="middle">EDITOR</text>
  <text x="420" y="110" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#0F172A">FULL CONTROL</text>
  <text x="420" y="130" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#DC2626">High Privilege Level</text>
  <rect x="420" y="145" width="140" height="1" fill="#E2E8F0"/>
  <text x="420" y="170" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&check; Can rewrite &amp; delete all text</text>
  <text x="420" y="195" font-family="system-ui, sans-serif" font-size="9.5" fill="#475569">&check; Can share access with others</text>
  <text x="420" y="220" font-family="system-ui, sans-serif" font-size="9.5" fill="#DC2626">&cross; High risk if link is public!</text>
  <rect x="415" y="245" width="150" height="60" rx="6" fill="#FEF2F2"/>
  <text x="490" y="268" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#991B1B" text-anchor="middle">Best for: Co-Authors</text>
  <text x="490" y="284" font-family="system-ui, sans-serif" font-size="8.5" fill="#64748B" text-anchor="middle">Trusted teammates creating project work</text>
</svg>"""
    },
    # 62
    {
        "num": "62",
        "index": "13",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "Cloud Productivity",
        "title": "Real-time Collaboration: Co-Authoring & Version History",
        "subtitle": "How Operational Transformation algorithms merge keystrokes from 10 simultaneous users, and how to time-travel using Version History.",
        "analogy_title": "A Giant Shared Whiteboard in the Sky",
        "analogy_text": "Before cloud docs, teammates emailed Word files named `Report_v1_final_revised_FINAL2.docx`, causing chaos. Google Docs is like <strong>standing together in front of a giant classroom whiteboard</strong>: everyone holds a different colored marker, writing simultaneously without erasing each other's work.",
        "steps": [
            ("1", "Simultaneous Cursors", "Multiple students edit the same essay in real time from separate laptops across different cities."),
            ("2", "Suggesting Mode", "Edits appear as highlighted track changes with Accept (&check;) and Reject (&cross;) buttons for the project leader."),
            ("3", "Version History Time-Travel", "Every keystroke is auto-saved with a timestamp. You can see who typed what at 2:15 PM last Tuesday and restore that version in 1 click!")
        ],
        "rule": "Audit Defense: In group projects, Version History shows the exact percentage of sentences written by each team member &mdash; eliminating arguments about who contributed to the assignment!",
        "fig_title": "Figure 13 &bull; Real-time Multi-User Cloud Editing Canvas",
        "takeaway": "Key Takeaway: Simultaneous multi-cursor co-authoring + Suggesting Mode + 1-Click Version Restoration.",
        "notes": "Demonstrate the shortcut Ctrl + Alt + Shift + H to open Version History in Google Docs.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Google Docs Editor Frame -->
  <rect x="30" y="30" width="540" height="300" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
  <!-- Editor Toolbar -->
  <rect x="30" y="30" width="540" height="38" rx="8" fill="#F8FAFC"/>
  <rect x="45" y="40" width="180" height="18" rx="3" fill="#E2E8F0"/>
  <text x="55" y="53" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#0F172A">Annual Project Submission.docx</text>
  <!-- Active Multi-User Avatars -->
  <circle cx="460" cy="49" r="12" fill="#0284C7"/>
  <text x="460" y="53" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#FFFFFF" text-anchor="middle">HV</text>
  <circle cx="490" cy="49" r="12" fill="#059669"/>
  <text x="490" y="53" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#FFFFFF" text-anchor="middle">PS</text>
  <circle cx="520" cy="49" r="12" fill="#D97706"/>
  <text x="520" y="53" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#FFFFFF" text-anchor="middle">AK</text>
  <!-- Document Page -->
  <rect x="55" y="85" width="490" height="230" rx="4" fill="#FFFFFF" stroke="#F1F5F9"/>
  <text x="75" y="115" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#0F172A">Executive Summary: IT Competency Standards</text>
  <text x="75" y="145" font-family="system-ui, sans-serif" font-size="11" fill="#334155">In accordance with the 2026 undergraduate NME curriculum,</text>
  <!-- User 1 Cursor (Blue) -->
  <rect x="375" y="132" width="2" height="16" fill="#0284C7"/>
  <rect x="377" y="122" width="60" height="14" rx="2" fill="#0284C7"/>
  <text x="407" y="132" font-family="system-ui, sans-serif" font-size="8" font-weight="700" fill="#FFFFFF" text-anchor="middle">Hari (typing)</text>
  <!-- Suggesting Mode Box -->
  <rect x="75" y="165" width="450" height="55" rx="6" fill="#ECFDF5" stroke="#A7F3D0"/>
  <text x="90" y="188" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#047857">Suggesting Mode (Priya): "Replace legacy flowchart with dynamic SVG matrix"</text>
  <rect x="430" y="175" width="36" height="24" rx="4" fill="#059669"/>
  <text x="448" y="191" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">&check;</text>
  <rect x="475" y="175" width="36" height="24" rx="4" fill="#EF4444"/>
  <text x="493" y="191" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">&cross;</text>
  <!-- Version History Bar -->
  <rect x="75" y="240" width="450" height="60" rx="6" fill="#F8FAFC" stroke="#CBD5E1"/>
  <text x="90" y="260" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0F172A">Version History Snapshot &bull; Tuesday 2:15 PM</text>
  <text x="90" y="278" font-family="system-ui, sans-serif" font-size="9" fill="#64748B">38 edits by 3 contributors &bull; Revert to this revision in 1 click</text>
  <rect x="420" y="255" width="90" height="28" rx="4" fill="#0284C7"/>
  <text x="465" y="273" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#FFFFFF" text-anchor="middle">Restore Version</text>
</svg>"""
    },
    # 63
    {
        "num": "63",
        "index": "14",
        "unit": "Unit 4",
        "unit_full": "Unit 4 &bull; Internet & Cloud",
        "category": "Assistive Tools",
        "title": "Voice AI & Instant Multilingual Translation",
        "subtitle": "Leveraging speech-to-text neural models for hands-free typing, auditory proofreading via text-to-speech, and instant document translation.",
        "analogy_title": "An Executive Stenographer & Multi-Language Interpreter",
        "analogy_text": "Using Voice AI is like having a <strong>personal stenographer sitting beside you</strong> who types 150 words per minute as you speak, paired with a <strong>diplomatic interpreter</strong> who instantly translates your English project into Tamil, Hindi, or Telugu in under 3 seconds.",
        "steps": [
            ("1", "Voice Typing (Speech-to-Text)", "Press `Ctrl + Shift + S` in Google Docs. Speak punctuation aloud ('comma', 'new paragraph') for rapid hands-free drafting."),
            ("2", "Auditory Proofreading (TTS)", "When you read your own writing on screen, your brain skips typos. Having text-to-speech read it aloud instantly exposes awkward phrasing."),
            ("3", "Neural Document Translation", "Go to `Tools &rarr; Translate document` to generate a duplicate copy in Tamil or Hindi with layout preserved.")
        ],
        "rule": "Accessibility Best Practice: Voice typing enables students with repetitive strain injuries or physical disabilities to complete long undergraduate dissertations without fatigue.",
        "fig_title": "Figure 14 &bull; Voice AI & Translation Pipeline",
        "takeaway": "Key Takeaway: Voice Typing speeds drafting 3x; Auditory TTS catches silent typos; Neural AI translates instantly.",
        "notes": "Encourage non-computer students who struggle with keyboard typing speed to embrace voice typing for rapid first drafts.",
        "svg": """<svg viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="360" rx="12" fill="#F8FAFC"/>
  <!-- Pipeline: Audio Wave -> Neural AI -> Translated Document -->
  <rect x="25" y="45" width="165" height="270" rx="10" fill="#FFFFFF" stroke="#0284C7" stroke-width="1.5"/>
  <rect x="40" y="60" width="70" height="24" rx="4" fill="#E0F2FE"/>
  <text x="75" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0369A1" text-anchor="middle">PHASE 1</text>
  <text x="40" y="110" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#0F172A">VOICE INPUT</text>
  <text x="40" y="128" font-family="system-ui, sans-serif" font-size="9" fill="#64748B">Acoustic Audio Waveform</text>
  <!-- Soundwave representation -->
  <path d="M 40 180 Q 55 140 70 180 T 100 180 T 130 180 T 160 180" fill="none" stroke="#0284C7" stroke-width="3"/>
  <text x="107" y="225" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#0369A1" text-anchor="middle">Ctrl + Shift + S</text>
  <text x="40" y="255" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569">Spoken English / Regional</text>
  <text x="40" y="270" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569">Punctuation commands</text>
  <!-- Arrow 1 -->
  <line x1="190" y1="180" x2="215" y2="180" stroke="#0284C7" stroke-width="3" stroke-linecap="round"/>
  <!-- Phase 2: Neural Engine -->
  <rect x="215" y="45" width="170" height="270" rx="10" fill="#FFFFFF" stroke="#059669" stroke-width="1.5"/>
  <rect x="230" y="60" width="70" height="24" rx="4" fill="#ECFDF5"/>
  <text x="265" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#047857" text-anchor="middle">PHASE 2</text>
  <text x="230" y="110" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#0F172A">AI TRANSLATION</text>
  <text x="230" y="128" font-family="system-ui, sans-serif" font-size="9" fill="#64748B">Deep Transformer Models</text>
  <rect x="230" y="155" width="140" height="70" rx="6" fill="#F0FDF4" stroke="#BBF7D0"/>
  <text x="300" y="180" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#166534" text-anchor="middle">Tools &rarr; Translate</text>
  <text x="300" y="200" font-family="system-ui, sans-serif" font-size="9" fill="#15803D" text-anchor="middle">100+ Languages</text>
  <text x="230" y="255" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569">Tamil, Telugu, Hindi, French</text>
  <text x="230" y="270" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569">Preserves bold, tables &amp; font</text>
  <!-- Arrow 2 -->
  <line x1="385" y1="180" x2="410" y2="180" stroke="#059669" stroke-width="3" stroke-linecap="round"/>
  <!-- Phase 3: Auditory Proofreading -->
  <rect x="410" y="45" width="165" height="270" rx="10" fill="#FFFFFF" stroke="#9333EA" stroke-width="1.5"/>
  <rect x="425" y="60" width="70" height="24" rx="4" fill="#FAF5FF"/>
  <text x="460" y="76" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#7E22CE" text-anchor="middle">PHASE 3</text>
  <text x="425" y="110" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#0F172A">AUDIO PROOF</text>
  <text x="425" y="128" font-family="system-ui, sans-serif" font-size="9" fill="#64748B">Text-to-Speech (TTS)</text>
  <circle cx="492" cy="180" r="28" fill="#FAF5FF" stroke="#9333EA" stroke-width="2"/>
  <polygon points="485,170 505,180 485,190" fill="#9333EA"/>
  <text x="492" y="235" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#7E22CE" text-anchor="middle">Listen to Essay</text>
  <text x="425" y="265" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569">Catches missing words</text>
  <text x="425" y="280" font-family="system-ui, sans-serif" font-size="8.5" fill="#475569">Reveals clunky sentences</text>
</svg>"""
    }
]

print(f"data_unit4 part 2 initialized with {len(unit4_part2_topics)} topics.")
