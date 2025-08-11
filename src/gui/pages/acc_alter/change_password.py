from pages.page import *
from mysql.connector import Error

class ChangePass:
    def run(args = []):
        inp = ("",)
        log_msg = " "

        while log_msg[0] != 'S':
            os.system('cls')
            inp = ChangePass.display(log_msg)

            if inp[0] == "-1":
                break
            
            log_msg = ChangePass.logic(inp)
        return

    def logic(inp):
        log_msg = "Successfully changed password"
        try:
            ChangePass.__change_pass(inp)
        except LibSysError as l:
            log_msg = str(l)
        return log_msg

    def display(log_msg):
        print("Changing Password")
        print(log_msg)
        new_code = input("New Password: ")
        old_code = input("Input Old Password: ")
        return (new_code, old_code)

    def __change_pass(inp):
        new_passcode = inp[0]
        old_passcode = inp[1]
        procedure = "changePassword"
        param = [Lib.logged, new_passcode, old_passcode]

        try:
            Lib.cursor().callproc(procedure, param)
        except Error as e:
            LibErrors.throw(e)
        Lib.commit()

        
