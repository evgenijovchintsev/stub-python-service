"""Minimal stub for fastapi package used in tests."""

class FastAPI:
    def __init__(self):
        self.routes = {}

    def get(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator

# expose FastAPI at package level
__all__ = ["FastAPI"]
