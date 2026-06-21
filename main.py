"""FastAPI application entry point."""

from fastapi import FastAPI

from config import settings
from utils import hello

app = FastAPI(debug=settings.debug)


@app.get("/health")
async def health():
    """Return service liveness status."""
    return {"status": "ok"}


@app.get("/hello")
async def get_hello():
    """Return hello world string."""
    return hello()
