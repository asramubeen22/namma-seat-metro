from pathlib import Path
import shutil

def filter_vacant_only():
    print("=== FILTERING VACANT SEATS ONLY ===")
    
    # Paths
    dataset_dir = Path("data/dataset")
    
    # Process train and val sets
    for split in ['train', 'val']:
        labels_dir = dataset_dir / "labels" / split
        images_dir = dataset_dir / "images" / split
        
        print(f"Processing {split} set...")
        
        # Process each label file
        for label_file in labels_dir.glob("*.txt"):
            with open(label_file, 'r') as f:
                lines = f.readlines()
            
            # Filter only vacant_seat (class 1)
            vacant_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) >= 5:
                    class_id = parts[0]
                    # Keep only vacant_seat (class 1)
                    if class_id == '1':
                        vacant_lines.append(line)
            
            # If no vacant seats found, delete the image and label
            if not vacant_lines:
                print(f"❌ No vacant seats in {label_file.name}, removing...")
                label_file.unlink()
                # Also remove corresponding image
                image_file = images_dir / f"{label_file.stem}.jpg"
                if image_file.exists():
                    image_file.unlink()
            else:
                # Write back only vacant seat annotations
                with open(label_file, 'w') as f:
                    f.writelines(vacant_lines)
                print(f"✅ Kept {len(vacant_lines)} vacant seats in {label_file.name}")
    
    print("🎉 Filtering complete! Only vacant seats remain.")

if __name__ == "__main__":
    filter_vacant_only()