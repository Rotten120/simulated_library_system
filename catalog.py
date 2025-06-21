import json

class Catalog:
    def __init__(self, file_path):
        file = open(file_path, 'r')
        data = json.loads(file.read())

        self.title = data["title"]
        self.author = data["author"]
        self.genre = data["genre"]
        self.ref = data["reference"]
        self.__path = file_path

    def update(self):
        file = open(self.__path, 'w')
        data = json.dumps(self.__parse())
        file.write(data)
        
    def __parse(self):
        return {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "reference": self.ref
        }
    
    def print(self):
        data = self.__parse()
        data["path"] = self.__path
        print(data)
