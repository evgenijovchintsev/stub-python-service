# Minimal stub of FastAPI for testing
class FastAPI:
    def __init__(self):
        self.routes = {}
    def get(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator
