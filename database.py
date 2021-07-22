# importing database sqlite

import sqlite3

# table creation , id has a auto-incremental funtionality in sqlite
CREATE_BEANS_TABLE = "CREATE TABLE IF NOT EXISTS beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT, " \
                     "rating INTEGER); "

# here we have to pass three values from user side
INSERT_BEAN = "INSERT INTO beans (name, method, rating) VALUES(?, ?, ?);"

# get all the beans
GET_ALL_BEANS = "SELECT * FROM beans;"

GET_BEANS_BY_NAME = "SELECT * FROM beans WHERE name = ?;"

GET_BEST_PREPARATION_FOR_BEAN = """
SELECT * FROM beans
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;"""


# creating a Database
# sqlite3 works from file

def connect():
    return sqlite3.connect("data.db")
    # connection = sqlite3.connect("data.db")


# execute the query for set up out db connection
def create_table(connection):
    with connection:
        return connection.execute(CREATE_BEANS_TABLE)


def add_bean(connection, name, method, rating):
    with connection:
        return connection.execute(INSERT_BEAN, (name, method, rating))


def get_all_beans(connection):
    with connection:
        return connection.execute(GET_ALL_BEANS).fetchall()


def get_beans_by_name(connection, name):
    with connection:
        return connection.execute(GET_BEANS_BY_NAME, (name,)).fetchall()


def get_best_preparation_for_bean(connection, name):
    with connection:
        return connection.execute(GET_BEST_PREPARATION_FOR_BEAN, (name,)).fetchall()

