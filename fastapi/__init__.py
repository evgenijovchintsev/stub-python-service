class FastAPI:
    def __init__(self, *args, **kwargs):
        self.routes = []
    def get(self, path):
        def decorator(func):
            self.routes.append(("GET", path, func))
            return func
        return decorator
class TestClient:
    def __init__(self, app):
        self.app = app
    def get(self, path):
        for method, p, fn in self.app.routes:
            if method == "GET" and p == path:
                response = fn()
                return type("Response", (), {"status_code":200,"json":lambda:response})
        return type("Response", (), {"status_code":404,"json":lambda:{}})()