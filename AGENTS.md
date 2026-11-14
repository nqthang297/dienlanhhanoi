AGENTS.md — Quy định dự án
==========================

Nội dung
--------

* Tuyệt đối không thêm, sửa, xóa bất kỳ nội dung/section nào. Chỉ thực hiện khi có yêu cầu rõ ràng từ user.

Cấu trúc file & folder
----------------------

* Root folder chỉ chứa các file cần thiết để landing page chạy được (HTML/CSS/JS/assets).
* Mọi file hỗ trợ quá trình làm việc của agent (ghi chú, bản nháp, tài liệu tạm...) lưu trong 1 folder riêng — không rải rác ở root hay nơi khác.
* THƯ MỤC HỖ TRỢ BẮT BUỘC: Mọi file phục vụ quá trình làm việc của agent (script cào dữ liệu, ghi chú, bản nháp, tài liệu tạm, test script...) BẮT BUỘC phải lưu trong thư mục: `.agents/` (nằm ngay bên trong project). TUYỆT ĐỐI KHÔNG lưu file ra ngoài phạm vi project (cấm lưu vào các thư mục hệ thống như `tmp`, `.gemini`, `brain`, `appDataDir`)
* Thêm/sửa/xóa các file hỗ trợ chỉ thực hiện trong folder này, không tác động ra ngoài.
* NGUYÊN TẮC BẮT BUỘC: Tuyệt đối KHÔNG ĐƯỢC PHÉP xóa bất kì file hay folder nào nằm ngoài folder dự án

Công nghệ
---------

* HTML, CSS, JavaScript thuần

CSS
---

* Sửa giao diện tại source of truth/root cause, không vá bằng override hay `!important`. Chỉ tạo class/variant riêng hoặc dùng `!important` khi người dùng yêu cầu và cần áp dụng cục bộ, không ảnh hưởng phần tử khác.
* Khi sửa giao diện: nếu thay đổi cần áp dụng cho toàn bộ những nơi đang dùng chung 1 giá trị, sửa tại CSS variable. Nếu user chỉ muốn sửa riêng cho 1 phần tử cụ thể, sửa tại class riêng của phần tử đó (tạo class/variant riêng nếu class hiện tại đang dùng chung cho nhiều phần tử khác).
* Cấm hardcode: không viết trực tiếp mã màu (#hex, rgb), số đo tùy ý, font-size lẻ... trong class/id — mọi giá trị phải gọi qua `var(--ten-bien)`.
* Trước khi tạo biến mới, kiểm tra biến tương ứng đã có trong `:root` chưa và tái sử dụng, tránh trùng lặp.
* Class và CSS variable đặt tên rõ nghĩa (BEM hoặc semantic), không đặt tên mơ hồ.

## YÊU CẦU TUÂN THỦ:

- Khi đang sửa landing page nào thì thì tuyệt tối không được để không ảnh hưởng tới trang chủ và các landing page khác
1. **Phân cấp thị giác**
   
   - Tiêu đề chính (h1, h2) lớn/nổi bật rõ rệt hơn tiêu đề phụ và nội dung chi tiết
   - Từ khóa/số liệu quan trọng cần bôi đậm hoặc tăng font-size
   - CTA chính dùng màu tương phản cao nhất so với nền
   - Text phụ (subtitle, caption) nên giảm độ nổi bật (giảm opacity)
   - Cần có giải pháp để làm nổi bật các chữ quan trọng trong tiêu đề hoặc trong nội dung bằng các cách khác nhau, ví dụ: Underline decoration, Tăng weight, Background highlight, Badge/Pill bao quanh...

2. **Nhịp điệu bố cục**
   
   - Không dùng cùng 1 kiểu layout cho 3 section liên tiếp
   - Đan xen khối "dày" (Bento Grid, Mosaic Grid, Multi-column Card) với khối "thoáng" (Hero tối giản, Split 2 cột rộng, Center 1 cột)
   - Kết hợp linh hoạt các bố cục section, linh hoạt các loại card gird, sử dụng có section sử dụng ảnh, có section sử dụng icon

3. **Zig-zag layout**
   
   - Các section dạng Split (chữ – ảnh) liên tiếp hoặc gần nhau bắt buộc phải đảo vị trí chữ/ảnh qua lại giữa các section

4. **Mẫu quét mắt người dùng**
   
   - Z-pattern cho Hero: logo trái trên, CTA phụ/menu phải trên, tiêu đề + CTA chính ở giữa/dưới
   - F-pattern cho phần nhiều chữ: thông tin quan trọng ở góc trái trên, bullet rõ ràng ở mép trái

5. **Đa dạng background section** — không nhất thiết dùng hết tất cả các loại, nhưng cần phối hợp nhiều loại khác nhau và không dùng cùng loại nền ở 3 section liên tiếp
   
   - Solid Color — màu đặc, phẳng: dùng cho section thông thường, cần sự rõ ràng, tối giản
   - Gradient Linear — chuyển màu theo đường thẳng (ngang/dọc/chéo): dùng cho Hero, CTA, section cần năng lượng, chuyển động
   - Gradient Radial — chuyển màu từ tâm ra ngoài: dùng cho Hero, hiệu ứng spotlight, tạo điểm nhấn trung tâm
   - Gradient Mesh — nhiều điểm màu pha trộn phức tạp: dùng cho Hero cao cấp, creative/agency, section cần visual mạnh
   - SVG Shape / Blob — hình hữu cơ bất đối xứng trang trí: dùng cho Hero, CTA, điểm nhấn không cần ảnh
   - Geometric Pattern — pattern lặp hình học (grid, dot, line, triangle): dùng cho section cần texture nhẹ, tránh flat design đơn điệu
   - Noise / Grain Texture — texture hạt mịn phủ nền: dùng khi cần cảm giác thủ công, ấm áp, cao cấp
   - Image Background — ảnh thật làm nền, thường kèm overlay bán trong suốt: dùng cho Hero full-width, section cần cảm xúc mạnh
   - Video Background — video loop làm nền: dùng cho Hero sản phẩm/dịch vụ cần demo trực quan
   - Glass / Frosted — nền mờ trong suốt (backdrop-filter blur): dùng cho card nổi trên ảnh, modal, floating element
   - Dark Overlay — lớp màu tối phủ lên ảnh/video (40–70% opacity): dùng khi cần đảm bảo text dễ đọc trên nền ảnh/video

6. **Quy định về icon:** Dùng một bộ thư viện icon SVG phẳng, tối giản và đồng bộ (ví dụ như Lucide Icons, Hugeicons, Font Awesome)
