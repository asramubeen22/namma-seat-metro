from ultralytics import YOLO
import cv2
import numpy as np
from pathlib import Path
import json
import time

def process_video_realtime(video_path, output_path="processed_video.mp4"):
    print("🎥 Starting CCTV-style video processing...")
    
    # Load trained model
    model = YOLO('runs/detect/train/weights/best.pt')
    
    # Open video file
    cap = cv2.VideoCapture(str(video_path))
    
    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Setup video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    print(f"Processing video: {video_path}")
    print(f"Video specs: {width}x{height} at {fps} FPS")
    
    frame_count = 0
    vacant_data = []
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Run vacant seat detection
        results = model(frame)
        
        # Count vacant seats
        vacant_count = len(results[0].boxes) if results[0].boxes else 0
        
        # Store data for frontend
        vacant_data.append({
            "frame": frame_count,
            "timestamp": frame_count / fps,
            "vacant_seats": vacant_count
        })
        
        # Add overlay to frame
        cv2.putText(frame, f"Vacant Seats: {vacant_count}", (20, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Frame: {frame_count}", (20, 90), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Write frame to output video
        out.write(frame)
        
        frame_count += 1
        
        # Print progress every 100 frames
        if frame_count % 100 == 0:
            print(f"Processed {frame_count} frames...")
    
    cap.release()
    out.release()
    
    # Save vacant seat data
    with open('vacant_data.json', 'w') as f:
        json.dump(vacant_data, f)
    
    print(f"✅ Processing complete!")
    print(f"Total frames: {frame_count}")
    print(f"Output video: {output_path}")
    print(f"Vacant data: vacant_data.json")
    
    return output_path

if __name__ == "__main__":
    # Process your CCTV video
    video_path = "data/raw_videos/VID-20251113-WA0011.mp4"  # Change to your video
    process_video_realtime(video_path)