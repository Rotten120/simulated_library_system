from lib_sys_ui import LibSysUi as ui
from queries import Queries
from errors import *
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

    def __get(self, key, params = None):
        query = Queries.get(key)
        self.__cursor.execute(query, params)
        return self.__cursor.fetchall()

    def __set(self, key, params = None):
        query = Queries.get(key)
        self.__cursor.execute(query, params)
        self.__conn.commit()

    def main(self):
        choose = -1
        log_msg = ""
        self.__logged = 0
        funcs = [self.login, self.signup, self.exit]
        while choose == -1:
            os.system('cls')
            try:
                opt = int(ui.main(log_msg)) - 1
                choose = self.__is_opt_valid(opt, 0, 2)
            except ValueError:
                log_msg = "Invalid input"
            except OptionError as o:
                log_msg = o
        funcs[choose]()

    def login(self):
        log_msg = ""
        while self.__logged <= 0:
            os.system('cls')
            log = ui.login(log_msg)
            
            if log[0] == "-1":
                self.main()

            try:
                self.__logged = self.__get("login", log)[0][0]
            except mysql.connector.Error as e:
                if e.errno == 50001:
                    log_msg = "Username does not exist"
                if e.errno == 50002:
                    log_msg = "Incorrect Password"
            else:
                break
        self.menu()

    def signup(self):
        log_msg = ""
        signup_done = False
        while not signup_done:
            os.system('cls')
            log = ui.signup(log_msg)

            if log[0] == "-1":
                self.main()
            
            try:
                self.__set("signup", log)
            except mysql.connector.errors.IntegrityError:
                log_msg = "Username already exists"
            else:
                signup_done = True
        self.main()

    def menu(self):
        choose = -1
        log_msg = ""
        funcs = [self.borrow_cat, self.return_cat, self.main]
        while choose == -1:
            os.system('cls')
            try:
                opt = int(ui.menu(log_msg)) - 1
                choose = self.__is_opt_valid(opt, 0, 2)
            except ValueError:
                log_msg = "Invalid input"
            except OptionError as o:
                log_msg = o
        funcs[choose]()

    def borrow_cat(self):
        inp = 0
        log_msg = ""
        while inp != -1:
            os.system('cls')
            catalogs = self.__get("display_cat")

            try:
                inp = int(ui.borrow_cat(log_msg, catalogs))
                params = (self.__logged, inp)
                self.__set("borrow_cat", params)
            except ValueError:
                log_msg = "Invalid input"
            except mysql.connector.errors.IntegrityError:
                log_msg = "Catalog does not exist"
            else:
                log_msg = "Catalog Borrowed!"
        self.menu()

    def return_cat(self):
        inp = 0
        log_msg = ""
        while inp != -1:
            os.system('cls')
            transacts = self.__get_acc_transacts()

            try:
                inp = int(ui.return_cat(log_msg, transacts))
                params = (self.__logged, inp)
                self.__set("return_cat", params)
                
                if self.__cursor.rowcount == 0:
                    raise ValueNotFoundError("Transaction ID")
            except ValueError:
                log_msg = "Invalid Input"
            except ValueNotFoundError as v:
                log_msg = v
            else:
                log_msg = "Catalog Returned!"
        self.menu()

    def __get_acc_transacts(self):
        procedure = "getAccTransact"
        param = [self.__logged]
        
        self.__cursor.callproc(procedure, param)
        results = self.__cursor.stored_results()

        transacts = next(results, None).fetchall()
        return transacts

    def __is_opt_valid(val, lo, hi):
        option = val
        if not(lo <= option <= hi):
            raise OptionError(lo, hi)
        return option

    def exit(self):
        self.__cursor.close()
        self.__conn.close()
        quit()

if __name__ == "__main__":
    library = LibSys()
    library.main()
