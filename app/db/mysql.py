import MySQLdb
from MySQLdb import Connection

from app.data.exceptions.DBException import DBException

conn: Connection = None

db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '',
    'db': 'test'
}

def connect_to_db():
    try:
        conn: Connection = MySQLdb.connect(**db_config)
        return conn
    except Exception as e:
        print(e)
        raise DBException