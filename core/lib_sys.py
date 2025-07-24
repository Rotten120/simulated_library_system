from lib_sys_ui import LibSysUi as ui
from filter_val import Filter
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
        self.log_msg = ""
        self.__logged = 0

    def __del__(self):
        self.__cursor.close()
        self.__conn.close()

    def __get(self, query, params = None):
        self.__cursor.execute(query, params)
        return self.__cursor.fetchall()

    def __set(self, query, params = None):
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
                choose = Filter.valid_option(opt, 0, 2)
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

            query = "SELECT getAccountID(%s, %s);"
            
            try:
                self.__logged = self.__get(query, log)[0][0]
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
        while True:
            os.system('cls')
            log = ui.signup(log_msg)
            query = "INSERT INTO accounts (username, passcode, privilege) VALUES (%s, %s, %s);"

            try:
                self.__set(query, log)
            except mysql.connector.errors.IntegrityError:
                log_msg = "Username already exists"
            else:
                break
        self.main()

    def menu(self):
        choose = -1
        log_msg = ""
        funcs = [self.borrow_cat, self.return_cat, self.main]
        while choose == -1:
            os.system('cls')
            try:
                opt = int(ui.menu(log_msg)) - 1
                choose = Filter.valid_option(opt, 0, 2)
            except ValueError:
                log_msg = "Invalid input"
            except OptionError as o:
                log_msg = o
        funcs[choose]()

    def borrow_cat(self):
        inp = -1
        log_msg = ""
        while True:
            os.system('cls')
            query = "SELECT * FROM catalogs;"
            catalogs = self.__get(query)

            query = "INSERT INTO transacts (accountID, catalogID) VALUES (%s, %s);"
            params = (self.__logged, inp)

            try:
                inp = int(ui.borrow_cat(log_msg, catalogs))
                self.__set(query, params)
                log_msg = "Catalog Borrowed!"
            except ValueError:
                log_msg = "Invalid input"
            except mysql.connector.errors.IntegrityError:
                if inp == -1:
                    break
                log_msg = "Catalog does not exist"                
        self.menu()

    def return_cat(self):
        inp = -1
        log_msg = ""
        while True:
            os.system('cls')
            transacts = self.__get_acc_transacts()

            query = "DELETE FROM transacts WHERE accountID = %s AND transactID = %s;"
            params = (self.__logged, inp)

            try:
                inp = int(ui.return_cat(log_msg, transacts))
                self.__set(query, params)
                if self.__cursor.rowcount > 0:
                    log_msg = "Catalog Returned!"
                else:
                    log_msg = "Transaction ID does not exist"
                if inp == -1:
                    break
            except ValueError:
                log_msg = "Invalid Input"
        self.menu()

    def __get_acc_transacts(self):
        procedure = "getAccTransact"
        param = [self.__logged]
        
        self.__cursor.callproc(procedure, param)
        results = self.__cursor.stored_results()

        transacts = next(results, None).fetchall()
        return transacts

    def exit(self):
        self.__cursor.close()
        self.__conn.close()
        quit()

if __name__ == "__main__":
    library = LibSys()
    library.main()
