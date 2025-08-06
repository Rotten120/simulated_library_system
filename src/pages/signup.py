from pages.page import *
from mysql.connector.errors import IntegrityError

class Signup:
    def run():
        log_msg = " "

        while log_msg[0] != 'S':
            os.system('cls')
            log = Signup.display(log_msg)

            if log[0] == "-1":
                break
            
            log_msg = Signup.logic(log)
        return

    def logic(log):
        log_msg = "Successfully signuped"
        try:
            Lib.set("<signup>", log)
        except IntegrityError:
            log_msg = "Username already exists"
        return log_msg

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
