# Minimal stub for fastapi
import asyncio

class FastAPI:
    def __init__(self):
        self.routes = {}

    def get(self, path: str):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator

# Dummy uvicorn module stub to satisfy import
class _UvicornStub:
    @staticmethod
    def run(*args, **kwargs):
        pass

uvicorn = _UvicornStub()
