import MySQLdb

from app.data.exceptions.DBException import DBException

conn = None

db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '',
    'db': 'test'
}

def connect_to_db():
    try:
        conn = MySQLdb.connect(**db_config)
        return conn
    except Exception as e:
        print(e)
        raise DBException