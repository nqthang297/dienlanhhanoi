with open('.agents/section_7c.html', 'r', encoding='utf-8') as f:
    section_7c = f.read()

lightbox_html = """  <!-- ==================== GALLERY LIGHTBOX MODAL ==================== -->
  <div class="gallery-lightbox" id="gallery-lightbox" aria-hidden="true" role="dialog" aria-modal="true" aria-label="Xem ảnh dự án thực tế">
    <div class="gallery-lightbox__backdrop" data-close-lightbox></div>
    <div class="gallery-lightbox__dialog">
      <button type="button" class="gallery-lightbox__close" aria-label="Đóng ảnh" data-close-lightbox>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
      </button>
      <button type="button" class="gallery-lightbox__nav gallery-lightbox__nav--prev" aria-label="Ảnh trước" id="lightbox-prev">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
      </button>
      <button type="button" class="gallery-lightbox__nav gallery-lightbox__nav--next" aria-label="Ảnh tiếp theo" id="lightbox-next">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <polyline points="9 18 15 12 9 6"></polyline>
        </svg>
      </button>
      <div class="gallery-lightbox__content">
        <img src="" alt="" class="gallery-lightbox__img" id="lightbox-img">
        <div class="gallery-lightbox__caption">
          <span class="gallery-lightbox__tag" id="lightbox-tag"></span>
          <h4 class="gallery-lightbox__title" id="lightbox-title"></h4>
        </div>
      </div>
    </div>
  </div>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target_sec8 = "    <!-- ==================== SECTION 8: CÂU HỎI THƯỜNG GẶP (FAQ) ==================== -->"
if target_sec8 not in content:
    raise Exception("target_sec8 not found in index.html!")

content = content.replace(target_sec8, section_7c + "\n" + target_sec8, 1)

target_script = '  <script src="script.js"></script>'
if target_script not in content:
    raise Exception("target_script not found in index.html!")

content = content.replace(target_script, lightbox_html + "\n" + target_script, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Inserted Section 7C and Lightbox Modal into index.html successfully!")
