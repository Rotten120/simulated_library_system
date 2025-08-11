from core.lib_sys_error import LibSysError

class StockInsufficientError(LibSysError):
    def __init__(self, msg = "Insufficient Stocks"):
        super().__init__(msg)

class BorrowExceededError(LibSysError):
    def __init__(self, msg = "Exceeded allowed borrow count"):
        super().__init__(msg)
