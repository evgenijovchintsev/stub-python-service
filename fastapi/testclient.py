"""Minimal stub for fastapi.testclient used in tests."""
from typing import Any

class Response:
    def __init__(self, json_data: Any):
        self._json = json_data
        self.status_code = 200
    def json(self) -> Any:
        return self._json

class TestClient:
    def __init__(self, app):
        self.app = app
    def get(self, path: str) -> Response:
        # Find the route function
        func = self.app.routes.get(path)
        if not func:
            return Response({"detail": "Not Found"})
        result = func()
        # If coroutine (async), run it synchronously for stub purposes
        if hasattr(result, "__await__"):
            import asyncio
            result = asyncio.run(result)
        return Response(result)

# expose TestClient at package level
__all__ = ["TestClient", "Response"]