from item import Item
import json

class User(Item):
    def imp(file_path):
        file = open(file_path, 'r')
        data = json.loads(file.read())

        directory = file_path[:file_path.rfind('\\')]
        user = User(data, directory)

        file.close()
        return user

    def edit(self, data):
        if self.id == data["id"]:
            self.username = data["username"]
            self.__password = data["password"]
            self.privilege = data["privilege"]
    
    def parse(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.__password,
            "privilege": self.privilege
        }

    def print(self):
        print("ID:\t\t\t", self.id)
        print("Username:\t\t", self.username)
        print("Password:\t\t", '*' * len(self.__password))
        print("Borrowing Privileges:\t", self.privilege)


