with open('.agents/gallery_cards.html', 'r', encoding='utf-8') as f:
    cards = f.read()

section_html = f"""    <!-- ==================== SECTION 7C: HÌNH ẢNH THỰC TẾ ==================== -->
    <section class="gallery-section" id="hinh-anh">
      <div class="container">
        <div class="section-header">
          <div class="section-badge section-badge--blue-pill">HÌNH ẢNH THỰC TẾ CỦA DỰ ÁN</div>
          <h2 class="section-title">
            Cần Mẫn Làm Việc <span class="underline-curve-blue">Phục Vụ Khách Hàng</span> Mỗi Ngày
          </h2>
          <p class="section-subtitle">
            Hơn 10.000+ ca sửa chữa, bảo dưỡng điều hòa, tủ lạnh, máy giặt, máy lọc nước, bếp từ được đội ngũ kỹ thuật viên tay nghề cao của Điện Lạnh Hà Nội hoàn thành trực tiếp tại nhà khách hàng khắp 12 Quận thủ đô.
          </p>
        </div>

        <!-- Filter Tabs -->
        <div class="gallery-filters" role="tablist" aria-label="Bộ lọc hình ảnh dự án thực tế">
          <button type="button" class="gallery-filter-btn is-active" data-filter="all" role="tab" aria-selected="true">
            Tất Cả <span class="gallery-filter-count">28</span>
          </button>
          <button type="button" class="gallery-filter-btn" data-filter="dieu-hoa" role="tab" aria-selected="false">
            Điều Hòa <span class="gallery-filter-count">7</span>
          </button>
          <button type="button" class="gallery-filter-btn" data-filter="tu-lanh" role="tab" aria-selected="false">
            Tủ Lạnh <span class="gallery-filter-count">3</span>
          </button>
          <button type="button" class="gallery-filter-btn" data-filter="may-giat" role="tab" aria-selected="false">
            Máy Giặt <span class="gallery-filter-count">8</span>
          </button>
          <button type="button" class="gallery-filter-btn" data-filter="may-loc-nuoc" role="tab" aria-selected="false">
            Máy Lọc Nước <span class="gallery-filter-count">5</span>
          </button>
          <button type="button" class="gallery-filter-btn" data-filter="bep-tu" role="tab" aria-selected="false">
            Bếp Từ <span class="gallery-filter-count">5</span>
          </button>
        </div>

        <!-- Gallery Grid -->
        <div class="gallery-grid" id="project-gallery">
{cards}
        </div>

        <!-- Load more button -->
        <div class="gallery-more-wrap">
          <button type="button" class="gallery-more-btn" id="gallery-more-btn">
            <span>Xem Thêm Hình Ảnh Thực Tế</span>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
        </div>

        <!-- Bottom CTA Banner -->
        <div class="gallery-cta-banner">
          <div class="gallery-cta-banner__content">
            <h3 class="gallery-cta-banner__title">Thiết Bị Nhà Bạn Đang Gặp Trục Trặc?</h3>
            <p class="gallery-cta-banner__desc">Đội thợ kỹ thuật gần nhất luôn sẵn sàng có mặt sau 15 – 30 phút. Kiểm tra miễn phí 100% tại nhà.</p>
          </div>
          <div class="cta-group">
            <a href="tel:0962099028" class="btn-cta btn-cta--red">
              <span class="btn-cta__icon-phone" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="currentColor">
                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                </svg>
              </span>
              <span class="btn-cta__text-group">
                <span class="btn-cta__label">GỌI THỢ NGAY</span>
                <strong class="btn-cta__phone">0962.099.028</strong>
              </span>
            </a>
            <a href="https://zalo.me/0962099028" target="_blank" rel="noopener noreferrer" class="btn-cta btn-cta--zalo-outline">
              <span class="btn-cta__zalo-bubble" aria-hidden="true">Zalo</span>
              <span class="btn-cta__zalo-single">CHAT ZALO 24/7</span>
            </a>
          </div>
        </div>
      </div>
    </section>
"""

with open('.agents/section_7c.html', 'w', encoding='utf-8') as f:
    f.write(section_html)

print("Generated .agents/section_7c.html successfully!")
