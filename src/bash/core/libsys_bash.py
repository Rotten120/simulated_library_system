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
        LibSysBash.__conn = mysql.connector.connect(
            host = dblog["host"],
            user = dblog["user"],
            password = dblog["pass"],
            database = dblog["db"]
        )

        LibSysBash.__cursor = LibSysBash.__conn.cursor()
        LibSysBash.__cmds = cmds
        LibSysBash.config = config

    def run():
        prompt = ""
        while True:
            prompt = input("$ ")
            args = prompt.split()
            cmd = args[0]
            
            LibSysBash.run_cmd(cmd, args[1:])

    def cursor():
        return LibSysBash.__cursor

    def commit():
        LibSysBash.__conn.commit()

    def get(key, params = None):
        try:
            query = Queries.get(key)
            LibSysBash.__cursor.execute(query, params)
            return LibSysBash.__cursor.fetchall()
        except mysql.connector.Error as e:
            LibErrors.throw(e)

    def set(key, params = None):
        try:
            query = Queries.get(key)
            LibSysBash.__cursor.execute(query, params)
            LibSysBash.__conn.commit()
        except mysql.connector.Error as e:
            LibErrors.throw(e)

    def run_cmd(cmd, params = []):
        try:
            LibSysBash.__cmds[cmd].execute(params)
        except KeyError:
            print(f"lib: `{cmd}` is not a lib command. See 'lib --help'")
    

    
    

