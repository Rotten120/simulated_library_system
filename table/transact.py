from table.catalog import Catalog
from table.account import Acc
from table.item import Item
import json

class Transaction(Item):
    def imp(file_path):
        file = open(file_path, 'r')
        data = json.loads(file.read())

        directory = file_path[:file_path.rfind('\\')]
        transact = Transaction(data, directory)

        file.close()
        return transact

    def edit(self, data):
        if self.id == data["id"]:
            self.borrower = data["borrower"]
            self.catalog = data["catalog"]
            self.borrow_date = data["borrow date"]
            self.due_date = data["due date"]

    def parse(self):
        return {
            "id": self.id,
            "borrower": self.borrower,
            "catalog": self.catalog,
            "borrow date": self.borrow_date,
            "due date": self.due_date
        }

    def print(self, dirs):
        catalog = Catalog.create_path(dirs["catalog"], self.catalog)
        account = Acc.create_path(dirs["account"], self.borrower)

        print("Id:", self.id)
        print("Borrower:", account.username)
        print("Catalog:", catalog.title)
        print("Borrow Date", self.borrow_date)
        print("Due Date", self.due_date)
