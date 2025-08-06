from core.libsys import LibSys
from pages import *

# remove this <ROOT> and replace all of its instances
# with the informtion necessary before
# executing in your own device
import ROOT

def get_pages():
    return {
        "main_menu": MainMenu,
        "login": Login,
        "signup": Signup,
        "menu": Menu,
        "borrow_cat": BorrowCatalog,
        "return_cat": ReturnCatalog,
        "acc_setting": AccSetting
    }

def libsys_init(pages = {}):
    LibSys.init(
        "localhost",
        ROOT.user,      # replace with your superuser
        ROOT.password,  # replace with your superuser's password
        "sim_lib_sys",  # replace with name of database
        pages
    )

def main():
    pages = get_pages()
    libsys_init(pages)
    LibSys.switch_page("main_menu")

if __name__ == "__main__":
    main()
    
