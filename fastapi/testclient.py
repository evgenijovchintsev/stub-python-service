class Response:
    def __init__(self, status_code=200, json_data=None):
        self.status_code = status_code
        self._json_data = json_data or {}

    def json(self):
        return self._json_data

class TestClient:
    def __init__(self, app):
        self.app = app

    def get(self, path):
        # Very simple stub: if route exists return its response
        func = self.app.routes.get(path)
        if func is None:
            return Response(status_code=404)
        result = func()
        if isinstance(result, dict):
            return Response(json_data=result)
        return Response(json_data={})
