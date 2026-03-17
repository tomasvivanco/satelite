from fastapi.testclient import TestClient

from app.api.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_analysis_run() -> None:
    response = client.post(
        "/analysis/run",
        json={"input_type": "coordinates", "latitude": 10.0, "longitude": 20.0},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "completed"
    assert "metrics" in body
