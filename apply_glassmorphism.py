import re

with open('index-redesign.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
css_updates = {
    # Remove background from body to ensure it's transparent over canvas if needed, but hero-shade handles it
    'background: var(--paper);': 'background: transparent;',
    
    # Stat-strip
    '.stat-strip {\n            display: grid;\n            grid-template-columns: repeat(4, 1fr);\n            border-top: 1px solid var(--line);\n            border-bottom: 1px solid var(--line);\n        }': 
    '.stat-strip {\n            display: grid;\n            grid-template-columns: repeat(4, 1fr);\n            gap: 16px;\n        }',
    
    '.stat {\n            padding: 34px 24px;\n            border-right: 1px solid var(--line);\n        }':
    '.stat {\n            padding: 34px 24px;\n            background: rgba(17,20,17,.68);\n            border: 1px solid rgba(255,255,255,.16);\n            border-radius: 24px;\n            backdrop-filter: blur(18px);\n            -webkit-backdrop-filter: blur(18px);\n        }',
    
    '.stat:last-child { border-right: 0; }': '',
    
    '.stat b {\n            display: block;\n            font-family: \'Space Grotesk\', sans-serif;\n            font-size: 42px;\n            letter-spacing: -.05em;\n        }':
    '.stat b {\n            display: block;\n            font-family: \'Space Grotesk\', sans-serif;\n            font-size: 42px;\n            letter-spacing: -.05em;\n            color: white;\n        }',
    
    '.stat span { color: var(--muted); font-size: 13px; line-height: 1.4; }':
    '.stat span { color: rgba(255,255,255,0.7); font-size: 13px; line-height: 1.4; }',
    
    # Dark section transparent
    '.dark-section {\n            background: #171916;\n            color: #f7f7f2;\n        }':
    '.dark-section {\n            background: transparent;\n            color: #f7f7f2;\n        }',
    
    # Process item transparent
    '.process-item {\n            min-height: 260px;\n            padding: 30px;\n            background: #1d201c;\n            position: relative;\n        }':
    '.process-item {\n            min-height: 260px;\n            padding: 30px;\n            background: transparent;\n            border-right: 1px solid rgba(255,255,255,0.1);\n            position: relative;\n        }',
    
    '.process-item p { margin: 0; color: #9ca29a; font-size: 14px; line-height: 1.55; }':
    '.process-item p { margin: 0; color: rgba(255,255,255,0.7); font-size: 14px; line-height: 1.55; }',
    
    '.process-item h3 { margin: 55px 0 10px; font-size: 21px; }':
    '.process-item h3 { margin: 55px 0 10px; font-size: 21px; color: white; }',
    
    # Features
    '.feature {\n            display: grid;\n            grid-template-columns: 44px 1fr;\n            gap: 14px;\n            padding: 17px 0;\n            border-top: 1px solid var(--line);\n        }':
    '.feature {\n            display: grid;\n            grid-template-columns: 44px 1fr;\n            gap: 14px;\n            padding: 17px 0;\n            border-top: 1px solid rgba(255,255,255,0.1);\n        }',
    
    '.feature:last-child { border-bottom: 1px solid var(--line); }':
    '.feature:last-child { border-bottom: 1px solid rgba(255,255,255,0.1); }',
    
    '.feature b { display: block; margin-bottom: 4px; }':
    '.feature b { display: block; margin-bottom: 4px; color: white; }',
    
    '.feature span { color: var(--muted); font-size: 13px; line-height: 1.45; }':
    '.feature span { color: rgba(255,255,255,0.7); font-size: 13px; line-height: 1.45; }',
    
    # FAQ details
    'details {\n            border-top: 1px solid var(--line);\n            padding: 22px 0;\n        }':
    'details {\n            border-top: 1px solid rgba(255,255,255,0.1);\n            padding: 22px 0;\n        }',
    
    'details:last-child { border-bottom: 1px solid var(--line); }':
    'details:last-child { border-bottom: 1px solid rgba(255,255,255,0.1); }',
    
    'summary {\n            cursor: pointer;\n            list-style: none;\n            font-weight: 800;\n            display: flex;\n            align-items: center;\n            justify-content: space-between;\n            gap: 20px;\n        }':
    'summary {\n            cursor: pointer;\n            list-style: none;\n            font-weight: 800;\n            display: flex;\n            align-items: center;\n            justify-content: space-between;\n            gap: 20px;\n            color: white;\n        }',
    
    'details p { color: var(--muted); line-height: 1.6; max-width: 720px; margin: 14px 0 0; }':
    'details p { color: rgba(255,255,255,0.7); line-height: 1.6; max-width: 720px; margin: 14px 0 0; }',
    
    # Footer
    'footer { background: #11130f; color: white; }':
    'footer { background: rgba(17,20,17,.68); backdrop-filter: blur(18px); color: white; border-top: 1px solid rgba(255,255,255,0.1); }',
    
    # Extra CSS class for glass wrapper
    '.glass-dark {': '.glass-wrapper {\n            background: rgba(17,20,17,.68);\n            border: 1px solid rgba(255,255,255,.16);\n            backdrop-filter: blur(18px);\n            -webkit-backdrop-filter: blur(18px);\n            border-radius: 36px;\n            padding: 40px;\n            color: white;\n        }\n        .glass-dark {'
}

for old, new in css_updates.items():
    content = content.replace(old, new)

# 2. Update HTML Structure

# Projects Title Wrapper
projects_old = """                <div class="flex flex-col md:flex-row md:items-end md:justify-between gap-8 mb-12">
                    <div>
                        <div class="eyebrow">Проекты</div>
                        <h2 class="display text-5xl md:text-6xl font-bold tracking-tight mt-5 mb-4">Дома, в которых<br>хочется остаться.</h2>
                    </div>
                    <p class="max-w-md text-gray-500 leading-relaxed">
                        Не ограничиваемся одним шаблоном. Подбираем архитектуру,
                        площадь и планировку под участок, бюджет и сценарий жизни.
                    </p>
                </div>"""
projects_new = """                <div class="glass-wrapper mb-12">
                    <div class="flex flex-col md:flex-row md:items-end md:justify-between gap-8">
                        <div>
                            <div class="eyebrow" style="color: white;">Проекты</div>
                            <h2 class="display text-5xl md:text-6xl font-bold tracking-tight mt-5 mb-4 text-white">Дома, в которых<br>хочется остаться.</h2>
                        </div>
                        <p class="max-w-md text-gray-300 leading-relaxed">
                            Не ограничиваемся одним шаблоном. Подбираем архитектуру,
                            площадь и планировку под участок, бюджет и сценарий жизни.
                        </p>
                    </div>
                </div>"""
content = content.replace(projects_old, projects_new)

# Process Section Wrapper
process_old = """                <div class="mb-12">
                    <div class="eyebrow">Как всё происходит</div>
                    <h2 class="display text-5xl md:text-6xl font-bold tracking-tight mt-5">Понятно от первого<br>звонка до ключей.</h2>
                </div>"""
process_new = """                <div class="glass-wrapper mb-12">
                    <div class="eyebrow" style="color: white;">Как всё происходит</div>
                    <h2 class="display text-5xl md:text-6xl font-bold tracking-tight mt-5 text-white">Понятно от первого<br>звонка до ключей.</h2>
                </div>"""
content = content.replace(process_old, process_new)

# Material Section Wrapper
material_old = """        <section class="section">
            <div class="container split">
                <div class="material-visual">
                    <div class="material-badge">
                        <strong>Дерево — основа.</strong>
                        <span>Сухая строганая доска камерной сушки — один из ключевых материалов, заявленных в текущем проекте.</span>
                    </div>
                </div>

                <div>
                    <div class="eyebrow">Материалы и контроль</div>
                    <h2 class="display text-5xl md:text-6xl font-bold tracking-tight mt-5 mb-6">Когда качество<br>видно в деталях.</h2>
                    <p class="text-gray-500 text-lg leading-relaxed">
                        Хороший каркас начинается не с красивого фасада, а с того,
                        что остаётся внутри стен. Поэтому отдельно рассказываем
                        о древесине, защите и точности сборки.
                    </p>"""
material_new = """        <section class="section">
            <div class="container glass-wrapper split" style="padding: 40px;">
                <div class="material-visual">
                    <div class="material-badge">
                        <strong>Дерево — основа.</strong>
                        <span>Сухая строганая доска камерной сушки — один из ключевых материалов, заявленных в текущем проекте.</span>
                    </div>
                </div>

                <div>
                    <div class="eyebrow" style="color: white;">Материалы и контроль</div>
                    <h2 class="display text-5xl md:text-6xl font-bold tracking-tight mt-5 mb-6 text-white">Когда качество<br>видно в деталях.</h2>
                    <p class="text-gray-300 text-lg leading-relaxed">
                        Хороший каркас начинается не с красивого фасада, а с того,
                        что остаётся внутри стен. Поэтому отдельно рассказываем
                        о древесине, защите и точности сборки.
                    </p>"""
content = content.replace(material_old, material_new)

# FAQ Section Wrapper
faq_old = """        <section class="section" style="padding-top:45px;">
            <div class="container">
                <div class="faq-grid">
                    <div>
                        <div class="eyebrow">Вопросы</div>
                        <h2 class="display text-5xl font-bold tracking-tight mt-5 mb-5">Без мелкого<br>шрифта.</h2>
                        <p class="text-gray-500 leading-relaxed max-w-md">
                            Собрал здесь вопросы, которые логично закрыть до первого
                            разговора. Цены и комплектации лучше считать под конкретный проект.
                        </p>
                    </div>
                    <div>"""
faq_new = """        <section class="section" style="padding-top:45px;">
            <div class="container glass-wrapper" style="padding: 40px;">
                <div class="faq-grid">
                    <div>
                        <div class="eyebrow" style="color: white;">Вопросы</div>
                        <h2 class="display text-5xl font-bold tracking-tight mt-5 mb-5 text-white">Без мелкого<br>шрифта.</h2>
                        <p class="text-gray-300 leading-relaxed max-w-md">
                            Собрал здесь вопросы, которые логично закрыть до первого
                            разговора. Цены и комплектации лучше считать под конкретный проект.
                        </p>
                    </div>
                    <div>"""
content = content.replace(faq_old, faq_new)

# Contact CTA
cta_old = """        <section id="contact" class="section" style="padding-top:45px;padding-bottom:90px;">
            <div class="container">
                <div class="cta">
                    <div class="cta-content">
                        <div class="eyebrow">Следующий шаг</div>"""
cta_new = """        <section id="contact" class="section" style="padding-top:45px;padding-bottom:90px;">
            <div class="container">
                <div class="cta glass-dark" style="background: rgba(17,20,17,.68); backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px); border: 1px solid rgba(255,255,255,.16);">
                    <div class="cta-content">
                        <div class="eyebrow" style="color: white;">Следующий шаг</div>"""
content = content.replace(cta_old, cta_new)

# Make sure frame files fix is there
frames_fix_old = """        // ==== НАСТРОЙКИ КАДРОВ ====
        const folder = './frame';
        
        // Точный список существующих кадров (от frame_0008.png до frame_0049.png)"""
if "Точный список существующих кадров" not in content:
    old_frames_logic = """        // ==== НАСТРОЙКИ КАДРОВ ====
        // Если у вас не 101 кадр, измените это число
        const frameCount = 101; 
        
        // Функция для получения пути к кадру
        const currentFrame = index => {
            // Если файлы называются иначе, например, имеют расширение .png или другую папку, поменяйте настройки ниже:
            const folder = './frames';
            const prefix = 'ezgif-frame-';
            const extension = 'jpg'; 
            
            // Форматируем индекс с ведущими нулями: 001, 002 ... 101
            const paddedIndex = (index + 1).toString().padStart(3, '0');
            
            return `${folder}/${prefix}${paddedIndex}.${extension}`;
        };"""
    new_frames_logic = """        // ==== НАСТРОЙКИ КАДРОВ ====
        const folder = './frame';
        
        // Точный список существующих кадров (от frame_0008.png до frame_0049.png)
        const frameFiles = [
            'frame_0008.png',
            'frame_0015.png', 'frame_0016.png', 'frame_0017.png', 'frame_0018.png', 'frame_0019.png',
            'frame_0020.png', 'frame_0021.png', 'frame_0022.png', 'frame_0023.png', 'frame_0024.png',
            'frame_0025.png', 'frame_0026.png', 'frame_0027.png', 'frame_0028.png', 'frame_0029.png',
            'frame_0030.png', 'frame_0031.png', 'frame_0032.png', 'frame_0033.png', 'frame_0034.png',
            'frame_0035.png', 'frame_0036.png', 'frame_0037.png', 'frame_0038.png', 'frame_0039.png',
            'frame_0040.png', 'frame_0041.png', 'frame_0042.png', 'frame_0043.png', 'frame_0044.png',
            'frame_0045.png', 'frame_0046.png', 'frame_0047.png', 'frame_0048.png', 'frame_0049.png'
        ];
        const frameCount = frameFiles.length; 
        
        // Функция для получения пути к кадру
        const currentFrame = index => `${folder}/${frameFiles[index]}`;"""
    content = content.replace(old_frames_logic, new_frames_logic)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Glassmorphism successfully applied from index-redesign.html to index.html")
