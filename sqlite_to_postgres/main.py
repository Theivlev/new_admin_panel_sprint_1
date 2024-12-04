import logging
import os

import psycopg
from psycopg import ClientCursor
from psycopg.rows import dict_row

import sqlite3

from config import DATABASE_CONFIG
from load_data import load_from_sqlite


if __name__ == '__main__':
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    db_path = os.path.join(basedir, 'sqlite_to_postgres', 'db.sqlite')

    dsl = DATABASE_CONFIG['postgres']
    try:

        with sqlite3.connect(db_path) as sqlite_conn, psycopg.connect(
            **dsl, row_factory=dict_row, cursor_factory=ClientCursor
        ) as pg_conn:
            load_from_sqlite(sqlite_conn, pg_conn)

    except sqlite3.Error as error:
        logging.error(f'Ошибка при работе с SQLite: {error}')

    except psycopg.Error as error:
        logging.error(f'Ошибка при работе с PostgreSQL: {error}')

    except Exception as error:
        logging.error(f'Неизвестная ошибка: {error}')

    else:
        logging.info('🎉  Данные успешно перенесены!!!')
