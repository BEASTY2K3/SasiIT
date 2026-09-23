#!/usr/bin/env python3
"""
Generate Printable Question Paper PDF and Answer Key PDF
Institution: Sasi College
Course: IT Skills for Employment
Total MCQs: 25 (5 from each of the 5 Units)
Tailored for students with foundational computer knowledge.
Options are evenly and naturally distributed across (A), (B), (C), and (D).
"""

import os
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "..", "public")

questions_data = [
    # -------------------------------------------------------------
    # UNIT 1: COMPUTER HARDWARE & FUNDAMENTALS (Q01 - Q05)
    # -------------------------------------------------------------
    {
        "q_num": 1,
        "unit": "Unit 1: Computer Hardware & Fundamentals",
        "topic": "Topic 04: Processor (CPU) Role & Central Architecture",
        "question": "Which internal component is widely known as the 'Brain' of the computer because it interprets and executes program instructions and performs all calculations?",
        "options": {
            "A": "Computer Monitor",
            "B": "Hard Disk Drive (HDD)",
            "C": "Central Processing Unit (CPU)",
            "D": "Computer Keyboard"
        },
        "correct": "C",
        "explanation": "The Central Processing Unit (CPU) is known as the brain of the computer. It fetches instructions from memory, decodes them, and executes them (performing arithmetic, logical, and control operations).",
        "distractors": {
            "A": "A Monitor is an output display device that shows visual output, not an instruction processor.",
            "B": "A Hard Disk Drive is secondary storage used to hold files permanently, not to calculate or execute code.",
            "D": "A Keyboard is an input hardware peripheral used for typing characters."
        }
    },
    {
        "q_num": 2,
        "unit": "Unit 1: Computer Hardware & Fundamentals",
        "topic": "Topic 05: Primary Memory (RAM vs. ROM Volatility)",
        "question": "Which type of computer memory is 'volatile', meaning that all data stored in it is instantly erased when the computer is turned off or restarted?",
        "options": {
            "A": "Read-Only Memory (ROM)",
            "B": "Random Access Memory (RAM)",
            "C": "Hard Disk Drive (HDD)",
            "D": "USB Pen Drive"
        },
        "correct": "B",
        "explanation": "RAM (Random Access Memory) is temporary, volatile working memory. When you open applications, they are loaded into RAM for fast access by the CPU. When electrical power is switched off, everything in RAM is wiped clean.",
        "distractors": {
            "A": "ROM retains essential startup instructions permanently even without electrical power.",
            "C": "Hard Disk Drives provide persistent secondary storage that keeps your files safe when the power is off.",
            "D": "USB Pen Drives use non-volatile flash memory to store portable files permanently."
        }
    },
    {
        "q_num": 3,
        "unit": "Unit 1: Computer Hardware & Fundamentals",
        "topic": "Topic 13 & 15: Input vs. Output Peripherals",
        "question": "Which of the following devices is strictly an **Input Device** used to enter data, text, and commands into the computer?",
        "options": {
            "A": "Computer Keyboard",
            "B": "Display Monitor",
            "C": "Laser Printer",
            "D": "Audio Speaker"
        },
        "correct": "A",
        "explanation": "A keyboard is an input device that allows users to send alphanumeric keystrokes and control signals directly into the computer.",
        "distractors": {
            "B": "A Display Monitor is an output device that visually presents data to the user.",
            "C": "A Laser Printer is an output device that creates physical paper copies of digital documents.",
            "D": "An Audio Speaker is an output device that converts digital audio signals into audible sound waves."
        }
    },
    {
        "q_num": 4,
        "unit": "Unit 1: Computer Hardware & Fundamentals",
        "topic": "Topic 09 & 10: Secondary Storage Media (HDD vs. SSD)",
        "question": "What type of modern storage drive uses electronic flash memory chips with zero spinning parts, providing significantly faster boot and file opening speeds than a mechanical Hard Disk?",
        "options": {
            "A": "Compact Disc (CD-ROM)",
            "B": "Floppy Disk",
            "C": "Magnetic Cassette Tape",
            "D": "Solid State Drive (SSD)"
        },
        "correct": "D",
        "explanation": "Solid State Drives (SSDs) use electronic NAND flash memory chips. Because they have no moving mechanical parts, they access files almost instantaneously compared to spinning hard disk platters.",
        "distractors": {
            "A": "CD-ROM is an optical disc format read by an optical laser drive.",
            "B": "Floppy Disks are obsolete magnetic storage media that held only 1.44 MB.",
            "C": "Magnetic Tape is a sequential tape format primarily used for legacy offline archiving."
        }
    },
    {
        "q_num": 5,
        "unit": "Unit 1: Computer Hardware & Fundamentals",
        "topic": "Topic 18: Computer Network Scope (LAN vs. WAN)",
        "question": "A computer network that interconnects computers and devices within a limited physical geographical area, such as a single computer lab, office building, or college campus, is known as a:",
        "options": {
            "A": "Wide Area Network (WAN)",
            "B": "Local Area Network (LAN)",
            "C": "Metropolitan Area Network (MAN)",
            "D": "Global Satellite Network"
        },
        "correct": "B",
        "explanation": "LAN (Local Area Network) connects computers and printers within a small, confined area like a home, lab, or office building, allowing fast local data transfer and hardware sharing.",
        "distractors": {
            "A": "A WAN (Wide Area Network) spans broad geographic boundaries like states, entire countries, or the globe (e.g. the Internet).",
            "C": "A MAN (Metropolitan Area Network) covers an entire city or large municipal region.",
            "D": "Satellite networks connect stations across orbit for intercontinental telecommunications."
        }
    },

    # -------------------------------------------------------------
    # UNIT 2: OPERATING SYSTEMS & WINDOWS MANAGEMENT (Q06 - Q10)
    # -------------------------------------------------------------
    {
        "q_num": 6,
        "unit": "Unit 2: Operating Systems & Windows Management",
        "topic": "Topic 23: Purpose & Role of the Operating System",
        "question": "What is the primary function of an **Operating System** (such as Windows 10, macOS, or Linux) on a personal computer?",
        "options": {
            "A": "To act as a bridge between computer hardware and the user, managing software programs, files, and memory",
            "B": "To design and edit marketing brochures",
            "C": "To supply physical electrical power from the wall socket",
            "D": "To manufacture microprocessor chips"
        },
        "correct": "A",
        "explanation": "The Operating System (OS) is the fundamental system software that manages computer hardware (processor, memory, disks) and provides an environment where application software can run and users can interact.",
        "distractors": {
            "B": "Marketing brochures are designed using specialized software like Canva, Adobe InDesign, or MS Publisher.",
            "C": "Physical electrical power is delivered by the power supply unit (SMPS) and wall socket.",
            "D": "Microchip manufacturing is a physical industrial semiconductor fabrication process."
        }
    },
    {
        "q_num": 7,
        "unit": "Unit 2: Operating Systems & Windows Management",
        "topic": "Topic 32: Universal Windows Keyboard Shortcuts",
        "question": "Which standard keyboard shortcut is used in Windows and Microsoft Office to **Copy** selected text, images, or files to the clipboard?",
        "options": {
            "A": "Ctrl + X",
            "B": "Ctrl + V",
            "C": "Ctrl + C",
            "D": "Ctrl + Z"
        },
        "correct": "C",
        "explanation": "Ctrl + C copies the selected item onto the system clipboard while leaving the original item in place.",
        "distractors": {
            "A": "Ctrl + X cuts the selected item (removes it from its current position to the clipboard).",
            "B": "Ctrl + V pastes the copied or cut item from the clipboard to the cursor position.",
            "D": "Ctrl + Z undoes the most recent user action."
        }
    },
    {
        "q_num": 8,
        "unit": "Unit 2: Operating Systems & Windows Management",
        "topic": "Topic 26: Windows File Explorer & File Recovery",
        "question": "When you delete a document or folder from your hard drive by pressing the `Delete` key in Windows, where does it temporarily go so you can easily restore it if needed?",
        "options": {
            "A": "Device Manager",
            "B": "Control Panel",
            "C": "Windows Update",
            "D": "Recycle Bin"
        },
        "correct": "D",
        "explanation": "The Windows Recycle Bin serves as a safety holding area for deleted files on local drives, allowing users to restore mistakenly deleted items back to their original folder.",
        "distractors": {
            "A": "Device Manager manages hardware drivers and peripheral connections.",
            "B": "Control Panel configures operating system and hardware settings.",
            "C": "Windows Update installs security patches and operating system feature updates."
        }
    },
    {
        "q_num": 9,
        "unit": "Unit 2: Operating Systems & Windows Management",
        "topic": "Topic 29: System Maintenance & Disk Hygiene",
        "question": "Which built-in Windows maintenance tool safely scans your hard drive to find and delete temporary files, system cache, and empty the Recycle Bin to free up disk storage?",
        "options": {
            "A": "Disk Cleanup (or Storage Sense)",
            "B": "Paint 3D",
            "C": "Windows Media Player",
            "D": "Notepad"
        },
        "correct": "A",
        "explanation": "Disk Cleanup (and Windows 10 Storage Sense) scans storage drives for temporary Internet files, setup logs, thumbnail caches, and recycle bin items, safely reclaiming valuable gigabytes of space.",
        "distractors": {
            "B": "Paint 3D is a simple raster and 3D modeling creative tool.",
            "C": "Windows Media Player is an application used for playing music tracks and video files.",
            "D": "Notepad is a lightweight plain text editor."
        }
    },
    {
        "q_num": 10,
        "unit": "Unit 2: Operating Systems & Windows Management",
        "topic": "Topic 25: Workplace Security & Screen Hygiene",
        "question": "When stepping away from your workstation or computer desk in an office or college lab, which keyboard shortcut instantly **Locks** your Windows screen to prevent unauthorized access?",
        "options": {
            "A": "Alt + F4",
            "B": "Windows Key + L",
            "C": "Ctrl + Shift + Esc",
            "D": "Windows Key + P"
        },
        "correct": "B",
        "explanation": "Pressing Windows Key + L immediately locks your Windows session. Your open apps and documents remain intact in the background, but the computer cannot be accessed without entering your password/PIN.",
        "distractors": {
            "A": "Alt + F4 closes the currently active program window.",
            "C": "Ctrl + Shift + Esc directly opens the Windows Task Manager.",
            "D": "Windows Key + P opens the multi-monitor display projection menu."
        }
    },

    # -------------------------------------------------------------
    # UNIT 3: OFFICE PRODUCTIVITY TRIAD (WORD, EXCEL, PPT) (Q11 - Q15)
    # -------------------------------------------------------------
    {
        "q_num": 11,
        "unit": "Unit 3: Office Productivity Triad",
        "topic": "Topic 31 & 38: Word Processing & Resume Creation",
        "question": "Which application software in the Microsoft Office suite is specifically designed for writing, editing, and formatting professional resumes, formal letters, and reports?",
        "options": {
            "A": "Microsoft Excel",
            "B": "Microsoft Access",
            "C": "Microsoft Word",
            "D": "Microsoft PowerPoint"
        },
        "correct": "C",
        "explanation": "Microsoft Word is the dedicated word processing application in Microsoft Office, engineered for creating typographic documents, reports, business letters, and formatted CVs/resumes.",
        "distractors": {
            "A": "Microsoft Excel is a spreadsheet application designed for numerical calculations and tables.",
            "B": "Microsoft Access is a relational database management tool.",
            "D": "Microsoft PowerPoint is presentation software designed for visual slide decks."
        }
    },
    {
        "q_num": 12,
        "unit": "Unit 3: Office Productivity Triad",
        "topic": "Topic 43: MS Excel Formula Syntax Fundamentals",
        "question": "In Microsoft Excel, what symbol MUST you type as the very first character in a cell to tell Excel that you are entering a mathematical formula or calculation?",
        "options": {
            "A": "Plus sign (`+`)",
            "B": "Hashtag (`#`)",
            "C": "Dollar sign (`$`)",
            "D": "Equal sign (`=`)"
        },
        "correct": "D",
        "explanation": "In Microsoft Excel, every formula or function must begin with an equal sign (`=`). Without it, Excel treats the entered text as a plain label or string rather than a calculation.",
        "distractors": {
            "A": "A plus sign is an addition operator inside formulas, not the standard initiating formula trigger.",
            "B": "Hashtags are used in error indicators (like `###` when a column is too narrow).",
            "C": "Dollar signs are used inside formulas to create absolute cell references (e.g. `$A$1`)."
        }
    },
    {
        "q_num": 13,
        "unit": "Unit 3: Office Productivity Triad",
        "topic": "Topic 44: Core Spreadsheet Calculation Functions",
        "question": "Which Excel function is used to calculate the combined total of numbers across a specified range of cells (for example, adding all numbers from cell A1 to A10)?",
        "options": {
            "A": "`=ADD(A1:A10)`",
            "B": "`=SUM(A1:A10)`",
            "C": "`=TOTAL(A1:A10)`",
            "D": "`=COUNT(A1:A10)`"
        },
        "correct": "B",
        "explanation": "The `=SUM()` function is the standard Excel function that adds all numeric values across the given cell range.",
        "distractors": {
            "A": "`=ADD()` is not a valid built-in Microsoft Excel formula.",
            "C": "`=TOTAL()` is not a recognized function in Excel.",
            "D": "`=COUNT()` counts how many cells contain numbers in a range, but does not calculate their total sum."
        }
    },
    {
        "q_num": 14,
        "unit": "Unit 3: Office Productivity Triad",
        "topic": "Topic 48: MS PowerPoint Slide Architecture",
        "question": "In Microsoft PowerPoint, what is an individual page or visual screen within a presentation deck called?",
        "options": {
            "A": "Slide",
            "B": "Worksheet",
            "C": "Document",
            "D": "Artboard"
        },
        "correct": "A",
        "explanation": "Each individual screen or presentation page in PowerPoint is called a 'Slide'. A sequence of slides together makes up a presentation slide deck.",
        "distractors": {
            "B": "A Worksheet is a grid of rows and columns in Microsoft Excel.",
            "C": "A Document is a file created in Microsoft Word.",
            "D": "An Artboard is a vector canvas term used in graphic tools like Adobe Illustrator."
        }
    },
    {
        "q_num": 15,
        "unit": "Unit 3: Office Productivity Triad",
        "topic": "Topic 48: PowerPoint Delivery & Keyboard Controls",
        "question": "Which functional shortcut key is used in Microsoft PowerPoint to immediately launch the Slide Show in full-screen presentation mode starting from the first slide?",
        "options": {
            "A": "F1",
            "B": "F7",
            "C": "F5",
            "D": "F12"
        },
        "correct": "C",
        "explanation": "Pressing `F5` in PowerPoint launches the slideshow in full screen from slide 1. (Pressing `Shift + F5` starts the show from the currently selected slide).",
        "distractors": {
            "A": "F1 opens Microsoft Office Help documentation.",
            "B": "F7 triggers the Spelling and Grammar proofing tool.",
            "D": "F12 opens the 'Save As' dialog window."
        }
    },

    # -------------------------------------------------------------
    # UNIT 4: INTERNET, CLOUD COLLABORATION & DIGITAL PAYMENTS (Q16 - Q20)
    # -------------------------------------------------------------
    {
        "q_num": 16,
        "unit": "Unit 4: Internet, Cloud & Digital Services",
        "topic": "Topic 51: Web Architecture & URL Anatomy",
        "question": "In a complete website web address such as `https://www.google.com`, what does the common prefix acronym **WWW** stand for?",
        "options": {
            "A": "Wide World Web",
            "B": "Western Wireless Web",
            "C": "World Web Wireless",
            "D": "World Wide Web"
        },
        "correct": "D",
        "explanation": "WWW stands for World Wide Web, the global system of interlinked hypertext documents and multimedia accessed via the Internet.",
        "distractors": {
            "A": "'Wide World Web' is a common incorrect phrasing.",
            "B": "'Western Wireless Web' is completely inaccurate.",
            "C": "'World Web Wireless' is an incorrect permutation."
        }
    },
    {
        "q_num": 17,
        "unit": "Unit 4: Internet, Cloud & Digital Services",
        "topic": "Topic 52: Web Browsers vs. Search Engines",
        "question": "Which of the following is a **Web Browser** application used to open, view, and navigate pages and websites across the internet?",
        "options": {
            "A": "Google Chrome",
            "B": "Microsoft Excel",
            "C": "Adobe Photoshop",
            "D": "Windows Media Player"
        },
        "correct": "A",
        "explanation": "Google Chrome is a modern web browser that renders HTML, CSS, and web pages from servers so you can view websites.",
        "distractors": {
            "B": "Microsoft Excel is spreadsheet software for data calculations.",
            "C": "Adobe Photoshop is graphic design and image manipulation software.",
            "D": "Windows Media Player is an application for playing multimedia video and music files."
        }
    },
    {
        "q_num": 18,
        "unit": "Unit 4: Internet, Cloud & Digital Services",
        "topic": "Topic 57: Corporate Email Addressing & Privacy",
        "question": "When sending an official email to multiple recipients, which address field should you use to hide recipient email addresses from each other to preserve their privacy?",
        "options": {
            "A": "To",
            "B": "CC (Carbon Copy)",
            "C": "BCC (Blind Carbon Copy)",
            "D": "Subject Line"
        },
        "correct": "C",
        "explanation": "BCC stands for Blind Carbon Copy. When addresses are placed in BCC, each recipient receives the email without being able to see any of the other recipients' email addresses, protecting privacy and preventing accidental 'Reply-All' spam.",
        "distractors": {
            "A": "The 'To' field displays all recipient email addresses publicly to everyone who receives the email.",
            "B": "The 'CC' field also keeps all email addresses fully visible to all recipients.",
            "D": "The 'Subject Line' is where the title or topic of the email is typed."
        }
    },
    {
        "q_num": 19,
        "unit": "Unit 4: Internet, Cloud & Digital Services",
        "topic": "Topic 60: Cloud Storage Services Ecosystem",
        "question": "Which widely used cloud storage service provided by Google gives users 15 GB of free online storage to save files, backup photos, and share documents from anywhere?",
        "options": {
            "A": "Google Maps",
            "B": "Google Drive",
            "C": "Google Play Store",
            "D": "Google Translate"
        },
        "correct": "B",
        "explanation": "Google Drive is Google's cloud storage service that lets users store files safely in cloud data centers, share links with specific permissions, and sync data across smartphones and computers.",
        "distractors": {
            "A": "Google Maps is a GPS navigation and route mapping service.",
            "C": "Google Play Store is an Android marketplace for downloading applications and games.",
            "D": "Google Translate is a language translation utility."
        }
    },
    {
        "q_num": 20,
        "unit": "Unit 4: Internet, Cloud & Digital Services",
        "topic": "Topic 70: Digital Payments & UPI Security Principles",
        "question": "When using UPI mobile payment apps (such as Google Pay, PhonePe, or Paytm), which is the most critical security rule regarding your secret **UPI PIN**?",
        "options": {
            "A": "You must enter your UPI PIN whenever someone wants to send or transfer money into your bank account.",
            "B": "You should share your secret UPI PIN with customer support executives over the phone.",
            "C": "You must enter your UPI PIN to claim lottery or refund prizes from unknown callers.",
            "D": "You NEVER enter your UPI PIN to receive money; entering your UPI PIN is only required when you are transferring (paying) money OUT of your account."
        },
        "correct": "D",
        "explanation": "The golden rule of UPI is that receiving money NEVER requires entering your PIN. Entering your UPI PIN is strictly and exclusively used to authorize deductions (debiting money) from your bank account.",
        "distractors": {
            "A": "Believing you must enter a PIN to receive money is the most common scam trick used by cyber fraudsters to steal money.",
            "B": "Legitimate customer support representatives will never ask for your private PIN or OTP.",
            "C": "Lottery/refund claims asking for a PIN are fraudulent phishing attempts."
        }
    },

    # -------------------------------------------------------------
    # UNIT 5: CYBER SECURITY, THREATS & ONLINE SAFETY (Q21 - Q25)
    # -------------------------------------------------------------
    {
        "q_num": 21,
        "unit": "Unit 5: Cyber Security, Threats & Online Safety",
        "topic": "Topic 71 & 72: Malware Threat Definition",
        "question": "What broad term is used to describe any harmful computer software (such as viruses, worms, and spyware) intentionally designed to damage, spy on, or steal data from a computer?",
        "options": {
            "A": "Malware (Malicious Software)",
            "B": "Hardware",
            "C": "Freeware",
            "D": "Firmware"
        },
        "correct": "A",
        "explanation": "Malware is an umbrella term short for 'Malicious Software'. It encompasses computer viruses, worms, trojans, ransomware, spyware, and adware created to harm systems or steal information.",
        "distractors": {
            "B": "Hardware refers to the tangible, physical components of a computer (cables, chips, monitor).",
            "C": "Freeware is legitimate software distributed free of monetary charge for users.",
            "D": "Firmware is permanent low-level code programmed into read-only memory chips."
        }
    },
    {
        "q_num": 22,
        "unit": "Unit 5: Cyber Security, Threats & Online Safety",
        "topic": "Topic 81: Antivirus Defense Mechanisms",
        "question": "What is the primary function of installing an **Antivirus** software application (such as Windows Defender or Quick Heal) on your computer system?",
        "options": {
            "A": "To increase the physical speed of your broadband internet router",
            "B": "To automatically repair damaged hardware cables and monitor screens",
            "C": "To detect, prevent, quarantine, and remove malicious viruses and security threats from your computer",
            "D": "To increase the physical storage size of your hard drive"
        },
        "correct": "C",
        "explanation": "Antivirus software constantly scans system files, incoming downloads, and removable USB drives to detect malware signatures and suspicious behavior, isolating or deleting threats before they cause damage.",
        "distractors": {
            "A": "Antivirus does not alter physical internet bandwidth provided by your telecom service provider.",
            "B": "Antivirus is software; it cannot physically repair broken electrical cables or cracked monitors.",
            "D": "Antivirus does not increase the physical capacity of storage hardware."
        }
    },
    {
        "q_num": 23,
        "unit": "Unit 5: Cyber Security, Threats & Online Safety",
        "topic": "Topic 83: Social Engineering & Phishing Attacks",
        "question": "What type of online cyber scam involves fraudulent emails or fake website messages that pretend to be from trusted banks or organizations to trick you into giving away your passwords or card numbers?",
        "options": {
            "A": "Defragmentation",
            "B": "Phishing",
            "C": "Screen Casting",
            "D": "Data Compression"
        },
        "correct": "B",
        "explanation": "Phishing is a form of social engineering where attackers impersonate trustworthy entities (like banks, payment apps, or college portals) through deceptive emails or links to steal credentials, passwords, or credit card details.",
        "distractors": {
            "A": "Defragmentation is a system maintenance routine that arranges file clusters on a hard drive.",
            "C": "Screen Casting is a feature used to wirelessly stream your computer screen to a TV or projector.",
            "D": "Data Compression reduces file size (e.g. creating a ZIP archive)."
        }
    },
    {
        "q_num": 24,
        "unit": "Unit 5: Cyber Security, Threats & Online Safety",
        "topic": "Topic 87: Password Hygiene & Account Protection",
        "question": "Which of the following practices creates the strongest, most secure **Password** to protect your personal and email accounts from hackers?",
        "options": {
            "A": "Using your own first name followed by `123` (e.g., `Rahul123`)",
            "B": "Using your date of birth or mobile telephone number",
            "C": "Using the word `password` so you do not forget it",
            "D": "A combination of at least 8 to 12 characters including uppercase and lowercase letters, numbers, and special symbols (e.g., `@`, `#`, `!`)"
        },
        "correct": "D",
        "explanation": "A strong password combines length (at least 8–12 characters) with complexity (uppercase letters, lowercase letters, digits, and special symbols). This makes it computationally infeasible for hackers to guess via brute-force or dictionary attacks.",
        "distractors": {
            "A": "Names combined with `123` are among the top 10 most easily cracked passwords globally.",
            "B": "Birthdays and phone numbers are easily discovered through social media profiling.",
            "C": "'password' is the single most commonly cracked password in cyber security history."
        }
    },
    {
        "q_num": 25,
        "unit": "Unit 5: Cyber Security, Threats & Online Safety",
        "topic": "Topic 90: National Incident Reporting & Help Desk",
        "question": "Which official National Cyber Crime toll-free helpline number has been launched by the Government of India for citizens to immediately report financial cyber frauds and digital online crimes?",
        "options": {
            "A": "100",
            "B": "108",
            "C": "1930",
            "D": "1098"
        },
        "correct": "C",
        "explanation": "1930 is the national Citizen Financial Cyber Fraud Reporting helpline in India (formerly 155260), integrated with `cybercrime.gov.in`. Reporting within the 'Golden Hour' allows authorities to freeze stolen funds in banking channels before fraudsters withdraw them.",
        "distractors": {
            "A": "100 is the general police emergency number.",
            "B": "108 is the medical ambulance emergency response service.",
            "D": "1098 is the Childline emergency helpline for children in distress."
        }
    }
]

# -------------------------------------------------------------
# GENERATE QUESTION PAPER HTML
# -------------------------------------------------------------
qp_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Question Paper - IT Skills for Employment - Sasi College</title>
  <style>
    @page {
      size: A4 portrait;
      margin: 12mm 14mm 12mm 14mm;
      @bottom-right {
        content: "Page " counter(page) " of " counter(pages);
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 8pt;
        color: #64748b;
      }
    }
    
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    
    body {
      font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
      color: #0f172a;
      background: #ffffff;
      font-size: 9.2pt;
      line-height: 1.38;
      -webkit-font-smoothing: antialiased;
    }
    
    /* Institutional Header */
    .exam-header {
      border: 2px solid #0f172a;
      border-radius: 4px;
      padding: 10px 14px;
      margin-bottom: 12px;
      background: #ffffff;
    }
    
    .college-name {
      text-align: center;
      font-size: 15pt;
      font-weight: 800;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: #0f172a;
    }
    
    .exam-title-bar {
      border-top: 1px solid #cbd5e1;
      border-bottom: 1px solid #cbd5e1;
      margin: 6px 0;
      padding: 5px 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 9.5pt;
      font-weight: 700;
      color: #0369a1;
    }
    
    .exam-meta-grid {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr 1.5fr;
      gap: 6px;
      font-size: 8.5pt;
      margin-top: 4px;
    }
    
    .meta-item strong {
      color: #0f172a;
    }
    
    /* Candidate Fill-in Details */
    .candidate-box {
      border: 1px dashed #64748b;
      border-radius: 4px;
      padding: 8px 12px;
      margin-bottom: 12px;
      display: grid;
      grid-template-columns: 1.2fr 1fr 1fr;
      gap: 12px;
      font-size: 8.5pt;
      background: #f8fafc;
    }
    
    .candidate-line {
      display: flex;
      align-items: baseline;
      gap: 6px;
    }
    
    .candidate-line strong {
      white-space: nowrap;
      color: #334155;
    }
    
    .fill-dots {
      border-bottom: 1px dotted #94a3b8;
      flex-grow: 1;
      height: 14px;
    }
    
    /* General Instructions */
    .instructions-bar {
      background: #f1f5f9;
      border-left: 3px solid #0284c7;
      padding: 6px 10px;
      margin-bottom: 12px;
      font-size: 8pt;
      color: #334155;
    }
    
    .instructions-bar ol {
      margin-left: 18px;
      margin-top: 2px;
    }
    
    /* Section Divider */
    .section-banner {
      background: #0f172a;
      color: #ffffff;
      padding: 4px 10px;
      font-size: 8.5pt;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      margin: 10px 0 8px 0;
      border-radius: 3px;
      display: flex;
      justify-content: space-between;
    }
    
    .section-banner span.sec-marks {
      font-weight: 400;
      font-size: 8pt;
      color: #94a3b8;
    }
    
    /* Question Card */
    .question-card {
      margin-bottom: 8px;
      page-break-inside: avoid;
      break-inside: avoid;
      padding-bottom: 4px;
      border-bottom: 1px dotted #e2e8f0;
    }
    
    .question-text {
      font-weight: 600;
      color: #0f172a;
      display: flex;
      align-items: flex-start;
      gap: 6px;
      margin-bottom: 4px;
    }
    
    .q-num {
      font-weight: 800;
      color: #0284c7;
      min-width: 22px;
    }
    
    /* Options Grid (2x2) */
    .options-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 3px 12px;
      padding-left: 28px;
    }
    
    .option-item {
      display: flex;
      align-items: flex-start;
      gap: 5px;
      font-size: 8.8pt;
      color: #334155;
    }
    
    .opt-letter {
      font-weight: 700;
      color: #0f172a;
      min-width: 18px;
    }
    
    /* OMR Response Grid at End */
    .omr-sheet {
      page-break-inside: avoid;
      break-inside: avoid;
      border: 1px solid #0f172a;
      border-radius: 4px;
      padding: 8px 12px;
      margin-top: 14px;
      background: #ffffff;
    }
    
    .omr-title {
      font-size: 9pt;
      font-weight: 800;
      text-transform: uppercase;
      text-align: center;
      margin-bottom: 6px;
      color: #0f172a;
    }
    
    .omr-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 6px 14px;
    }
    
    .omr-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 8pt;
      padding: 2px 0;
      border-bottom: 1px dashed #f1f5f9;
    }
    
    .omr-q-num {
      font-weight: 700;
      width: 22px;
      color: #475569;
    }
    
    .bubbles {
      display: flex;
      gap: 4px;
    }
    
    .bubble {
      width: 13px;
      height: 13px;
      border: 1px solid #334155;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 6.5pt;
      font-weight: 600;
      color: #475569;
    }
    
    .sign-row {
      margin-top: 10px;
      display: flex;
      justify-content: space-between;
      font-size: 8pt;
      color: #475569;
      border-top: 1px solid #cbd5e1;
      padding-top: 8px;
    }
  </style>
</head>
<body>

  <!-- Institutional Header -->
  <header class="exam-header">
    <div class="college-name">SASI COLLEGE</div>
    
    <div class="exam-title-bar">
      <span>IT SKILLS FOR EMPLOYMENT</span>
      <span>MULTIPLE CHOICE QUESTION ASSESSMENT</span>
    </div>
    
    <div class="exam-meta-grid">
      <div class="meta-item"><strong>Max Marks:</strong> 25 Marks</div>
      <div class="meta-item"><strong>Duration:</strong> 45 Minutes</div>
      <div class="meta-item"><strong>Total Questions:</strong> 25 MCQs</div>
      <div class="meta-item"><strong>Marking:</strong> 1 Mark Each (No Negative Marks)</div>
    </div>
  </header>

  <!-- Candidate Details Filling Block -->
  <div class="candidate-box">
    <div class="candidate-line">
      <strong>Student Name:</strong>
      <span class="fill-dots"></span>
    </div>
    <div class="candidate-line">
      <strong>Register / Roll No:</strong>
      <span class="fill-dots"></span>
    </div>
    <div class="candidate-line">
      <strong>Date / Dept:</strong>
      <span class="fill-dots"></span>
    </div>
  </div>

  <!-- Instructions to Students -->
  <div class="instructions-bar">
    <strong>Instructions to Candidates:</strong>
    <ol>
      <li>All 25 questions are compulsory. Each question carries exactly 1 mark. There is no negative marking.</li>
      <li>Each question contains four options: (A), (B), (C), and (D). Shade or mark the correct option clearly.</li>
      <li>Record your final answers on the OMR Response Sheet provided on the final page of this booklet.</li>
    </ol>
  </div>
"""

# Render Questions grouped by Units
current_unit = None
unit_letters = {"Unit 1": "A", "Unit 2": "B", "Unit 3": "C", "Unit 4": "D", "Unit 5": "E"}

for q in questions_data:
    unit_prefix = q["unit"].split(":")[0]
    if unit_prefix != current_unit:
        current_unit = unit_prefix
        sec_letter = unit_letters.get(current_unit, "A")
        qp_html += f"""
  <div class="section-banner">
    <span>SECTION {sec_letter} &bull; {q['unit'].upper()}</span>
    <span class="sec-marks">[5 Questions &bull; 5 Marks]</span>
  </div>
"""

    qp_html += f"""  <div class="question-card">
    <div class="question-text">
      <span class="q-num">{q['q_num']:02d}.</span>
      <span>{q['question']}</span>
    </div>
    <div class="options-grid">
      <div class="option-item"><span class="opt-letter">(A)</span> <span>{q['options']['A']}</span></div>
      <div class="option-item"><span class="opt-letter">(B)</span> <span>{q['options']['B']}</span></div>
      <div class="option-item"><span class="opt-letter">(C)</span> <span>{q['options']['C']}</span></div>
      <div class="option-item"><span class="opt-letter">(D)</span> <span>{q['options']['D']}</span></div>
    </div>
  </div>
"""

# Append OMR Response Sheet at the end
qp_html += """
  <!-- Standardized OMR Response Sheet -->
  <div class="omr-sheet">
    <div class="omr-title">Candidate OMR Response Sheet (Questions 01 &ndash; 25)</div>
    <div class="omr-grid">
"""

for col in range(5):
    qp_html += "      <div class=\"omr-col\">\n"
    for row in range(5):
        q_idx = col * 5 + row + 1
        qp_html += f"""        <div class="omr-row">
          <span class="omr-q-num">{q_idx:02d}</span>
          <div class="bubbles">
            <span class="bubble">A</span>
            <span class="bubble">B</span>
            <span class="bubble">C</span>
            <span class="bubble">D</span>
          </div>
        </div>
"""
    qp_html += "      </div>\n"

qp_html += """    </div>
    <div class="sign-row">
      <span>Candidate's Signature: _______________________</span>
      <span>Invigilator's Verification Signature: _______________________</span>
    </div>
  </div>

</body>
</html>
"""

qp_path = os.path.join(OUTPUT_DIR, "question_paper.html")
with open(qp_path, "w", encoding="utf-8") as f:
    f.write(qp_html)

print(f"Saved {qp_path}")



# -------------------------------------------------------------
# GENERATE DETAILED ANSWER KEY HTML
# -------------------------------------------------------------
ak_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Official Answer Key & Solutions Guide - Sasi College</title>
  <style>
    @page {
      size: A4 portrait;
      margin: 12mm 14mm 12mm 14mm;
      @bottom-right {
        content: "Page " counter(page) " of " counter(pages);
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 8pt;
        color: #64748b;
      }
    }
    
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    
    body {
      font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
      color: #0f172a;
      background: #ffffff;
      font-size: 8.8pt;
      line-height: 1.38;
      -webkit-font-smoothing: antialiased;
    }
    
    .ans-header {
      border: 2px solid #059669;
      border-radius: 4px;
      padding: 10px 14px;
      margin-bottom: 12px;
      background: #f0fdf4;
    }
    
    .college-name {
      text-align: center;
      font-size: 15pt;
      font-weight: 800;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: #065f46;
    }
    
    .exam-title-bar {
      border-top: 1px solid #a7f3d0;
      border-bottom: 1px solid #a7f3d0;
      margin: 5px 0;
      padding: 4px 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 9pt;
      font-weight: 700;
      color: #047857;
    }
    
    /* Key Matrix Table */
    .key-table-wrap {
      margin-bottom: 12px;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      overflow: hidden;
    }
    
    .key-table-title {
      background: #065f46;
      color: #ffffff;
      font-size: 8.5pt;
      font-weight: 700;
      text-align: center;
      padding: 4px 0;
      text-transform: uppercase;
    }
    
    table.master-key-table {
      width: 100%;
      border-collapse: collapse;
      text-align: center;
      font-size: 8pt;
    }
    
    table.master-key-table th {
      background: #e2e8f0;
      color: #1e293b;
      padding: 4px 1px;
      border: 1px solid #cbd5e1;
      font-weight: 700;
    }
    
    table.master-key-table td {
      padding: 5px 1px;
      border: 1px solid #cbd5e1;
      font-weight: 800;
    }
    
    table.master-key-table td.correct-val {
      background: #dcfce7;
      color: #166534;
      font-size: 9.5pt;
    }
    
    /* Solution Cards */
    .solution-card {
      border: 1px solid #e2e8f0;
      border-radius: 4px;
      padding: 7px 10px;
      margin-bottom: 7px;
      page-break-inside: avoid;
      break-inside: avoid;
      background: #ffffff;
    }
    
    .sol-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 3px;
    }
    
    .sol-q-title {
      font-weight: 800;
      font-size: 8.8pt;
      color: #0f172a;
    }
    
    .sol-correct-badge {
      background: #10b981;
      color: #ffffff;
      padding: 2px 7px;
      border-radius: 3px;
      font-weight: 700;
      font-size: 8pt;
    }
    
    .sol-topic-ref {
      font-size: 7.5pt;
      font-weight: 600;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 0.03em;
      margin-bottom: 2px;
    }
    
    .sol-question-snippet {
      font-style: italic;
      color: #334155;
      font-size: 8.2pt;
      margin-bottom: 4px;
    }
    
    .sol-rationale {
      background: #f8fafc;
      border-left: 3px solid #10b981;
      padding: 4px 8px;
      font-size: 8pt;
      color: #1e293b;
      margin-bottom: 4px;
    }
    
    .sol-distractor-box {
      border-top: 1px dashed #e2e8f0;
      padding-top: 3px;
      font-size: 7.8pt;
      color: #475569;
      margin-top: 4px;
    }
    
    .sol-distractor-box strong {
      color: #b91c1c;
    }

    .unit-div-banner {
      background: #f1f5f9;
      border-left: 3px solid #059669;
      padding: 4px 8px;
      font-size: 8.5pt;
      font-weight: 700;
      text-transform: uppercase;
      margin: 10px 0 6px 0;
      color: #0f172a;
    }
  </style>
</head>
<body>

  <!-- Header -->
  <header class="ans-header">
    <div class="college-name">SASI COLLEGE</div>
    
    <div class="exam-title-bar">
      <span>OFFICIAL ANSWER KEY &amp; PEDAGOGICAL SOLUTIONS MATRIX</span>
      <span>IT SKILLS FOR EMPLOYMENT</span>
    </div>
    
    <div style="font-size: 8pt; color: #475569; margin-top: 3px;">
      <strong>Assessment:</strong> 25 MCQ Examination &bull; <strong>Total Marks:</strong> 25 &bull; <strong>Syllabus Coverage:</strong> Units 1 to 5 (5 Questions/Unit)
    </div>
  </header>

  <!-- Master Key Table 1-25 -->
  <div class="key-table-wrap">
    <div class="key-table-title">Quick Reference Key Matrix (Questions 01 &ndash; 25)</div>
    <table class="master-key-table">
      <thead>
        <tr>
          <th>Q01</th><th>Q02</th><th>Q03</th><th>Q04</th><th>Q05</th>
          <th>Q06</th><th>Q07</th><th>Q08</th><th>Q09</th><th>Q10</th>
          <th>Q11</th><th>Q12</th><th>Q13</th><th>Q14</th><th>Q15</th>
          <th>Q16</th><th>Q17</th><th>Q18</th><th>Q19</th><th>Q20</th>
          <th>Q21</th><th>Q22</th><th>Q23</th><th>Q24</th><th>Q25</th>
        </tr>
      </thead>
      <tbody>
        <tr>
"""

for q in questions_data:
    ak_html += f"          <td class=\"correct-val\">{q['correct']}</td>\n"

ak_html += """        </tr>
      </tbody>
    </table>
  </div>
"""

# Render Detailed Solution Cards
current_unit = None
for q in questions_data:
    unit_prefix = q["unit"].split(":")[0]
    if unit_prefix != current_unit:
        current_unit = unit_prefix
        ak_html += f"""  <div class="unit-div-banner">{q['unit'].upper()} &bull; SOLUTIONS (Q{q['q_num']:02d} &ndash; Q{q['q_num']+4:02d})</div>\n"""

    correct_key = q["correct"]
    correct_text = q["options"][correct_key]

    distractors_html = ""
    for d_key, d_text in q["distractors"].items():
        distractors_html += f"<div><strong>Option ({d_key}) is Incorrect:</strong> {d_text}</div>\n"

    ak_html += f"""  <div class="solution-card">
    <div class="sol-header">
      <span class="sol-q-title">Question {q['q_num']:02d}</span>
      <span class="sol-correct-badge">CORRECT ANSWER: ({correct_key}) {correct_text}</span>
    </div>
    <div class="sol-topic-ref">{q['topic']}</div>
    <div class="sol-question-snippet">"{q['question']}"</div>
    
    <div class="sol-rationale">
      <strong>Why ({correct_key}) is Correct:</strong> {q['explanation']}
    </div>
    
    <div class="sol-distractor-box">
      {distractors_html}
    </div>
  </div>
"""

ak_html += """
</body>
</html>
"""

ak_path = os.path.join(OUTPUT_DIR, "answer_key.html")
with open(ak_path, "w", encoding="utf-8") as f:
    f.write(ak_html)

print(f"Saved {ak_path}")

