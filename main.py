from library_system_client_ui import *
from utils.get_date import Date
import os

directory = {
    "account": "database\\account_lists",
    "catalog": "database\\catalog_lists",
    "transact": "database\\transact_lists"
}

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
        self.__logged = Acc(empty_data, "")

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
                print("Username not found")
                continue

            result = results[0]
            if not result.password_check(data["password"]):
                print("Incorrect password")
                continue
            
            print("Successfully logged in")
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
        catalog_id = 0

        while catalog_id != -1:
            os.system('cls')
            self.borrow_catalogs_ui()
            catalog_id = self._borrow_get_input()
            if not self._catalogs.id_exists(catalog_id):
                continue

            catalog = self._catalogs.items[catalog_id]
            data = {
                "id": random.randrange(0, 999999),
                "borrower": self.__logged.id,
                "catalog": catalog.id,
                "borrow date": Date.today(),
                "due date": Date.next_month()
            }

            transact_id = self._transacts.add(self.__logged, catalog, data)
            if transact_id == -1:
                continue
        self.menu()

    def return_catalogs(self):
        transact_id = 0

        while transact_id != -1:
            os.system('cls')
            self.transaction_details_ui(self.__logged.transacts)
            transact_id = self._return_catalogs_ui()
            if not self._transacts.id_exists(transact_id):
                continue

            transaction = self._transacts.items[transact_id]
            catalog = self._catalogs.items[transaction.catalog]
            self._transacts.remove(self.__logged, catalog, transact_id)
        self.menu()

if __name__ == "__main__":
    library = LibSysClient(directory)
    library.start()
