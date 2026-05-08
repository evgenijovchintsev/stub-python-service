# Minimal test client for the FastAPI stub
import asyncio
from typing import Any

class Response:
    def __init__(self, status_code: int, json_data: Any):
        self.status_code = status_code
        self._json = json_data
    def json(self):
        return self._json

class TestClient:
    def __init__(self, app):
        self.app = app

    def get(self, path: str):
        handler = self.app.routes.get(path)
        if not handler:
            return Response(404, None)
        # If handler is async, run it
        if asyncio.iscoroutinefunction(handler):
            result = asyncio.run(handler())
        else:
            result = handler()
        return Response(200, result)
