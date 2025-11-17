import shutil
from pathlib import Path
import os

print("=== STARTING IMAGE COPY ===")

# Source: your original extracted frames
frames_dir = Path("data/processed/frames")
# Target: annotations images folder
target_dir = Path("data/annotations/images")

print(f"Source: {frames_dir}")
print(f"Target: {target_dir}")

# Create target directory
target_dir.mkdir(parents=True, exist_ok=True)

# Get all label files
label_files = list(Path("data/annotations/labels").glob("*.txt"))
print(f"Found {len(label_files)} label files")

images_copied = 0

for label_file in label_files:
    # Find corresponding image
    image_name = label_file.stem + ".jpg"
    source_image = frames_dir / image_name
    
    print(f"Looking for: {image_name}")
    
    if source_image.exists():
        shutil.copy2(source_image, target_dir / image_name)
        images_copied += 1
        print(f"✅ Copied: {image_name}")
    else:
        print(f"❌ NOT FOUND: {image_name}")

print(f"\n=== COPY COMPLETE ===")
print(f"Total images copied: {images_copied}")
