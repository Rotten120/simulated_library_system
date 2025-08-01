from pages.page import *
from mysql.connector.errors import IntegrityError

class Signup:
    def run():
        log_msg = ""
        signup_done = False

        while not signup_done:
            os.system('cls')
            log = Signup.display(log_msg)

            if log[0] == "-1":
                Lib.switch_page("main_menu")

            try:
                Lib.set("<signup>", log)
            except IntegrityError:
                log_msg = "Username already exists"
            else:
                signup_done = True
        Lib.switch_page("main_menu")

    def display(log_msg):
        print("Signup")
        print(log_msg)
        
        username = input("Username: ")
        passcode = input("Password: ")
        privilege = Signup.__get_privilege()
        return (username, passcode, privilege)

    
    def __get_privilege():
        print("Choose Borrowing Privilege:")
        print(" 1) Basic\n 2) Student")
        print(" 3) Instructor\n 4) Staff")
        
        choose = -1
        while not(1 <= choose <= 4):
            try: choose = int(input("Choose: "))
            except: continue
        
        return choose
