from pages.page import *
from utils.date_time_format import DateTime

class ReturnCatalog:
    def run():
        inp = 0
        log_msg = ""

        while inp != -1:
            os.system('cls')
            transacts = ReturnCatalog.__get_acc_transacts()
    
            try:
                inp = int(ReturnCatalog.display(log_msg, transacts))
                params = (Lib.logged, inp)
                Lib.set("<return_cat>", params)
                ReturnCatalog.transact_exists()
            except ValueError:
                log_msg = "Invalid input"
            except ValueNotFoundError as v:
                log_msg = v
            else:
                log_msg = "Catalog Returned!"

        Lib.switch_page("menu")

    def display(log_msg, transacts):
        layout = "{:<6} {:<20} {:<15} {:<6} {:<19} {:<19} {:<6} {:<4}"
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
            raise ValueNotFoundError("Transaction ID")

    def __format_transact(transact):
        li_transact = list(transact)
        li_transact[4] = DateTime.print_date_time(li_transact[4])
        li_transact[5] = DateTime.print_date_time(li_transact[5])
        return li_transact

    def __get_acc_transacts():
        procedure = "getAccTransact"
        param = [Lib.logged]
        
        Lib.cursor().callproc(procedure, param)
        results = Lib.cursor().stored_results()

        transacts = next(results, None).fetchall()
        return transacts
