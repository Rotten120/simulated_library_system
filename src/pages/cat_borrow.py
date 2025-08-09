from pages.page import *
from utils.filter_value import FilterValue as filt

class CatBorrow:
    def run(cid, catalog):
        log_msg = ""

        while True:
            os.system('cls')
            inp = CatBorrow.display(log_msg, catalog)

            if inp == "-1":
                break

            out = CatBorrow.logic(cid, inp)
            log_msg = out[0]
        return

    def logic(cid, inp):
        log_msg = "Catalog Borrowed!"
        try:
            stocks = int(inp)
            params = (Lib.logged, cid, stocks)
            Lib.set("<borrow_cat>", params)
            tid = Lib.get("<recent_tid>", (Lib.logged, cid))[0][0]
        except ValueError:
            log_msg = "Invalid Input"
        except LibSysError as l:
            log_msg = l
        else:
            return (log_msg, tid)
        return (log_msg, 0)

    def display(log_msg, catalog):
        layout = "{:<6} {:<20} {:<15} {:<13} {:<20} {:<10} {:<6} {:<20}"
        header = ["ID", "TITLE", "AUTHOR", "RELEASED YEAR", "GENRE", "MEDIA", "STOCKS", "REFERENCES"]
        print(layout.format(*header), end = "\n\n")

        print(layout.format(*list(catalog)), end = "\n\n\n")
        print(log_msg, end = "\n\n")

        return input("Input copies to borrow: ")
            
