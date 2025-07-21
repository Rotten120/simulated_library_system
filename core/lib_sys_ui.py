class LibSysUi:
    @staticmethod
    def main():
        print("Library System")
        print("1 Login")
        print("2 Signup")
        print("3 Exit")

        choose = -1
        while not(1 <= choose <= 3):
            try: choose = int(input("Input: "))
            except: continue
        return choose - 1

    @staticmethod
    def login():
        print("Login")
        username = input("Username: ")
        passcode = input("Password: ")
        return (username, passcode)
            
    @staticmethod
    def signup():
        print("Signup")
        username = input("Username: ")
        passcode = input("Password: ")
        privilege = LibSysUi.__get_privilege()
        return (username, passcode, privilege)

    @staticmethod
    def menu():
        print("Menu")
        print("1 Borrow Catalogs")
        print("2 Return Catalogs")
        print("3 Back to Main")

        choose = -1
        while not(1 <= choose <= 3):
            try: choose = int(input("Input: "))
            except: continue
        return choose - 1

    @staticmethod
    def borrow_cat(catalogs):
        layout = "{:<6} {:<20} {:<15} {:<10} {:<6} {:<20}"
        header = ["ID", "TITLE", "AUTHOR", "GENRE", "STOCKS", "REFERENCES"]
        print(layout.format(*header), end = "\n\n")

        for catalog in catalogs:
            print(layout.format(*list(catalog)), end = "\n\n")
        print()

    @staticmethod
    def return_cat(transacts):
        layout = "{:<6} {:<20} {:<15} {:<6} {:<19} {:<19} {:<6}"
        header = ["ID", "TITLE", "AUTHOR", "COPIES", "BORROWED DATE", "DUE DATE", "STATUS"]
        print(layout.format(*header), end = "\n\n")

        for transact in transacts:
            li_transact = list(transact)
            li_transact[4] = LibSysUi.__print_date_time(li_transact[4])
            li_transact[5] = LibSysUi.__print_date_time(li_transact[5])
            print(layout.format(*li_transact), end = "\n\n")
        print()

    def __get_privilege():
        print("Choose Borrowing Privilege:")
        print(" 1) Basic\n 2) Student")
        print(" 3) Instructor\n 4) Staff")
        options = ["Basic", "Student", "Instructor", "Staff"]
        
        choose = -1
        while not(1 <= choose <= 4):
            try: choose = int(input("Choose: "))
            except: continue
        
        return options[choose - 1]

    def __print_date_time(date_time):
        dt = (date_time.timetuple())[:6]
        tt = f"{dt[0]}/{dt[1]}/{dt[2]} {dt[3]}:{dt[4]}:{dt[5]}"
        return tt
