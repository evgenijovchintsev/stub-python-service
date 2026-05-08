class FastAPI:
    def __init__(self, *args, **kwargs):
        pass
    def get(self, path):
        def decorator(func):
            # minimal stub; store route if needed
            return func
        return decorator
