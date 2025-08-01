from pages.page import *
from mysql.connector.errors import IntegrityError
from mysql.connector import Error

class ChangeUser:
    def run():
        inp = ("",)
        log_msg = ""

        while inp[0] != "-1":
            os.system('cls')

            try:
                inp = ChangeUser.display(log_msg)
                ChangeUser.__change_user(inp)
            except IntegrityError:
                log_msg = "Username already exist"
            except Error as e:
                if e.errno == 50002:
                    log_msg = "Incorrect Password"
            else:
                break

    def display(log_msg):
        print("Changing Username")
        print(log_msg)
        user = input("New username: ")
        code = input("Input password: ")
        return (user, code)

    def __change_user(inp):
        username = inp[0]
        passcode = inp[1]
        procedure = "changeUsername"
        param = [Lib.logged, username, passcode]

        Lib.cursor().callproc(procedure, param)
        Lib.commit()

        
