from pages.page import *
from utils.filter_value import FilterValue as filt
from pages.acc_alter import *

class AccSetting:
    def run():
        choose = 0
        log_msg = ""

        while choose != -1:
            os.system('cls')
            account = AccSetting.__get_acc_details()

            try:
                choose = AccSetting.display(log_msg, account)
                filt.val_in_range(choose, 1, 3)
            except ValueError:
                log_msg = "Invalid Input"
            except OptionError as o:
                log_msg = o;
            else:
                opts = [ChangeUser, ChangePass, ChangePriv]
                opts[choose - 1].run()
                    
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
        return int(input("Input: "))
        
    def __get_acc_details():
        procedure = "getAccDetails"
        param = [Lib.logged]
        
        Lib.cursor().callproc(procedure, param)
        results = Lib.cursor().stored_results()

        account = next(results, None).fetchall()
        return account
