from abc import ABC, abstractmethod
import json
import os

class Item(ABC):
    def __init__(self, data, directory):
        self.id = data["id"]
        self.__path = directory + "\\" + str(self.id) + ".txt"
        self.edit(data)

    def write(self):
        file = open(self.__path, 'w')
        file.write(json.dumps(self.parse()))
        file.close()

    def rmv(self):
        if os.path.isfile(self.__path):
            os.remove(self.__path)
            return True
        return False

    def get_path(self):
        return self.__path

    def create_path(directory, item_id):
        return directory + '\\' + str(item_id) + ".txt"

    @abstractmethod
    def imp(file_path):
        pass

    @abstractmethod
    def edit(self, data):
        pass

    @abstractmethod
    def parse(self):
        pass
