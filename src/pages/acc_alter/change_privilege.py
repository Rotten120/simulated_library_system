from pages.page import *
from mysql.connector import Error
from utils.filter_value import FilterValue as filt

class ChangePriv:
    def run():
        inp = (0,)
        log_msg = ""

        while inp[0] != -1:
            os.system('cls')

            try:
                inp = ChangePriv.display(log_msg)
                choose = filt.val_in_range(inp[0], 1, 4)
                ChangePriv.__change_priv(inp)
            except ValueError:
                log_msg = "Invalid Input"
            except OptionError as o:
                log_msg = o
                if inp[0] == -1: continue
            except MisMatchError as m:
                log_msg = m.root("Password")
            else:
                break

    def display(log_msg):
        print("Changing Privilege")
        print(log_msg)
        print("1 Baisc")
        print("2 Student")
        print("3 Instructor")
        print("4 Staff")
        print()
        privID = int(input("Input: "))
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
        
