from fastapi.testclient import TestClient
from app import app
client = TestClient(app)
def test_homepage():
    response = client.get("/") 
    assert response.status_code  == 200
    assert "<title>Tejas Portfolio</title>" in response.text

