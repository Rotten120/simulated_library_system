from table.account import Account
from table_manager.table_manager import TableManager

class AccountManager(TableManager):
    def add(self, data):
        results = self.search("username", data["username"])
        if len(results) == 0:
            return super().add(data)
        return False

    def edit(self, aid, data, password):
        if not self.valid_id(aid) or not acc.password_check(password):
            return Fals
        return super().edit(aid, data)
    
    def remove(self, aid, password):
        if not self.valid_id(aid) or not acc.password_check(password):
            return False
        return super().remove(aid)
