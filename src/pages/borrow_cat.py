from pages.page import *
from pages.cat_details import CatDetails
from mysql.connector.errors import IntegrityError
from mysql.connector import Error

class BorrowCatalog:
    def run():
        log_msg = ""

        while True:
            os.system('cls')
            catalogs = Lib.get("<display_cat>")
            inp = BorrowCatalog.display(log_msg, catalogs)

            if inp == "-1":
                break
            
            log_msg = BorrowCatalog.logic(inp)
        return

    def logic(inp):
        log_msg = "Catalog opened"
        try:
            cid = int(inp)
            BorrowCatalog.__catalog_exists(cid)
        except ValueError:
            log_msg = "Invalid Input"
        except ValueNotFoundError:
            log_msg = "Catalog does not exist"
        else:
            CatDetails.run(cid)
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
        cid_exists = Lib.get("<cat_exists>", (cid,))
        if not cid_exists:
            raise ValueNotFoundError
