from sqlite3 import connect

connection = connect('sales.db')
cursor = connection.cursor()
CREATE_USERS_TABLE = """Create table if not Exists users
                       (id Integer primary key,
                        first_name Text,
                        last_name Text,
                        user_name Text, 
                        password Text
                        );"""
CREATE_USER = """INSERT INTO users (first_name,last_name, user_name,password) VALUES(?,?,?,?); """

CHECK_USER = """SELECT user_name,password from users where user_name=? """


def create_table():
    with connection:
        cursor.execute(CREATE_USERS_TABLE)


def create_user(first_name, last_name, user_name, password):
    with connection:
        cursor.execute(CREATE_USER, (first_name, last_name, user_name, password))


def check_user(user_name):
    with connection:
        cursor.execute(CHECK_USER, (user_name,))
        return cursor.fetchone()
