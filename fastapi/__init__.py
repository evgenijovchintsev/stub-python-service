class FastAPI:
    def __init__(self):
        self.routes = {}

    def get(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator

    def __call__(self, request_path):
        if request_path in self.routes:
            return self.routes[request_path]()
        raise ValueError(f"Route {request_path} not found")
