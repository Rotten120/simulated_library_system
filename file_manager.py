from abc import ABC, abstractmethod
import random
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
        item_id = self.generate_id(data["id"])
        item = self.create_item(data)
        
        self.items[item_id] = item
        self.items[item_id].write()
        return item_id

    def edit(self, item_id, data):
        if item_id in self.items:
            item = self.items[item_id]
            item.edit(data)
            item.write()
            return True
        return False

    def remove(self, item_id):
        if item_id in self.items:
            self.items[item_id].rmv()
            del self.items[item_id]
            return True
        return False

    def search(self, key, prompt):
        results = []
        for item_id in self.items:
            if self.items[item_id].parse()[key] == prompt:
                results.append(self.items[item_id])
        return results

    def print(self):
        for item_id in self.items:
            print(end = "\n\n")
            self.items[item_id].print()

    def generate_id(self, item_id):
        while item_id in self.items:
            item_id = random.randrange(0, 999999)
        return item_id

    @abstractmethod
    def import_item(self, file_path):
        pass

    @abstractmethod
    def create_item(self, data):
        pass
