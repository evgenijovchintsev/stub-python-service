class FastAPI:
    def __init__(self):
        self.routes = {}

    def get(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator

class TestClient:
    def __init__(self, app):
        self.app = app

    def get(self, path):
        handler = self.app.routes.get(path)
        if not handler:
            raise Exception("Not found")
        response = handler()
        class Resp:
            status_code = 200
            def json(self_inner):
                return response
        return Resp()