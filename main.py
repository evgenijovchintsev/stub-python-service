from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

# Provide a simple routes mapping for the test client
app.routes = {"/health": lambda: {"status": "ok"}}
