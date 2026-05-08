class DummyResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self._json_data = json_data

    def json(self):
        return self._json_data

class TestClient:
    def __init__(self, app_instance):
        self.app = app_instance

    def get(self, path):
        func = self.app.routes.get(path)
        if not func:
            return DummyResponse(status_code=404, json_data=None)
        result = func()
        return DummyResponse(status_code=200, json_data=result)
