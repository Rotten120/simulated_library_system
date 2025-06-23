from account import Acc
from file_manager import FileManager

class UserMgr(FileManager):
    #username and id has to be unique
    def add(self, data):
        results = self.search("username", data["username"])
        if len(results) == 0:
            super().add(data)
        else:
            print("Username already exists")

    #modified version of edit that also validates password
    def edit(self, item_id, data, password):
        if not(item_id in self.items):
            print("Item ID does not exist in directory")
            return

        item = self.items[item_id]
        if item.password_check(password):
            item.edit(data)
        else:
            print("Wrong password")

    #modified version of edit that also validates password
    def remove(self, item_id, password):
        if not(item_id in self.items):
            print("Item ID does not exist in directory")
            return
        
        item = self.items[item_id]
        if item.password_check(password):
            item.rmv(data)
            del item
        else:
            print("Wrong password")
    
    def import_item(self, file_path):
        return Acc.imp(file_path)

    def create_item(self, data):
        return Acc(data, self.dir)
