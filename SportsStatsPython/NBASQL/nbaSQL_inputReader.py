import sqlite3
import pandas as pd

def create_connection(path):

    connection = None

    try:

        connection = sqlite3.connect(path)

        print("Connection to SQLite DB successful")

    except sqlite3.Error as e:

        print(f"The error '{e}' occurred")


    return connection

def print_sql(path):
    connection = sqlite3.connect(":memory:")

    cursor = connection.cursor()


    sql_file = open(path)

    sql_as_string = sql_file.read()

    cursor.executescript(sql_as_string)


    for row in cursor.execute("SELECT * FROM players"):

        print(row)


def parseSQL(file):
    with open(file, 'r') as f:
        data = f.read()
        f.close()
    data = data.split('\n')
    for player in data:
        if 'INSERT INTO' not in player:  # player lines start with INSERT INTO
            pass

        else:
            player = player.split(',')
            playerAttributes = {}
            for i in range(1, int(len(player) / 2)):
                playerAttributes[player[i]] = player[len(player) + i]
            pass






if __name__ == "__main__":
    import sys
    sys.path.append('/home/nathan/Documents/pythonPractice/SportsStatsPython/')
    import nbaClasses as nba
    file = 'nba_players.sql'
    parseSQL(file)
