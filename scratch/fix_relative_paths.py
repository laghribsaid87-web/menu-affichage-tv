import re

models = ['menu_model1_emirates.html', 'menu_model2_urban.html', 'menu_model3_vibrant.html', 'viewer.html', 'dashboard_pro.html', 'menu_items.json']

for m in models:
    path = f"c:/Users/pc/Desktop/menu/{m}"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace src="/cutouts_cropped/ with src="cutouts_cropped/
    # Replace src="/processed_images/ with src="processed_images/
    # Replace "/cutouts_cropped/ with "cutouts_cropped/
    new_content = content.replace('src="/cutouts_cropped/', 'src="cutouts_cropped/')
    new_content = new_content.replace('src="/processed_images/', 'src="processed_images/')
    new_content = new_content.replace('"/cutouts_cropped/', '"cutouts_cropped/')
    new_content = new_content.replace('"/processed_images/', '"processed_images/')
    
    # Also fetch('/api/menu_items') -> check if fails fallback to 'menu_items.json'
    if content != new_content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Fixed relative paths in {m}")
    else:
        print(f"No changes needed in {m}")

