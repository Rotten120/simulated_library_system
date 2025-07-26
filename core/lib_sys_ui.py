class LibSysUi:
    @staticmethod
    def main(log_msg):
        print("Library System")
        print("1 Login")
        print("2 Signup")
        print("3 Exit")
        print(log_msg)
        return input("Input: ")

    @staticmethod
    def login(log_msg):
        print("Login")
        print(log_msg)
        
        username = input("Username: ")
        passcode = input("Password: ")
        return (username, passcode)
            
    @staticmethod
    def signup(log_msg):
        print("Signup")
        print(log_msg)
        
        username = input("Username: ")
        passcode = input("Password: ")
        privilege = LibSysUi.__get_privilege()
        return (username, passcode, privilege)

    @staticmethod
    def menu(log_msg):
        print("Menu")
        print("1 Borrow Catalogs")
        print("2 Return Catalogs")
        print("3 Back to Main")
        print(log_msg)
        return input("Input: ")

    @staticmethod
    def borrow_cat(log_msg, catalogs):
        layout = "{:<6} {:<20} {:<15} {:<13} {:<10} {:<10} {:<6} {:<20}"
        header = ["ID", "TITLE", "AUTHOR", "RELEASED YEAR", "GENRE", "MEDIA", "STOCKS", "REFERENCES"]
        print(layout.format(*header), end = "\n\n")

        for catalog in catalogs:
            print(layout.format(*list(catalog)), end = "\n\n")
        print()
        print(log_msg, end = "\n\n")
        return input("Input: ")
    
    @staticmethod
    def return_cat(log_msg, transacts):
        layout = "{:<6} {:<20} {:<15} {:<6} {:<19} {:<19} {:<6}"
        header = ["ID", "TITLE", "AUTHOR", "COPIES", "BORROWED DATE", "DUE DATE", "STATUS"]
        print(layout.format(*header), end = "\n\n")

        for transact in transacts:
            li_transact = list(transact)
            li_transact[4] = LibSysUi.__print_date_time(li_transact[4])
            li_transact[5] = LibSysUi.__print_date_time(li_transact[5])
            print(layout.format(*li_transact), end = "\n\n")
        print()
        print(log_msg, end ="\n\n")
        return input("Input: ")

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
