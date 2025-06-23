from user import User
from file_manager import FileManager

class UserMgr(FileManager):
    def import_item(self, file_path):
        return User.imp(file_path)

    def create_item(self, data):
        return User(data, self.dir)

data = {
    "id": 6410011,
    "username": "VONVON",
    "password": "asdjalskd",
    "privilege": "STUDENT"
}

a = UserMgr("user_lists")
a.add(data)
