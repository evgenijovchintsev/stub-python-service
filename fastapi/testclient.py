"""Minimal stub of fastapi.testclient for testing purposes."""
import asyncio
from typing import Any, Dict

class Response:
    def __init__(self, json_data: Any):
        self._json = json_data
        self.status_code = 200

    def json(self) -> Any:
        return self._json

class TestClient:
    def __init__(self, app: "FastAPI"):
        self.app = app

    def get(self, path: str) -> Response:
        handler = self.app.routes.get(path)
        if handler is None:
            raise ValueError(f"No route for {path}")
        # If the handler is async, run it in an event loop
        if asyncio.iscoroutinefunction(handler):
            result = asyncio.run(handler())
        else:
            result = handler()
        return Response(result)

__all__ = ["TestClient"]
