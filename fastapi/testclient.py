class Response:
    def __init__(self, data):
        self.status_code = 200
        self._data = data
    def json(self):
        return self._data

class TestClient:
    def __init__(self, app):
        self.app = app
    def get(self, path):
        handler = self.app.routes.get(path)
        if not handler:
            raise Exception("404")
        data = handler()
        return Response(data)
