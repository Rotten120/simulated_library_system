from core.libsys import LibSys
from pages import *

# remove this <ROOT> and replace all of its instances
# with the informtion necessary before
# executing in your own device
import ROOT

if __name__ == "__main__":
    pages = {
        "main_menu": MainMenu,
        "login": Login,
        "signup": Signup,
        "menu": Menu,
        "borrow_cat": BorrowCatalog,
        "return_cat": ReturnCatalog,
        "acc_setting": AccSetting
    }

    LibSys.init(
        "localhost",
        ROOT.user,      # replace with your superuser
        ROOT.password,  # replace with your superuser's password
        "sim_lib_sys",  # replace with name of database
        pages
    )

    LibSys.switch_page("main_menu")
    
