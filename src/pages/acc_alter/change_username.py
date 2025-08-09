from pages.page import *
from mysql.connector.errors import IntegrityError
from mysql.connector import Error

class ChangeUser:
    def run():
        inp = ("",)
        log_msg = " "

        while log_msg[0] != 'S':
            os.system('cls')
            inp = ChangeUser.display(log_msg)

            if inp[0] == "-1":
                break
            
            log_msg = ChangeUser.logic(inp)
        return

    def logic(inp):
        log_msg = "Successfully changed username"
        try:
            ChangeUser.__change_user(inp)
        except IntegrityError:
            log_msg = "Username already exist"
        except LibSysError as l:
            log_msg = str(l)
        return log_msg

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

        try:
            Lib.cursor().callproc(procedure, param)
        except Error as e:
            LibErrors.throw(e)
            
        Lib.commit()

        
