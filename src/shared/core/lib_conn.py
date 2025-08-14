import mysql.connector
from shared.core.lib_errors import LibErrors
from shared.core.queries import Queries

class LibConn:
    __conn = None
    __cursor = None

    def init(server, acc, pw, db):
        LibConn.__conn = mysql.connector.connect(
            host = server,
            user = acc,
            password = pw,
            database = db
        )

        LibConn.__cursor = LibConn.__conn.cursor()

    def cursor():
        return LibConn.__cursor

    def commit():
        LibConn.__conn.commit()

    def get(key, params = None):
        try:
            query = Queries.get(key)
            LibConn.__cursor.execute(query, params)
            return LibConn.__cursor.fetchall()
        except mysql.connector.Error as e:
            LibErrors.throw(e)

    def set(key, params = None):
        try:
            query = Queries.get(key)
            LibConn.__cursor.execute(query, params)
            LibConn.__conn.commit()
        except mysql.connector.Error as e:
            LibErrors.throw(e)
