from item import Item
import json

class Catalog(Item):
    def imp(file_path):
        file = open(file_path, 'r')
        data = json.loads(file.read())

        directory = file_path[:file_path.rfind('\\')]
        catalog = Catalog(data, directory)

        file.close()
        return catalog
    
    def edit(self, data):
        if self.id == data["id"]:
            self.title = data["title"]
            self.author = data["author"]
            self.genre = data["genre"]
            self.ref = data["reference"]
    
    def parse(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "reference": self.ref
        }
    
    def print(self):
        print("ID:\t\t", self.id)
        print("Title:\t\t", self.title)
        print("Author:\t\t", self.author)
        print("Genre:\t\t", self.genre)
        print("Reference:\t", self.ref)
