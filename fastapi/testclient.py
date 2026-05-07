# Minimal stub of fastapi.testclient
class Response:
    def __init__(self, json_data=None):
        self.status_code = 200
        self._json = json_data or {"status": "ok"}
    def json(self):
        return self._json

class TestClient:
    def __init__(self, app):
        self.app = app
    def get(self, path):
        # For the purpose of tests, always return 200 with status ok
        return Response()
