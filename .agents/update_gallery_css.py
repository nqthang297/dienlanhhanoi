with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace section 7c block
start_tag = "/* ==================== SECTION 7C: HÌNH ẢNH THỰC TẾ ==================== */"
end_tag = "/* ==================== SECTION 8: FAQ ==================== */"

idx1 = css.find(start_tag)
idx2 = css.find(end_tag)

if idx1 == -1 or idx2 == -1:
    raise Exception("Tags not found in style.css!")

new_sec7c = """/* ==================== SECTION 7C: HÌNH ẢNH THỰC TẾ ==================== */
.gallery-section {
  background: var(--color-white);
  padding-block: var(--section-py);
  border-top: var(--border-thin);
}

.gallery-filters {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: var(--gallery-filter-gap);
  margin-bottom: var(--space-8);
}

.gallery-filter-btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2-5) var(--space-4-5);
  background: var(--color-blue-50);
  color: var(--color-navy-900);
  border: var(--border-card);
  border-radius: var(--radius-pill);
  font-size: var(--fs-sm);
  font-weight: var(--fw-bold);
  font-family: inherit;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.gallery-filter-btn:hover {
  background: var(--color-blue-100);
  color: var(--color-blue-700);
  border-color: var(--color-blue-300);
  transform: translateY(var(--translate-hover-subtle));
}

.gallery-filter-btn.is-active {
  background: var(--grad-btn-blue);
  color: var(--color-white);
  border-color: var(--color-blue-600);
  box-shadow: var(--shadow-btn-blue);
}

.gallery-filter-count {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-0) var(--space-2);
  min-width: 1.25rem;
  height: 1.25rem;
  border-radius: var(--radius-pill);
  background: var(--color-blue-200);
  color: var(--color-blue-900);
  font-size: var(--fs-2xs);
  font-weight: var(--fw-black);
}

.gallery-filter-btn.is-active .gallery-filter-count {
  background: var(--color-white-glass-22);
  color: var(--color-white);
}

/* Unique Masonry Mosaic Layout */
.gallery-mosaic {
  column-count: 4;
  column-gap: var(--space-4);
  margin-bottom: var(--space-8);
}

.gallery-item {
  break-inside: avoid;
  margin-bottom: var(--space-4);
  border-radius: var(--radius-xl);
  overflow: hidden;
  position: relative;
  box-shadow: var(--shadow-card);
  border: var(--border-card);
  background: var(--color-blue-50);
  cursor: pointer;
  transition: transform var(--transition-fast), box-shadow var(--transition-fast), border-color var(--transition-fast);
}

.gallery-item:hover {
  transform: translateY(var(--translate-hover));
  box-shadow: var(--shadow-card-hover);
  border-color: var(--color-blue-300);
}

.gallery-item.is-hidden {
  display: none !important;
}

.gallery-item__frame {
  position: relative;
  width: var(--size-full);
  display: block;
  overflow: hidden;
  line-height: var(--lh-none);
}

.gallery-item__img {
  width: var(--size-full);
  height: auto;
  display: block;
  transition: transform var(--transition-normal);
}

.gallery-item:hover .gallery-item__img {
  transform: scale(1.05);
}

.gallery-item__overlay {
  position: absolute;
  inset: var(--space-0);
  background: var(--color-overlay-badge);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  backdrop-filter: blur(2px);
  -webkit-backdrop-filter: blur(2px);
  transition: opacity var(--transition-fast);
}

.gallery-item:hover .gallery-item__overlay {
  opacity: 1;
}

.gallery-item__zoom-icon {
  width: var(--icon-box-md);
  height: var(--icon-box-md);
  border-radius: var(--radius-pill);
  background: var(--color-white-glass-35);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  color: var(--color-white);
  border: var(--border-card-white);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-shadow: var(--shadow-badge);
  transition: transform var(--transition-fast), background var(--transition-fast), color var(--transition-fast);
}

.gallery-item:hover .gallery-item__zoom-icon {
  transform: scale(1.1);
  background: var(--color-white);
  color: var(--color-blue-700);
}

.gallery-item__zoom-icon svg {
  width: var(--icon-sm);
  height: var(--icon-sm);
}

/* Load more button */
.gallery-more-wrap {
  text-align: center;
  margin-bottom: var(--space-10);
}

.gallery-more-btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-3-5) var(--space-7);
  background: var(--color-white);
  color: var(--color-blue-700);
  border: var(--border-blue-outline);
  border-radius: var(--radius-pill);
  font-size: var(--fs-base);
  font-weight: var(--fw-extrabold);
  font-family: inherit;
  cursor: pointer;
  box-shadow: var(--shadow-card);
  transition: all var(--transition-fast);
}

.gallery-more-btn:hover {
  background: var(--color-blue-600);
  color: var(--color-white);
  border-color: var(--color-blue-600);
  transform: translateY(var(--translate-hover-subtle));
  box-shadow: var(--shadow-btn-blue);
}

.gallery-more-btn svg {
  width: var(--icon-sm);
  height: var(--icon-sm);
  transition: transform var(--transition-fast);
}

.gallery-more-btn:hover svg {
  transform: translateY(2px);
}

/* CTA Banner inside Gallery */
.gallery-cta-banner {
  background: var(--grad-ice-section);
  border-radius: var(--radius-2xl);
  border: var(--border-card);
  padding: var(--space-7) var(--space-8);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-6);
  box-shadow: var(--shadow-card);
}

.gallery-cta-banner__title {
  font-size: var(--fs-h3-service);
  font-weight: var(--fw-black);
  color: var(--color-navy-900);
  margin-bottom: var(--space-1-5);
}

.gallery-cta-banner__desc {
  font-size: var(--fs-sm);
  color: var(--color-slate-600);
}

/* Lightbox Modal (Pure Photo View) */
.gallery-lightbox {
  position: fixed;
  inset: var(--space-0);
  z-index: var(--z-modal);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--transition-fast);
}

.gallery-lightbox.is-open {
  opacity: 1;
  pointer-events: auto;
}

.gallery-lightbox__backdrop {
  position: absolute;
  inset: var(--space-0);
  background: var(--color-backdrop-modal);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.gallery-lightbox__dialog {
  position: relative;
  z-index: 1;
  max-width: var(--lightbox-max-w);
  width: 92%;
  border-radius: var(--radius-2xl);
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: var(--shadow-card-strong);
}

.gallery-lightbox__close {
  position: absolute;
  top: var(--space-4);
  right: var(--space-4);
  z-index: 2;
  width: var(--icon-box-sm);
  height: var(--icon-box-sm);
  border-radius: var(--radius-pill);
  background: var(--color-white-glass-35);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  color: var(--color-white);
  border: var(--border-card-white);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background var(--transition-fast), transform var(--transition-fast);
}

.gallery-lightbox__close:hover {
  background: var(--color-red-500);
  transform: scale(1.1);
}

.gallery-lightbox__close svg {
  width: var(--icon-sm);
  height: var(--icon-sm);
}

.gallery-lightbox__nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 2;
  width: var(--icon-box-md);
  height: var(--icon-box-md);
  border-radius: var(--radius-pill);
  background: var(--color-white-glass-35);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  color: var(--color-white);
  border: var(--border-card-white);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background var(--transition-fast), transform var(--transition-fast);
}

.gallery-lightbox__nav:hover {
  background: var(--color-blue-600);
  transform: translateY(-50%) scale(1.1);
}

.gallery-lightbox__nav svg {
  width: var(--icon-md);
  height: var(--icon-md);
}

.gallery-lightbox__nav--prev {
  left: var(--space-4);
}

.gallery-lightbox__nav--next {
  right: var(--space-4);
}

.gallery-lightbox__content {
  display: flex;
  align-items: center;
  justify-content: center;
  width: var(--size-full);
}

.gallery-lightbox__img {
  max-width: var(--size-full);
  max-height: 85vh;
  width: auto;
  height: auto;
  object-fit: contain;
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-card-strong);
}
"""

css = css[:idx1] + new_sec7c + "\n" + css[idx2:]

# Update 1080px responsive
target_1080 = """  .services-grid-bottom,
  .process-grid,
  .stats-grid,
  .reviews-grid,
  .site-footer__grid,
  .gallery-grid {
    grid-template-columns: var(--grid-3col);
  }"""

replace_1080 = """  .services-grid-bottom,
  .process-grid,
  .stats-grid,
  .reviews-grid,
  .site-footer__grid {
    grid-template-columns: var(--grid-1col);
  }

  .gallery-mosaic {
    column-count: 3;
    column-gap: var(--space-3-5);
  }"""

if target_1080 in css:
    css = css.replace(target_1080, replace_1080, 1)

# Update 768px responsive
old_mobile_gallery = """  /* Gallery Mobile */
  .gallery-grid {
    grid-template-columns: var(--grid-2col);
    gap: var(--space-3);
  }

  .gallery-card__media {
    height: var(--gallery-img-h-mobile);
  }

  .gallery-card__info {
    padding: var(--space-3);
  }

  .gallery-card__title {
    font-size: var(--fs-xs);
  }

  .gallery-filter-btn {
    font-size: var(--fs-xs);
    padding: var(--space-2) var(--space-3);
  }

  .gallery-lightbox__caption {
    flex-direction: column;
    align-items: flex-start;
    gap: var(--space-1);
    padding: var(--space-3) var(--space-4);
  }

  .gallery-lightbox__title {
    font-size: var(--fs-xs);
  }

  .gallery-lightbox__nav {
    width: var(--icon-box-sm);
    height: var(--icon-box-sm);
  }"""

new_mobile_gallery = """  /* Gallery Mobile */
  .gallery-mosaic {
    column-count: 2;
    column-gap: var(--space-2-5);
  }

  .gallery-item {
    margin-bottom: var(--space-2-5);
    border-radius: var(--radius-lg);
  }

  .gallery-filter-btn {
    font-size: var(--fs-xs);
    padding: var(--space-2) var(--space-3);
  }

  .gallery-lightbox__nav {
    width: var(--icon-box-sm);
    height: var(--icon-box-sm);
  }

  .gallery-lightbox__nav svg {
    width: var(--icon-sm);
    height: var(--icon-sm);
  }"""

if old_mobile_gallery in css:
    css = css.replace(old_mobile_gallery, new_mobile_gallery, 1)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css with unique Masonry Mosaic Gallery!")
