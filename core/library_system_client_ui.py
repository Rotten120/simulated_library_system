from core.base_imports import *
import random

class LibSysClientUi:
    def __init__(self, dirs):
        self._catalogs = CatalogManager(Catalog, dirs["catalog"])
        self._accounts = AccountManager(Account, dirs["account"])
        self._transacts = TransactManager(Transaction, dirs["transact"])

    def start_ui(self):
        print('_' * 55)
        print("LIBRARY SYSTEM".center(55), end = "\n\n")
        print()
        print("(1) Login", end = "\n\n")
        print("(2) Sign up", end = "\n\n")
        print("(3) Exit", end = "\n\n")
        print('_' * 55)

        while True:
            choose = input("Choose: ")
            if choose in ["1", "2", "3"]:
                return choose

    def menu_ui(self):
        print('_' * 55)
        print("MENU".center(55))
        print()
        print(" 1) Borrow Catalogs", end = "\n\n")
        print(" 2) Return Catalogs", end = "\n\n")
        print(" 3) Log out", end = "\n\n")
        print('_' * 55)

        while True:
            choose = input("Choose: ")
            if choose in ["1", "2", "3"]:
                return choose
    
    def login_ui(self):
        print('_' * 55)
        print("Login".center(55), end = "\n\n")
        print()
        data = {
            "username": input("Username: "),
            "password": input("Password: ")
        }
        print('_' * 55)
        return data

    def sign_up_ui(self):
        print('_' * 55)
        print("Sign up".center(55))
        print()
        data = {
            "username": input("Username: "),
            "password": input("Password: "),
            "privilege": self.__get_privilege()
        }
        print('_' * 55)
        return data

    def borrow_catalogs_ui(self):
        table = "{:<6} {:<20} {:<15} {:<10} {:<6} {:<20}"
        header = ["ID", "TITLE", "AUTHOR", "GENRE", "STOCKS", "REFERENCES"]
        print(table.format(*header), end = "\n\n")

        for cid in self._catalogs.tables:
            catalog = self._catalogs.tables[cid]
            data = list(catalog.parse().values())
            print(table.format(*data), end = "\n\n")
        print('_' * 85)
        
    def _borrow_get_input(self):
        while True:
            try:
                cid = int(input("Input catalog ID to borrow: "))
            except:
                continue
            break
        return cid

    def transaction_details_ui(self, trids):
        table = "{:<6} {:<20} {:<15} {:<15} {:<15}"
        header = ["ID", "TITLE", "AUTHOR", "BORROWED DATE", "DUE DATE"]
        print(table.format(*header), end = "\n\n")

        for trid in trids:
            transact = self._transacts.search("id", trid)[0]
            catalog = self._catalogs.search("id", transact.catalog)[0]

            data = [
                transact.id, catalog.title, catalog.author,
                transact.borrow_date, transact.due_date
            ]

            print(table.format(*data), end = "\n\n")
        print('_' * 85)

    def _return_catalogs_ui(self):
        while True:
            try:
                tid = int(input("Input transact ID to return: "))
            except:
                continue
            break
        return tid
    
    def __get_privilege(self):
        print("Choose Borrowing Privilege:")
        print(" 1) Basic\n 2) Student")
        print(" 3) Instructor\n 4) Staff")

        options = [
            "Basic", "Student",
            "Instructor", "Staff"
        ]
        
        while True:
            try:
                choose = int(input("Choose: "))
                return options[choose - 1]
            except:
                continue            
        return "Basic"        
