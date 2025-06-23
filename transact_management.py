from transact import Transaction
from account import Acc
from file_manager import FileManager

class TransactMgr(FileManager):
    def add(self, data, directory):
        transact_id = super().add(data)
        
        acc_path = directory + '\\' + str(data["borrower"]) + ".txt"
        acc = Acc.imp(acc_path)

        data = acc.parse()
        data["transacts"].append(transact_id)
        acc.edit(data)
        acc.write()
        
        return transact_id

    def remove(self, item_id, directory):
        acc_id = self.items[item_id].borrower
        if super().remove(item_id):
            acc_path = directory + '\\' + str(acc_id) + ".txt"
            acc = Acc.imp(acc_path)
            acc.transacts.remove(item_id)
            acc.write()
            return True

        return False

    def print(self, dirs):
        for item_id in self.items:
            print(end = "\n\n")
            self.items[item_id].print(dirs)
    
    def import_item(self, file_path):
        return Transaction.imp(file_path)

    def create_item(self, data):
        return Transaction(data, self.dir)
