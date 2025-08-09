from pages.page import *
from pages.cat_borrow import CatBorrow
from utils.filter_value import FilterValue as filt

class CatDetails:
    def run(cid = 0):
        log_msg = ""

        while True:
            os.system('cls')
            catalog = Lib.get("<get_catalog>", (cid,))[0]
            inp = CatDetails.display(log_msg, catalog)
            out = CatDetails.filter(inp)

            log_msg = out[0]
            opt = out[1]

            if opt == 2:
                break
            if opt != -1:
                CatDetails.logic(opt, cid, catalog)

    def filter(inp):
        try:
            opt = int(inp)
            filt.val_in_range(opt, 1, 2)
        except ValueError:
            log_msg = "Invalid Input"
        except LibSysError as l:
            log_msg = l
        else:
            return ("", opt)
        return (log_msg, -1)

    def logic(opt, cid, catalog):
        if opt == 1:
            CatBorrow.run(cid, catalog)     

    def display(log_msg, catalog):
        layout = "{:<6} {:<20} {:<15} {:<13} {:<20} {:<10} {:<6} {:<20}"
        header = ["ID", "TITLE", "AUTHOR", "RELEASED YEAR", "GENRE", "MEDIA", "STOCKS", "REFERENCES"]
        print(layout.format(*header), end = "\n\n")

        print(layout.format(*list(catalog)), end = "\n\n\n")
        print(log_msg, end = "\n\n")

        print("1 Borrow Catalog")
        print("2 Return")

        return input("Input: ")
        
