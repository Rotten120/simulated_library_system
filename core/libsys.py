import mysql.connector
from core.queries import Queries

class LibSys:
    __conn = None
    __cursor = None
    __pages = {}
    logged = 0

    def init(server, acc, pw, db, windows):
        LibSys.__conn = mysql.connector.connect(
            host = server,
            user = acc,
            password = pw,
            database = db
        )

        LibSys.__cursor = LibSys.__conn.cursor()
        LibSys.__pages = windows
        LibSys.logged = 0

    def cursor():
        return LibSys.__cursor

    def get(key, params = None):
        query = Queries.get(key)
        LibSys.__cursor.execute(query, params)
        return LibSys.__cursor.fetchall()

    def set(key, params = None):
        query = Queries.get(key)
        LibSys.__cursor.execute(query, params)
        LibSys.__conn.commit()

    def switch_page(key):
        LibSys.__pages[key].run()

    
    

    
    
