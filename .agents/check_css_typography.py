with open(r'g:\dien lanh ha noi\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find all selectors matching h1-h4, section-title, card titles, p, body
selectors_to_check = [
    'h1', 'h2', 'h3', 'h4', 'body', 'p',
    '.hero-section__title', '.section-title', '.branches-section__title',
    '.commitment-card__title', '.service-card__title', '.process-card__title',
    '.offer-card__title', '.faq-item__question', '.branch-card__name'
]

matches = re.findall(r'([^{}]+)\{([^}]+)\}', text)
for sel, body in matches:
    clean_sel = ' '.join(sel.split())
    for target in selectors_to_check:
        if re.search(r'(^|[,\s>+~])' + re.escape(target) + r'($|[,\s>+~.:])', clean_sel):
            # print font properties
            fonts = [line.strip() for line in body.split(';') if any(k in line for k in ['font-size', 'line-height', 'font-weight'])]
            if fonts:
                print(f'{clean_sel}:')
                for fprop in fonts:
                    print(f'   {fprop}')
