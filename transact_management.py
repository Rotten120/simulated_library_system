from transact import Transaction
from account import Acc
from file_manager import FileManager

class TransactMgr(FileManager):
    def add(self, acc, catalog, data):
        if catalog.stock <= 0:
            return -1
        
        transact_id = super().add(data)
        self.__add_acc_transact(acc, transact_id)
        self.__rmv_stock(catalog)
        return transact_id
    
    def remove(self, acc, catalog, transact_id):
        if super().remove(transact_id):
            self.__rmv_acc_transact(acc, transact_id)
            self.__add_stock(catalog)
            return True
        return False

    def __add_acc_transact(self, acc, transact_id):
        acc.transacts.append(transact_id)
        acc.write()

    def __add_stock(self, catalog):
        catalog.stock += 1
        catalog.write()

    def __rmv_acc_transact(self, acc, transact_id):
        acc.transacts.remove(transact_id)
        acc.write()

    def __rmv_stock(self, catalog):
        catalog.stock -= 1
        catalog.write()

    def print(self, dirs):
        for item_id in self.items:
            print(end = "\n\n")
            self.items[item_id].print(dirs)
    
    def import_item(self, file_path):
        return Transaction.imp(file_path)

    def create_item(self, data):
        return Transaction(data, self.dir)
