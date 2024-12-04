import logging
import sqlite3
from dataclasses import asdict
from typing import Generator, List

import psycopg
from psycopg import connection as _connection

from models import (
    FilmWork,
    Genre,
    GenreFilmWork,
    PersonFilmWork,
    Person
)

from utils import sqlite_cursor_context


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


BATCH_SIZE = 100

DATA_CLASSES = [FilmWork, Genre, GenreFilmWork, Person, PersonFilmWork]


def extract_data(sqlite_cursor: sqlite3.Cursor, table: str) -> Generator[List[sqlite3.Row], None, None]:
    logger.info(f"Начало извлечения данных из таблицы {table}.")
    try:
        sqlite_cursor.execute(f'SELECT * FROM {table}')
        while results := sqlite_cursor.fetchmany(BATCH_SIZE):
            logger.info(f"Извлечено {len(results)} записей из таблицы {table}.")
            yield results
    except sqlite3.Error as error:
        logger.error(f"Ошибка при извлечении данных из таблицы {table} : {error}")


def transform_data(sqlite_cursor: sqlite3.Cursor):

    for data_class in DATA_CLASSES:
        table_name = data_class.__table_name__
        logger.info(f"Начало трансформации данных из таблицы {table_name}.")
        try:
            for batch in extract_data(sqlite_cursor, table_name):
                logger.info(f"Преобразование данных из таблицы {table_name}.")
                yield [data_class(**{column: row[column] for column in row.keys()}) for row in batch]
        except Exception as error:
            logger.error(f'Ошибка преобразования данных из таблицы {table_name}: {error}')


def load_data(sqlite_cursor: sqlite3.Cursor, pg_cursor: psycopg.Cursor):
    for batch in transform_data(sqlite_cursor):
        for dto_instance in batch:

            table_name = dto_instance.__table_name__
            fields = [field for field in dto_instance.__dataclass_fields__ if field != '__table_name__']
            values = asdict(dto_instance)

            placeholders = ', '.join(['%s'] * len(fields))
            columns = ', '.join(fields)
            query = f'INSERT INTO content.{table_name} ({columns}) VALUES ({placeholders}) ON CONFLICT (id) DO NOTHING'
            try:
                pg_cursor.execute(query, [values[field] for field in fields])
                logger.info(f"Успешно вставлена запись в таблицу {table_name}. ID: {values['id']}")
            except psycopg.Error as error:
                logger.error(f'Ошибка вставки данных в таблицу {table_name}: {error}')


def load_from_sqlite(sqlite_conn: sqlite3.Connection, pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""
    with sqlite_cursor_context(sqlite_conn) as sqlite_cursor:
        with pg_conn.cursor() as pg_cursor:
            try:
                load_data(sqlite_cursor, pg_cursor)
            except Exception as error:
                logger.error(f"Ошибка загрузки данных из SQLite в Postgres: {error}")
