from lib_sys_ui import LibSysUi as ui
import mysql.connector
import os

class LibSys:
    def __init__(self):
        self.__conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "RottenFlesh@123",
            database = "sim_lib_sys"
        )

        self.__cursor = self.__conn.cursor()
        self.__logged = 0

    def __del__(self):
        self.__cursor.close()
        self.__conn.close()

    def __get(self, query, params = None):
        self.__cursor.execute(query, params)
        return self.__cursor.fetchall()

    def __get_procedure(self, procedure, params = None):
        self.__cursor.callproc(procedure, params)
        return self.__cursor.stored_results()

    def __set(self, query, params = None):
        self.__cursor.execute(query, params)
        self.__conn.commit()

    def main(self):
        choose = -1
        self.__logged = 0
        funcs = [self.login, self.signup, self.exit]
        while not(0 <= choose <= 2):
            os.system('cls')
            choose = ui.main()
        funcs[choose]()

    def login(self):
        while self.__logged <= 0:
            os.system('cls')
            log = ui.login()
            
            if log[0] == "-1":
                self.main()

            # ----------- Exceptions ----------- #
            if self.__logged == -1:
                print("Username does not exists")
            if self.__logged == -2:
                print("Incorrect Password")
            # ---------------------------------- #

            query = "SELECT getAccountID(%s, %s);"
            self.__logged = self.__get(query, log)[0][0]
        self.menu()

    def signup(self):
        while True:
            os.system('cls')
            log = ui.signup()
            query = "INSERT INTO accounts (username, passcode, privilege) VALUES (%s, %s, %s);"

            try:
                self.__set(query, log)
                break
            except mysql.connector.errors.IntegrityError:
                print("Username already exists, try another")
        self.main()

    def menu(self):
        choose = -1
        funcs = [self.borrow_cat, self.return_cat, self.main]
        while not(0 <= choose <= 2):
            os.system('cls')
            choose = ui.menu()
        funcs[choose]()

    def borrow_cat(self):
        inp = -1
        while True:
            os.system('cls')
            query = "SELECT * FROM catalogs;"
            catalogs = self.__get(query)
            
            inp = ui.borrow_cat(catalogs)
            if inp == -1:
                break

            query = "INSERT INTO transacts (accountID, catalogID) VALUES (%s, %s);"
            params = (self.__logged, inp)

            try:
                self.__set(query, params)
                print("Catalog Borrowed!")
            except mysql.connector.errors.IntegrityError:
                print("Catalog does not exists")
        self.menu()

    def return_cat(self):
        inp = -1
        while True:
            os.system('cls')
            procedure = "getAccTransact"
            param = [self.__logged]
            transacts = next(self.__get_procedure(procedure, param), None).fetchall()   #HEEHHHHH

            inp = ui.return_cat(transacts)
            if inp == -1:
                break

            query = "DELETE FROM transacts WHERE accountID = %s AND transactID = %s;"
            params = (self.__logged, inp)

            self.__set(query, params)
            if self.__cursor.rowcount > 0:
                print("Catalog Returned!")
            else:
                print("Transaction ID does not exist")
        self.menu()

    def exit(self):
        self.__cursor.close()
        self.__conn.close()
        quit()

if __name__ == "__main__":
    library = LibSys()
    library.menu()
