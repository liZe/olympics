"""Web API."""

from fastapi import FastAPI

from . import db

app = FastAPI()


# Simple API entry points

@app.get("/countries/")
def countries(id: int | None = None):
    """List of all countries.

    If id is not None, the list contains only the country with given id.

    """
    return db.get_countries(id)


@app.get("/athletes/")
def athletes(id: int | None = None):
    """List of athletes.

    If id is not None, the list contains only the athlete with given id.

    """
    return db.get_athletes(id)


@app.get("/disciplines/")
def disciplines(id: int | None = None):
    """List of disciplines.

    If id is not None, the list contains only the discipline with given id.

    """
    return db.get_disciplines(id)


@app.get("/teams/")
def teams(id: int | None = None):
    """List of teams.

    If id is not None, the list contains only the team with given id.

    """
    return db.get_teams(id)


@app.get("/events/")
def events(id: int | None = None):
    """List of events.

    If id is not None, the list contains only the event with given id.

    """
    return db.get_events(id)


@app.get("/medals/")
def medals(id: int | None = None):
    """List of medals.

    If id is not None, the list contains only the medal with given id.

    """
    return db.get_medals(id)


@app.get("/discipline-athletes/{discipline_id}")
def discipline_athletes(discipline_id: int):
    """List of athlete ids linked to given discipline id."""
    return db.get_discipline_athletes(discipline_id)


# Complex API entry points

@app.get("/top-countries/")
def top_countries(top: int | None = 10):
    """Medal count ranking of countries.

    Countries are ranked by gold medals, then silver medals, then bronze
    medals.

    Number of countries is limited to the given top number.

    """
    return db.get_top_countries(top)


@app.get("/collective-medals/")
def collective_medals(team_id: int | None = None):
    """List of medals for team events.

    If team_id is not None, the list contains only the medals won by team with
    given id.

    """
    return db.get_collective_medals(team_id)


@app.get("/top-collective/")
def top_collective(top: int | None = 10):
    """Medal count ranking of countries for team events.

    Number of countries is limited to the given top number.

    """
    return db.get_top_collective(top)


@app.get("/individual-medals/")
def individual_medals(athlete_id: int | None = None):
    """List of medals for individual events.

    If athlete_id is not None, the list contains only the medals won by athlete
    with given id.

    """
    return db.get_individual_medals(athlete_id)


@app.get("/top-individual/")
def top_individual(top: int | None = 10):
    """Medal count ranking of athletes for individual events.

    Number of athletes is limited to the given top number.

    """
    return db.get_top_individual(top)
