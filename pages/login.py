from pages.page import *
from mysql.connector import Error

class Login:
    def run():
        log_msg = ""

        while Lib.logged <= 0:
            os.system('cls')
            log = Login.display(log_msg)

            if log[0] == "-1":
                Lib.switch_page("main_menu")

            try:
                Lib.logged = Lib.get("<login>", log)[0][0]
            except Error as e:
                Login.check_exceptions(e.errno)
            except ValueNotFoundError as v:
                log_msg = v
            except MisMatchError as m:
                log_msg = m
            else:
                break
        Lib.switch_page("menu")

    def display(log_msg):
        print("Login")
        print(log_msg)
        
        username = input("Username: ")
        passcode = input("Password: ")
        return (username, passcode)

    def check_exceptions(errno):
        if errno == 50001:
            raise ValueNotFoundError("Username")
        if errno == 50002:
            raise MisMatchError("Password")
