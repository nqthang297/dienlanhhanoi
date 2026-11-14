with open(r'g:\dien lanh ha noi\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# find services section
start = text.find('services-section')
end = text.find('</section>', start)
services_html = text[start:end]

cards = re.findall(r'<div class="service-card[^"]*">([\s\S]+?)</div>\s*<!-- \/service-card -->', services_html)
print(f'Service cards: {len(cards)}')
for c in cards:
    title = re.search(r'<h3[^>]*>(.*?)</h3>', c)
    svg = re.search(r'<svg[^>]*>([\s\S]+?)</svg>', c)
    t_text = title.group(1).strip() if title else 'No title'
    svg_paths = svg.group(1).strip() if svg else 'No svg'
    print('Title:', t_text)
    print('SVG paths:', svg_paths[:120])
    print('---')
