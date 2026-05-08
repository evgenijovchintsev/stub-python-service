"""Minimal stub for fastapi package used in tests."""

from typing import Callable, Any

class FastAPI:
    def __init__(self):
        self.routes = {}

    def get(self, path: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            self.routes[path] = func
            return func
        return decorator

# expose FastAPI at package level
__all__ = ["FastAPI"]
