from pages.page import *
from mysql.connector import Error

class ChangePass:
    def run():
        inp = ("",)
        log_msg = ""

        while inp[0] != "-1":
            os.system('cls')

            try:
                inp = ChangePass.display(log_msg)
                ChangePass.__change_pass(inp)
            except MisMatchError as m:
                log_msg = m.root("Password")
            else:
                break

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

        
