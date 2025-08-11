from pages.page import *
from pages.cat_details import CatDetails
from mysql.connector.errors import IntegrityError
from mysql.connector import Error

class CatalogMenu:
    def run(args = []):
        log_msg = ""

        while True:
            os.system('cls')
            catalogs = Lib.get("<display_cat_menu>")
            inp = CatalogMenu.display(log_msg, catalogs)

            if inp == "-1":
                break
            
            log_msg = CatalogMenu.logic(inp)
        return

    def logic(inp):
        log_msg = ""
        try:
            cid = int(inp)
            CatalogMenu.__catalog_exists(cid)
        except ValueError:
            log_msg = "Invalid Input"
        except LibSysError as l:
            log_msg = l
        else:
            Lib.switch_page("cat_details", [cid])
        return log_msg

    def display(log_msg, catalogs):
        layout = "{:<6} {:<20} {:<15} {:<6}"
        header = ["ID", "TITLE", "AUTHOR", "COPIES"]
        print(layout.format(*header), end = "\n\n")

        for catalog in catalogs:
            print(layout.format(*list(catalog)), end = "\n\n")
        print()
        print(log_msg, end = "\n\n")
        return input("Input: ")

    def __catalog_exists(cid):
        cid_exists = Lib.get("<do_cat_exist>", (cid,))[0][0]
        if not cid_exists:
            raise CatalogNotFoundError
