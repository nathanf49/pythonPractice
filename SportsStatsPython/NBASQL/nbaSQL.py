import sqlite3
from sqlite3 import Error

def create_connection(path):

    connection = None

    try:

        connection = sqlite3.connect(path)

        print("Connection to SQLite DB successful")

    except Error as e:

        print(f"The error '{e}' occurred")


    return connection

def print_sql(path):
    connection = sqlite3.connect(":memory:")

    cursor = connection.cursor()


    sql_file = open(str(path))

    sql_as_string = sql_file.read()

    cursor.executescript(sql_as_string)


    for row in cursor.execute("SELECT * FROM airports"):

        print(row)