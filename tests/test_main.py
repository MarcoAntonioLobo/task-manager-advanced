from fastapi.testclient import TestClient
from app.main import app  # ajuste esse import conforme sua estrutura real

client = TestClient(app)

def test_read_healthcheck():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
