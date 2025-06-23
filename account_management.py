from account import Acc
from file_manager import FileManager

class AccMgr(FileManager):
    def add(self, data):
        results = self.search("username", data["username"])
        if len(results) == 0:
            return super().add(data)
        return False

    def edit(self, item_id, data, password):
        try:
            item = self.items[item_id]
        except KeyError:
            return False

        if item.password_check(password):
            return super().edit(item_id, data)
        return False
    
    def remove(self, item_id, password):
        try:
            item = self.items[item_id]
        except KeyError:
            return False

        if item.password_check(password):
            return super().remove(item_id)
        return False
    
    def import_item(self, file_path):
        return Acc.imp(file_path)

    def create_item(self, data):
        return Acc(data, self.dir)
