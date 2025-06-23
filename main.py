import random
from account import Acc
from account_management import AccMgr
from catalog_management import CatalogMgr

directory = {
    "account": "account_lists",
    "catalog": "catalog_lists"
}

class LibSys:
    def __init__(self, dirs):
        empty_data = {
            "id": 0,
            "username": "",
            "password": "",
            "privilege": ""
        }

        self.catalogs = CatalogMgr(dirs["catalog"])
        self.accounts = AccMgr(dirs["account"])
        self.logged = Acc(empty_data, "")

    def login(self):
        while True:
            print("Login")

            username = input("Username: ")
            password = input("Password: ")
            results = self.accounts.search("username", "Zedric")

            if len(results) != 1:
                print("Username not found")
                continue

            result = list(results.values())[0]
            if not result.password_check(password):
                print("Incorrect password")
                continue
                
            #break is reached when
                #username exists
                #password matches
            
            print("Successfully logged in")
            self.logged = result
            break
    
    def create_account(self):
        username_exists = True

        while username_exists:
            print("Sign up")
            
            username = input("Username: ")
            password = input("Password: ")
            privilege = input("Borrowing Privileges: ")

            data = {
                "id": random.randrange(0, 999999),
                "username": username,
                "password": password,
                "privilege": privilege
            }

            username_exists = not self.accounts.add(data)
            
        print("Successfuly created account")
        self.login()
                        
