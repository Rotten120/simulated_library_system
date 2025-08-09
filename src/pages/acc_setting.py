from pages.page import *
from utils.filter_value import FilterValue as filt
from pages.acc_alter import *

class AccSetting:
    def run(args = []):
        log_msg = ""

        while True:
            os.system('cls')
            account = Lib.get("<get_account>", (Lib.logged,))

            inp = AccSetting.display(log_msg, account)
            out = AccSetting.filter(inp)

            log_msg = out[0]
            opt = out[1]

            if opt == 5:
                break
            if opt != -1:
                AccSetting.logic(opt)
        return

    def filter(inp):        
        try:
            opt = int(inp)
            filt.val_in_range(opt, 1, 5)
        except ValueError:
            log_msg = "Invalid Input"
        except LibSysError as l:
            log_msg = l
        else:
            return ("", opt)
        return (log_msg, -1)

    def logic(inp):            
        sub_pages = ["change_user", "change_pass", "change_priv", "delete_acc"]
        sub_page = sub_pages[inp - 1]
        Lib.switch_page(sub_page)

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
        print("4 Delete account")
        print("5 Back to menu")
        return input("Input: ")
