from fastapi.testclient import TestClient
import app

def test_health():
    client = TestClient(app.app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}