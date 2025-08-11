from pages.page import *
from mysql.connector import Error
from utils.filter_value import FilterValue as filt

class ChangePriv:
    def run(args = []):
        inp = ("",)
        log_msg = " "

        while log_msg[0] != 'S':
            os.system('cls')
            inp = ChangePriv.display(log_msg)

            if inp[0] == "-1":
                break
            
            log_msg = ChangePriv.logic(inp)
        return

    def logic(inp):
        log_msg = "Successfully changed privilege"
        try:
            param = (int(inp[0]), inp[1])
            filt.val_in_range(param[0], 1, 4)
            ChangePriv.__change_priv(param)
        except ValueError:
            log_msg = "Invalid Input"
        except LibSysError as l:
            log_msg = str(l)
        return log_msg

    def display(log_msg):
        print("Changing Privilege")
        print(log_msg)
        print("1 Baisc")
        print("2 Student")
        print("3 Instructor")
        print("4 Staff")
        print()
        privID = input("Input: ")
        code = input("Input password: ")
        return (privID, code)

    def __change_priv(inp):
        procedure = "changePrivilege"
        param = [Lib.logged, inp[0], inp[1]]

        try:
            Lib.cursor().callproc(procedure, param)
        except Error as e:
            LibErrors.throw(e)
        Lib.commit()
        
