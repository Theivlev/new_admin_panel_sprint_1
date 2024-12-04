import os
from dotenv import load_dotenv


load_dotenv()

DATABASE_CONFIG = {
    'sqlite_db_path': 'sqlite_to_postgres/db.sqlite',
    'postgres': {
        'dbname': os.getenv('POSTGRES_DB'),
        'user': os.getenv('POSTGRES_USER'),
        'password': os.getenv('POSTGRES_PASSWORD'),
        'host': os.getenv('POSTGRES_HOST'),
        'port': os.getenv('POSTGRES_PORT'),
    }
}
