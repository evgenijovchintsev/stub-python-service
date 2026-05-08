class FastAPI:
    def __init__(self):
        self.routes = {}

    def get(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator

# expose submodule for testclient
import types
testclient = types.SimpleNamespace()
class Response:
    def __init__(self, status_code, body=None):
        self.status_code = status_code
        self._body = body

    def json(self):
        return self._body

class TestClient:
    def __init__(self, app):
        self.app = app

    def get(self, path):
        func = self.app.routes.get(path)
        if not func:
            return Response(404)
        result = func()
        # Assume the function returns a dict for simplicity
        return Response(200, result)

# Attach TestClient to submodule
import sys
sys.modules[__name__ + ".testclient"] = types.ModuleType("fastapi.testclient")
sys.modules[__name__ + ".testclient"].TestClient = TestClient
