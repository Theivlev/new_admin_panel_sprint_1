from contextlib import contextmanager
import sqlite3


@contextmanager
def sqlite_cursor_context(conn: sqlite3.Connection):
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        yield cursor
    finally:
        cursor.close()
