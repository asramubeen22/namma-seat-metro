from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "SIMPLE TEST - IT WORKS!"}

@app.get("/test")
def test():
    return {"status": "test endpoint working"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)