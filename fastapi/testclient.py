class Response:
    def __init__(self, json_data):
        self.status_code = 200
        self._json = json_data
    def json(self):
        return self._json

class TestClient:
    def __init__(self, app):
        self.app = app
    def get(self, path):
        if path in self.app.routes:
            result = self.app.routes[path]()
            return Response(result)
        raise ValueError(f"Route {path} not found")