from olympics import db


def test_countries():
    rows = db.get_countries()
    assert len(rows) > 100

def test_countries_avec_id():
    rows = db.get_countries(1)
    assert len(rows) == 1
       
def test_athletes():
    rows = db.get_athletes()
    assert len(rows) > 100
    
def test_athletes_avec_id():
    rows = db.get_athletes(1)
    assert len(rows) == 1
    
def test_disciplines():
    rows = db.get_disciplines()
    assert len(rows) >= 39
    
def test_disciplines_avec_id():
    rows = db.get_disciplines(id)
    assert len(rows) == 1
    
def test_teams():
    rows = db.get_teams()
    assert len(rows) >= 45
    
def test_teams_avec_id():
    rows = db.get_teams(1)
    assert len(rows) == 1
    
def test_events():
    rows = db.get_events()
    assert len(rows) >= 45
    
def test_events_avec_id():
    rows = db.get_events(1)
    assert len(rows) == 1
    
def test_get_medals():
    rows = db.get_medals()
    assert len(rows) >= 45
    
def test_get_medals_avec_id():
    rows = db.get_medals(1)
    assert len(rows) == 1
    
def test_get_discipline_athletes_avec_id():
    rows = db.get_discipline_athletes(1)
    assert len(rows) == 291

def test_get_collective_medals():
    rows = db.get_collective_medals()
    assert len(rows) > 0  
   
def test_get_collective_medals_with_team_id():
    rows = db.get_collective_medals(1)
    assert len(rows) == 290
    
def test_get_top_collective():
    rows = db.get_top_collective()
    assert len(rows) > 0  
   
def test_get_top_collective_with_team_id():
    rows = db.get_top_collective(1)
    assert len(rows) == 1
    
def test_get_individual_medals():
    rows = db.get_individual_medals()
    assert len(rows) > 0  
   
def test_get_individual_medals_with_team_id():
    rows = db.get_individual_medals(1)
    assert len(rows) == 1
    
def test_get_top_individual():
    rows = db.get_top_individual()
    assert len(rows) > 0  
   
def test_get_top_individual_with_team_id():
    rows = db.get_top_individual(1)
    assert len(rows) == 1
    

    
    
    
    

    
    