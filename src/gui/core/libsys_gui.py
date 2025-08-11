import mysql.connector
from core.lib_errors import LibErrors
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

    def commit():
        LibSys.__conn.commit()

    def get(key, params = None):
        try:
            query = Queries.get(key)
            LibSys.__cursor.execute(query, params)
            return LibSys.__cursor.fetchall()
        except mysql.connector.Error as e:
            LibErrors.throw(e)

    def set(key, params = None):
        try:
            query = Queries.get(key)
            LibSys.__cursor.execute(query, params)
            LibSys.__conn.commit()
        except mysql.connector.Error as e:
            LibErrors.throw(e)

    def switch_page(key, args = []):
        LibSys.__pages[key].run(args)

    
    

    
    
