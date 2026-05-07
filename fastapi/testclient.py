from typing import Any

class Response:
    def __init__(self, data: Any):
        self._data = data
        self.status_code = 200

    def json(self):
        return self._data

class TestClient:
    def __init__(self, app):
        self.app = app

    def get(self, path):
        func = self.app.routes.get(path)
        if not func:
            raise Exception("Not found")
        data = func()
        return Response(data)
