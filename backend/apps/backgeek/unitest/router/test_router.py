from fastapi.testclient import TestClient

from router.router import app

client = TestClient(app)


def test_router_alive():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
