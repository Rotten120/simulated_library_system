class OptionError(Exception):
    def __init__(self, lo = None, hi= None):
        msg: str = "Option not in choices."
        if lo != None and hi != None:
            msg += f" Must be between {lo} and {hi}."
        super().__init__(msg)

class ValueNotFoundError(Exception):
    def __init__(self, key = "Value"):
        super().__init__(key + " does not exist")

class MisMatchError(Exception):
    def __init__(self, key = "Value"):
        super().__init__(key + " is incorrect")

class StockError(Exception):
    def __init__(self):
        super().__init__("Insufficient Stocks")

class BorrowError(Exception):
    def __init__(self):
        super().__init__("Exceeded allowed borrow count")


