from table.transact import Transaction
from table.account import Account
from table_manager.table_manager import TableManager

class TransactManager(TableManager):
    def add(self, acc, catalog, data):
        if catalog.stock <= 0:
            return -1
        
        trid = super().add(data)
        self.__add_acc_transact(acc, trid)
        self.__rmv_stock(catalog)
        return trid
    
    def remove(self, acc, catalog, trid):
        if super().remove(trid):
            self.__rmv_acc_transact(acc, trid)
            self.__add_stock(catalog)
            return True
        return False

    def __add_acc_transact(self, acc, trid):
        acc.transacts.append(trid)
        acc.write()

    def __add_stock(self, catalog):
        catalog.stock += 1
        catalog.write()

    def __rmv_acc_transact(self, acc, trid):
        acc.transacts.remove(trid)
        acc.write()

    def __rmv_stock(self, catalog):
        catalog.stock -= 1
        catalog.write()
