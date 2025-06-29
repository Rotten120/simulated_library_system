import random
import os

class TableManager:
    def __init__(self, table_class, directory):
        self.tables = {}
        self.__table_class = table_class
        self.__dir = directory
        
        self.__get_tables()

    def __get_tables(self):
        for entry in os.scandir(self.__dir):
            if entry.is_file():
                table = self.__table_class.imp(entry.path)
                self.tables[table.id] = table

    def add(self, data):
        tid = self.generate_id(data["id"])
        table = self.__table_class(data, self.__dir)
        
        self.tables[tid] = table
        self.tables[tid].write()
        return tid

    def edit(self, tid, data):
        if not(tid in self.tables):
            return False
        
        table = self.tables[tid]
        table.edit(data)
        table.write()
        return True

    def remove(self, tid):
        if not(tid in self.tables):
            return False
        self.tables[tid].rmv()
        del self.tables[tid]
        return True

    def search(self, key, prompt):
        results = []
        for tid in self.tables:
            if self.tables[tid].parse()[key] == prompt:
                results.append(self.tables[tid])
        return results

    def valid_id(self, tid):
        return not(tid in self.tables) and (0 <= tid <= 999999)

    def generate_id(self, tid = -1):
        while not self.valid_id(tid):
            tid = random.randrange(0, 999999)
        return tid
