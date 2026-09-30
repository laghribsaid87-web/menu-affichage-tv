import re

with open(r'c:\Users\pc\Desktop\menu\tv2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace fetch URL to use tv param
fetch_regex = r"const res = await fetch\('menu_data\.json'\);"
new_fetch = """const urlParams = new URLSearchParams(window.location.search);
            const targetTv = urlParams.get('tv') || '1';
            const res = await fetch(`/api/menu/${targetTv}`);"""
content = re.sub(fetch_regex, new_fetch, content)

# Add smart scaling logic in <head>
smart_scale_script = """
    <script>
        function resizeCanvas() {
            // Check orientation from global menuData if available, else default horizontal
            const isVertical = (window.menuData && window.menuData.orientation === 'vertical');
            const baseWidth = isVertical ? 1080 : 1920;
            const baseHeight = isVertical ? 1920 : 1080;
            
            document.body.style.width = baseWidth + 'px';
            document.body.style.height = baseHeight + 'px';
            
            const scaleX = window.innerWidth / baseWidth;
            const scaleY = window.innerHeight / baseHeight;
            const scale = Math.min(scaleX, scaleY);
            
            document.body.style.transform = `scale(${scale})`;
            document.body.style.transformOrigin = 'top left';
            
            const scaledWidth = baseWidth * scale;
            const scaledHeight = baseHeight * scale;
            document.body.style.marginLeft = `${(window.innerWidth - scaledWidth) / 2}px`;
            document.body.style.marginTop = `${(window.innerHeight - scaledHeight) / 2}px`;
        }
        window.addEventListener('resize', resizeCanvas);
        // Call it after data loads too
    </script>
"""
content = content.replace('</head>', smart_scale_script + '\n</head>')

# Call resizeCanvas after loadData finishes fetching menuData
content = content.replace('buildDynamicViews();', 'resizeCanvas();\n            buildDynamicViews();')

with open(r'c:\Users\pc\Desktop\menu\viewer.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("viewer.html generated successfully!")
