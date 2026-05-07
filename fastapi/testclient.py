from . import FastAPI, Response

class TestClient:
    def __init__(self, app: FastAPI):
        self.app = app

    def get(self, path):
        func = self.app.routes.get(path)
        if not func:
            return Response(404, {})
        result = func()
        if isinstance(result, dict):
            return Response(200, result)
        return Response(200, {})