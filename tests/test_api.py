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

def test_events():
    response = client.get('/events/')
    assert response.status_code == 200
    assert len(response.json()) > 20  

def test_medals():
    response = client.get('/medals/')
    assert response.status_code == 200
    assert len(response.json()) > 10  

def test_discipline_athletes():
    discipline_id = 1
    response = client.get(f'/discipline-athletes/{discipline_id}')
    assert response.status_code == 200
    assert len(response.json()) > 0  
    
def test_top_countries():
    response = client.get('/top-countries/')
    assert response.status_code == 200
    assert len(response.json()) > 5 

def test_collective_medals():
    team_id = 1
    response = client.get(f'/collective-medals/?team_id={team_id}')
    assert response.status_code == 200
    assert len(response.json()) > 0  
    
def test_top_collective():
    response = client.get('/top-collective/')
    assert response.status_code == 200
    assert len(response.json()) > 5  

def test_individual_medals():
    athlete_id = 1
    response = client.get(f'/individual-medals/?athlete_id={athlete_id}')
    assert response.status_code == 200
    assert len(response.json()) > 0  
    
def test_top_individual():
    response = client.get('/top-individual/')
    assert response.status_code == 200
    assert len(response.json()) > 5  

