from fastapi.testclient import TestClient
from app.interfaces.api import app

client = TestClient(app)

def test_search_valid_query():
    response = client.get("/search?q=test")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_search_empty_query():
    response = client.get("/search?q=%20")
    assert response.status_code == 422  

def test_search_special_characters():
    response = client.get("/search?q=$$$")
    assert response.status_code == 400  