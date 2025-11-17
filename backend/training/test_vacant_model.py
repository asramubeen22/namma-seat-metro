from ultralytics import YOLO
from pathlib import Path

print("🧪 Testing vacant seat detection model...")

# Load the trained model
model = YOLO('runs/detect/train/weights/best.pt')

# Test on validation images
val_images = list(Path("data/dataset/images/val").glob("*.jpg"))

print(f"Testing on {len(val_images)} validation images...")

for img_path in val_images:
    print(f"🔍 Testing: {img_path.name}")
    
    # Run detection
    results = model(img_path)
    
    # Count vacant seats detected
    vacant_count = len(results[0].boxes) if results[0].boxes else 0
    print(f"   ✅ Detected {vacant_count} vacant seats")
    
    # Save result image
    output_path = f"test_result_{img_path.name}"
    results[0].save(filename=output_path)
    print(f"   💾 Saved: {output_path}")

print("🎉 Testing complete! Check the result images.")