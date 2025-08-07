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
            
            out = Signup.logic(log)
            log_msg = out[0]
        return

    def logic(log):
        log_msg = "Successfully signuped"
        try:
            Lib.set("<create_account>", log)
            lib_log = Lib.get("<get_account_id>", log)
        except IntegrityError:
            log_msg = "Username already exists"
        else:
            return (log_msg, lib_log)
        return (log_msg, 0)

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
