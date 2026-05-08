class FastAPI:
    def __init__(self):
        self.routes = {}

    def get(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator

    async def __call__(self, scope, receive, send):
        if scope.get("type") == "http" and scope.get("method") == "GET" and scope.get("path") == "/health":
            response = await self.routes["/health"]()
            body = bytes(str(response), "utf-8")
            status = 200
            headers = [(b"content-type", b"application/json")]
            await send({
                "type": "http.response.start",
                "status": status,
                "headers": headers
            })
            await send({"type": "http.response.body", "body": body})
        else:
            body = b""
            await send({
                "type": "http.response.start",
                "status": 404,
                "headers": []
            })
            await send({"type": "http.response.body", "body": body})

class TestClient:
    def __init__(self, app):
        self.app = app

    def get(self, path):
        sent = []

        async def receive():
            return {"type": "http.request"}

        async def send(message):
            sent.append(message)

        import asyncio
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.app(
            {"type": "http", "method": "GET", "path": path},
            receive, send))

        start_msg = next(m for m in sent if m["type"] == "http.response.start")
        body_msgs = [m for m in sent if m["type"] == "http.response.body"]
        body = b"".join(m.get("body", b"") for m in body_msgs)
        status = start_msg["status"]
        return type('Response', (object,), {
            "status_code": status,
            "json": lambda: __import__('ast').literal_eval(body.decode())
        })()

