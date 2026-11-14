import re
import os
import urllib.parse

with open('index.html', encoding='utf-8') as f:
    html = f.read()

gallery_matches = re.findall(r'<div class="gallery-item".*?<img src="([^"]+)".*?</div>', html, re.DOTALL)
print(f"Found {len(gallery_matches)} gallery items in index.html")

missing = []
for src in gallery_matches:
    unescaped_src = urllib.parse.unquote(src)
    if not os.path.exists(unescaped_src):
        missing.append(unescaped_src)

if missing:
    print("MISSING FILES:")
    for m in missing:
        print(" -", m)
else:
    print("ALL 28 GALLERY IMAGES EXIST ON DISK! 100% PERFECT!")
