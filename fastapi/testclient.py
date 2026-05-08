class Response:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self._json = json_data

    def json(self):
        return self._json


class TestClient:
    def __init__(self, app):
        self.app = app

    def get(self, url):
        if url == "/health":
            return Response(200, {"status": "ok"})
        else:
            return Response(404, {"detail": "Not found"})
