"""
FastAPI application entry point.
"""
from fastapi import FastAPI
import uvicorn

# Import the existing app instance from app.py
from app import app as api_app

# Expose the same API under the main module for running with uvicorn
app = api_app

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
