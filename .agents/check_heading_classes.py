import re
from collections import Counter

with open(r'g:\dien lanh ha noi\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'<(h[1-6])[^>]*class="([^"]*)"[^>]*>', text)
c = Counter(matches)
for (tag, cls), count in c.items():
    print(f'<{tag}> class="{cls}": {count}')
