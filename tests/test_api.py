from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict():
    response = client.post("/predict", json={"x": 3})
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert data["prediction"] == 7.0
