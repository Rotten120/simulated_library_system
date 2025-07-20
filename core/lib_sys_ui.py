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
