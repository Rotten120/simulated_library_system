from core.libsys import LibSys
from pages import *

# remove this <ROOT> and replace all of its instances
# with the informtion necessary before
# executing in your own device
from ROOT import Root

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
        Root.user,      # replace with your superuser
        Root.password,  # replace with your superuser's password
        "sim_lib_sys",
        pages
    )

    LibSys.switch_page("main_menu")
    
