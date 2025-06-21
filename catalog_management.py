import os
from catalog import *

class CatalogManagement:
    def __init__(self):
        catalogs = []

    def get_catalogs(self, directory):
        for entry in os.scandir(directory):
            if entry.is_file():
                cat = Catalog(entry.path)
                catalogs.append(cat)
