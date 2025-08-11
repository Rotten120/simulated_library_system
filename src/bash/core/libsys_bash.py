import mysql.connector
from shared.core.lib_errors import LibErrors
from shared.core.queries import Queries

class LibSysBash:
    __conn = None
    __cursor = None
    __cmds = {}
    config = {}

    def init(config, cmds):
        dblog = config["dblog"]
        LibSys.__conn = mysql.connector.connect(
            host = dblog["host"],
            user = dblog["user"],
            password = dblog["pass"],
            database = dblog["db"]
        )

        LibSys.__cursor = LibSys.__conn.cursor()
        LibSys.__cmds = cmds
        LibSys.config = config

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

    def run_cmd(cmd, params = []):
        LibSys[cmd].execute(params)
    

    
    

