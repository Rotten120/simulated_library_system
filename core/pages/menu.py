from core.pages.base_imports import *
from utils.filter_value import FilterValue as filt

class Menu:
    def run():
        choose = -1
        log_msg = ""
        Lib.logged = 0

        while choose == -1:
            os.system('cls')
            
            try:
                opt = int(Menu.display(log_msg))
                choose = filt.val_in_range(opt, 1, 3)
            except ValueError:
                log_msg = "Invalid Input"
            except OptionError as o:
                log_msg = o

        if opt == 1:
            Lib.switch_page("borrow_cat")
        if opt == 2:
            Lib.switch_page("return_cat")
        if opt == 3:
            Lib.switch_page("main_menu")

    def display(log_msg):
        print("Menu")
        print("1 Borrow Catalogs")
        print("2 Return Catalogs")
        print("3 Back to Main")
        print(log_msg)
        return input("Input: ")
        
