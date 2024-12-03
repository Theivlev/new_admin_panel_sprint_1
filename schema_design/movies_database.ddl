CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    rating DECIMAL(2, 1),
    type TEXT NOT NULL,
    created timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    modified timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS content.genre (
    id uuid PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    modified timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_genre_name ON content.genre(name);


CREATE TABLE IF NOT EXISTS content.genre_film_work (
    id uuid PRIMARY KEY,
    genre_id uuid,
    film_work_id uuid,
    created TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (genre_id) REFERENCES content.genre(id) ON DELETE CASCADE,
    FOREIGN KEY (film_work_id) REFERENCES content.film_work(id) ON DELETE CASCADE
);


CREATE INDEX idx_genre_film_work_genre_id ON content.genre_film_work(genre_id);
CREATE INDEX idx_genre_film_work_film_work_id ON content.genre_film_work(film_work_id);



CREATE TABLE IF NOT EXISTS content.person (
    id uuid PRIMARY KEY,
    full_name TEXT NOT NULL,
    created timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    modified timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);


CREATE INDEX idx_person_full_name ON content.person(full_name);


CREATE TABLE IF NOT EXISTS content.person_film_work (
    id uuid PRIMARY KEY,
    role TEXT NOT NULL,
    created timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    person_id uuid,
    film_work_id uuid,
    FOREIGN KEY (person_id) REFERENCES content.person(id) ON DELETE CASCADE,
    FOREIGN KEY (film_work_id) REFERENCES content.film_work(id) ON DELETE CASCADE
);


CREATE INDEX idx_person_film_work_person_id ON content.person_film_work(person_id);
CREATE INDEX idx_person_film_work_film_work_id ON content.person_film_work(film_work_id);

CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.modified = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER trg_film_work_modified
BEFORE UPDATE ON content.film_work
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER trg_genre_modified
BEFORE UPDATE ON content.genre
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER trg_person_modified
BEFORE UPDATE ON content.person
FOR EACH ROW EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER trg_person_film_work_modified
BEFORE UPDATE ON content.person_film_work
FOR EACH ROW EXECUTE FUNCTION update_modified_column();