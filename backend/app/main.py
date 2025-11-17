from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, RedirectResponse  # ← ADD RedirectResponse
import os

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DEBUG: Print startup info
print("=" * 50)
print("🚀 SERVER STARTING - DEBUG MODE")
print("=" * 50)
print(f"📁 Current directory: {os.getcwd()}")
print(f"📄 index.html exists: {os.path.exists('index.html')}")
print(f"📄 seat-occupancy.html exists: {os.path.exists('seat-occupancy.html')}")

# List all files in current directory
print("📂 Files in backend directory:")
for file in os.listdir('.'):
    if file.endswith('.html') or file == 'app':
        print(f"   - {file}")

print("=" * 50)

# Serve HTML files
@app.get("/")
async def serve_dashboard():
    print("📊 / endpoint called - serving dashboard")
    if os.path.exists("index.html"):
        print("✅ Serving index.html")
        return FileResponse("index.html")
    else:
        print("❌ index.html NOT FOUND!")
        return {"error": "index.html not found", "files": os.listdir('.')}

@app.get("/seat-occupancy")
async def serve_seat_occupancy():
    print("💺 /seat-occupancy endpoint called")
    if os.path.exists("seat-occupancy.html"):
        print("✅ Serving seat-occupancy.html")
        return FileResponse("seat-occupancy.html")
    else:
        print("❌ seat-occupancy.html NOT FOUND!")
        return {"error": "seat-occupancy.html not found", "files": os.listdir('.')}

# 🆕 ADD THIS REDIRECT ROUTE
@app.get("/seat-occupancy.html")
async def redirect_seat_occupancy():
    """Redirect from seat-occupancy.html to seat-occupancy"""
    print("🔄 Redirecting /seat-occupancy.html to /seat-occupancy")
    return RedirectResponse(url="/seat-occupancy")

# API endpoints
@app.get("/api/")
def api_root():
    return {"message": "✅ Namma Seat Backend API is WORKING!"}

@app.get("/test")
async def test():
    return {"status": "Test endpoint working"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/api/seats")
def get_all_seats():
    return {
        "T1": "VACANT", "T2": "OCCUPIED", "T3": "VACANT",
        "T4": "VACANT", "T5": "OCCUPIED", "T6": "VACANT",
        "T7": "VACANT", "T8": "VACANT", "T9": "OCCUPIED",
        "T10": "VACANT", "T11": "OCCUPIED", "T12": "VACANT"
    }