with open(r'g:\dien lanh ha noi\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re

print("=== CHECKING VARIABLES IN :ROOT (DESKTOP) ===")
root_block = re.search(r':root\s*\{([^}]+)\}', text).group(1)
for line in root_block.split('\n'):
    if any(k in line for k in ['--fs-h1:', '--lh-h1:', '--fw-h1:', '--fs-h2:', '--lh-h2:', '--fw-h2:', '--fs-h3:', '--lh-h3:', '--fw-h3:', '--fs-h4:', '--lh-h4:', '--fw-h4:', '--fs-p:', '--lh-p:', '--fw-p:']):
        print(' ', line.strip())

print("\n=== CHECKING VARIABLES IN @media (max-width: 1024px) (TABLET) ===")
tablet_block = re.search(r'@media\s*\(max-width:\s*1024px\)\s*\{([^}]+:root\s*\{[^}]+\})', text, re.DOTALL)
if tablet_block:
    for line in tablet_block.group(0).split('\n'):
        if any(k in line for k in ['--fs-', '--lh-', '--fw-']):
            print(' ', line.strip())

print("\n=== CHECKING VARIABLES IN @media (max-width: 768px) (MOBILE) ===")
mobile_block = re.search(r'@media\s*\(max-width:\s*768px\)\s*\{([^}]+:root\s*\{[^}]+\})', text, re.DOTALL)
if mobile_block:
    for line in mobile_block.group(0).split('\n'):
        if any(k in line for k in ['--fs-', '--lh-', '--fw-']):
            print(' ', line.strip())

print("\n=== VERIFYING CSS SELECTOR INTEGRITY ===")
key_selectors = [
    'h1', 'h2', 'h3', 'h4', 'body', 'p',
    '.hero-section__title', '.section-title', '.process-section .section-title',
    '.branches-section__title', '.commitment-card__title', '.service-card__title',
    '.process-card__title', '.offer-card__title', '.branch-card__name', '.faq-item__question'
]
for sel in key_selectors:
    m = re.search(r'(^|\n)(' + re.escape(sel) + r')\s*\{([^}]+)\}', text)
    if m:
        props = [p.strip() for p in m.group(3).split(';') if any(k in p for k in ['font-size', 'line-height', 'font-weight'])]
        print(f'{sel} -> {", ".join(props)}')
    else:
        print(f'WARNING: {sel} NOT FOUND')
