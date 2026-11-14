with open(r'g:\dien lanh ha noi\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find media queries
media_blocks = re.findall(r'(@media[^{]+\{([\s\S]+?\n\}))\n(?=@media|\Z)', text)
print(f'Total media blocks: {len(media_blocks)}')
for mb, inner in media_blocks:
    header = mb.split('{')[0].strip()
    print('---', header, '---')
    for line in inner.split('\n'):
        if any(k in line for k in ['--fs', '--lh', '--fw', 'font-size', 'line-height', 'font-weight']):
            print('  ', line.strip())
