import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove .hero-side { display: none; } from the mobile media query
content = content.replace('.hero-side { display: none; }', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed mobile visibility of .hero-side!")
