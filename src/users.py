from models import database


class Users(object):
    def __init__(self, username, password, first_name, last_name):
        self.name = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def sign(first_name, last_name, username, password):
        database.create_user(first_name, last_name, username, password)

    @staticmethod
    def login(username, password):
        user = database.check_user(username)
        username,pass_word = user
        # print(username,pass_word)
        if pass_word == password:
            return True
        else:
            return False

    @staticmethod
    def lop():
        if Users.login("jamesebere@gmail.com", "prick123"):
            print("users ")
        else:
            print("kop")
        # if user:
        #     for user_name, pass_word in user:
        #         if password == pass_word:
        #             print("Madness")
        # else:
        #     return print("good")


# Users.lop()
