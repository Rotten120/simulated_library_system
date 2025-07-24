from lib_sys_ui import LibSysUi as ui
from filter_val import Filter
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
        self.__logged = 0
        funcs = [self.login, self.signup, self.exit]
        while choose == -1:
            os.system('cls')
            opt = ui.main()
            choose = Filter.valid_option(opt, 0, 2)
        funcs[choose]()

    def login(self):
        signal_id = 0
        while self.__logged <= 0:
            os.system('cls')
            log = ui.login(signal_id)
            
            if log[0] == "-1":
                self.main()

            query = "SELECT getAccountID(%s, %s);"
            self.__logged = self.__get(query, log)[0][0]

            if self.__logged == -1:
                signal_id = 2
            if self.__logged == -2:
                signal_id = 3
        self.menu()

    def signup(self):
        signal_id = 0
        while True:
            os.system('cls')
            log = ui.signup(signal_id)
            query = "INSERT INTO accounts (username, passcode, privilege) VALUES (%s, %s, %s);"

            try:
                self.__set(query, log)
                break
            except mysql.connector.errors.IntegrityError:
                signal_id = 4
        self.main()

    def menu(self):
        choose = -1
        funcs = [self.borrow_cat, self.return_cat, self.main]
        while choose == -1:
            os.system('cls')
            opt = ui.menu()
            choose = Filter.valid_option(opt, 0, 2)
        funcs[choose]()

    def borrow_cat(self):
        inp = -1
        signal_id = 0
        while True:
            os.system('cls')
            query = "SELECT * FROM catalogs;"
            catalogs = self.__get(query)
            
            inp = ui.borrow_cat(signal_id, catalogs)
            if inp == -1:
                break

            query = "INSERT INTO transacts (accountID, catalogID) VALUES (%s, %s);"
            params = (self.__logged, inp)

            try:
                self.__set(query, params)
                signal_id = 5
            except mysql.connector.errors.IntegrityError:
                signal_id = 6
        self.menu()

    def return_cat(self):
        inp = -1
        signal_id = 0
        while True:
            os.system('cls')
            transacts = self.__get_acc_transacts()

            inp = ui.return_cat(signal_id, transacts)
            if inp == -1:
                break

            query = "DELETE FROM transacts WHERE accountID = %s AND transactID = %s;"
            params = (self.__logged, inp)

            self.__set(query, params)
            if self.__cursor.rowcount > 0:
                signal_id = 7
            else:
                signal_id = 8
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
