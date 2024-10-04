from olympics import db


def test_countries():
    rows = db.get_countries()
    assert len(rows) > 100

def test_countries_avec_id():
    rows = db.get_countries(id=1)
    assert len(rows) == 1
       
def test_athletes():
    rows = db.get_athletes()
    assert len(rows) 
    