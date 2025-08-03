from core.errors import *

class LibErrors:
    errnos = {
        50001: ValueNotFoundError,
        50002: MisMatchError,
        50003: BorrowError, #INVALID VALUE TO BORROW
        50004: BorrowError, #CatalogID cannot be changed, #INTEGRITY ERROR
        50005: StockError,
        50006: BorrowError,
        50008: OptionError
    }

    def throw(error):
        #USER EXCEPTIONS
        if error.errno in LibErrors.errnos:
            LibErrors.exceptions(error.errno)
        #BUILT-IN MYSQL EXCEPTIONS
        else:
            raise error

    def exceptions(errno, param = None):
        if param != None:
            raise LibErrors.errnoso[errno](param)
        else:
            raise LibErrors.errnos[errno]
