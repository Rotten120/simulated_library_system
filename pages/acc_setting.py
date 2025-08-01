from pages.page import *
from utils.filter_value import FilterValue as filt
from pages.acc_alter import *

class AccSetting:
    def run():
        inp = 0
        log_msg = ""

        while inp != -1:
            os.system('cls')
            account = AccSetting.__get_acc_details()

            try:
                inp = int(AccSetting.display(log_msg, account))
                choose = filt.val_in_range(inp, 1, 3)
            except ValueError:
                log_msg = "Invalid Input"
            except OptionError as o:
                log_msg = o;
            else:
                if inp == 1:
                    ChangeUser.run()
                if inp == 2:
                    ChangePass.run()
                if inp == 3:
                    ChangePriv.run()
                    
        Lib.switch_page("menu")

    def display(log_msg, account):
        layout = "{:<6} {:<15} {:<15} {:<10}"
        header = ["ID", "USERNAME", "PASSWORD", "PRIVILEGE"]
        print(layout.format(*header), end = "\n")

        li_account = list(account[0])
        li_account[2] = len(li_account[2]) * '*'
        print(layout.format(*li_account), end = "\n\n")
        
        print(log_msg)

        print("1 Change username")
        print("2 Change password")
        print("3 Change privilege")
        return input("Input: ")
        
    def __get_acc_details():
        procedure = "getAccDetails"
        param = [Lib.logged]
        
        Lib.cursor().callproc(procedure, param)
        results = Lib.cursor().stored_results()

        account = next(results, None).fetchall()
        return account
