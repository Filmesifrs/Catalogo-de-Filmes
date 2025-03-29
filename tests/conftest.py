import psycopg2
from psycopg2 import sql

def get_db_connection():
    return psycopg2.connect(
        dbname="test_db",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
