from olympics import db


def test_countries():
    rows = db.get_countries()
    assert len(rows) > 100
