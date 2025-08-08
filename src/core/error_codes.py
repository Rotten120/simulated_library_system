from core.errors import *

class LibErrors:
    errnos = {
        50001: ValueNotFoundError,
        50002: UsernameNotFoundError,
        50003: CatalogNotFoundError,
        50004: TransactNotFoundError,

        50005: MisMatchError,
        50006: IncorrectPasswordError,

        50007: StockInsufficientError,
        50008: BorrowExceededError,

        50009: OptionError

        #50010: INVALID VALUE TO BORROW
        #50011: CATALOGID CANNOT BE CHANGED
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
            raise LibErrors.errnos[errno](param)
        else:
            raise LibErrors.errnos[errno]
