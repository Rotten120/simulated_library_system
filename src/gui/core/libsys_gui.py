from shared.core.lib_conn import LibConn

class LibSys(LibConn):
    __pages = {}
    logged = 0

    def init(host, user, pw, db, windows):
        LibConn.init(host, user, pw, db)
        LibSys.__pages = windows
        LibSys.logged = 0

    def switch_page(key, args = []):
        LibSys.__pages[key].run(args)

    
    

    
    
