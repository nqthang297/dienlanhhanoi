with open(r'g:\dien lanh ha noi\style.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# check lines from line 2340 to end
lines = text.split('\n')
for i, l in enumerate(lines[2340:], 2341):
    # check for hardcoded hex or px not in comments
    clean_line = re.sub(r'/\*.*?\*/', '', l)
    if re.search(r':\s*[^;]*#[0-9a-fA-F]{3,8}', clean_line):
        print(f'Line {i}: hardcoded color: {l}')
    # check for px not in var or comment
    if re.search(r':\s*[^;]*\b\d+px\b', clean_line) and not 'var(' in clean_line:
        print(f'Line {i}: hardcoded px: {l}')
print('Check completed.')
