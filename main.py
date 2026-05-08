#!/usr/bin/env python
import os
from fastapi import FastAPI
import uvicorn

# Import the existing app instance
import app

if __name__ == "__main__":
    # Determine host and port from environment variables for flexibility
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app.app, host=host, port=port)
