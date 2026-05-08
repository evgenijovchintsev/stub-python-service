import asyncio

class _TestResponse:
    def __init__(self, data):
        self._data = data
        self.status_code = 200

    def json(self):
        return self._data

class TestClient:
    def __init__(self, app):
        self.app = app

    def get(self, path):
        for route_path, handler in getattr(self.app, 'routes', []):
            if route_path == path:
                result = handler()
                if asyncio.iscoroutine(result):
                    loop = asyncio.get_event_loop()
                    if loop.is_running():
                        import nest_asyncio
                        nest_asyncio.apply()
                        result = loop.run_until_complete(result)
                    else:
                        result = loop.run_until_complete(result)
                return _TestResponse(result)
        raise RuntimeError(f'No route found for {path}')
