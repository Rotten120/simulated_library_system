from json import loads

class Catalog:
    def __init__(self, file_path):
        file = open(file_path, 'r')
        data = loads(file.read())

        self.title = data["title"]
        self.author = data["author"]
        self.genre = data["genre"]
        self.ref = data["reference"]
        self.path = file_path

    
