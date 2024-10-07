from fastapi.testclient import TestClient
from olympics import api

client = TestClient(api.app)

def test_countries():
    response = client.get('/countries/')
    assert response.status_code == 200
    assert len(response.json()) > 100

def test_athletes():
    response = client.get('/athletes/')
    assert response.status_code == 200
    assert len(response.json()) > 100  

def test_disciplines():
    response = client.get('/disciplines/')
    assert response.status_code == 200
    assert len(response.json()) > 10  

def test_teams():
    response = client.get('/teams/')
    assert response.status_code == 200
    assert len(response.json()) > 5  

