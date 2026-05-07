"""Minimal stub of the fastapi package for testing purposes."""

class FastAPI:
    def __init__(self):
        self.routes = {}
    def get(self, path):
        def decorator(func):
            self.routes[("GET", path)] = func
            return func
        return decorator

# expose TestClient in submodule fastapi.testclient
class _TestClient:
    def __init__(self, app):
        self.app = app
    def get(self, path):
        key = ("GET", path)
        if key not in self.app.routes:
            raise ValueError(f"Route {path} not found")
        func = self.app.routes[key]
        # simulate async function call
        result = func()
        return type('Response', (), {
            'status_code': 200,
            'json': lambda: result
        })

# create a submodule object
import types
_testclient_module = types.ModuleType("testclient")
setattr(_testclient_module, "TestClient", _TestClient)
import sys
sys.modules[__name__ + ".testclient"] = _testclient_module
