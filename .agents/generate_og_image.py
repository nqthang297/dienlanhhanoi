import os
from PIL import Image, ImageDraw, ImageFont

def create_og_image():
    w, h = 1200, 630
    og = Image.new('RGB', (w, h), (3, 74, 166))
    draw = ImageDraw.Draw(og)

    # Gradient background from deep navy blue to bright royal blue
    for x in range(w):
        ratio = x / w
        r = int(3 * (1 - ratio) + 2 * ratio)
        g = int(58 * (1 - ratio) + 86 * ratio)
        b = int(140 * (1 - ratio) + 196 * ratio)
        draw.line([(x, 0), (x, h)], fill=(r, g, b))

    # Add decorative icy circle pattern in top-left
    draw.ellipse([(-100, -100), (300, 300)], fill=None, outline=(255, 255, 255, 30), width=3)
    draw.ellipse([(-50, -50), (250, 250)], fill=None, outline=(255, 255, 255, 20), width=2)

    # Paste hero banner on the right side if available
    hero_path = 'assets/asset-pack/hero-technician-banner.png'
    if os.path.exists(hero_path):
        hero = Image.open(hero_path).convert('RGBA')
        # Target height = 580, keep aspect ratio
        aspect = hero.width / hero.height
        new_h = 580
        new_w = int(new_h * aspect)
        hero = hero.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        # Position at the right
        paste_x = w - new_w + 50
        paste_y = (h - new_h) // 2 + 20
        og.paste(hero, (paste_x, paste_y), hero)

    # Try to load a nice font or fallback
    font_bold = None
    font_large = None
    font_sub = None
    font_badge = None

    font_paths = [
        "C:\\Windows\\Fonts\\arialbd.ttf",
        "C:\\Windows\\Fonts\\segoeuib.ttf",
        "C:\\Windows\\Fonts\\tahomabd.ttf"
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                font_badge = ImageFont.truetype(fp, 22)
                font_large = ImageFont.truetype(fp, 52)
                font_sub = ImageFont.truetype(fp, 30)
                font_bold = ImageFont.truetype(fp, 36)
                break
            except Exception:
                pass

    if not font_large:
        font_large = ImageFont.load_default()
        font_sub = font_large
        font_badge = font_large
        font_bold = font_large

    # Left content box
    margin_x = 70

    # Badge: HỆ THỐNG ĐIỆN LẠNH UY TÍN HÀ NỘI
    badge_text = "★ HỆ THỐNG ĐIỆN LẠNH UY TÍN HÀ NỘI ★"
    draw.rounded_rectangle([(margin_x, 60), (margin_x + 440, 105)], radius=22, fill=(234, 88, 12))
    draw.text((margin_x + 22, 70), badge_text, fill=(255, 255, 255), font=font_badge)

    # Main Title
    title_line1 = "ĐIỆN LẠNH HÀ NỘI"
    title_line2 = "Sửa Chữa Tại Nhà"
    draw.text((margin_x, 130), title_line1, fill=(255, 255, 255), font=font_large)
    draw.text((margin_x, 195), title_line2, fill=(250, 204, 21), font=font_large)

    # Subtitles / Bullet Points
    bullets = [
        "✓ Có mặt sau 15 - 30 phút tại 12 Quận Hà Nội",
        "✓ Sửa trực tiếp tại nhà - Báo giá trước",
        "✓ Linh kiện chuẩn hãng - Bảo hành 6 - 24 tháng"
    ]
    cur_y = 280
    for b in bullets:
        draw.text((margin_x, cur_y), b, fill=(241, 245, 249), font=font_sub)
        cur_y += 48

    # Hotline box
    cur_y += 20
    draw.rounded_rectangle([(margin_x, cur_y), (margin_x + 480, cur_y + 85)], radius=16, fill=(220, 38, 38))
    draw.text((margin_x + 30, cur_y + 12), "HOTLINE 24/7:", fill=(254, 226, 226), font=font_badge)
    draw.text((margin_x + 30, cur_y + 38), "0962.099.028", fill=(255, 255, 255), font=font_bold)

    og.save('assets/og-image.jpg', 'JPEG', quality=92)
    print("Generated assets/og-image.jpg (1200x630)")

if __name__ == '__main__':
    create_og_image()
