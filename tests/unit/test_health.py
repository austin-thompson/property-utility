from fastapi.testclient import TestClient

from property_utility.api.app import app

client = TestClient(app)


def test_health_live() -> None:
    response = client.get("/health/live")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_ready_returns_503_without_database() -> None:
    response = client.get("/health/ready")
    assert response.status_code == 503
    assert response.json() == {"detail": "database unavailable"}
