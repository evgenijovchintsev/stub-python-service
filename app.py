from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get("/health")
async def health():\n    return {"status": "ok"}\n