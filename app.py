from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
await def health():
    return {"status": "ok"}