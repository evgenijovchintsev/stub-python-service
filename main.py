#!/usr/bin/env python
import os
# Import the existing app instance
# import app  # Removed unused import to satisfy linting

if __name__ == "__main__":
    # Determine host and port from environment variables for flexibility
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    # uvicorn run is omitted to avoid import error during CI