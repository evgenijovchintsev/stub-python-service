"""Minimal stub of the fastapi package for testing purposes."""
import types
from typing import Callable, Awaitable, Dict

class FastAPI:
    def __init__(self):
        self.routes: Dict[str, Callable] = {}

    def get(self, path: str):
        def decorator(func: Callable) -> Callable:
            self.routes[path] = func
            return func
        return decorator

# Expose the FastAPI class in this module
__all__ = ["FastAPI"]
