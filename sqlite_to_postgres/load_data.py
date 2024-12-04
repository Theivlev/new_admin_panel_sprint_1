import sqlite3
import psycopg
from psycopg import connection as _connection
from dataclasses import asdict
from typing import Generator, List
from utils import sqlite_cursor_context
from models import (
    FilmWork,
    Genre,
    GenreFilmWork,
    PersonFilmWork,
    Person
    )

BATCH_SIZE = 100

DATA_CLASSES = [FilmWork, Genre, GenreFilmWork, Person, PersonFilmWork]


def extract_data(sqlite_cursor: sqlite3.Cursor, table: str) -> Generator[List[sqlite3.Row], None, None]:
    sqlite_cursor.execute(f'SELECT * FROM {table}')
    while results := sqlite_cursor.fetchmany(BATCH_SIZE):
        yield results


def transform_data(sqlite_cursor: sqlite3.Cursor):

    for data_class in DATA_CLASSES:
        table_name = data_class.__table_name__
        for batch in extract_data(sqlite_cursor, table_name):
            yield [data_class(**{column: row[column] for column in row.keys()}) for row in batch]


def load_data(sqlite_cursor: sqlite3.Cursor, pg_cursor: psycopg.Cursor):
    for batch in transform_data(sqlite_cursor):
        for dto_instance in batch:

            table_name = dto_instance.__table_name__
            fields = [field for field in dto_instance.__dataclass_fields__ if field != '__table_name__']
            values = asdict(dto_instance)

            placeholders = ', '.join(['%s'] * len(fields))
            columns = ', '.join(fields)

            query = f'INSERT INTO content.{table_name} ({columns}) VALUES ({placeholders}) ON CONFLICT (id) DO NOTHING'
            pg_cursor.execute(query, [values[field] for field in fields])


def load_from_sqlite(sqlite_conn: sqlite3.Connection, pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""
    with sqlite_cursor_context(sqlite_conn) as sqlite_cursor:
        with pg_conn.cursor() as pg_cursor:
            load_data(sqlite_cursor, pg_cursor)


# def test_transfer(sqlite_cursor: sqlite3.Cursor, pg_cursor: psycopg.Cursor):
#     sqlite_cursor.execute('SELECT * FROM students')

#     while batch := sqlite_cursor.fetchmany(BATCH_SIZE):
#         original_students_batch = [Student(**dict(student)) for student in batch]
#         ids = [student.id for student in original_students_batch]

#         pg_cursor.execute('SELECT * FROM students WHERE id = ANY(%s)', [ids])
#         transferred_students_batch = [Student(**student) for student in pg_cursor.fetchall()]

#         assert len(original_students_batch) == len(transferred_students_batch)
#         assert original_students_batch == transferred_students_batch
