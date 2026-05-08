# Minimal stub of fastapi for tests
class FastAPI:
    def __init__(self):
        self.routes = {}

    def get(self, path: str):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator

# Minimal TestClient implementation
class TestClient:
    def __init__(self, app: FastAPI):
        self.app = app

    def get(self, path: str):
        func = self.app.routes.get(path)
        if not func:
            raise Exception(f"404 Not Found for {path}")
        # Call the async function synchronously for test purposes
        result = func()
        return DummyResponse(result)

class DummyResponse:
    def __init__(self, data):
        self.status_code = 200
        self._data = data

    def json(self):
        return self._data
