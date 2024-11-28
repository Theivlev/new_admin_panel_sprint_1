CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    rating FLOAT,
    type TEXT NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre (
    id uuid PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre_film_work (
    id uuid PRIMARY KEY,
    genre_id uuid,
    film_work_id uuid,
    FOREIGN KEY (genre_id) REFERENCES content.genre(id) ON DELETE CASCADE,
    FOREIGN KEY (film_work_id) REFERENCES content.film_work(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS content.person (
    id uuid PRIMARY KEY,
    full_name TEXT NOT NULL,
    created timestamp with time zone,
    modified timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.person_film_work (
    id uuid PRIMARY KEY,
    role TEXT NOT NULL,
    created timestamp with time zone,
    person_id uuid,
    film_work_id uuid,
    FOREIGN KEY (person_id) REFERENCES content.person(id) ON DELETE CASCADE,
    FOREIGN KEY (film_work_id) REFERENCES content.film_work(id) ON DELETE CASCADE
);
