class Response:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self._json = json_data

    def json(self):
        return self._json

class TestClient:
    def __init__(self, app):
        self.app = app

    def get(self, path):
        try:
            result = self.app(path)
            if isinstance(result, dict):
                return Response(200, result)
            else:
                return Response(500, {})
        except Exception as e:  # noqa: W0612
            _ = e
            return Response(404, {})