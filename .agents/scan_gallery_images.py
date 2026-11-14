import os
from PIL import Image

cats = {
    'dieu hoa': 'Điều hòa',
    'tu lanh': 'Tủ lạnh',
    'may giat': 'Máy giặt',
    'may loc nuoc': 'Máy lọc nước',
    'bep tu': 'Bếp từ'
}

base = 'assets/images'
data = []

for folder, label in cats.items():
    dir_path = os.path.join(base, folder)
    if not os.path.exists(dir_path):
        continue
    files = sorted(os.listdir(dir_path))
    for idx, f in enumerate(files):
        if not f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            continue
        fp = os.path.join(dir_path, f)
        img = Image.open(fp)
        data.append({
            'folder': folder,
            'label': label,
            'filename': f,
            'path': f"assets/images/{folder}/{f}",
            'url_path': f"assets/images/{folder.replace(' ', '%20')}/{f}",
            'width': img.width,
            'height': img.height,
            'aspect': round(img.width / img.height, 2)
        })

print(f"Total images found: {len(data)}")
for d in data[:5]:
    print(d)
