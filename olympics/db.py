"""Database connection and low-level SQL requests."""

import sqlite3
from pathlib import Path


db = Path(__file__).parents[1] / 'database' / 'olympics.db'


def get_connection():
    """Get connection to database."""
    connection = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys')
    cursor.close()
    return connection


def get_countries(id=None):
    """Get list of countries.

    If id is not None, the list contains only the country with given id.

    """
    cursor = get_connection().cursor()
    if id is None:
        rows = cursor.execute('''
            SELECT *
            FROM country
        ''').fetchall()
    else:
        rows = cursor.execute('''
            SELECT *
            FROM country
            WHERE id = ?
        ''', (id,)).fetchall()
    cursor.close()
    return rows


def get_athletes(id=None):
    """Get list of athletes.

    If id is not None, the list contains only the athlete with given id.

    """
    cursor = get_connection().cursor()
    if id is None:
        rows = cursor.execute('''
            SELECT *
            FROM athlete
        ''').fetchall()
    else:
        rows = cursor.execute('''
            SELECT *
            FROM athlete
            WHERE id = ?
        ''', (id,)).fetchall()
    cursor.close()
    return rows


def get_disciplines(id=None):
    """Get list of disciplines.

    If id is not None, the list contains only the discipline with given id.

    """
    cursor = get_connection().cursor()
    if id is None:
        rows = cursor.execute('''
            SELECT *
            FROM discipline
        ''').fetchall()
    else:
        rows = cursor.execute('''
            SELECT *
            FROM discipline
            WHERE id = ?
        ''', (id,)).fetchall()
    cursor.close()
    return rows


def get_teams(id=None):
    """Get list of teams.

    If id is not None, the list contains only the team with given id.

    """
    cursor = get_connection().cursor()
    if id is None:
        rows = cursor.execute('''
            SELECT *
            FROM team
        ''').fetchall()
    else:
        rows = cursor.execute('''
            SELECT *
            FROM team
            WHERE id = ?
        ''', (id,)).fetchall()
    cursor.close()
    return rows


def get_events(id=None):
    """Get list of events.

    If id is not None, the list contains only the event with given id.

    """
    cursor = get_connection().cursor()
    if id is None:
        rows = cursor.execute('''
            SELECT *
            FROM event
        ''').fetchall()
    else:
        rows = cursor.execute('''
            SELECT *
            FROM event
            WHERE id = ?
        ''', (id,)).fetchall()
    cursor.close()
    return rows


def get_medals(id=None):
    """Get list of medals.

    If id is not None, the list contains only the medal with given id.

    """
    cursor = get_connection().cursor()
    if id is None:
        rows = cursor.execute('''
            SELECT *
            FROM medal
        ''').fetchall()
    else:
        rows = cursor.execute('''
            SELECT *
            FROM medal
            WHERE id = ?
        ''', (id,)).fetchall()
    cursor.close()
    return rows


def get_discipline_athletes(discipline_id):
    """Get athlete ids linked to given discipline id."""
    cursor = get_connection().cursor()
    rows = cursor.execute('''
        SELECT *
        FROM discipline_athlete
        WHERE discipline_id = ?
    ''', (discipline_id,)).fetchall()
    cursor.close()
    return rows


def get_top_countries(top=10):
    """Get medal count ranking of countries.

    Countries are ranked by gold medals, then silver medals, then bronze
    medals.

    Number of countries is limited to the given top number.

    """
    cursor = get_connection().cursor()
    rows = cursor.execute('''
        SELECT
            country.name,
            sum(CASE type WHEN 'gold' THEN 1 ELSE 0 END) AS gold,
            sum(CASE type WHEN 'silver' THEN 1 ELSE 0 END) AS silver,
            sum(CASE type WHEN 'bronze' THEN 1 ELSE 0 END) AS bronze
        FROM medal
        LEFT JOIN athlete
        ON medal.athlete_id = athlete.id
        LEFT JOIN team
        ON medal.team_id = team.id
        RIGHT JOIN country
        ON (country.id IN (team.country_id, athlete.country_id))
        GROUP BY country.id
        ORDER BY gold DESC, silver DESC, bronze DESC
        LIMIT ?
    ''', (top,)).fetchall()
    cursor.close()
    return rows


def get_collective_medals(team_id=None):
    """Get list of medals for team events.

    If team_id is not None, the list contains only the medals won by team with
    given id.

    """
    cursor = get_connection().cursor()
    sql = '''
        SELECT
            country.name,
            discipline.name AS discipline,
            event.name AS event,
            medal.type,
            medal.date
        FROM medal
        JOIN team
        ON medal.team_id = team.id
        JOIN country
        ON team.country_id = country.id
        JOIN event
        ON medal.event_id = event.id
        JOIN discipline
        ON event.discipline_id = discipline.id
    '''
    rows = cursor.execute(sql).fetchall()
    cursor.close()
    return rows


def get_top_collective(top=10):
    """Get medal count ranking of countries for team events.

    Number of countries is limited to the given top number.

    """
    cursor = get_connection().cursor()
    rows = cursor.execute('''
        SELECT
            country.name AS country,
            sum(1) AS medals
        FROM medal
        JOIN team
        ON medal.team_id = team.id
        JOIN country
        ON team.country_id = country.id
        GROUP BY country
        ORDER BY medals DESC
        LIMIT ?
    ''', (top,)).fetchall()
    cursor.close()
    return rows


def get_individual_medals(athlete_id=None):
    """Get list of medals for individual events.

    If athlete_id is not None, the list contains only the medals won by athlete
    with given id.

    """
    cursor = get_connection().cursor()
    sql = '''
        SELECT
            athlete.name,
            country.name AS country,
            discipline.name AS discipline,
            event.name AS event,
            medal.type,
            medal.date
        FROM medal
        JOIN athlete
        ON medal.athlete_id = athlete.id
        JOIN country
        ON athlete.country_id = country.id
        JOIN event
        ON medal.event_id = event.id
        JOIN discipline
        ON event.discipline_id = discipline.id
    '''
    if athlete_id is None:
        rows = cursor.execute(sql).fetchall()
    else:
        sql += 'WHERE athlete.id = ?'
        rows = cursor.execute(sql, (athlete_id,)).fetchall()
    cursor.close()
    return rows


def get_top_individual(top=10):
    """Get medal count ranking of athletes for individual events.

    Number of athletes is limited to the given top number.

    """
    cursor = get_connection().cursor()
    rows = cursor.execute('''
        SELECT
            athlete.name,
            athlete.gender,
            country.name AS country,
            sum(1) AS medals
        FROM medal
        JOIN athlete
        ON medal.athlete_id = athlete.id
        JOIN country
        ON athlete.country_id = country.id
        GROUP BY athlete.name, country
        ORDER BY medals DESC
        LIMIT ?
    ''', (top,)).fetchall()
    cursor.close()
    return rows
