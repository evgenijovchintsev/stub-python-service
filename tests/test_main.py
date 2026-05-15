from main import app
import pytest

@pytest.mark.asyncio
def test_health():
    response = await app.get("/health")
    assert response.status_code == 200