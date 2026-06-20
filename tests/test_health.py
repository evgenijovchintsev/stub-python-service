"""Tests for the /health endpoint."""

from fastapi.testclient import TestClient
import main
from utils import hello


def test_health():
    """GET /health returns 200 with status ok."""
    client = TestClient(main.app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_hello():
    """hello() returns 'hello world'."""
    assert hello() == "hello world"
