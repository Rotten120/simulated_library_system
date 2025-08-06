from pages.page import *
from mysql.connector.errors import IntegrityError
from mysql.connector import Error

class BorrowCatalog:
    def run():
        cid = 0
        log_msg = ""

        while cid != -1:
            os.system('cls')
            catalogs = Lib.get("<display_cat>")
            inp = BorrowCatalog.display(log_msg, catalogs)
            out = BorrowCatalog.logic(inp)
            
            log_msg = out[0]
            cid = out[1]
        return

    def logic(inp):
        if inp == "-1":
            return ("Leaving page...", -1)
        
        log_msg = "Catalog Borrowed!"
        try:
            cid = int(inp)
            params = (Lib.logged, cid)
            Lib.set("<borrow_cat>", params)
        except ValueError:
            log_msg = "Invalid Input"
            cid = 0
        except IntegrityError:
            log_msg = "Catalog does not exist"
        except StockError as s:
            log_msg = s
        except BorrowError as b:
            log_msg = b
        return (log_msg, cid)

    def display(log_msg, catalogs):
        layout = "{:<6} {:<20} {:<15} {:<13} {:<20} {:<10} {:<6} {:<20}"
        header = ["ID", "TITLE", "AUTHOR", "RELEASED YEAR", "GENRE", "MEDIA", "STOCKS", "REFERENCES"]
        print(layout.format(*header), end = "\n\n")

        for catalog in catalogs:
            print(layout.format(*list(catalog)), end = "\n\n")
        print()
        print(log_msg, end = "\n\n")
        return input("Input: ")
