from pages.page import *
from utils.filter_value import FilterValue as filt

class MainMenu:
    def run(args = []):
        log_msg = ""
        
        while True:
            os.system('cls')
            Lib.logged = 0
            inp = MainMenu.display(log_msg)  
            out = MainMenu.filter(inp)

            log_msg = out[0]
            opt = out[1]

            if opt == 3:
                break
            if opt != -1:
                MainMenu.logic(opt)
        return

    def filter(inp):
        try:
            opt = int(inp)
            filt.val_in_range(opt, 1, 3)
        except ValueError:
            log_msg = "Invalid Input"
        except LibSysError as l:
            log_msg = l
        else:
            return ("", opt)   
        return (log_msg, -1)

    def logic(opt):
        pages = ["login", "signup"]
        page = pages[opt - 1]
        Lib.switch_page(page)

    def display(log_msg):
        print("Library System")
        print("1 Login")
        print("2 Signup")
        print("3 Exit")
        print(log_msg)
        return input("Input: ")
        
