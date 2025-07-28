from core.libsys import LibSys
from core.pages.main_menu import MainMenu
from core.pages.login import Login
from core.pages.signup import Signup

if __name__ == "__main__":
    pages = {
        "main_menu": MainMenu,
        "login": Login,
        "signup": Signup
    }
    
    LibSys.init(
        "localhost",
        "root",
        "RottenFlesh@123",
        "sim_lib_sys",
        pages
    )

    LibSys.switch_page("main_menu")
