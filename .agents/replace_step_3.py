import os
from PIL import Image

src_path = 'C:/Users/quyth/.gemini/antigravity/brain/40163d84-5334-4e65-be0b-989343542a7f/.user_uploaded/media_1794634267817_83fefa92.png'
dest_path = 'assets/asset-pack/composite_step_3.png'
dest_orig = 'assets/asset-pack/step-3-bao-gia-original.png'

# Open uploaded image
img = Image.open(src_path).convert('RGBA')

# Save original copy in asset-pack
img.save(dest_orig, 'PNG')
print(f"Saved original image to {dest_orig} ({img.size})")

# Crop tight bounding box
bbox = img.getbbox()
cropped = img.crop(bbox)

# Create 400x200 canvas (matching other composite_step_*.png)
canvas_w, canvas_h = 400, 200
canvas = Image.new('RGBA', (canvas_w, canvas_h), (0, 0, 0, 0))

# Target height ~ 180 to fit harmoniously with step 1, 2, 4, 5, 6
target_h = 180
target_w = int(cropped.width * (target_h / cropped.height))

# In case target_w > canvas_w - 20, scale down proportionally
if target_w > canvas_w - 20:
    target_w = canvas_w - 20
    target_h = int(cropped.height * (target_w / cropped.width))

resized = cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)

# Center on canvas
paste_x = (canvas_w - target_w) // 2
paste_y = (canvas_h - target_h) // 2
canvas.paste(resized, (paste_x, paste_y), resized)

# Save to composite_step_3.png
canvas.save(dest_path, 'PNG')
print(f"Successfully updated {dest_path} with 400x200 composite (target size: {target_w}x{target_h})")
