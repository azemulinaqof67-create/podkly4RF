import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up CTA section and make it use pure Tailwind for layout to avoid any overflow/cropping
cta_old = 'class="cta glass-dark" style="background: rgba(17,20,17,.68); backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px); border: 1px solid rgba(255,255,255,.16);"'
cta_new = 'class="cta glass-dark w-full max-w-full overflow-hidden rounded-[26px] p-6 sm:p-8 md:p-14" style="background: rgba(17,20,17,.68); backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px); border: 1px solid rgba(255,255,255,.16);"'
content = content.replace(cta_old, cta_new)

# 2. Fix the CTA content max-width to not overflow
form_old = 'class="mt-8 flex flex-col gap-4 w-full max-w-md"'
form_new = 'class="mt-8 flex flex-col gap-4 w-full sm:max-w-md mx-auto"'
content = content.replace(form_old, form_new)

# 3. Clean up the Footer Grid to ensure it's visible and doesn't have missing columns
footer_grid_html_old = '<div class="footer-grid">'
footer_grid_html_new = '<div class="grid grid-cols-1 md:grid-cols-3 gap-10 pt-10 pb-8">'
content = content.replace(footer_grid_html_old, footer_grid_html_new)

# Make footer-title text brighter so it's not invisible on dark bg
content = content.replace('.footer-title { font-size: 13px; color: #a1a79d;', '.footer-title { font-size: 13px; color: #ffffff;')

# Fix footer-muted text colors just in case
content = content.replace('class="footer-muted max-w-sm mt-4"', 'class="footer-muted max-w-sm mt-4 text-gray-400"')
content = content.replace('class="footer-muted mt-3"', 'class="footer-muted mt-3 text-gray-400"')

# Ensure footer bottom is visible
content = content.replace('class="footer-bottom"', 'class="footer-bottom flex flex-col md:flex-row justify-between gap-4 pt-6 border-t border-white/10 text-gray-500 text-xs pb-24"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed layout bugs!")
