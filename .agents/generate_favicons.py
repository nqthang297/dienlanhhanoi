import os
import math
from PIL import Image, ImageDraw

def create_favicon_png(size, filename):
    # Create RGBA image with blue gradient rounded rect and snowflake
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Scale factor
    scale = size / 64.0
    corner_radius = int(14 * scale)

    # Draw rounded background with gradient approximation (blue #0356c7)
    # Background color: royal blue #0256c4 to #013b8e
    for y in range(size):
        ratio = y / size
        r = int(2 * (1 - ratio) + 1 * ratio)
        g = int(86 * (1 - ratio) + 59 * ratio)
        b = int(196 * (1 - ratio) + 142 * ratio)
        draw.line([(0, y), (size, y)], fill=(r, g, b, 255))

    # Mask for rounded corners
    mask = Image.new('L', (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([(0, 0), (size - 1, size - 1)], radius=corner_radius, fill=255)
    
    # Apply mask to background
    bg = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    bg.paste(img, (0, 0), mask)

    # Draw snowflake lines
    fg = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    fg_draw = ImageDraw.Draw(fg)
    center = size / 2.0
    
    # 8-arm snowflake
    arm_len = 22.0 * scale
    branch_len = 5.5 * scale
    branch_pos = 14.0 * scale
    line_w = max(1, int(round(2.6 * scale)))

    for angle_deg in [0, 45, 90, 135, 180, 225, 270, 315]:
        rad = math.radians(angle_deg)
        x2 = center + arm_len * math.cos(rad)
        y2 = center + arm_len * math.sin(rad)
        fg_draw.line([(center, center), (x2, y2)], fill=(255, 255, 255, 255), width=line_w)

        # Draw branches (v-chevrons)
        bx = center + branch_pos * math.cos(rad)
        by = center + branch_pos * math.sin(rad)
        for offset in [-45, 45]:
            brad = math.radians(angle_deg + 180 + offset)
            cx = bx + branch_len * math.cos(brad)
            cy = by + branch_len * math.sin(brad)
            fg_draw.line([(bx, by), (cx, cy)], fill=(255, 255, 255, 255), width=line_w)

    final_img = Image.alpha_composite(bg, fg)
    final_img.save(filename, 'PNG')
    print(f"Generated {filename} ({size}x{size})")

def main():
    os.makedirs('assets', exist_ok=True)
    create_favicon_png(16, 'assets/favicon-16x16.png')
    create_favicon_png(32, 'assets/favicon-32x32.png')
    create_favicon_png(48, 'assets/favicon-48x48.png')
    create_favicon_png(180, 'assets/apple-touch-icon.png')
    create_favicon_png(192, 'assets/android-chrome-192x192.png')
    create_favicon_png(512, 'assets/android-chrome-512x512.png')

    # Also save favicon.ico with multi-resolution
    img16 = Image.open('assets/favicon-16x16.png')
    img32 = Image.open('assets/favicon-32x32.png')
    img48 = Image.open('assets/favicon-48x48.png')
    img32.save('favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
    img32.save('assets/favicon.ico', format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
    print("Generated favicon.ico in root and assets/")

if __name__ == '__main__':
    main()
