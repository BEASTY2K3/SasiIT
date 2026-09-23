#!/usr/bin/env python3
"""
HTML Presentation Generator: Unit 4 & Unit 5 Canva Visual Edition
Combines all 42 topics into unit4_5_presentation.html
"""

import sys
import os

# Import modular datasets
from data_unit4 import unit4_topics
from data_unit4_part2 import unit4_part2_topics
from data_unit4_part3 import unit4_part3_topics
from data_unit5_part1 import unit5_part1_topics
from data_unit5_part2 import unit5_part2_topics
from data_unit5_part3 import unit5_part3_topics

all_topics = (
    unit4_topics +
    unit4_part2_topics +
    unit4_part3_topics +
    unit5_part1_topics +
    unit5_part2_topics +
    unit5_part3_topics
)

total_count = len(all_topics)
print(f"Total topics loaded: {total_count}")

# Verify 42 topics
if total_count != 42:
    print(f"WARNING: Expected 42 topics, found {total_count}")

html_parts = []

html_parts.append("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Unit 4 &amp; 5: Internet, Cloud &amp; Cyber Defense &mdash; Visual Presentation</title>
  <meta name="description" content="Canva-style high-impact visual master presentation for non-computer students covering Unit 4 (Internet, Cloud & Digital India) and Unit 5 (Cyber Security, Threats & Indian Cyber Law) with dedicated diagrams for every topic.">
  <link rel="stylesheet" href="unit4_5_styles.css">
</head>
<body>

  <!-- Top Realtime Linear Progress Bar -->
  <div class="presentation-progress-bar" id="progressBar"></div>

  <div class="presentation-app">
    <!-- Header Navigation Utility Bar -->
    <header class="pres-header">
      <div class="brand-wrap">
        <div class="college-badge">
          <span class="dot"></span>
          <span>SASI COLLEGE</span>
        </div>
        <h1 class="deck-title">
          <span>IT Skills: Unit 4 &amp; 5</span>
          <span class="deck-tag">Visual Edition</span>
        </h1>
      </div>

      <!-- Unit Switcher Tabs -->
      <nav class="unit-switcher" aria-label="Units">
        <button class="unit-tab-btn active-u4" id="unit4Tab" title="Jump to Unit 4 (Internet &amp; Cloud)">
          <span>Unit 4: Internet &amp; Cloud</span>
        </button>
        <button class="unit-tab-btn" id="unit5Tab" title="Jump to Unit 5 (Cyber Defense &amp; Law)">
          <span>Unit 5: Cyber Defense &amp; Law</span>
        </button>
      </nav>

      <!-- Utility Header Controls -->
      <div class="header-controls">
        <div class="slide-counter-pill" id="slideCounter">01 / 42</div>

        <button class="ctrl-btn" id="prevBtn" title="Previous Slide (Arrow Left)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"></polyline></svg>
        </button>
        <button class="ctrl-btn primary" id="nextBtn" title="Next Slide (Space / Arrow Right)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </button>

        <button class="ctrl-btn" id="overviewBtn" title="Slide Overview Grid (Esc)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
        </button>
        <button class="ctrl-btn" id="notesBtn" title="Presenter Notes Drawer (N)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
        </button>
        <button class="ctrl-btn" id="fullscreenBtn" title="Toggle Fullscreen (F)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"></path></svg>
        </button>
        <button class="ctrl-btn" id="printBtn" title="Print Handout (Ctrl+P)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
        </button>
      </div>
    </header>

    <!-- Presentation Stage Viewport -->
    <main class="stage-wrapper">
      <div class="slide-deck" id="slideDeck">
""")

# Render all 42 slides
for i, t in enumerate(all_topics):
    active_cls = " active" if i == 0 else ""
    slide_num = i + 1
    total_slides = 42

    steps_html = ""
    for s_num, s_title, s_desc in t["steps"]:
        steps_html += f"""          <div class="step-item">
            <span class="step-num">{s_num}</span>
            <div class="step-desc"><strong>{s_title}:</strong> {s_desc}</div>
          </div>
"""

    slide_html = f"""        <!-- SLIDE {slide_num:02d}: {t['title']} -->
        <article class="slide-card{active_cls}" data-slide="{slide_num}" data-unit="{t['unit']}" data-topic="{t['num']}" data-notes="{t['notes']}">
          <div class="slide-header-meta">
            <div class="slide-badges">
              <span class="badge-unit">{t['unit_full']}</span>
              <span class="badge-topic-number">Topic {t['num']}</span>
              <span class="badge-pedagogy">{t['category']}</span>
            </div>
            <div class="slide-position-index">{slide_num:02d} / {total_slides:02d}</div>
          </div>

          <div class="slide-kicker">{t['category']} &bull; Topic {t['num']}</div>
          <h2 class="slide-heading">{t['title']}</h2>
          <p class="slide-subtitle">{t['subtitle']}</p>

          <div class="slide-grid">
            <!-- Left Column: Non-Tech Student Pedagogy -->
            <div class="pedagogy-col">
              <!-- 1. Real-World Analogy -->
              <div class="analogy-card">
                <div class="analogy-header">
                  <span class="analogy-tag">Everyday Analogy</span>
                  <span class="analogy-title">{t['analogy_title']}</span>
                </div>
                <p class="analogy-text">{t['analogy_text']}</p>
              </div>

              <!-- 2. Simplified Mechanism -->
              <div class="mechanism-card">
                <div class="mechanism-title">How It Works in 3 Simple Steps</div>
                <div class="step-list">
{steps_html}                </div>
              </div>

              <!-- 3. Practical Workplace & Everyday Rule -->
              <div class="rule-banner">
                <span class="rule-icon">&#9888;</span>
                <div class="rule-text"><strong>{t['rule'].split(':')[0]}:</strong>{':'.join(t['rule'].split(':')[1:])}</div>
              </div>
            </div>

            <!-- Right Column: Dedicated High-Resolution Visual SVG Diagram -->
            <div class="visual-col">
              <div class="visual-frame">
                <div class="visual-frame-header">
                  <span class="visual-caption-badge">{t['fig_title']}</span>
                  <span class="visual-resolution-tag">Vector SVG</span>
                </div>
                <div class="svg-container">
                  {t['svg']}
                </div>
                <div class="visual-takeaway-bar">
                  <span class="takeaway-dot"></span>
                  <span>{t['takeaway']}</span>
                </div>
              </div>
            </div>
          </div>
        </article>
"""
    html_parts.append(slide_html)

# Append Bottom Bar, Modals, and Script links
html_parts.append("""      </div>
    </main>

    <!-- Bottom Navigation Bar for Touch & Quick Controls -->
    <footer class="pres-bottom-bar">
      <div class="nav-buttons-group">
        <button class="ctrl-btn" id="bottomPrevBtn">&larr; Previous</button>
        <button class="ctrl-btn primary" id="bottomNextBtn">Next &rarr;</button>
      </div>

      <div class="nav-key-hint">
        <span>Navigation Keys:</span>
        <span class="kbd-badge">&rarr; / Space</span> Next
        <span class="kbd-badge">&larr;</span> Prev
        <span class="kbd-badge">F</span> Fullscreen
        <span class="kbd-badge">Esc</span> Overview
        <span class="kbd-badge">N</span> Notes
      </div>

      <div style="font-family: var(--font-mono); font-size: 0.72rem; color: #64748B;">
        <a href="index.html" style="color: #0284C7; text-decoration: none; font-weight: 600;">&larr; Return to Master 275-Slide Deck</a>
      </div>
    </footer>
  </div>

  <!-- Slide Overview Modal (Thumbnails Matrix) -->
  <div class="overview-modal" id="overviewModal" role="dialog" aria-label="Slide Overview Matrix">
    <div class="overview-dialog">
      <div class="overview-header">
        <h2 class="overview-title">Slide Overview Matrix (42 Topics)</h2>
        <div class="overview-filter-bar">
          <input type="text" id="overviewSearch" class="overview-search" placeholder="Search topic name or #..." aria-label="Search slides">
          <button class="ctrl-btn" id="closeOverviewBtn">Close &times;</button>
        </div>
      </div>
      <div class="overview-grid" id="overviewGrid">
        <!-- Dynamic thumbnails injected by app.js -->
      </div>
    </div>
  </div>

  <!-- Presenter Notes Drawer -->
  <aside class="notes-drawer" id="notesDrawer">
    <div class="notes-header">
      <span class="notes-title">Presenter Pedagogical Speech Notes</span>
      <button class="ctrl-btn" id="closeNotesBtn" style="padding: 0.2rem 0.4rem; font-size: 0.75rem;">&times;</button>
    </div>
    <div class="notes-body" id="notesContent">
      Select a slide to view instructor talking points and classroom discussion guidance.
    </div>
  </aside>

  <!-- Interactive Presentation Engine Script -->
  <script src="unit4_5_app.js"></script>
</body>
</html>
""")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "..", "public")
output_path = os.path.join(OUTPUT_DIR, "unit4_5_presentation.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write("".join(html_parts))

file_size = os.path.getsize(output_path)
print(f"Successfully generated {output_path} ({file_size:,} bytes, {total_count} slides)!")

