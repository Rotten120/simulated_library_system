from transact import Transaction
from account import Acc
from file_manager import FileManager

class TransactMgr(FileManager):
    def add(self, data, directory):
        transact_id = super().add(data)
        acc_path = Acc.create_path(directory, data["borrower"])
        self.__add_acc_transact(acc_path, transact_id)
        return transact_id

    def remove(self, transact_id, directory):
        acc_id = self.items[transact_id].borrower
        if super().remove(transact_id):
            acc_path = Acc.create_path(directory, acc_id)
            self.__rmv_acc_transact(acc_path, transact_id)
            return True

        return False

    def __add_acc_transact(self, acc_path, transact_id):
        acc = Acc.imp(acc_path)
        acc.transacts.append(transact_id)
        acc.write()

    def __rmv_acc_transact(self, acc_path, transact_id):
        acc = Acc.imp(acc_path)
        acc.transacts.remove(transact_id)
        acc.write()

    def print(self, dirs):
        for item_id in self.items:
            print(end = "\n\n")
            self.items[item_id].print(dirs)
    
    def import_item(self, file_path):
        return Transaction.imp(file_path)

    def create_item(self, data):
        return Transaction(data, self.dir)
