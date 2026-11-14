document.addEventListener('DOMContentLoaded', () => {
  // FAQ Accordion Toggle
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach((item) => {
    const trigger = item.querySelector('.faq-item__trigger');
    if (!trigger) return;

    trigger.addEventListener('click', () => {
      const isOpen = item.classList.contains('faq-item--open');

      faqItems.forEach((otherItem) => {
        otherItem.classList.remove('faq-item--open');
        const otherTrigger = otherItem.querySelector('.faq-item__trigger');
        if (otherTrigger) {
          otherTrigger.setAttribute('aria-expanded', 'false');
        }
      });

      if (!isOpen) {
        item.classList.add('faq-item--open');
        trigger.setAttribute('aria-expanded', 'true');
      }
    });
  });

  // Mobile Menu Toggle
  const siteHeader = document.querySelector('.site-header');
  const mobileToggle = document.querySelector('.mobile-menu-toggle');
  const navLinks = document.querySelectorAll('.main-nav__link');

  if (mobileToggle && siteHeader) {
    mobileToggle.addEventListener('click', () => {
      const isExpanded = siteHeader.classList.toggle('site-header--menu-open');
      mobileToggle.setAttribute('aria-expanded', String(isExpanded));
    });
  }

  navLinks.forEach((link) => {
    link.addEventListener('click', () => {
      navLinks.forEach((l) => l.classList.remove('main-nav__link--active'));
      link.classList.add('main-nav__link--active');
      if (siteHeader) {
        siteHeader.classList.remove('site-header--menu-open');
      }
      if (mobileToggle) {
        mobileToggle.setAttribute('aria-expanded', 'false');
      }
    });
  });

  // Smooth Scroll-Reveal with Stagger Animation
  const revealTargets = [
    { selector: '.section-header', type: 'reveal-up', stagger: false },
    { selector: '.hero-section__content', type: 'reveal-up', stagger: false },
    { selector: '.hero-section__visual', type: 'reveal-fade', stagger: false },
    { selector: '.commitment-card', type: 'reveal-up', stagger: true, parent: '.commitments-grid' },
    { selector: '.services-grid-top .service-card', type: 'reveal-up', stagger: true, parent: '.services-grid-top' },
    { selector: '.services-grid-bottom .service-card', type: 'reveal-up', stagger: true, parent: '.services-grid-bottom' },
    { selector: '.comparison-table-wrap', type: 'reveal-up', stagger: false },
    { selector: '.comparison-section .cta-group', type: 'reveal-up', stagger: false },
    { selector: '.process-card', type: 'reveal-up', stagger: true, parent: '.process-grid' },
    { selector: '.process-section .cta-group', type: 'reveal-up', stagger: false },
    { selector: '.offers-section__tech-col', type: 'reveal-fade', stagger: false },
    { selector: '.offer-card', type: 'reveal-up', stagger: true, parent: '.offers-grid' },
    { selector: '.offers-section__cta, .offers-section__gift-bar', type: 'reveal-up', stagger: false },
    { selector: '.stat-card', type: 'reveal-up', stagger: true, parent: '.stats-grid' },
    { selector: '.review-card', type: 'reveal-up', stagger: true, parent: '.reviews-grid' },
    { selector: '.branches-section__header', type: 'reveal-up', stagger: false },
    { selector: '.branches-card', type: 'reveal-up', stagger: false },
    { selector: '.gallery-filters', type: 'reveal-up', stagger: false },
    { selector: '.gallery-item', type: 'reveal-up', stagger: true, parent: '.gallery-mosaic' },
    { selector: '.gallery-cta-banner', type: 'reveal-up', stagger: false },
    { selector: '.faq-item', type: 'reveal-up', stagger: true, parent: '.faq-list' },
    { selector: '.faq-section__cta', type: 'reveal-up', stagger: false },
    { selector: '.site-footer__brand-bar', type: 'reveal-up', stagger: false },
    { selector: '.site-footer__col', type: 'reveal-up', stagger: true, parent: '.site-footer__grid' }
  ];

  // Initialize reveal classes
  revealTargets.forEach((group) => {
    const elements = document.querySelectorAll(group.selector);
    elements.forEach((el, index) => {
      el.classList.add('reveal-init', group.type);
      if (group.stagger) {
        // Stagger animation timing: 70ms per card
        const delay = Math.min(index * 70, 500);
        el.style.transitionDelay = `${delay}ms`;
      }
    });
  });

  // IntersectionObserver for trigger
  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -45px 0px',
    threshold: 0.12
  };

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('reveal-active');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.reveal-init').forEach((el) => {
    revealObserver.observe(el);
  });

  // ==================== GALLERY FILTERING & LOAD MORE ====================
  const galleryFilters = document.querySelectorAll('.gallery-filter-btn');
  const galleryItems = document.querySelectorAll('.gallery-item');
  const galleryMoreBtn = document.getElementById('gallery-more-btn');
  const INITIAL_VISIBLE_COUNT = 12;
  let isAllExpanded = false;
  let currentFilter = 'all';

  function updateGalleryVisibility() {
    let visibleMatchCount = 0;
    galleryItems.forEach((item) => {
      const category = item.getAttribute('data-category');
      const isMatch = currentFilter === 'all' || category === currentFilter;

      if (!isMatch) {
        item.classList.add('is-hidden');
      } else {
        if (currentFilter === 'all' && !isAllExpanded && visibleMatchCount >= INITIAL_VISIBLE_COUNT) {
          item.classList.add('is-hidden');
        } else {
          item.classList.remove('is-hidden');
        }
        visibleMatchCount++;
      }
    });

    if (galleryMoreBtn && galleryMoreBtn.parentElement) {
      if (currentFilter !== 'all' || isAllExpanded || visibleMatchCount <= INITIAL_VISIBLE_COUNT) {
        galleryMoreBtn.parentElement.style.display = 'none';
      } else {
        galleryMoreBtn.parentElement.style.display = 'block';
      }
    }
  }

  galleryFilters.forEach((btn) => {
    btn.addEventListener('click', () => {
      galleryFilters.forEach((b) => {
        b.classList.remove('is-active');
        b.setAttribute('aria-selected', 'false');
      });
      btn.classList.add('is-active');
      btn.setAttribute('aria-selected', 'true');
      currentFilter = btn.getAttribute('data-filter') || 'all';
      updateGalleryVisibility();
    });
  });

  if (galleryMoreBtn) {
    galleryMoreBtn.addEventListener('click', () => {
      isAllExpanded = true;
      updateGalleryVisibility();
    });
  }

  updateGalleryVisibility();

  // ==================== GALLERY LIGHTBOX MODAL (PURE PHOTO) ====================
  const lightbox = document.getElementById('gallery-lightbox');
  const lightboxImg = document.getElementById('lightbox-img');
  const lightboxPrev = document.getElementById('lightbox-prev');
  const lightboxNext = document.getElementById('lightbox-next');
  let currentLightboxIndex = 0;

  function getVisibleItems() {
    return Array.from(galleryItems).filter((item) => !item.classList.contains('is-hidden'));
  }

  function showLightboxIndex(index) {
    const visibleItems = getVisibleItems();
    if (!visibleItems.length) return;
    if (index < 0) index = visibleItems.length - 1;
    if (index >= visibleItems.length) index = 0;
    currentLightboxIndex = index;

    const item = visibleItems[index];
    const img = item.querySelector('.gallery-item__img');

    if (img && lightboxImg) {
      lightboxImg.src = img.src;
      lightboxImg.alt = img.alt;
    }
  }

  function openLightbox(item) {
    if (!lightbox) return;
    const visibleItems = getVisibleItems();
    const index = visibleItems.indexOf(item);
    if (index !== -1) {
      showLightboxIndex(index);
      lightbox.classList.add('is-open');
      lightbox.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeLightbox() {
    if (!lightbox) return;
    lightbox.classList.remove('is-open');
    lightbox.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  galleryItems.forEach((item) => {
    item.addEventListener('click', () => openLightbox(item));
  });

  if (lightbox) {
    lightbox.querySelectorAll('[data-close-lightbox]').forEach((el) => {
      el.addEventListener('click', closeLightbox);
    });

    if (lightboxPrev) {
      lightboxPrev.addEventListener('click', (e) => {
        e.stopPropagation();
        showLightboxIndex(currentLightboxIndex - 1);
      });
    }

    if (lightboxNext) {
      lightboxNext.addEventListener('click', (e) => {
        e.stopPropagation();
        showLightboxIndex(currentLightboxIndex + 1);
      });
    }

    document.addEventListener('keydown', (e) => {
      if (!lightbox.classList.contains('is-open')) return;
      if (e.key === 'Escape') closeLightbox();
      if (e.key === 'ArrowLeft') showLightboxIndex(currentLightboxIndex - 1);
      if (e.key === 'ArrowRight') showLightboxIndex(currentLightboxIndex + 1);
    });
  }
});
