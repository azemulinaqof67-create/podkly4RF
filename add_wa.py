import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace Unsplash images with local frames
content = content.replace('https://images.unsplash.com/photo-1518780664697-55e3ad937233?auto=format&fit=crop&w=1400&q=85', './frame/frame_0015.png')
content = content.replace('https://images.unsplash.com/photo-1542314831-c6a4d1428b4a?auto=format&fit=crop&w=1100&q=85', './frame/frame_0025.png')
content = content.replace('https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1100&q=85', './frame/frame_0035.png')
content = content.replace('https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1400&q=85', './frame/frame_0045.png')
content = content.replace('https://images.unsplash.com/photo-1581404172461-807bc5ce4e7f?auto=format&fit=crop&w=1200&q=85', './frame/frame_0049.png')

# 2. Add WhatsApp floating button
# First add CSS for it
wa_css = """        .floating-wa {
            position: fixed;
            right: 20px;
            bottom: 74px;
            z-index: 50;
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: #25D366;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 14px 40px rgba(0,0,0,.2);
            transition: transform .25s ease;
        }
        .floating-wa:hover { transform: translateY(-2px); }
        .floating-wa svg { width: 24px; height: 24px; fill: white; }
"""
if '.floating-wa {' not in content:
    content = content.replace('        .floating-contact {', wa_css + '        .floating-contact {')

# Mobile CSS adjustment for both buttons
if '.floating-wa { right: 14px; bottom: 64px; }' not in content:
    content = content.replace('.floating-contact { right: 14px; bottom: 14px; }', 
                              '.floating-contact { right: 14px; bottom: 14px; }\n            .floating-wa { right: 14px; bottom: 64px; }')

# HTML for WA button
wa_html = """    <a href="https://wa.me/70000000000" target="_blank" class="floating-wa" aria-label="Написать в WhatsApp">
        <svg viewBox="0 0 24 24"><path d="M12.031 0C5.385 0 0 5.388 0 12.033c0 2.648.69 5.226 1.996 7.5L.435 24l4.57-1.198c2.19.1 4.39.2 6.5.2 6.646 0 12.031-5.388 12.031-12.033S18.677 0 12.031 0zm.019 20.016c-2.235 0-4.42-.596-6.34-1.725l-.454-.268-3.393.89.907-3.311-.295-.47c-1.24-1.97-1.896-4.247-1.896-6.599 0-5.717 4.654-10.373 10.375-10.373 5.72 0 10.373 4.656 10.373 10.373 0 5.717-4.653 10.373-10.373 10.373zM17.72 14.1c-.313-.157-1.848-.912-2.135-1.018-.286-.105-.494-.157-.702.157-.209.313-.805 1.018-.987 1.227-.183.209-.365.234-.678.077-.313-.157-1.32-.487-2.513-1.55-1.192-1.062-1.996-2.375-2.231-2.793-.235-.418-.026-.645.131-.801.14-.14.313-.365.469-.548.156-.183.209-.313.313-.523.104-.209.052-.392-.026-.548-.078-.156-.702-1.696-.963-2.322-.253-.611-.51-.527-.702-.537-.182-.009-.39-.011-.598-.011-.208 0-.547.078-.834.392-.286.313-1.093 1.071-1.093 2.613 0 1.542 1.12 3.033 1.276 3.242.156.209 2.213 3.376 5.358 4.735 3.145 1.359 3.145.904 3.718.852.573-.052 1.848-.755 2.109-1.485.26-.73.26-1.356.182-1.486-.078-.13-.286-.209-.599-.366z"/></svg>
    </a>"""
if '<a href="https://wa.me' not in content:
    content = content.replace('<a href="#contact" class="floating-contact">', wa_html + '\n    <a href="#contact" class="floating-contact">')

# 3. Reduce gap between CTA and Footer on mobile
if 'padding-top:45px;padding-bottom:90px;' in content:
    # On mobile, we will use Tailwind classes instead of inline styles for CTA padding
    content = content.replace('style="padding-top:45px;padding-bottom:90px;"', 'class="section pb-12 md:pb-24 pt-12"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Images, WA button, and spacing updated!")
