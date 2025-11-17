import shutil
from pathlib import Path
import os

def extract_makesense_export():
    # Source folder (makesense export)
    source_dir = Path("data/annotations/labels_my-project-name_2025-11-16-08-23-59")
    
    # Target directories
    images_dir = Path("data/annotations/images")
    labels_dir = Path("data/annotations/labels")
    
    # Create directories
    images_dir.mkdir(parents=True, exist_ok=True)
    labels_dir.mkdir(parents=True, exist_ok=True)
    
    print("Looking for files in:", source_dir)
    
    # Find all files
    all_files = list(source_dir.rglob("*"))
    print(f"Found {len(all_files)} files/directories")
    
    # Copy images and labels
    images_copied = 0
    labels_copied = 0
    
    for file_path in all_files:
        if file_path.is_file():
            # Check if it's an image
            if file_path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
                shutil.copy2(file_path, images_dir / file_path.name)
                images_copied += 1
                print(f"Copied image: {file_path.name}")
            
            # Check if it's a label file
            elif file_path.suffix.lower() == '.txt':
                shutil.copy2(file_path, labels_dir / file_path.name)
                labels_copied += 1
                print(f"Copied label: {file_path.name}")
    
    print(f"\nExtraction complete!")
    print(f"Images copied: {images_copied}")
    print(f"Labels copied: {labels_copied}")
    
    # Check if we have a classes.txt
    classes_file = source_dir / "classes.txt"
    if classes_file.exists():
        shutil.copy2(classes_file, Path("data/annotations/classes.txt"))
        print("Copied classes.txt")
    else:
        # Create classes.txt manually
        with open("data/annotations/classes.txt", "w") as f:
            f.write("occupied_seat\nvacant_seat\n")
        print("Created classes.txt manually")

if __name__ == "__main__":
    extract_makesense_export()