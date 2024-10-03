CREATE TABLE country (
  id INTEGER PRIMARY KEY NOT NULL,
  code TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  CHECK (length(code) = 3)
);

CREATE TABLE athlete (
  id INTEGER PRIMARY KEY NOT NULL,
  name TEXT NOT NULL,
  gender TEXT NOT NULL,
  country_id INTEGER NOT NULL REFERENCES country (id),
  CHECK (gender IN ('female', 'male'))
);

CREATE TABLE discipline (
  id INTEGER PRIMARY KEY NOT NULL,
  name TEXT NOT NULL
);

CREATE TABLE team (
  id INTEGER PRIMARY KEY NOT NULL,
  gender TEXT NOT NULL,
  country_id INTEGER NOT NULL REFERENCES country (id),
  discipline_id INTEGER NOT NULL REFERENCES discipline (id),
  CHECK (gender IN ('female', 'male', 'mixed'))
);

CREATE TABLE discipline_athlete (
  id INTEGER PRIMARY KEY NOT NULL,
  discipline_id INTEGER NOT NULL REFERENCES discipline (id),
  athlete_id INTEGER NOT NULL REFERENCES athlete (id)
);

CREATE TABLE event (
  id INTEGER PRIMARY KEY NOT NULL,
  discipline_id INTEGER NOT NULL REFERENCES discipline (id),
  name TEXT NOT NULL,
  gender TEXT NOT NULL,
  CHECK (gender IN ('female', 'male', 'mixed'))
);

CREATE TABLE medal (
  id INTEGER PRIMARY KEY NOT NULL,
  date DATE NOT NULL,
  type TEXT NOT NULL,
  event_id INTEGER NOT NULL REFERENCES event (id),
  athlete_id INTEGER REFERENCES athlete (id),
  team_id INTEGER REFERENCES team (id),
  CHECK (
    (athlete_id IS NOT NULL OR team_id IS NOT NULL) AND
    (type IN ('gold', 'silver', 'bronze')))
);
