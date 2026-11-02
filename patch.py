import sys

with open('tv_dynamic.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_script = """    <script>
        const bocadillos = [
            { name: "BOCADILLO CHEESE", price: "24", img: "processed_images/bocadillo cheese 24 dh.png" },
            { name: "BOCADILLO COMPLET", price: "29", img: "processed_images/bocadillo complet 29 dh.png" },
            { name: "BOCADILLO TANGEROIS", price: "24", img: "processed_images/bocadillo tangerois 24 dh.png" },
            { name: "BOCADILLO THON", price: "22", img: "processed_images/bocadillo thon 22 dh.png" },
            { name: "TORTILLIA ROYALE", price: "30", img: "processed_images/bocadillo tortillia royale 30 dh.png" },
            { name: "BOCADILLO TORTILLIA", price: "22", img: "processed_images/bocadillo_tortillia 22 dh.png" }
        ];

        const sandwiches = [
            { name: "SANDWICH AMERICAIN", price: "35", img: "processed_images/sandwich americain 35 dh.png" },
            { name: "VIANDE HACHE", price: "30", img: "processed_images/sandwich viande hache 30 dh.png" },
            { name: "SANDWICHE MIXTE", price: "35", img: "processed_images/sandwiche mixte 35 dh.png" },
            { name: "SANDWICHE POULET", price: "30", img: "processed_images/sandwiche poulet 30 dh.png" },
            { name: "SANDWICHE SAUSSICE", price: "30", img: "processed_images/sandwiche saussice 30.png" }
        ];

        // Split items for top display so they aren't too crowded
        // We will just show 4 items max on top to keep it looking premium.
        const screens = [
            { title: "NOS BOCADILLOS", items: bocadillos.slice(0, 4) },
            { title: "NOS SANDWICHES", items: sandwiches.slice(0, 4) }
        ];"""

new_script = """    <script>
        let bocadillos = [];
        let sandwiches = [];
        let screens = [];
        let allItems = [];

        // Fetch Data from Server
        fetch('/api/dynamic_menu')
            .then(res => res.json())
            .then(data => {
                bocadillos = data.bocadillos || [];
                sandwiches = data.sandwiches || [];
                
                screens = [
                    { title: "NOS BOCADILLOS", items: bocadillos.slice(0, 4) },
                    { title: "NOS SANDWICHES", items: sandwiches.slice(0, 4) }
                ];

                allItems = [...bocadillos, ...sandwiches];
                // Shuffle array for spotlight randomness
                for (let i = allItems.length - 1; i > 0; i--) {
                    const j = Math.floor(Math.random() * (i + 1));
                    [allItems[i], allItems[j]] = [allItems[j], allItems[i]];
                }

                // Start Top Slider
                cycleScreens();
                setInterval(cycleScreens, DURATION);

                // Start Bottom Spotlight
                renderSpotlight();
                setInterval(renderSpotlight, SPOTLIGHT_DURATION);
            })
            .catch(err => console.error("Error loading menu data:", err));"""

if old_script in content:
    content = content.replace(old_script, new_script)
else:
    print('Failed to find old script block 1')
    sys.exit(1)

old_script2 = """        // ==========================================
        // SPOTLIGHT ANIMATION (BOTTOM SECTION)
        // ==========================================
        const allItems = [...bocadillos, ...sandwiches];
        // Shuffle array for randomness
        for (let i = allItems.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [allItems[i], allItems[j]] = [allItems[j], allItems[i]];
        }
        
        let currentSpotlight = 0;"""

new_script2 = """        // ==========================================
        // SPOTLIGHT ANIMATION (BOTTOM SECTION)
        // ==========================================
        let currentSpotlight = 0;"""

if old_script2 in content:
    content = content.replace(old_script2, new_script2)
else:
    print('Failed to find old script block 2')

old_script3 = """        window.onload = () => {
            // Start Top Slider
            cycleScreens();
            setInterval(cycleScreens, DURATION);

            // Start Bottom Spotlight
            renderSpotlight();
            setInterval(renderSpotlight, SPOTLIGHT_DURATION);
        };
    </script>"""

new_script3 = """    </script>"""

if old_script3 in content:
    content = content.replace(old_script3, new_script3)
else:
    print('Failed to find old script block 3')

with open('tv_dynamic.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
