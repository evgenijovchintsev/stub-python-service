"""Tests for the /health endpoint."""

from fastapi.testclient import TestClient
import main


def test_health():
    """GET /health returns 200 with status ok."""
    client = TestClient(main.app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
