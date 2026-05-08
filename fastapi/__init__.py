class FastAPI:
    def __init__(self):
        pass

    def get(self, _path):
        def decorator(func):
            return func
        return decorator
