"""FastAPI application entry point."""

from fastapi import FastAPI

from config import settings

app = FastAPI(debug=settings.debug)


@app.get("/health")
async def health():
    """Return service liveness status."""
    return {"status": "ok"}
