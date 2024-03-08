import sqlite3
from sqlite3 import Error

# Creates a connection to the given database
def create_connection(db_file):
    con = None
    try:
        con = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return con