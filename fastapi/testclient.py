import asyncio
from . import FastAPI

class Response:
    def __init__(self, json_data):
        self._json = json_data
        self.status_code = 200

    def json(self):
        return self._json

class TestClient:
    def __init__(self, app: FastAPI):
        self.app = app

    def get(self, path: str):
        handler = self.app.routes.get(path)
        if handler is None:
            return Response({"detail": "Not Found"})
        result = asyncio.run(handler())
        return Response(result)
