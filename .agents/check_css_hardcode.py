import re

with open('style.css', encoding='utf-8') as f:
    lines = f.readlines()

in_root = True
hardcoded = []

for idx, line in enumerate(lines, 1):
    stripped = line.strip()
    if ':root' in stripped:
        in_root = True
    if in_root and stripped == '}':
        in_root = False
        continue

    if not in_root:
        # Check for #hex or rgb( not inside comments or var()
        # ignore comments
        clean = re.sub(r'/\*.*?\*/', '', stripped)
        # Check for #hex
        hex_matches = re.findall(r'#[0-9a-fA-F]{3,8}', clean)
        # Check for rgb or rgba
        rgba_matches = re.findall(r'rgba?\(', clean)
        if hex_matches or rgba_matches:
            hardcoded.append((idx, line.strip()))

if hardcoded:
    print(f"Found {len(hardcoded)} potential hardcoded lines outside :root:")
    for lno, text in hardcoded[:10]:
        print(f"Line {lno}: {text}")
else:
    print("NO hardcoded colors outside :root found! 100% compliant with CSS variables!")
