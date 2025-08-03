from pages.page import *
from utils.filter_value import FilterValue as filt

class Menu:
    def run():
        choose = -1
        log_msg = ""

        while choose == -1:
            os.system('cls')
            
            try:
                opt = Menu.display(log_msg)
                filt.val_in_range(opt, 1, 4)
            except ValueError:
                log_msg = "Invalid Input"
            except OptionError as o:
                log_msg = o

        opts = ["borrow_cat", "return_cat", "acc_setting", "main_menu"]
        Lib.switch_page(opts[opt - 1])

    def display(log_msg):
        print("Menu")
        print("1 Borrow Catalogs")
        print("2 Return Catalogs")
        print("3 Account Settings")
        print("4 Back to Main")
        print(log_msg)
        return int(input("Input: "))
        
