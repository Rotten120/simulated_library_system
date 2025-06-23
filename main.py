import random
from account import Acc
from account_management import AccMgr
from catalog_management import CatalogMgr

directory = {
    "account": "account_lists",
    "catalog": "catalog_lists"
}

class LibSysClient:
    def __init__(self, dirs):
        empty_data = {
            "id": 0,
            "username": "",
            "password": "",
            "privilege": ""
        }

        self.__catalogs = CatalogMgr(dirs["catalog"])
        self.__accounts = AccMgr(dirs["account"])
        self.__logged = Acc(empty_data, "")

    def login(self):
        while True:
            print("Login")

            username = input("Username: ")
            password = input("Password: ")
            results = self.__accounts.search("username", "Zedric")

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
            self.__logged = result
            break
    
    def create_account(self):
        username_exists = True

        while username_exists:
            print("Sign up")
            
            username = input("Username: ")
            password = input("Password: ")
            privilege = self.__get_privilege()

            data = {
                "id": random.randrange(0, 999999),
                "username": username,
                "password": password,
                "privilege": privilege
            }

            username_exists = not self.__accounts.add(data)
            
        print("Successfuly created account")
        self.login()

    def __get_privilege(self):
        print("Choose Borrowing Privilege:")
        print(" 1) Basic\n 2) Student")
        print(" 3) Instructor\n 4) Staff")

        privs = [
            "Basic", "Student",
            "Instructor", "Staff"
        ]
        
        while True:
            try:
                priv = int(input("Choose: "))
                return privs[priv - 1]
            except:
                continue            
        return "Basic"


        
