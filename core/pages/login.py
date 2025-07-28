from core.pages.base_imports import *
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
                if e.errno == 50001:
                    log_msg = "Username does not exist"
                if e.errno == 50002:
                    log_msg = "Incorrect Password"
            else:
                break
        Lib.switch_page("menu")

    def display(log_msg):
        print("Login")
        print(log_msg)
        
        username = input("Username: ")
        passcode = input("Password: ")
        return (username, passcode)
