print('=== FRAME EXTRACTION STARTED ===')

import cv2
from pathlib import Path
import os

print('Imports successful!')

# Create directories
video_dir = Path('data/raw_videos')
output_dir = Path('data/processed/frames')
output_dir.mkdir(parents=True, exist_ok=True)

print(f'Looking for videos in: {video_dir}')

# Find all videos
videos = list(video_dir.glob('*.mp4'))
print(f'Found {len(videos)} videos')

if not videos:
    print('No videos found!')
    exit()

print('Starting extraction...')

# Process first video only for testing
video = videos[0]
print(f'Processing: {video.name}')

cap = cv2.VideoCapture(str(video))
if not cap.isOpened():
    print(f'Cannot open video: {video.name}')
    exit()

print('Video opened successfully!')

frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    # Save every 30th frame
    if frame_count % 30 == 0:
        filename = output_dir / f'frame_{saved_count:04d}.jpg'
        success = cv2.imwrite(str(filename), frame)
        if success:
            saved_count += 1
            print(f'Saved frame {saved_count}')
        else:
            print('Failed to save frame')
    
    frame_count += 1
    
    # Stop after 10 saved frames for testing
    if saved_count >= 10:
        break

cap.release()
print(f'Extraction complete! Saved {saved_count} frames.')
