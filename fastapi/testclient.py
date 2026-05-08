class DummyResponse:
    def __init__(self, status_code, json_body=None):
        self.status_code = status_code
        self._json = json_body

    def json(self):
        return self._json

class TestClient:
    def __init__(self, app):
        self.app = app

    def get(self, path):
        func = self.app.routes.get(path)
        if not func:
            return DummyResponse(404)
        result = func()
        return DummyResponse(200, result)
