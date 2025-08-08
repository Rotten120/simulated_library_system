from core.errors import *
from core.error_codes import ErrorCodes as err

class LibErrors:
    errnos = {
        err.VALUE_NOT_FOUND:    ValueNotFoundError,
        err.USERNAME_NOT_FOUND: UsernameNotFoundError,
        err.CATALOG_NOT_FOUND:  CatalogNotFoundError,
        err.TRANSACT_NOT_FOUND: TransactNotFoundError,

        err.MISMATCH:           MisMatchError,
        err.INCORRECT_PASSWORD: IncorrectPasswordError,

        err.STOCK_INSUFFICIENT: StockInsufficientError,
        err.BORROW_EXCEEDED:    BorrowExceededError,

        err.OPTION_ERROR:       OptionError

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
        exc_class = LibErrors.errnos[errno]
        raise exc_class(param) if param else exc_class()
