from .main_menu import MainMenu
from .login import Login
from .signup import Signup
from .menu import Menu
from .catalog_menu import CatalogMenu
from .cat_details import CatDetails
from .return_cat import ReturnCatalog
from .acc_setting import AccSetting

from .acc_alter import *

def get_pages():
    return {
        "main_menu": MainMenu,
        "login": Login,
        "signup": Signup,
        "menu": Menu,
        "catalog_menu": CatalogMenu,
        "return_cat": ReturnCatalog,
        "acc_setting": AccSetting,
        "cat_details": CatDetails
    } | acc_alter.get_pages()
