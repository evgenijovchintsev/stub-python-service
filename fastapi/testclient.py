class Response:
    def __init__(self, data):
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
            raise ValueError(f"No route for {path}")
        data = func()
        return Response(data)
