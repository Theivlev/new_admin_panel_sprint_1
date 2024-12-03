import sqlite3
from contextlib import contextmanager  


db_path = 'C:/Users/Alexey/Dev/new_admin_panel_sprint_1/sqlite_to_postgres/db.sqlite'


@contextmanager
def conn_context(db_path: str):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


with conn_context(db_path) as conn:
    curs = conn.cursor()
    curs.execute("SELECT * FROM film_work;")
    data = curs.fetchall()
    print(dict(data[0]))
