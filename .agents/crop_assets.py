import os
from PIL import Image, ImageDraw

OUT_DIR = r"g:\dien lanh ha noi\assets\images\lp"
os.makedirs(OUT_DIR, exist_ok=True)

IMG1 = r"C:/Users/quyth/.gemini/antigravity/brain/a07a83d3-6de9-4fbe-b082-a4fb47097c96/.user_uploaded/media_1794528630398_2f384aa8.jpg"
IMG2 = r"C:/Users/quyth/.gemini/antigravity/brain/a07a83d3-6de9-4fbe-b082-a4fb47097c96/.user_uploaded/media_1794528630382_39935ca0.jpg"
IMG3 = r"C:/Users/quyth/.gemini/antigravity/brain/a07a83d3-6de9-4fbe-b082-a4fb47097c96/.user_uploaded/media_1794528630424_0b1912bd.jpg"

im1 = Image.open(IMG1) # 682 x 1024
im2 = Image.open(IMG2) # 724 x 1024
im3 = Image.open(IMG3) # 724 x 1024

crops_1 = {
    "hero-illustration.jpg": (328, 38, 676, 336),
    "commit-tech.jpg": (0, 392, 206, 598),
    "srv-1.jpg": (24, 714, 162, 751),
    "srv-2.jpg": (189, 714, 327, 751),
    "srv-3.jpg": (354, 714, 493, 751),
    "srv-4.jpg": (520, 714, 658, 751),
    "srv-5.jpg": (36, 888, 90, 932),
    "srv-6.jpg": (260, 888, 314, 932),
    "srv-7.jpg": (494, 888, 540, 932),
}

for name, box in crops_1.items():
    im1.crop(box).save(os.path.join(OUT_DIR, name), quality=95)

crops_2 = {
    "step-1.jpg": (76, 728, 198, 796),
    "step-2.jpg": (285, 732, 438, 794),
    "step-3.jpg": (545, 725, 676, 796),
    "step-4.jpg": (64, 922, 212, 996),
    "step-5.jpg": (288, 920, 438, 994),
    "step-6.jpg": (518, 916, 686, 996),
}

for name, box in crops_2.items():
    im2.crop(box).save(os.path.join(OUT_DIR, name), quality=95)

offer_tech = im3.crop((0, 72, 162, 385)).copy()
draw_ot = ImageDraw.Draw(offer_tech)
bg_top = offer_tech.getpixel((120, 8))
draw_ot.rectangle([125, 0, 162, 25], fill=bg_top)
bg_bot = offer_tech.getpixel((145, 265))
draw_ot.rectangle([135, 270, 162, 313], fill=bg_bot)
offer_tech.save(os.path.join(OUT_DIR, "offer-tech.jpg"), quality=95)

crops_3 = {
    "offer-icon-1.jpg": (175, 98, 256, 200),
    "offer-icon-2.jpg": (440, 98, 535, 204),
    "offer-icon-3.jpg": (175, 224, 256, 326),
    "offer-icon-4.jpg": (440, 222, 548, 324),
    "rev-avatar-1.jpg": (34, 647, 79, 694),
    "rev-avatar-2.jpg": (258, 647, 304, 694),
    "rev-avatar-3.jpg": (484, 647, 530, 694),
    "hq-building.jpg": (18, 822, 206, 945),
}

for name, box in crops_3.items():
    im3.crop(box).save(os.path.join(OUT_DIR, name), quality=95)

print("Clean crops saved.")
