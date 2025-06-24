from table.catalog import Catalog
from table_manager.file_manager import FileManager

class CatalogMgr(FileManager):
    def import_item(self, file_path):
        return Catalog.imp(file_path)

    def create_item(self, data):
        return Catalog(data, self.dir)

