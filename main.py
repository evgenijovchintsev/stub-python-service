"""FastAPI application entry point."""

from fastapi import FastAPI
from typing import Optional, Union

from config import settings

app = FastAPI(debug=settings.debug)


@app.get("/health")
async def health():
    """Return service liveness status."""
    return {"status": "ok"}


@app.get("/users/{user_id}")
async def get_user(user_id: Union[str, int], path_param: Optional[dict] = None):
    """Return user data by ID.

    Extracts the user_id from the URL path parameter and returns the corresponding user record.

    Args:
        user_id (Union[str, int]): The user identifier extracted from the /users/{user_id} route. Accepts both string UUIDs and integer IDs.
        path_param (Optional[dict]): Additional context or metadata passed along with the request.
    """
    return {
        "user_id": user_id,
        "path_param": path_param
    }
