from abc import ABC, abstractmethod
import os

class FileManager(ABC):
    def __init__(self, directory):
        self.dir = directory
        self.items = self.__get_items()

    def __get_items(self):
        items = {}
        for entry in os.scandir(self.dir):
            if entry.is_file():
                item = self.import_item(entry.path)
                items[item.id] = item
        return items

    def add(self, data):
        item_id = data["id"]
        item = self.create_item(data)

        if not(item_id in self.items):
            item.write()
            self.items[item_id] = item
        else:
            print("Item ID already exists in directory")

    def edit(self, data):
        item_id = data["id"]
        if item_id in self.items:
            self.items[item_id].edit(data)
        else:
            print("Item ID does not exists in directory")

    def remove(self, item_id):
        if item_id in self.items:
            self.items[item_id].rmv()
            del self.items[item_id]
        else:
            print("Item ID does not exists in directory")

    def search(self, key, prompt):
        no_results = True
        for item_id in self.items:
            if self.items[item_id].parse()[key] == prompt:
                no_results = False
                self.items[item_id].print()
        if no_results:
            print("No item matches the prompt inputted for", key)

    @abstractmethod
    def import_item(self, file_path):
        pass

    @abstractmethod
    def create_item(self, data):
        pass
