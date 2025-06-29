from table.table import Table
import json

class Account(Table):
    def imp(file_path):
        file = open(file_path, 'r')
        data = json.loads(file.read())

        directory = file_path[:file_path.rfind('\\')]
        acc = Account(data, directory)

        file.close()
        return acc

    def edit(self, data):
        if self.id != data["id"]:
            return False
        self.username = data["username"]
        self.__password = data["password"]
        self.privilege = data["privilege"]
        self.transacts = data["transacts"]
        return False
    
    def parse(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.__password,
            "privilege": self.privilege,
            "transacts": self.transacts
        }

    def print(self):
        print("ID:\t\t\t", self.id)
        print("Username:\t\t", self.username)
        print("Password:\t\t", '*' * len(self.__password))
        print("Borrowing Privileges:\t", self.privilege)
        print("Transaction IDs")

        for transact in self.transacts:
            print(" ", transact)

    def password_check(self, password):
        return self.__password == password


