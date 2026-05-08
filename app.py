from fastapi import FastAPI

app = FastAPI()

def health():
    return {"status": "ok"}

async def _health_wrapper():
    return health()

app.routes["/health"] = _health_wrapper
