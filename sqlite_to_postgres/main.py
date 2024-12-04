import sqlite3
import psycopg
from config import DATABASE_CONFIG
from load_data import load_from_sqlite
from psycopg.rows import dict_row
from psycopg import ClientCursor

import os
if __name__ == '__main__':
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    db_path = os.path.join(basedir, 'sqlite_to_postgres', 'db.sqlite')

    dsl = DATABASE_CONFIG['postgres']

    with sqlite3.connect(db_path) as sqlite_conn, psycopg.connect(
        **dsl, row_factory=dict_row, cursor_factory=ClientCursor
    ) as pg_conn:
        load_from_sqlite(sqlite_conn, pg_conn)

    print('🎉 Данные успешно перенесены !!!')
