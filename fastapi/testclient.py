# Minimal TestClient stub
class Response:
    def __init__(self, json_data):
        self._json = json_data
        self.status_code = 200
    def json(self):
        return self._json
class TestClient:
    def __init__(self, app):
        self.app = app
    def get(self, path):
        handler = self.app.routes.get(path)
        if handler is None:
            raise RuntimeError(f"No route for {path}")
        result = handler()
        return Response(result)
