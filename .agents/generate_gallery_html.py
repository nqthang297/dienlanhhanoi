import os
import json

data = [
    # DIEU HOA (7)
    {
        'category': 'dieu-hoa',
        'tag': 'Điều hòa',
        'file': 'assets/images/dieu%20hoa/1794444478042_1267629377072362715_1267629377072362715_d93af7abcdfdf6d597298a646eefd554.jpg',
        'title': 'Sửa chữa điều hòa không mát, chảy nước',
        'desc': 'Trực tiếp tại căn hộ Quận Cầu Giấy'
    },
    {
        'category': 'dieu-hoa',
        'tag': 'Điều hòa',
        'file': 'assets/images/dieu%20hoa/1794444478072_1267629377072362715_1267629377072362715_5e91222e0380a7673ad1718b3bd10096.jpg',
        'title': 'Vệ sinh, bảo dưỡng điều hòa treo tường',
        'desc': 'Xịt rửa dàn lạnh và khử khuẩn bằng dung dịch'
    },
    {
        'category': 'dieu-hoa',
        'tag': 'Điều hòa',
        'file': 'assets/images/dieu%20hoa/1794444478088_1267629377072362715_1267629377072362715_24bb2a8f995dd7e7585f171e4b37067d.jpg',
        'title': 'Kiểm tra áp suất và nạp gas điều hòa R32',
        'desc': 'Bổ sung gas chuẩn thông số kỹ thuật'
    },
    {
        'category': 'dieu-hoa',
        'tag': 'Điều hòa',
        'file': 'assets/images/dieu%20hoa/1794444478102_1267629377072362715_1267629377072362715_9190a8975b4423ef6a9c3ee16e99d26c.jpg',
        'title': 'Sửa bo mạch điều hòa Inverter nhấp nháy đèn',
        'desc': 'Đo đạc linh kiện và thay thế tụ kích nguồn'
    },
    {
        'category': 'dieu-hoa',
        'tag': 'Điều hòa',
        'file': 'assets/images/dieu%20hoa/1794444478114_1267629377072362715_1267629377072362715_b48aa1c5f030a6682a4d0cc648bed0e3.jpg',
        'title': 'Bảo dưỡng dàn nóng điều hòa ngoài ban công',
        'desc': 'Đảm bảo tản nhiệt tối ưu, tiết kiệm điện'
    },
    {
        'category': 'dieu-hoa',
        'tag': 'Điều hòa',
        'file': 'assets/images/dieu%20hoa/1794444478123_1267629377072362715_1267629377072362715_d85f581cda651a7567a0a373508ce5ca.jpg',
        'title': 'Thay thế block điều hòa Daikin Inverter',
        'desc': 'Linh kiện chính hãng 100%, bảo hành 12 tháng'
    },
    {
        'category': 'dieu-hoa',
        'tag': 'Điều hòa',
        'file': 'assets/images/dieu%20hoa/1794444478132_1267629377072362715_1267629377072362715_c32f15bcc0bff006d7314b8677b76e03.jpg',
        'title': 'Khắc phục quạt gió dàn lạnh kêu to',
        'desc': 'Cân chỉnh mô tơ và bạc đạn vận hành êm ái'
    },

    # TU LANH (3)
    {
        'category': 'tu-lanh',
        'tag': 'Tủ lạnh',
        'file': 'assets/images/tu%20lanh/1794444204688_1267629377072362715_1267629377072362715_11208d1c492dbbc6a058b9b8dee9d2a4.jpg',
        'title': 'Sửa tủ lạnh Side-by-Side không làm đá',
        'desc': 'Xử lý cụm van cấp nước và motor xoay đá'
    },
    {
        'category': 'tu-lanh',
        'tag': 'Tủ lạnh',
        'file': 'assets/images/tu%20lanh/1794444204720_1267629377072362715_1267629377072362715_f648d00c85ebb5f27570f516c1501ead.jpg',
        'title': 'Sửa tủ lạnh mất lạnh ngăn mát, đóng tuyết',
        'desc': 'Thay thế cảm biến nhiệt độ và cầu chì nhiệt'
    },
    {
        'category': 'tu-lanh',
        'tag': 'Tủ lạnh',
        'file': 'assets/images/tu%20lanh/1794444204736_1267629377072362715_1267629377072362715_afabca1a141fd57ba9605a00da2acb27.jpg',
        'title': 'Nạp gas và kiểm tra rò rỉ dàn nóng tủ lạnh',
        'desc': 'Hút chân không và nạp đúng lượng gas R600a'
    },

    # MAY GIAT (8)
    {
        'category': 'may-giat',
        'tag': 'Máy giặt',
        'file': 'assets/images/may%20giat/1794443582248_1267629377072362715_1267629377072362715_6232268ff4ac6cc81dba07e557af4c72.jpg',
        'title': 'Tháo lồng giặt vệ sinh khử khuẩn tại nhà',
        'desc': 'Tẩy sạch mảng bám cặn bẩn lâu năm'
    },
    {
        'category': 'may-giat',
        'tag': 'Máy giặt',
        'file': 'assets/images/may%20giat/1794443582276_1267629377072362715_1267629377072362715_803eab0257e3ac460673212c89fdf2ac.jpg',
        'title': 'Sửa máy giặt cửa ngang Electrolux không vắt',
        'desc': 'Khắc phục bơm xả nước và kiểm tra đường ống'
    },
    {
        'category': 'may-giat',
        'tag': 'Máy giặt',
        'file': 'assets/images/may%20giat/1794443582297_1267629377072362715_1267629377072362715_dc2a2d221139ece5c09e064395a0bf6d.jpg',
        'title': 'Thay thế gioăng cao su cửa trước máy giặt',
        'desc': 'Khắc phục tình trạng rò rỉ nước và mốc đen'
    },
    {
        'category': 'may-giat',
        'tag': 'Máy giặt',
        'file': 'assets/images/may%20giat/1794443582308_1267629377072362715_1267629377072362715_5e0b3b16aae78c8a4a1a2c383a8b3036.jpg',
        'title': 'Sửa bo mạch điều khiển máy giặt báo lỗi',
        'desc': 'Khôi phục hoàn toàn các chương trình giặt sấy'
    },
    {
        'category': 'may-giat',
        'tag': 'Máy giặt',
        'file': 'assets/images/may%20giat/1794444138758_1267629377072362715_1267629377072362715_b053f23b16cdb2bfd0a99871bee2c6db.jpg',
        'title': 'Vệ sinh máy giặt cửa trên lồng đứng LG',
        'desc': 'Bảo dưỡng định kỳ sạch bong như mới'
    },
    {
        'category': 'may-giat',
        'tag': 'Máy giặt',
        'file': 'assets/images/may%20giat/1794444138787_1267629377072362715_1267629377072362715_37e188e14e7848ca1b461c6562d20e2b.jpg',
        'title': 'Xử lý máy giặt rung lắc mạnh khi vắt tốc độ cao',
        'desc': 'Thay thế thụt giảm xóc và cân chỉnh chân đế'
    },
    {
        'category': 'may-giat',
        'tag': 'Máy giặt',
        'file': 'assets/images/may%20giat/1794444138812_1267629377072362715_1267629377072362715_671005df6b2d4f94913179d46577c9a0.jpg',
        'title': 'Sửa lỗi máy giặt cấp nước liên tục không ngắt',
        'desc': 'Thay phao áp lực nước và van từ chính hãng'
    },
    {
        'category': 'may-giat',
        'tag': 'Máy giặt',
        'file': 'assets/images/may%20giat/1794444138824_1267629377072362715_1267629377072362715_ba2193744871b33db83ef24aaa13742f.jpg',
        'title': 'Bảo dưỡng động cơ truyền động trực tiếp',
        'desc': 'Kiểm tra mâm từ và cảm biến tốc độ Hall'
    },

    # MAY LOC NUOC (5)
    {
        'category': 'may-loc-nuoc',
        'tag': 'Máy lọc nước',
        'file': 'assets/images/may%20loc%20nuoc/1794444002683_1267629377072362715_1267629377072362715_653b247b81cbbd807ab4385a36bc59dc.jpg',
        'title': 'Thay lõi lọc nước RO 1-2-3 định kỳ tại nhà',
        'desc': 'Lõi lọc Kangaroo/Karofi chính hãng có tem cào'
    },
    {
        'category': 'may-loc-nuoc',
        'tag': 'Máy lọc nước',
        'file': 'assets/images/may%20loc%20nuoc/1794444002711_1267629377072362715_1267629377072362715_6f2f187626e32274e2f83c8f1f438c1f.jpg',
        'title': 'Sửa máy lọc nước chảy yếu, nước thải ra nhiều',
        'desc': 'Thay màng thẩm thấu ngược RO và van Flow'
    },
    {
        'category': 'may-loc-nuoc',
        'tag': 'Máy lọc nước',
        'file': 'assets/images/may%20loc%20nuoc/1794444002728_1267629377072362715_1267629377072362715_f5170c2e04597139ada331faf451ffed.jpg',
        'title': 'Sửa máy lọc nước chạy liên tục không ngắt',
        'desc': 'Xử lý van áp cao và van áp thấp ngắt nguồn'
    },
    {
        'category': 'may-loc-nuoc',
        'tag': 'Máy lọc nước',
        'file': 'assets/images/may%20loc%20nuoc/1794444002741_1267629377072362715_1267629377072362715_c8184527690fa674ab85a9fa70dedf41.jpg',
        'title': 'Thay thế bơm tăng áp và cục nguồn Adapter',
        'desc': 'Khôi phục áp lực nước chuẩn 125 PSI'
    },
    {
        'category': 'may-loc-nuoc',
        'tag': 'Máy lọc nước',
        'file': 'assets/images/may%20loc%20nuoc/1794444073319_1267629377072362715_1267629377072362715_c961c05336167c1621ae4c82c243aead.jpg',
        'title': 'Khắc phục rò rỉ nước tại cút nối và vòi lọc',
        'desc': 'Thay gioăng chống tràn và test áp an toàn'
    },

    # BEP TU (5)
    {
        'category': 'bep-tu',
        'tag': 'Bếp từ',
        'file': 'assets/images/bep%20tu/1794444530984_1267629377072362715_1267629377072362715_9a48b6132e60a27cb62f0de48838ee4b.jpg',
        'title': 'Sửa bo mạch công suất bếp từ đôi nhập khẩu',
        'desc': 'Thay cặp IGBT và cầu Diode chính hãng'
    },
    {
        'category': 'bep-tu',
        'tag': 'Bếp từ',
        'file': 'assets/images/bep%20tu/1794444531018_1267629377072362715_1267629377072362715_c1d33f6657f17bab5cdf2a4e4d0e6a45.jpg',
        'title': 'Sửa bếp từ không nhận nồi, kêu tít tít rồi tắt',
        'desc': 'Xử lý mạch nhận nồi và tụ lọc nguồn 5uF'
    },
    {
        'category': 'bep-tu',
        'tag': 'Bếp từ',
        'file': 'assets/images/bep%20tu/1794444531042_1267629377072362715_1267629377072362715_ef0196df175b1459f1b0e1fd07a9ed96.jpg',
        'title': 'Sửa bếp từ báo các mã lỗi E0, E1, E2, E6',
        'desc': 'Đo cảm biến nhiệt đáy nồi và quạt giải nhiệt'
    },
    {
        'category': 'bep-tu',
        'tag': 'Bếp từ',
        'file': 'assets/images/bep%20tu/1794444531056_1267629377072362715_1267629377072362715_0250b6975ac824de1362166d57f835ec.jpg',
        'title': 'Khắc phục bếp từ bị nhảy aptomat khi bật',
        'desc': 'Sửa chập nguồn công suất và vệ sinh bo mạch'
    },
    {
        'category': 'bep-tu',
        'tag': 'Bếp từ',
        'file': 'assets/images/bep%20tu/1794444531066_1267629377072362715_1267629377072362715_233f7b83b02578cdaa9a34d1f94e3738.jpg',
        'title': 'Vệ sinh quạt gió và thay keo tản nhiệt mặt kính',
        'desc': 'Bảo dưỡng bếp từ Bosch, Chefs, Cata'
    }
]

out = []
for i, item in enumerate(data):
    card = f"""          <article class="gallery-card" data-category="{item['category']}">
            <div class="gallery-card__media">
              <img src="{item['file']}" alt="{item['title']}" class="gallery-card__img" loading="lazy">
              <div class="gallery-card__overlay">
                <button type="button" class="gallery-card__zoom-btn" aria-label="Xem ảnh lớn: {item['title']}">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                    <circle cx="11" cy="11" r="8"></circle>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                    <line x1="11" y1="8" x2="11" y2="14"></line>
                    <line x1="8" y1="11" x2="14" y2="11"></line>
                  </svg>
                </button>
              </div>
              <span class="gallery-card__tag">{item['tag']}</span>
            </div>
            <div class="gallery-card__info">
              <h3 class="gallery-card__title">{item['title']}</h3>
              <p class="gallery-card__location">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                  <circle cx="12" cy="10" r="3"></circle>
                </svg>
                <span>{item['desc']}</span>
              </p>
            </div>
          </article>"""
    out.append(card)

html_result = "\n".join(out)
with open('.agents/gallery_cards.html', 'w', encoding='utf-8') as f:
    f.write(html_result)

print("Generated .agents/gallery_cards.html successfully!")
