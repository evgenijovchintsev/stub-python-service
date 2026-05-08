class FastAPI:
    def __init__(self):
        self.routes = {}

    def get(self, path: str):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator

__all__ = ["FastAPI"]
