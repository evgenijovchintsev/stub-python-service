import asyncio
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
        func = self.app.routes.get(path)
        if not func:
            raise ValueError(f"No route for {path}")
        result = asyncio.run(func())
        return Response(result)
