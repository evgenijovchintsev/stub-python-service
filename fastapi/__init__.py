class FastAPI:
    def __init__(self):
        pass

    def get(self, path):
        def decorator(func):
            return func
        return decorator
