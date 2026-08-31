import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. GSAP start trigger for hero-side fade out
# Find the start: "top 20%" and replace with start: "top top"
content = content.replace('start: "top 20%",\n                end: "bottom top"', 'start: "top top",\n                end: "bottom top"')

# 2. Fix the CTA buttons to stack on mobile and link to WhatsApp
cta_old = """                        <div class="flex flex-wrap gap-3 mt-8">
                            <a class="btn btn-primary" href="#" aria-label="Связаться для расчёта стоимости">Получить расчёт →</a>
                            <a class="btn" style="border:1px solid rgba(255,255,255,.16);color:white;" href="#projects">Сначала посмотреть проекты</a>
                        </div>"""
cta_new = """                        <div class="flex flex-col sm:flex-row gap-3 mt-8 w-full">
                            <a class="btn btn-primary w-full sm:w-auto" href="https://wa.me/70000000000" target="_blank" aria-label="Связаться для расчёта стоимости">Получить расчёт →</a>
                            <a class="btn w-full sm:w-auto" style="border:1px solid rgba(255,255,255,.16);color:white;" href="#projects">Сначала посмотреть проекты</a>
                        </div>"""
content = content.replace(cta_old, cta_new)

# Fix floating button to also go to manager if they want?
floating_old = '<a href="#contact" class="floating-contact">Рассчитать дом →</a>'
floating_new = '<a href="https://wa.me/70000000000" target="_blank" class="floating-contact">Рассчитать дом →</a>'
content = content.replace(floating_old, floating_new)

# 3. Footer mobile optimization
# Add padding-bottom to footer to avoid overlap with floating button
footer_old = 'padding: 22px 0 30px;'
footer_new = 'padding: 22px 0 80px;'
content = content.replace(footer_old, footer_new)

# Also fix footer grid layout spacing for mobile to be less cramped
footer_grid_old = 'gap: 32px; padding-top: 52px;'
footer_grid_new = 'gap: 40px; padding-top: 40px;'
content = content.replace(footer_grid_old, footer_grid_new)

# Make footer titles more visible on mobile
content = content.replace('.footer-title {', '.footer-title { font-size: 13px; color: #a1a79d;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixes applied!")
