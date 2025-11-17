@echo off
echo Uploading videos to backend...

curl -X POST -F "file=@C:\Users\HP\OneDrive\Desktop\namma seat\videos\VID-20251113-WA0011.mp4" http://localhost:8000/upload-video/
curl -X POST -F "file=@C:\Users\HP\OneDrive\Desktop\namma seat\videos\WhatsApp Video 2025-11-14 at 22.33.54_b50dc007.mp4" http://localhost:8000/upload-video/
curl -X POST -F "file=@C:\Users\HP\OneDrive\Desktop\namma seat\videos\VID-20251113-WA0012.mp4" http://localhost:8000/upload-video/
curl -X POST -F "file=@C:\Users\HP\OneDrive\Desktop\namma seat\videos\VID-20251113-WA0013.mp4" http://localhost:8000/upload-video/
curl -X POST -F "file=@C:\Users\HP\OneDrive\Desktop\namma seat\videos\VID-20251113-WA0014.mp4" http://localhost:8000/upload-video/
curl -X POST -F "file=@C:\Users\HP\OneDrive\Desktop\namma seat\videos\WhatsApp Video 2025-11-14 at 22.24.25_9821f98c.mp4" http://localhost:8000/upload-video/
curl -X POST -F "file=@C:\Users\HP\OneDrive\Desktop\namma seat\videos\WhatsApp Video 2025-11-14 at 22.35.34_8b6b9e57.mp4" http://localhost:8000/upload-video/

echo All videos uploaded!
pause