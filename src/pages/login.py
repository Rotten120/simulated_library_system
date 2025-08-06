from pages.page import *
from mysql.connector import Error

class Login:
    def run():
        log_msg = ""

        while Lib.logged <= 0:
            os.system('cls')
            log = Login.display(log_msg)

            if log[0] == "-1":
                break
            
            log_msg = Login.logic(log)
        Lib.switch_page("menu")

    def logic(log):
        log_msg = "Successfully logged as " + log[0]
        try:
            Lib.logged = Lib.get("<login>", log)[0][0]
        except ValueNotFoundError as v:
            log_msg = v.root("Username")
        except MisMatchError as m:
            log_msg = m.root("Password")
        return log_msg

    def display(log_msg):
        print("Login")
        print(log_msg)
        
        username = input("Username: ")
        passcode = input("Password: ")
        return (username, passcode)
