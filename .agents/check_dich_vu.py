import os
import re

with open(r'g:\dien lanh ha noi\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('id="dich-vu"')
end = text.find('</section>', start)
section_content = text[start:end]

print("--- Check 'Xem chi tiết' button ---")
print("Occurrences of 'Xem chi tiết':", section_content.count('Xem chi tiết'))
print("Occurrences of 'btn-service-detail':", section_content.count('btn-service-detail'))

print("\n--- Check Images in Section 3 ---")
imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*alt=["\']([^"\']*)["\']', section_content)
for src, alt in imgs:
    exists = os.path.exists(os.path.join(r'g:\dien lanh ha noi', src))
    print(f"Alt: '{alt}' | Src: '{src}' | Exists: {exists}")
