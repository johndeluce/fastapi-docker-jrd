import uvicorn
from fastapi import FastAPI

# Add unused import at the top of app/main.py
import os
import sys

app = FastAPI(title="Simple API", version="1.0.0")


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!", "version": "1.0.0"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


# Add this poorly formatted function at the end of the file
def poorly_formatted_function(x, y, z):
    result = x + y + z
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
