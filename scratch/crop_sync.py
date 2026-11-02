from PIL import Image

im = Image.open(r"C:\Users\pc\.gemini\antigravity\brain\b2a7b082-394c-4260-942a-782b3765aac5\test_sync_screen.png")
# Tortilla Royale is second card (top center-left)
# Crop around x: 500-1100, y: 0-450
crop = im.crop((550, 0, 1150, 420))
crop.save(r"C:\Users\pc\.gemini\antigravity\brain\b2a7b082-394c-4260-942a-782b3765aac5\crop_sync_royale.png")
print("Saved crop_sync_royale.png")

