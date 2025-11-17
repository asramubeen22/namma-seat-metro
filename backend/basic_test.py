print("=== BASIC PYTHON TEST ===")
print("1. Python is working")

# Test basic imports
try:
    import sys
    print(f"2. Python version: {sys.version}")
except Exception as e:
    print(f"2. Error: {e}")

# Test path
try:
    from pathlib import Path
    video_dir = Path("data/raw_videos")
    print(f"3. Video directory exists: {video_dir.exists()}")
    
    if video_dir.exists():
        videos = list(video_dir.glob("*.mp4"))
        print(f"4. Found {len(videos)} videos")
        for v in videos[:3]:  # Show first 3
            print(f"   - {v.name}")
except Exception as e:
    print(f"3-4. Error: {e}")

print("=== TEST COMPLETE ===")