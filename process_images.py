import os
import urllib.request
from PIL import Image
from rembg import remove

RAW_DIR = "raw_images"
PROCESSED_DIR = "processed_images"

def ensure_directories():
    os.makedirs(RAW_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)

def download_samples_if_empty():
    if not os.listdir(RAW_DIR):
        print(f"No images found in {RAW_DIR}. Downloading sample images...")
        samples = [
            ("bocadillo.jpg", "https://images.unsplash.com/photo-1528735602780-2552fd46c7af?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"),
            ("fries.jpg", "https://images.unsplash.com/photo-1576107232684-1279f390859f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"),
            ("drink.jpg", "https://images.unsplash.com/photo-1556740738-b6a63e27c4df?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80")
        ]
        for filename, url in samples:
            print(f"Downloading {filename}...")
            urllib.request.urlretrieve(url, os.path.join(RAW_DIR, filename))
        print("Sample images downloaded.")

def process_images():
    ensure_directories()
    download_samples_if_empty()
    
    raw_files = os.listdir(RAW_DIR)
    for filename in raw_files:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            raw_path = os.path.join(RAW_DIR, filename)
            base_name = os.path.splitext(filename)[0]
            processed_filename = f"{base_name}.png"
            processed_path = os.path.join(PROCESSED_DIR, processed_filename)
            
            print(f"Processing {filename}...")
            try:
                # Load image
                input_image = Image.open(raw_path)
                
                # Remove background
                output_image = remove(input_image)
                
                # Save as transparent PNG
                output_image.save(processed_path, "PNG")
                print(f"Saved {processed_filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    process_images()
    print("Background removal complete.")
