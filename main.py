from core.libsys import LibSys
from core.pages import *

if __name__ == "__main__":
    pages = {
        "main_menu": MainMenu,
        "login": Login,
        "signup": Signup,
        "menu": Menu,
        "borrow_cat": BorrowCatalog,
        "return_cat": ReturnCatalog
    }
    
    LibSys.init(
        "localhost",
        "root",
        "RottenFlesh@123",
        "sim_lib_sys",
        pages
    )

    LibSys.switch_page("main_menu")
