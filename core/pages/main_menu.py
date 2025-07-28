from core.pages.base_imports import *
from utils.filter_value import FilterValue as filt

class MainMenu:
    def run():
        choose = -1
        log_msg = ""
        Lib.logged = 0

        while choose == -1:
            os.system('cls')
            
            try:
                opt = int(MainMenu.display(log_msg))
                choose = filt.val_in_range(opt, 0, 2)
            except ValueError:
                log_msg = "Invalid Input"
            except OptionError as o:
                log_msg = o

        if opt == 1:
            Lib.switch_page("login")
        if opt == 2:
            Lib.switch_page("signup")
        quit()

    def display(log_msg):
        print("Library System")
        print("1 Login")
        print("2 Signup")
        print("3 Exit")
        print(log_msg)
        return input("Input: ")
        
