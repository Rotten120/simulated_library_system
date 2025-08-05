from pages.page import *
from utils.filter_value import FilterValue as filt

class MainMenu:
    def run():
        choose = -1
        log_msg = ""
        Lib.logged = 0

        while choose == -1:
            os.system('cls')
            
            try:
                choose = MainMenu.display(log_msg)
                filt.val_in_range(choose, 1, 3)
            except ValueError:
                log_msg = "Invalid Input"
            except OptionError as o:
                log_msg = o
                choose = -1

        if choose == 3:
            quit()
        opts = ["login", "signup"]
        Lib.switch_page(opts[choose - 1])

    def display(log_msg):
        print("Library System")
        print("1 Login")
        print("2 Signup")
        print("3 Exit")
        print(log_msg)
        return int(input("Input: "))
        
