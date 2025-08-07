from pages.page import *
from utils.date_time_format import DateTime

class ReturnCatalog:
    def run():
        tid = 0
        log_msg = ""

        while True:
            os.system('cls')
            transacts = Lib.get("<get_transact>", (Lib.logged,))
            inp = ReturnCatalog.display(log_msg, transacts)

            if inp == "-1":
                break

            out = ReturnCatalog.logic(inp)
            log_msg = out[0]
        return

    def logic(inp):
        log_msg = "Catalog Returned!"
        try:
            tid = int(inp)
            params = (Lib.logged, tid)
            Lib.set("<return_cat>", params)
            ReturnCatalog.transact_exists()
        except ValueError:
            log_msg = "Invalid Input"
        except ValueNotFoundError as v:
            log_msg = v.root("Transaction ID")
        else:
            return (log_msg, tid)
        return (log_msg, 0)

    def display(log_msg, transacts):
        layout = "{:<6} {:<15} {:<15} {:<6} {:<19} {:<19} {:<6} {:<4}"
        header = ["ID", "TITLE", "AUTHOR", "COPIES", "BORROWED DATE", "DUE DATE", "STATUS", "FINE"]
        print(layout.format(*header), end = "\n\n")

        for transact in transacts:
            li_transact = ReturnCatalog.__format_transact(transact)
            print(layout.format(*li_transact), end = "\n\n")
        print()
        print(log_msg, end ="\n\n")
        return input("Input: ")

    def transact_exists():
        if Lib.cursor().rowcount == 0:
            raise ValueNotFoundError

    def __format_transact(transact):
        li_transact = list(transact)
        li_transact[4] = DateTime.print_date_time(li_transact[4])
        li_transact[5] = DateTime.print_date_time(li_transact[5])
        return li_transact
