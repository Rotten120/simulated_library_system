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

    def __get(self, query, params):
        self.__cursor.execute(query, params)
        return self.__cursor.fetchall()

    def __set(self, query, params):
        self.__cursor.execute(query, params)
        self.__conn.commit()

    def main(self):
        os.system('cls')
        choose = ui.main()
        funcs = [self.login, self.signup, self.exit]
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
        print(self.__logged)

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

    def exit(self):
        self.__cursor.close()
        self.__conn.close()
        quit()

if __name__ == "__main__":
    library = LibSys()
    library.main()
