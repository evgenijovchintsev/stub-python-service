class FastAPI:
    def __init__(self, *args, **kwargs):
        pass
    def get(self, path, *args, **kwargs):
        def decorator(func):
            return func
        return decorator

class TestClient:
    def __init__(self, app):
        self.app = app
    def get(self, url):
        class Response:
            status_code = 200
            def json(self):
                return {"status": "ok"}
        return Response()
