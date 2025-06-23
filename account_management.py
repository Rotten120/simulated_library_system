from account import Acc
from file_manager import FileManager

class AccMgr(FileManager):
    #username and id has to be unique
    def add(self, data):
        results = self.search("username", data["username"])
        if len(results) == 0:
            return super().add(data)

        print("Username already exists")
        return False

    #modified version of edit that also validates password
    def edit(self, item_id, data, password):
        if not(item_id in self.items):
            print("Item ID does not exist in directory")
            return False

        item = self.items[item_id]
        if item.password_check(password):
            val = item.edit(data)
            item.write()
            return val
        
        print("Wrong password")
        return False
    
    #modified version of edit that also validates password
    def remove(self, item_id, password):
        if not(item_id in self.items):
            print("Item ID does not exist in directory")
            return False
        
        item = self.items[item_id]
        if item.password_check(password):
            item.rmv(data)
            del item
            return True
        
        print("Wrong password")
        return False
    
    def import_item(self, file_path):
        return Acc.imp(file_path)

    def create_item(self, data):
        return Acc(data, self.dir)
