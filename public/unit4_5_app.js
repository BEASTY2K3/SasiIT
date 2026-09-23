/**
 * CANVA-STYLE PRESENTATION ENGINE - UNIT 4 & UNIT 5
 * Interactive Controls, Keyboard Shortcuts, Touch Gestures,
 * Multi-Resolution Scaling & Live Search Matrix
 */

document.addEventListener('DOMContentLoaded', () => {
  // DOM Elements
  const slides = Array.from(document.querySelectorAll('.slide-card'));
  const progressBar = document.getElementById('progressBar');
  const slideCounter = document.getElementById('slideCounter');
  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  const bottomPrevBtn = document.getElementById('bottomPrevBtn');
  const bottomNextBtn = document.getElementById('bottomNextBtn');
  const unit4Tab = document.getElementById('unit4Tab');
  const unit5Tab = document.getElementById('unit5Tab');
  const fullscreenBtn = document.getElementById('fullscreenBtn');
  const overviewBtn = document.getElementById('overviewBtn');
  const notesBtn = document.getElementById('notesBtn');
  const printBtn = document.getElementById('printBtn');
  
  // Overview Modal Elements
  const overviewModal = document.getElementById('overviewModal');
  const closeOverviewBtn = document.getElementById('closeOverviewBtn');
  const overviewSearch = document.getElementById('overviewSearch');
  const overviewGrid = document.getElementById('overviewGrid');
  
  // Notes Drawer Elements
  const notesDrawer = document.getElementById('notesDrawer');
  const closeNotesBtn = document.getElementById('closeNotesBtn');
  const notesContent = document.getElementById('notesContent');

  let currentSlideIndex = 0;
  const totalSlides = slides.length;

  if (totalSlides === 0) return;

  // Find index of first Unit 4 & Unit 5 slide
  const unit4FirstIndex = slides.findIndex(s => s.dataset.unit === 'Unit 4');
  const unit5FirstIndex = slides.findIndex(s => s.dataset.unit === 'Unit 5');

  /**
   * Initialize presentation
   */
  function init() {
    buildOverviewGrid();
    
    // Check URL Hash for initial slide (#slide-5)
    const hash = window.location.hash;
    let initialIndex = 0;
    if (hash && hash.startsWith('#slide-')) {
      const parsedNum = parseInt(hash.replace('#slide-', ''), 10);
      if (!isNaN(parsedNum) && parsedNum >= 1 && parsedNum <= totalSlides) {
        initialIndex = parsedNum - 1;
      }
    }

    goToSlide(initialIndex, false);
    setupEventListeners();
  }

  /**
   * Navigate to slide by index
   */
  function goToSlide(index, updateHash = true) {
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

    if (updateHash) {
      history.replaceState(null, null, `#slide-${index + 1}`);
    }
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
   * Update Progress, Counter, Unit Switchers, and Notes
   */
  function updateUIState() {
    const currentSlide = slides[currentSlideIndex];
    if (!currentSlide) return;

    // 1. Progress Bar
    const progress = ((currentSlideIndex + 1) / totalSlides) * 100;
    if (progressBar) progressBar.style.width = `${progress}%`;

    // 2. Slide Counter Pill
    if (slideCounter) {
      slideCounter.textContent = `${String(currentSlideIndex + 1).padStart(2, '0')} / ${String(totalSlides).padStart(2, '0')}`;
    }

    // 3. Unit Tab Highlighting
    const unit = currentSlide.dataset.unit;
    if (unit === 'Unit 4') {
      if (unit4Tab) unit4Tab.className = 'unit-tab-btn active-u4';
      if (unit5Tab) unit5Tab.className = 'unit-tab-btn';
    } else if (unit === 'Unit 5') {
      if (unit4Tab) unit4Tab.className = 'unit-tab-btn';
      if (unit5Tab) unit5Tab.className = 'unit-tab-btn active-u5';
    }

    // 4. Update Presenter Notes
    const notes = currentSlide.dataset.notes || 'Emphasize real-world workplace applications and non-technical student analogies.';
    if (notesContent) {
      notesContent.innerHTML = notes;
    }

    // 5. Update Overview Matrix Active State
    const thumbs = overviewGrid.querySelectorAll('.thumb-card');
    thumbs.forEach((thumb, i) => {
      if (i === currentSlideIndex) {
        thumb.classList.add('active');
      } else {
        thumb.classList.remove('active');
      }
    });

    // 6. Navigation Buttons disabled state
    if (prevBtn) prevBtn.disabled = (currentSlideIndex === 0);
    if (nextBtn) nextBtn.disabled = (currentSlideIndex === totalSlides - 1);
    if (bottomPrevBtn) bottomPrevBtn.disabled = (currentSlideIndex === 0);
    if (bottomNextBtn) bottomNextBtn.disabled = (currentSlideIndex === totalSlides - 1);
  }

  /**
   * Build Interactive Slide Overview Grid
   */
  function buildOverviewGrid() {
    overviewGrid.innerHTML = '';
    slides.forEach((slide, index) => {
      const heading = slide.querySelector('.slide-heading')?.textContent || `Slide ${index + 1}`;
      const unit = slide.dataset.unit || 'Unit 4';
      const topicNum = slide.querySelector('.badge-topic-number')?.textContent || `Topic ${index + 1}`;

      const card = document.createElement('div');
      card.className = `thumb-card ${index === currentSlideIndex ? 'active' : ''}`;
      card.dataset.unit = unit;
      card.dataset.index = index;
      card.dataset.search = `${heading} ${topicNum} ${unit}`.toLowerCase();

      card.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span class="thumb-unit-pill">${unit}</span>
          <span class="thumb-card-num">${String(index + 1).padStart(2, '0')}</span>
        </div>
        <div class="thumb-card-title">${heading}</div>
        <div style="font-size: 0.72rem; color: #64748B; font-family: var(--font-mono);">${topicNum}</div>
      `;

      card.addEventListener('click', () => {
        goToSlide(index);
        closeOverview();
      });

      overviewGrid.appendChild(card);
    });
  }

  /**
   * Filter overview grid via search
   */
  function filterOverviewGrid(query) {
    const q = query.trim().toLowerCase();
    const cards = overviewGrid.querySelectorAll('.thumb-card');
    cards.forEach(card => {
      if (!q || card.dataset.search.includes(q)) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  }

  function openOverview() {
    if (overviewModal) {
      overviewModal.classList.add('open');
      if (overviewSearch) {
        overviewSearch.value = '';
        filterOverviewGrid('');
        overviewSearch.focus();
      }
    }
  }

  function closeOverview() {
    if (overviewModal) {
      overviewModal.classList.remove('open');
    }
  }

  function toggleNotes() {
    if (notesDrawer) {
      notesDrawer.classList.toggle('open');
    }
  }

  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(() => {});
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      }
    }
  }

  /**
   * Setup Event Listeners
   */
  function setupEventListeners() {
    // Navigation buttons
    if (prevBtn) prevBtn.addEventListener('click', prevSlide);
    if (nextBtn) nextBtn.addEventListener('click', nextSlide);
    if (bottomPrevBtn) bottomPrevBtn.addEventListener('click', prevSlide);
    if (bottomNextBtn) bottomNextBtn.addEventListener('click', nextSlide);

    // Unit tabs
    if (unit4Tab) {
      unit4Tab.addEventListener('click', () => {
        if (unit4FirstIndex !== -1) goToSlide(unit4FirstIndex);
      });
    }
    if (unit5Tab) {
      unit5Tab.addEventListener('click', () => {
        if (unit5FirstIndex !== -1) goToSlide(unit5FirstIndex);
      });
    }

    // Utility actions
    if (overviewBtn) overviewBtn.addEventListener('click', openOverview);
    if (closeOverviewBtn) closeOverviewBtn.addEventListener('click', closeOverview);
    if (notesBtn) notesBtn.addEventListener('click', toggleNotes);
    if (closeNotesBtn) closeNotesBtn.addEventListener('click', toggleNotes);
    if (fullscreenBtn) fullscreenBtn.addEventListener('click', toggleFullscreen);
    if (printBtn) printBtn.addEventListener('click', () => window.print());

    // Search filter
    if (overviewSearch) {
      overviewSearch.addEventListener('input', (e) => {
        filterOverviewGrid(e.target.value);
      });
    }

    // Close overview when clicking backdrop
    if (overviewModal) {
      overviewModal.addEventListener('click', (e) => {
        if (e.target === overviewModal) {
          closeOverview();
        }
      });
    }

    // Keyboard Shortcuts
    document.addEventListener('keydown', (e) => {
      // Ignore if user is typing in the search box
      if (document.activeElement === overviewSearch) {
        if (e.key === 'Escape') closeOverview();
        return;
      }

      switch (e.key) {
        case 'ArrowRight':
        case ' ':
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
        case 'f':
        case 'F':
          e.preventDefault();
          toggleFullscreen();
          break;
        case 'Escape':
          e.preventDefault();
          if (overviewModal && overviewModal.classList.contains('open')) {
            closeOverview();
          } else {
            openOverview();
          }
          break;
        case 'n':
        case 'N':
          e.preventDefault();
          toggleNotes();
          break;
        case 'p':
        case 'P':
          if (e.ctrlKey || e.metaKey) {
            // allow native print handler
          }
          break;
        case '1':
          if (unit4FirstIndex !== -1) goToSlide(unit4FirstIndex);
          break;
        case '2':
          if (unit5FirstIndex !== -1) goToSlide(unit5FirstIndex);
          break;
      }
    });

    // Touch Swipe Support for Mobile & Tablets
    let touchStartX = 0;
    let touchEndX = 0;
    const stage = document.querySelector('.stage-wrapper');

    if (stage) {
      stage.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
      }, { passive: true });

      stage.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
      }, { passive: true });
    }

    function handleSwipe() {
      const diff = touchEndX - touchStartX;
      if (Math.abs(diff) > 50) {
        if (diff < 0) {
          nextSlide(); // swipe left -> next
        } else {
          prevSlide(); // swipe right -> prev
        }
      }
    }
  }

  // Run initialization
  init();
});
