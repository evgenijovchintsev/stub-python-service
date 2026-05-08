import asyncio
import inspect

class Response:
    def __init__(self, status_code=200, json_data=None):
        self.status_code = status_code
        self._json_data = json_data
    def json(self):
        return self._json_data

class TestClient:
    def __init__(self, app):
        self.app = app
    def get(self, path):
        handler = self.app.routes.get(path)
        if handler is None:
            return Response(status_code=404)
        if inspect.iscoroutinefunction(handler):
            result = asyncio.run(handler())
        else:
            result = handler()
        return Response(json_data=result)
