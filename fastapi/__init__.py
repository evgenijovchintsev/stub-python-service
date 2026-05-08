class FastAPI:
    def __init__(self):
        self.routes = []
    def get(self, path):
        def decorator(func):
            self.routes.append(("GET", path, func))
            return func
        return decorator

# Placeholder TestClient class for compatibility with testclient module.
class TestClient:
    pass
