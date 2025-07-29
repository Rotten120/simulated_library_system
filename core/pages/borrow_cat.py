from core.pages.page import *
from mysql.connector.errors import IntegrityError
from mysql.connector import Error

class BorrowCatalog:
    def run():
        inp = 0
        log_msg = ""

        while inp != -1:
            os.system('cls')
            catalogs = Lib.get("<display_cat>")

            try:
                inp = int(BorrowCatalog.display(log_msg, catalogs))
                params = (Lib.logged, inp)
                Lib.set("<borrow_cat>", params)
            except ValueError:
                log_msg = "Invalid input"
            except IntegrityError:
                log_msg = "Catalog does not exist"
            except Error as e:
                if e.errno == 50005:
                    log_msg = "Insufficient stocks"
            else:
                log_msg = "Catalog Borrowed!"

        Lib.switch_page("menu")

    def display(log_msg, catalogs):
        layout = "{:<6} {:<20} {:<15} {:<13} {:<20} {:<10} {:<6} {:<20}"
        header = ["ID", "TITLE", "AUTHOR", "RELEASED YEAR", "GENRE", "MEDIA", "STOCKS", "REFERENCES"]
        print(layout.format(*header), end = "\n\n")

        for catalog in catalogs:
            print(layout.format(*list(catalog)), end = "\n\n")
        print()
        print(log_msg, end = "\n\n")
        return input("Input: ")
