import requests
from pathlib import Path

# Your source videos path
videos_path = Path("C:/Users/HP/OneDrive/Desktop/namma seat/videos")

print("🎬 Uploading videos from:", videos_path)

# Find all video files
video_files = []
for ext in ['.mp4', '.avi', '.mov']:
    video_files.extend(videos_path.glob(f"*{ext}"))

print(f"📹 Found {len(video_files)} videos:")

for video in video_files:
    print(f"   - {video.name}")

print(f"\n🚀 Starting upload...")

# Upload each video
for video in video_files:
    try:
        print(f"⬆️  Uploading: {video.name}...")
        with open(video, 'rb') as f:
            files = {'file': (video.name, f, 'video/mp4')}
            response = requests.post('http://localhost:8000/upload-video/', files=files)
        
        if response.status_code == 200:
            print(f"✅ SUCCESS: {video.name}")
        else:
            print(f"❌ FAILED: {response.text}")
            
    except Exception as e:
        print(f"💥 ERROR: {e}")

print("\n🎉 Upload complete!")