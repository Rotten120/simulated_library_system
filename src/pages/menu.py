from pages.page import *
from utils.filter_value import FilterValue as filt

class Menu:
    def run():
        log_msg = ""

        while True:
            os.system('cls')
            inp = Menu.display(log_msg)
            out = Menu.filter(inp)

            log_msg = out[0]
            opt = out[1]

            if opt == 4:
                break
            if opt != -1:
                Menu.logic(opt)
        return

    def filter(inp):
        try:
            opt = int(inp)
            filt.val_in_range(opt, 1, 4)
        except ValueError:
            log_msg = "Invalid Input"
        except LibSysError as l:
            log_msg = l
        else:
            return ("", opt)
        return (log_msg, -1)

    def logic(opt):
        pages = ["catalog_menu", "return_cat", "acc_setting", "main_menu"]
        page = pages[opt - 1]
        Lib.switch_page(page)

    def display(log_msg):
        print("Menu")
        print("1 Browse Catalogs")
        print("2 Return Catalogs")
        print("3 Account Settings")
        print("4 Back to Main")
        print(log_msg)
        return input("Input: ")
        
