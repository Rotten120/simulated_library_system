from core.library_system_client_ui import *
from utils.get_date import Date
import os

class LibSysClient(LibSysClientUi):
    def __init__(self, dirs):
        super().__init__(dirs)
        empty_data = {
            "id": 0,
            "username": "",
            "password": "",
            "privilege": "",
            "transacts": []
        }
        self.__logged = Account(empty_data, "")

    def start(self):
        os.system('cls')
        choose = self.start_ui()
        if choose == "1":
            self.login()
        if choose == "2":
            self.sign_up()
        if choose == "3":
            quit()

    def menu(self):
        os.system('cls')
        choose = self.menu_ui()
        if choose == "1":
            self.borrow_catalogs()
        if choose == "2":
            self.return_catalogs()
        if choose == "3":
            self.start()

    def login(self):
        while True:
            os.system('cls')
            data = self.login_ui()
            if data["username"] == "-1":
                self.start()
            results = self._accounts.search("username", data["username"])

            if len(results) != 1:
                continue

            result = results[0]
            if not result.password_check(data["password"]):
                continue
            
            self.__logged = result
            self.menu()
        
    
    def sign_up(self):
        username_exists = True

        while username_exists:
            os.system('cls')
            data = self.sign_up_ui()
            data["id"] = random.randrange(0, 999999)
            data["transacts"] = []
            username_exists = not self._accounts.add(data)
        self.start()

    def borrow_catalogs(self):
        cid = 0

        while cid != -1:
            os.system('cls')
            self.borrow_catalogs_ui()
            cid = self._borrow_get_input()
            print(self._catalogs.valid_id(cid), cid)
            if self._catalogs.valid_id(cid) or cid == -1:
                continue

            catalog = self._catalogs.tables[cid]
            data = {
                "id": random.randrange(0, 999999),
                "borrower": self.__logged.id,
                "catalog": catalog.id,
                "borrow date": Date.today(),
                "due date": Date.next_month()
            }

            trid = self._transacts.add(self.__logged, catalog, data)
            if trid == -1:
                continue
        self.menu()

    def return_catalogs(self):
        trid = 0

        while trid != -1:
            os.system('cls')
            self.transaction_details_ui(self.__logged.transacts)
            trid = self._return_catalogs_ui()
            if self._transacts.valid_id(trid) or trid == -1:
                continue

            transaction = self._transacts.tables[trid]
            catalog = self._catalogs.tables[transaction.catalog]
            self._transacts.remove(self.__logged, catalog, trid)
        self.menu()
