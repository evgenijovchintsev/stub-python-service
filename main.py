from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

# Provide a simple routes dictionary for the testclient to use.
app.routes = {"/health": health}
