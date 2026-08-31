import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update footer CSS to have webkit backdrop filter
content = content.replace(
    'footer { background: rgba(17,20,17,.68); backdrop-filter: blur(18px); color: white; border-top: 1px solid rgba(255,255,255,0.1); }',
    'footer { background: rgba(17,20,17,.68); backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px); color: white; border-top: 1px solid rgba(255,255,255,0.1); }'
)

# Hide CTA before element on mobile
mobile_css_old = '@media (max-width: 640px) {'
mobile_css_new = '''@media (max-width: 640px) {
            .cta::before { display: none; }'''
content = content.replace(mobile_css_old, mobile_css_new)

# 2. Replace CTA content with a Form
cta_old = """                        <div class="flex flex-col sm:flex-row gap-3 mt-8 w-full">
                            <a class="btn btn-primary w-full sm:w-auto" href="https://wa.me/70000000000" target="_blank" aria-label="Связаться для расчёта стоимости">Получить расчёт →</a>
                            <a class="btn w-full sm:w-auto" style="border:1px solid rgba(255,255,255,.16);color:white;" href="#projects">Сначала посмотреть проекты</a>
                        </div>"""

cta_form = """                        <form id="calc-form" class="mt-8 flex flex-col gap-4 w-full max-w-md" onsubmit="event.preventDefault(); alert('Заявка отправлена!');">
                            <div>
                                <input type="text" placeholder="Ваше имя" required class="w-full bg-black/40 border border-white/20 rounded-2xl px-5 py-4 text-white placeholder-gray-400 focus:outline-none focus:border-white/50 transition-colors">
                            </div>
                            <div>
                                <input type="tel" id="phone-input" placeholder="+7 (999) 999-99-99" required class="w-full bg-black/40 border border-white/20 rounded-2xl px-5 py-4 text-white placeholder-gray-400 focus:outline-none focus:border-white/50 transition-colors">
                            </div>
                            <button type="submit" class="btn btn-primary w-full mt-2" aria-label="Связаться для расчёта стоимости">Получить расчёт →</button>
                            <p class="text-[11px] text-gray-500 text-center mt-2">Нажимая кнопку, вы соглашаетесь с политикой конфиденциальности.</p>
                        </form>
                        
                        <script src="https://unpkg.com/imask"></script>
                        <script>
                            document.addEventListener('DOMContentLoaded', () => {
                                const phoneInput = document.getElementById('phone-input');
                                IMask(phoneInput, {
                                    mask: '+{7} (000) 000-00-00'
                                });
                            });
                        </script>"""
content = content.replace(cta_old, cta_form)

# 3. Floating button link to #contact so it scrolls to the form
floating_old = '<a href="https://wa.me/70000000000" target="_blank" class="floating-contact">Рассчитать дом →</a>'
floating_new = '<a href="#contact" class="floating-contact">Рассчитать дом →</a>'
content = content.replace(floating_old, floating_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Form and footer updated!")
