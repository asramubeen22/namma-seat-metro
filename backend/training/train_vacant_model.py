from ultralytics import YOLO
import os

print("🚀 STARTING VACANT SEAT DETECTION MODEL TRAINING...")
print("This will train the model to detect ONLY vacant seats")

try:
    # Load a pre-trained YOLO model
    print("1. Loading pre-trained YOLO model...")
    model = YOLO('yolov8n.pt')
    print("✅ Pre-trained model loaded!")
    
    # Check if dataset exists
    print("2. Checking dataset...")
    if not os.path.exists('data/dataset.yaml'):
        print("❌ Dataset config not found!")
        exit()
    
    print("3. Starting training...")
    
    # Train the model for VACANT seats only
    results = model.train(
        data='data/dataset.yaml',
        epochs=50,  # Reduced for testing
        imgsz=640,
        batch=4,
        patience=10,
        save=True,
        device='cpu'
    )
    
    print("✅ VACANT SEAT TRAINING COMPLETED!")
    print("Model saved in: runs/detect/train/weights/best.pt")
    
except Exception as e:
    print(f"❌ TRAINING FAILED: {e}")
