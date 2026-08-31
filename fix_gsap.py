import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Step 2 fade in
content = content.replace(
'''        gsap.fromTo("#step2", 
            { opacity: 0, y: 50 },
            { 
                opacity: 1, 
                y: 0, 
                scrollTrigger: {
                    trigger: "#step2",
                    start: "top 80%",
                    end: "center center",
                    scrub: 1
                }
            }
        );''',
'''        gsap.fromTo("#step2 .hero-side", 
            { opacity: 0, y: 50 },
            { 
                opacity: 1, 
                y: 0, 
                scrollTrigger: {
                    trigger: "#step2 .hero-side",
                    start: "top 85%",
                    end: "center center",
                    scrub: 1
                }
            }
        );'''
)

# Step 2 fade out
content = content.replace(
'''        gsap.to("#step2", {
            opacity: 0,
            scrollTrigger: {
                trigger: "#step2",
                start: "top top",
                end: "bottom top",
                scrub: 1
            }
        });''',
'''        gsap.to("#step2 .hero-side", {
            opacity: 0,
            scrollTrigger: {
                trigger: "#step2 .hero-side",
                start: "top 20%",
                end: "bottom top",
                scrub: 1
            }
        });'''
)

# Step 3 fade in
content = content.replace(
'''        gsap.fromTo("#step3", 
            { opacity: 0, y: 50 },
            { 
                opacity: 1, 
                y: 0, 
                scrollTrigger: {
                    trigger: "#step3",
                    start: "top 80%",
                    end: "center center",
                    scrub: 1
                }
            }
        );''',
'''        gsap.fromTo("#step3 .hero-side", 
            { opacity: 0, y: 50 },
            { 
                opacity: 1, 
                y: 0, 
                scrollTrigger: {
                    trigger: "#step3 .hero-side",
                    start: "top 85%",
                    end: "center center",
                    scrub: 1
                }
            }
        );'''
)

# Step 3 fade out
content = content.replace(
'''        gsap.to("#step3", {
            opacity: 0,
            scrollTrigger: {
                trigger: "#step3",
                start: "top top",
                end: "bottom top",
                scrub: 1
            }
        });''',
'''        gsap.to("#step3 .hero-side", {
            opacity: 0,
            scrollTrigger: {
                trigger: "#step3 .hero-side",
                start: "top 20%",
                end: "bottom top",
                scrub: 1
            }
        });'''
)

# Step 4 fade in
content = content.replace(
'''        gsap.fromTo("#step4", 
            { opacity: 0, scale: 0.9, y: 50 },
            { 
                opacity: 1, 
                scale: 1,
                y: 0,
                scrollTrigger: {
                    trigger: "#step4",
                    start: "top 80%",
                    end: "center center",
                    scrub: 1
                }
            }
        );''',
'''        gsap.fromTo("#step4 .hero-panel", 
            { opacity: 0, scale: 0.9, y: 50 },
            { 
                opacity: 1, 
                scale: 1,
                y: 0,
                scrollTrigger: {
                    trigger: "#step4 .hero-panel",
                    start: "top 85%",
                    end: "center center",
                    scrub: 1
                }
            }
        );'''
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("GSAP triggers updated!")
