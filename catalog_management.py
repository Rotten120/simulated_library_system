from catalog import *

class CatMgr:    
    def __init__(self, directory):
        self.dir = directory
        self.catalogs = self.__get_catalogs()
        
    def __get_catalogs(self):
        cats = {}
        for entry in os.scandir(self.dir):
            if entry.is_file():
                cat = Catalog.imp(entry.path)
                cats[cat.id] = cat
        return cats

    def add(self, data):
        data_id = data["id"]
        catalog = Catalog(data)

        if not(data_id in self.catalogs):
            catalog.write()
            self.catalogs[data_id] = catalog
        else:
            print("Catalog ID already in directory")
        
    def edit(self, data):
        data_id = data["id"]
        if data_id in self.catalogs:
            self.catalogs[data_id].edit(data)
        else:
            print("Catalog ID does not exist")

    def remove(self, id_num):
        if id_num in self.catalogs:
            self.catalogs[id_num].rmv()
            del self.catalogs[id_num]
        else:
            print("Catalog ID does not exist")

    def search(self, key, prompt):
        no_results = True
        for cat_id in self.catalogs:
            if self.catalogs[cat_id].parse[key] == prompt:
                no_results = False
                self.catalogs[cat_id].print()
        if no_results:
            print("No catalog matches the prompt in", key)
