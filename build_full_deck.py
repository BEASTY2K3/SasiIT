#!/usr/bin/env python3
"""
Master Builder for Canva-Style Unit 4 & Unit 5 Presentation
Institution: Sasi College
Course: IT Skills for Employment
Total Slides: 42 (Topics 50 to 91)
Features:
- Non-Computer Science student pedagogy (Real-World Analogies)
- High-Resolution SVG Diagrams for Every Single Topic
- Responsive 16:9 Canva-grade layout
"""

import os
import sys

# We will define the full array of topics in modular dictionaries
topics = []

def add_topic(num, idx, unit, unit_full, cat, title, sub, a_title, a_text, steps, rule, fig_title, takeaway, notes, svg):
    topics.append({
        "num": num,
        "index": f"{idx:02d}",
        "unit": unit,
        "unit_full": unit_full,
        "category": cat,
        "title": title,
        "subtitle": sub,
        "analogy_title": a_title,
        "analogy_text": a_text,
        "steps": steps,
        "rule": rule,
        "fig_title": fig_title,
        "takeaway": takeaway,
        "notes": notes,
        "svg": svg
    })

print("Builder initialized. Ready to load topics.")
