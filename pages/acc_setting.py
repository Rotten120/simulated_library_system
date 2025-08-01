from pages.page import *
from utils.filter_value import FilterValue as filt

# IM CONTEMPLATING IF I SHOULD PACK OL SHIT IN ONE CLASS
# OR I SHOULD JUST CREATE CLASSES FOR EACH
# IF I INDEED CREATE CLASSES FOR EACH, SHOULD I BUNDLE THEIR FILES
# TOGETHER WITH THE OTHER PAGES?
# OR SHOULD I CREATE A FOLDER WITHIN PAGES FOR THEM
# WAKARANEEEEEEEEEEEEEEEEEEEEEEEEEE
class AccSetting:
    def run():
        inp = 0
        log_msg = ""

        while inp != -1:
            os.system('cls')
            account = AccSetting.__get_acc_details()

            try:
                inp = int(AccSetting.__display__acc_menu(log_msg, account))
                inp = filt.val_in_range(inp, 1, 3)
            except ValueError:
                log_msg = "Invalid Input"
            except OptionError as o:
                log_msg = o;

        Lib.switch_page("menu")

    def display(idx, log_msg, account):
        pass

    def __display_acc_menu(log_msg, account):
        layout = "{:<6} {:<15} {:<15} {:<10}"
        header = ["ID", "USERNAME", "PASSWORD", "PRIVILEGE"]
        print(layout.format(*header), end = "\n")

        li_account = list(account[0])
        li_account[2] = len(li_account[2]) * '*'
        print(layout.format(*li_account), end = "\n\n")
        
        print(log_msg)

        print("1 Change username")
        print("2 Change password")
        print("3 Change privilege")
        return input("Input: ")

    def __change_username(log_msg):
        print("Changing Username")
        print(log_msg)
        user = input("New username: ")
        code = input("Input password: ")
        return (user, code)

    def __change_password(log_msg):
        print("Changing Password")
        print(log_msg)
        new_code = input("New password: ")
        old_code = input("Old password: ")
        return (new_code, old_code)

    def __get_privilege():
        print("Choose Borrowing Privilege:")
        print(" 1) Basic\n 2) Student")
        print(" 3) Instructor\n 4) Staff")
        
        choose = -1
        while not(1 <= choose <= 4):
            try: choose = int(input("Choose: "))
            except: continue
        
        return choose
        
    def __get_acc_details():
        procedure = "getAccDetails"
        param = [Lib.logged]
        
        Lib.cursor().callproc(procedure, param)
        results = Lib.cursor().stored_results()

        account = next(results, None).fetchall()
        return account
