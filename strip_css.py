import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the hardcoded mobile paddings that override Tailwind
content = content.replace('.cta { padding: 34px 24px; border-radius: 26px; }', '')
content = content.replace('.footer-grid { grid-template-columns: 1fr; gap: 40px; padding-top: 40px; }', '')
content = content.replace('.footer-grid { grid-template-columns: 1fr 1fr; }', '')
content = content.replace('padding: 70px 0 45px;', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Stripped problematic CSS!")
