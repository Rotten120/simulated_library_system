from pages.page import *
from mysql.connector import Error

class DeleteAcc:
    def run(args = []):
        inp = ("",)
        log_msg = " "

        while log_msg[0] != 'S':
            os.system('cls')
            inp = DeleteAcc.display(log_msg)

            if inp[0] == "-1":
                break

            log_msg = DeleteAcc.logic(inp)
        else:
            Lib.switch_page("main_menu")
        return

    def logic(inp):
        log_msg = "Successfully deleted password"
        try:
            if not DeleteAcc.confirm_delete(inp[1]):
                return "Account deletion cancelled"
            DeleteAcc.__delete_acc(inp[0])
        except ValueError as v:
            log_msg = str(v)
        except LibSysError as l:
            log_msg = str(l)
        return log_msg
            
    def display(log_msg):
        print("Deleting Account")
        print(log_msg)
        password = input("Input Password: ")
        confirm = input("Are you sure? [y/n]: ")
        return (password, confirm)

    def confirm_delete(confirm):
        if confirm == 'y':
            return True
        elif confirm == 'n':
            return False
        else:
            raise ValueError("Confirmation not [y/n]")

    def __delete_acc(passcode):
        procedure = "deleteAccount"
        param = [Lib.logged, passcode]

        try:
            Lib.cursor().callproc(procedure, param)
        except Error as e:
            LibErrors.throw(e)
        Lib.commit()
        
