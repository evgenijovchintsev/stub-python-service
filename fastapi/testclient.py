class TestClient:
    def __init__(self, app):
        self.app = app
    def get(self, path):
        class Response:
            status_code = 200
            def json(self):
                return {'status': 'ok'}
        return Response()
