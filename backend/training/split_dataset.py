import os
import random
import shutil
from pathlib import Path

print("=== STARTING DATASET SPLIT ===")

def split_dataset():
    # Paths
    annotations_dir = Path("data/annotations")
    dataset_dir = Path("data/dataset")
    
    print(f"Annotations dir: {annotations_dir}")
    print(f"Dataset dir: {dataset_dir}")
    
    # Create dataset directories
    (dataset_dir / "images/train").mkdir(parents=True, exist_ok=True)
    (dataset_dir / "images/val").mkdir(parents=True, exist_ok=True)
    (dataset_dir / "labels/train").mkdir(parents=True, exist_ok=True)
    (dataset_dir / "labels/val").mkdir(parents=True, exist_ok=True)
    
    # Get all image files
    image_files = list(annotations_dir.glob("images/*.jpg"))
    print(f"Found {len(image_files)} image files")
    
    if not image_files:
        print("❌ No image files found!")
        return
    
    random.shuffle(image_files)
    
    # Split ratio (80% train, 20% validation)
    split_idx = int(0.8 * len(image_files))
    train_files = image_files[:split_idx]
    val_files = image_files[split_idx:]
    
    print(f"Total images: {len(image_files)}")
    print(f"Training: {len(train_files)}")
    print(f"Validation: {len(val_files)}")
    
    # Copy images and labels to train/val folders
    for img_path in train_files:
        # Copy image
        shutil.copy(img_path, dataset_dir / "images/train")
        
        # Copy corresponding label
        label_path = annotations_dir / "labels" / f"{img_path.stem}.txt"
        if label_path.exists():
            shutil.copy(label_path, dataset_dir / "labels/train")
            print(f"✅ Copied to train: {img_path.name}")
    
    for img_path in val_files:
        # Copy image
        shutil.copy(img_path, dataset_dir / "images/val")
        
        # Copy corresponding label
        label_path = annotations_dir / "labels" / f"{img_path.stem}.txt"
        if label_path.exists():
            shutil.copy(label_path, dataset_dir / "labels/val")
            print(f"✅ Copied to val: {img_path.name}")
    
    print("🎉 Dataset split complete!")

if __name__ == "__main__":
    split_dataset()
