cats_files = {
    'dieu-hoa': [
        'assets/images/dieu%20hoa/1794444478042_1267629377072362715_1267629377072362715_d93af7abcdfdf6d597298a646eefd554.jpg',
        'assets/images/dieu%20hoa/1794444478072_1267629377072362715_1267629377072362715_5e91222e0380a7673ad1718b3bd10096.jpg',
        'assets/images/dieu%20hoa/1794444478088_1267629377072362715_1267629377072362715_24bb2a8f995dd7e7585f171e4b37067d.jpg',
        'assets/images/dieu%20hoa/1794444478102_1267629377072362715_1267629377072362715_9190a8975b4423ef6a9c3ee16e99d26c.jpg',
        'assets/images/dieu%20hoa/1794444478114_1267629377072362715_1267629377072362715_b48aa1c5f030a6682a4d0cc648bed0e3.jpg',
        'assets/images/dieu%20hoa/1794444478123_1267629377072362715_1267629377072362715_d85f581cda651a7567a0a373508ce5ca.jpg',
        'assets/images/dieu%20hoa/1794444478132_1267629377072362715_1267629377072362715_c32f15bcc0bff006d7314b8677b76e03.jpg'
    ],
    'may-giat': [
        'assets/images/may%20giat/1794443582248_1267629377072362715_1267629377072362715_6232268ff4ac6cc81dba07e557af4c72.jpg',
        'assets/images/may%20giat/1794443582276_1267629377072362715_1267629377072362715_803eab0257e3ac460673212c89fdf2ac.jpg',
        'assets/images/may%20giat/1794443582297_1267629377072362715_1267629377072362715_dc2a2d221139ece5c09e064395a0bf6d.jpg',
        'assets/images/may%20giat/1794443582308_1267629377072362715_1267629377072362715_5e0b3b16aae78c8a4a1a2c383a8b3036.jpg',
        'assets/images/may%20giat/1794444138758_1267629377072362715_1267629377072362715_b053f23b16cdb2bfd0a99871bee2c6db.jpg',
        'assets/images/may%20giat/1794444138787_1267629377072362715_1267629377072362715_37e188e14e7848ca1b461c6562d20e2b.jpg',
        'assets/images/may%20giat/1794444138812_1267629377072362715_1267629377072362715_671005df6b2d4f94913179d46577c9a0.jpg',
        'assets/images/may%20giat/1794444138824_1267629377072362715_1267629377072362715_ba2193744871b33db83ef24aaa13742f.jpg'
    ],
    'tu-lanh': [
        'assets/images/tu%20lanh/1794444204688_1267629377072362715_1267629377072362715_11208d1c492dbbc6a058b9b8dee9d2a4.jpg',
        'assets/images/tu%20lanh/1794444204720_1267629377072362715_1267629377072362715_f648d00c85ebb5f27570f516c1501ead.jpg',
        'assets/images/tu%20lanh/1794444204736_1267629377072362715_1267629377072362715_afabca1a141fd57ba9605a00da2acb27.jpg'
    ],
    'may-loc-nuoc': [
        'assets/images/may%20loc%20nuoc/1794444002683_1267629377072362715_1267629377072362715_653b247b81cbbd807ab4385a36bc59dc.jpg',
        'assets/images/may%20loc%20nuoc/1794444002711_1267629377072362715_1267629377072362715_6f2f187626e32274e2f83c8f1f438c1f.jpg',
        'assets/images/may%20loc%20nuoc/1794444002728_1267629377072362715_1267629377072362715_f5170c2e04597139ada331faf451ffed.jpg',
        'assets/images/may%20loc%20nuoc/1794444002741_1267629377072362715_1267629377072362715_c8184527690fa674ab85a9fa70dedf41.jpg',
        'assets/images/may%20loc%20nuoc/1794444073319_1267629377072362715_1267629377072362715_c961c05336167c1621ae4c82c243aead.jpg'
    ],
    'bep-tu': [
        'assets/images/bep%20tu/1794444530984_1267629377072362715_1267629377072362715_9a48b6132e60a27cb62f0de48838ee4b.jpg',
        'assets/images/bep%20tu/1794444531018_1267629377072362715_1267629377072362715_c1d33f6657f17bab5cdf2a4e4d0e6a45.jpg',
        'assets/images/bep%20tu/1794444531042_1267629377072362715_1267629377072362715_ef0196df175b1459f1b0e1fd07a9ed96.jpg',
        'assets/images/bep%20tu/1794444531056_1267629377072362715_1267629377072362715_0250b6975ac824de1362166d57f835ec.jpg',
        'assets/images/bep%20tu/1794444531066_1267629377072362715_1267629377072362715_233f7b83b02578cdaa9a34d1f94e3738.jpg'
    ]
}

# Round-robin interleave
keys = list(cats_files.keys())
interleaved = []
max_len = max(len(v) for v in cats_files.values())

for i in range(max_len):
    for k in keys:
        if i < len(cats_files[k]):
            interleaved.append((k, cats_files[k][i]))

print(f"Total interleaved: {len(interleaved)}")

out_html = []
for idx, (cat, fpath) in enumerate(interleaved):
    item_html = f"""          <div class="gallery-item" data-category="{cat}">
            <div class="gallery-item__frame">
              <img src="{fpath}" alt="Hình ảnh thực tế dự án Điện Lạnh Hà Nội" class="gallery-item__img" loading="lazy">
              <div class="gallery-item__overlay">
                <span class="gallery-item__zoom-icon" aria-hidden="true">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="15 3 21 3 21 9"></polyline>
                    <polyline points="9 21 3 21 3 15"></polyline>
                    <line x1="21" y1="3" x2="14" y2="10"></line>
                    <line x1="3" y1="21" x2="10" y2="14"></line>
                  </svg>
                </span>
              </div>
            </div>
          </div>"""
    out_html.append(item_html)

with open('.agents/pure_gallery_items.html', 'w', encoding='utf-8') as f:
    f.write("\n".join(out_html))

print("Saved .agents/pure_gallery_items.html successfully!")
