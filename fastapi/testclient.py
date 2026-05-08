class Response:
    def __init__(self, status_code=200, json_data=None):
        self.status_code = status_code
        self._json = json_data or {}

    def json(self):
        return self._json

class TestClient:
    def __init__(self, app):
        self.app = app

    def get(self, path):
        handler = self.app.routes.get(path)
        if not handler:
            return Response(status_code=404)
        result = handler()
        # assume handler returns dict
        return Response(status_code=200, json_data=result)
