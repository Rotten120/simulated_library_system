import random
from account import Acc
from account_management import AccMgr
from catalog_management import CatalogMgr
from transact_management import TransactMgr

class LibSysClientUi:
    def __init__(self, dirs):
        self._catalogs = CatalogMgr(dirs["catalog"])
        self._accounts = AccMgr(dirs["account"])
        self._transacts = TransactMgr(dirs["transact"])

    def start_ui(self):
        print("LIBRARY SYSTEM")
        print(" 1) Login")
        print(" 2) Sign up")
        print(" 3) Exit")

        while True:
            choose = input("Choose: ")
            if choose in ["1", "2", "3"]:
                return choose

    def menu_ui(self):
        print("MENU")
        print(" 1) Borrow Catalogs")
        print(" 2) Return Catalogs")
        print(" 3) Log out")

        while True:
            choose = input("Choose: ")
            if choose in ["1", "2", "3"]:
                return choose
    
    def login_ui(self):
        print("Login")
        data = {
            "username": input("Username: "),
            "password": input("Password: ")
        }
        return data

    def sign_up_ui(self):
        print("Sign up")
        data = {
            "username": input("Username: "),
            "password": input("Password: "),
            "privilege": self.__get_privilege()
        }
        return data

    def borrow_catalogs_ui(self):
        table = "{:<6} {:<20} {:<15} {:<10} {:<6} {:<20}"
        header = ["ID", "TITLE", "AUTHOR", "GENRE", "STOCKS", "REFERENCES"]
        print(table.format(*header))

        for catalog_id in self._catalogs.items:
            catalog = self._catalogs.items[catalog_id]
            data = list(catalog.parse().values())
            print(table.format(*data))

    def _borrow_get_input(self):
        while True:
            try:
                catalog_id = int(input("Input catalog ID to borrow: "))
            except:
                continue
            break
        return catalog_id


    def transaction_details_ui(self, transact_ids):
        table = "{:<6} {:<20} {:<15} {:<15} {:<15}"
        header = ["ID", "TITLE", "AUTHOR", "BORROWED DATE", "DUE DATE"]
        print(table.format(*header))

        for transact_id in transact_ids:
            transact = self._transacts.search("id", transact_id)[0]
            catalog = self._catalogs.search("id", transact.catalog)[0]

            data = [
                transact.id, catalog.title, catalog.author,
                transact.borrow_date, transact.due_date
            ]

            print(table.format(*data))

    def _return_catalogs_ui(self):
        while True:
            try:
                transact_id = int(input("Input transact ID to return: "))
            except:
                continue
            break
        return transact_id
    
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
