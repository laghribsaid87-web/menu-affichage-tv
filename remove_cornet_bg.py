import os
from rembg import remove
from PIL import Image

def process_image(input_path, output_path):
    print(f"Processing {input_path}...")
    try:
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
        print(f"Saved {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

if __name__ == "__main__":
    # We will try frite.jpg and c.jfif
    process_image('raw_images/frite.jpg', 'processed_images/cornet1.png')
    process_image('raw_images/c.jfif', 'processed_images/cornet2.png')
    process_image('raw_images/IMG_1616.jpeg', 'processed_images/cornet3.png')
    process_image('raw_images/bocadillo cheese.webp', 'processed_images/cornet4.png')
