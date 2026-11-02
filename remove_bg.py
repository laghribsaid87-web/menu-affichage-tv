import os
import glob
from rembg import remove
from PIL import Image

def process_images():
    input_dir = 'processed_images'
    images = glob.glob(os.path.join(input_dir, '*.jpg'))
    
    if not images:
        print("No JPG images found in processed_images/")
        return

    for img_path in images:
        print(f"Processing {img_path}...")
        try:
            input_image = Image.open(img_path)
            output_image = remove(input_image)
            png_path = img_path.replace('.jpg', '.png')
            output_image.save(png_path)
            print(f"Saved {png_path}")
        except Exception as e:
            print(f"Error processing {img_path}: {e}")

if __name__ == "__main__":
    print("Starting background removal process...")
    process_images()
    print("Done!")
