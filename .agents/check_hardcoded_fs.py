with open(r'g:\dien lanh ha noi\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find any font-size that does NOT use var(--...)
matches = re.findall(r'font-size:\s*([^;]+);', text)
for m in matches:
    if not m.strip().startswith('var('):
        print('Hardcoded or clamp font-size:', m.strip())
