from library_system_client_ui import *

directory = {
    "account": "account_lists",
    "catalog": "catalog_lists",
    "transact": "transact_lists"
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
        choose = self.start_ui()

        if choose == "1":
            self.login()
        if choose == "2":
            self.sign_up()

    def menu(self):
        choose = self.menu_ui()

        if choose == "1":
            self.borrow_catalogs()
        if choose == "2":
            self.return_catalogs()
        if choose == "3":
            self.start()

    def login(self):
        while True:
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
            data = self.sign_up_ui()
            data["id"] = Acc.generate_id()
            username_exists = not self._accounts.add(data)
            
        print("Successfuly created account")
        self.start()

    def borrow_catalogs(self):
        self.borrow_catalogs_ui()
        catalog_id = 0

        while catalog_id != -1:
            catalog_id = self._borrow_get_input()
            catalogs = self._catalogs.search("id", catalog_id)
            if len(catalogs) == 0:
                continue
            catalog = catalogs[0]

            data = {
                "id": random.randrange(0, 999999),
                "borrower": self.__logged.id,
                "catalog": catalog.id,
                "borrow date": "today",
                "due date": "next month"
            }
            
            transact_id = self._transacts.add(data, self._accounts.dir)
            self.__logged.transacts.append(transact_id)
        self.menu()

    def return_catalogs(self):
        transact_id = 0

        while transact_id != -1:
            self.transaction_details_ui(self.__logged.transacts)
            transact_id = self._return_catalogs_ui()
            transacts = self._transacts.search("id", transact_id)
            if len(transacts) == 0:
                continue
            
            directory = self._accounts.dir
            self._transacts.remove(transact_id, directory)
            self.__logged.transacts.remove(transact_id)
        self.menu()

if __name__ == "__main__":
    library = LibSysClient(directory)
    library.start()
