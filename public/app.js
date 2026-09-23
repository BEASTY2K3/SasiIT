/**
 * IT Skills for Employment - Master Presentation Engine
 * Architecture: Senior Design System & Presentation Controls
 */

document.addEventListener('DOMContentLoaded', () => {
  // DOM References
  const slides = Array.from(document.querySelectorAll('.slide'));
  const progressBar = document.getElementById('progressBar');
  const slideCounter = document.getElementById('slideCounter');
  const sessionTimePill = document.getElementById('sessionTimePill');
  const dayTabs = document.querySelectorAll('.day-tab-btn');
  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  const overviewBtn = document.getElementById('overviewBtn');
  const notesBtn = document.getElementById('notesBtn');
  const fullscreenBtn = document.getElementById('fullscreenBtn');
  const printBtn = document.getElementById('printBtn');
  const overviewModal = document.getElementById('overviewModal');
  const closeOverviewBtn = document.getElementById('closeOverviewBtn');
  const overviewGrid = document.getElementById('overviewGrid');
  const notesDrawer = document.getElementById('notesDrawer');
  const closeNotesBtn = document.getElementById('closeNotesBtn');
  const notesContent = document.getElementById('notesContent');

  let currentSlideIndex = 0;
  const totalSlides = slides.length;

  // Day boundaries mapping
  const day1FirstIndex = slides.findIndex(slide => slide.dataset.day === '1');
  const day2FirstIndex = slides.findIndex(slide => slide.dataset.day === '2');

  /**
   * Initialize Presentation Engine
   */
  function init() {
    buildOverviewGrid();
    goToSlide(0, false);
    setupEventListeners();
  }

  /**
   * Jump to specific slide index
   */
  function goToSlide(index, smooth = true) {
    if (index < 0) index = 0;
    if (index >= totalSlides) index = totalSlides - 1;

    slides.forEach((slide, i) => {
      if (i === index) {
        slide.classList.add('active');
        slide.scrollTop = 0;
      } else {
        slide.classList.remove('active');
      }
    });

    currentSlideIndex = index;
    updateUIState();
  }

  function nextSlide() {
    if (currentSlideIndex < totalSlides - 1) {
      goToSlide(currentSlideIndex + 1);
    }
  }

  function prevSlide() {
    if (currentSlideIndex > 0) {
      goToSlide(currentSlideIndex - 1);
    }
  }

  /**
   * Update Progress, Counter, Notes & Schedule indicators
   */
  function updateUIState() {
    const currentSlide = slides[currentSlideIndex];
    if (!currentSlide) return;

    // 1. Progress Bar
    const percent = ((currentSlideIndex + 1) / totalSlides) * 100;
    if (progressBar) progressBar.style.width = `${percent}%`;

    // 2. Slide Counter
    if (slideCounter) {
      slideCounter.textContent = `${String(currentSlideIndex + 1).padStart(2, '0')} / ${String(totalSlides).padStart(2, '0')}`;
    }

    // 3. Current Day Tab Sync
    const currentDay = currentSlide.dataset.day || '1';
    dayTabs.forEach(tab => {
      if (tab.dataset.targetDay === currentDay) {
        tab.classList.add('active');
      } else {
        tab.classList.remove('active');
      }
    });

    // 4. Session Time Pill
    const sessionTime = currentSlide.dataset.time || '08:30 - 10:00 AM';
    if (sessionTimePill) {
      const timeText = sessionTimePill.querySelector('.time-text');
      if (timeText) timeText.textContent = sessionTime;
    }

    // 5. Presenter Notes Update
    const notes = currentSlide.dataset.notes || 'No specific pedagogical notes for this slide. Emphasize practical job-readiness concepts.';
    if (notesContent) {
      notesContent.innerHTML = notes;
    }

    // 6. Highlight active thumbnail in overview
    const thumbs = overviewGrid.querySelectorAll('.overview-thumb');
    thumbs.forEach((thumb, i) => {
      if (i === currentSlideIndex) {
        thumb.classList.add('current');
      } else {
        thumb.classList.remove('current');
      }
    });
  }

  /**
   * Build Interactive Slide Overview Grid
   */
  function buildOverviewGrid() {
    overviewGrid.innerHTML = '';
    slides.forEach((slide, index) => {
      const title = slide.querySelector('.slide-title')?.textContent || `Slide ${index + 1}`;
      const unit = slide.querySelector('.badge-unit')?.textContent || `Unit ${slide.dataset.unit || '1'}`;
      const day = slide.dataset.day || '1';

      const thumb = document.createElement('div');
      thumb.className = `overview-thumb ${index === 0 ? 'current' : ''}`;
      thumb.dataset.day = day;
      thumb.innerHTML = `
        <div class="thumb-number">SLIDE ${String(index + 1).padStart(2, '0')} &bull; DAY ${day}</div>
        <div class="thumb-title">${title}</div>
        <div class="thumb-unit">${unit}</div>
      `;

      thumb.addEventListener('click', () => {
        goToSlide(index);
        closeOverview();
      });

      overviewGrid.appendChild(thumb);
    });

    // Overview filter buttons
    const filterBtns = document.querySelectorAll('.overview-filter-btn');
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const filter = btn.dataset.filter;
        const thumbs = overviewGrid.querySelectorAll('.overview-thumb');
        thumbs.forEach(thumb => {
          if (filter === 'all' || thumb.dataset.day === filter) {
            thumb.style.display = 'flex';
          } else {
            thumb.style.display = 'none';
          }
        });
      });
    });
  }

  function toggleOverview() {
    if (overviewModal.classList.contains('open')) {
      closeOverview();
    } else {
      overviewModal.classList.add('open');
    }
  }

  function closeOverview() {
    overviewModal.classList.remove('open');
  }

  function toggleNotes() {
    notesDrawer.classList.toggle('open');
  }

  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(err => {
        console.warn(`Fullscreen error: ${err.message}`);
      });
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      }
    }
  }

  /**
   * Event Listeners & Keyboard Shortcuts
   */
  function setupEventListeners() {
    // Buttons
    if (prevBtn) prevBtn.addEventListener('click', prevSlide);
    if (nextBtn) nextBtn.addEventListener('click', nextSlide);
    if (overviewBtn) overviewBtn.addEventListener('click', toggleOverview);
    if (closeOverviewBtn) closeOverviewBtn.addEventListener('click', closeOverview);
    if (notesBtn) notesBtn.addEventListener('click', toggleNotes);
    if (closeNotesBtn) closeNotesBtn.addEventListener('click', () => notesDrawer.classList.remove('open'));
    if (fullscreenBtn) fullscreenBtn.addEventListener('click', toggleFullscreen);
    if (printBtn) printBtn.addEventListener('click', () => window.print());

    // Day Tabs
    dayTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const targetDay = tab.dataset.targetDay;
        if (targetDay === '1' && day1FirstIndex !== -1) {
          goToSlide(day1FirstIndex);
        } else if (targetDay === '2' && day2FirstIndex !== -1) {
          goToSlide(day2FirstIndex);
        }
      });
    });

    // Keyboard Shortcuts
    document.addEventListener('keydown', (e) => {
      // Don't trigger if user is typing in an input
      if (['input', 'textarea', 'select'].includes(e.target.tagName.toLowerCase())) return;

      switch (e.key) {
        case 'ArrowRight':
        case ' ': // Spacebar
        case 'PageDown':
          e.preventDefault();
          nextSlide();
          break;
        case 'ArrowLeft':
        case 'PageUp':
          e.preventDefault();
          prevSlide();
          break;
        case 'Home':
          e.preventDefault();
          goToSlide(0);
          break;
        case 'End':
          e.preventDefault();
          goToSlide(totalSlides - 1);
          break;
        case 'Escape':
          e.preventDefault();
          toggleOverview();
          break;
        case 'n':
        case 'N':
          toggleNotes();
          break;
        case 'f':
        case 'F':
          toggleFullscreen();
          break;
        case '1':
          if (day1FirstIndex !== -1) goToSlide(day1FirstIndex);
          break;
        case '2':
          if (day2FirstIndex !== -1) goToSlide(day2FirstIndex);
          break;
      }
    });
  }

  // Launch Engine
  init();
});
