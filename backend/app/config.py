import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Data paths
RAW_VIDEOS_DIR = BASE_DIR / "data" / "raw_videos"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
ANNOTATIONS_DIR = BASE_DIR / "data" / "annotations"

# Create directories if they don't exist
for directory in [RAW_VIDEOS_DIR, PROCESSED_DIR, ANNOTATIONS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Model settings
MODEL_CONFIG = {
    "input_size": (640, 640),
    "confidence_threshold": 0.5,
    "iou_threshold": 0.45
}