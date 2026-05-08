from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

# Ensure application can start without errors
@app.on_event("startup")
def startup_event():
    pass