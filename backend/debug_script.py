import subprocess
import sys

print("=== DEBUG SCRIPT ===")

# Check if script exists
script_path = "training/extract_frames.py"
print(f"1. Script exists: {os.path.exists(script_path)}")

# Try running with subprocess to see any errors
try:
    result = subprocess.run([sys.executable, script_path], 
                          capture_output=True, text=True)
    print(f"2. Return code: {result.returncode}")
    print(f"3. Output: {result.stdout}")
    if result.stderr:
        print(f"4. Errors: {result.stderr}")
except Exception as e:
    print(f"2. Error running script: {e}")

print("=== DEBUG COMPLETE ===")