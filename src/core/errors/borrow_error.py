class StockInsufficientError(Exception):
    def __init__(self, msg = "Insufficient Stocks"):
        super().__init__(msg)

class BorrowExceededError(Exception):
    def __init__(self, msg = "Exceeded allowed borrow count"):
        super().__init__(msg)
