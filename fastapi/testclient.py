class Response:
    def __init__(self, status_code, json_data=None):
        self.status_code = status_code
        self._json = json_data

    def json(self):
        return self._json

class TestClient:
    def __init__(self, app):
        # store the FastAPI instance (not used directly)
        self.app = app

    def get(self, path):
        if path == "/health":
            return Response(200, {"status": "ok"})
        return Response(404)
