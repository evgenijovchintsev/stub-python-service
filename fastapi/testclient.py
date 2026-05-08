import asyncio

class Response:
    def __init__(self, content):
        self._content = content
        self.status_code = 200

    def json(self):
        return self._content

class TestClient:
    def __init__(self, app):
        self.app = app

    def get(self, path):
        for route_path, func in self.app.routes:
            if route_path == path:
                result = func()
                if asyncio.iscoroutine(result):
                    content = asyncio.run(result)
                else:
                    content = result
                return Response(content)
        raise ValueError(f"Path {path} not found")
