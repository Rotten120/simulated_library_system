import json
import os

class Catalog:
    # CLASS INITIALIZE
    
    def __init__(self, data, directory):
        self.id = data["id"]
        self.__path = directory + "\\" + str(self.id) + ".txt"
        self.edit(data)

    def imp(file_path):
        file = open(file_path, 'r')
        data = json.loads(file.read())

        directory = file_path[:file_path.rfind('\\')]
        catalog = Catalog(data, directory)
        
        file.close()
        return catalog

    # OBJECTS MODIFY

    def edit(self, data):
        if self.id == data["id"]:
            self.title = data["title"]
            self.author = data["author"]
            self.genre = data["genre"]
            self.ref = data["reference"]

    # FILE MANAGEMENT

    def write(self):
        file = open(self.__path, 'w')
        file.write(json.dumps(self.parse()))
        file.close()

    def rmv(self):
        if os.path.isfile(self.__path):
            os.remove(self.__path)

    # GET METHODS

    def get_path(self):
        return self.__path
    
    def parse(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "reference": self.ref
        }
    
    def print(self):
        data = self.parse()
        data["path"] = self.__path
        print(data)
