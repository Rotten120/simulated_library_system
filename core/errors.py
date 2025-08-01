class OptionError(Exception):
    def __init__(self, lo = None, hi= None):
        msg: str = "Option not in choices."
        if lo != None and hi != None:
            msg += f" Must be between {lo} and {hi}."
        super().__init__(msg)

class ValueNotFoundError(Exception):
    def __init__(self, key = "Value"):
        super().__init__(key + " does not exist")

class IntegrityError(Exception):
    def __init__(self, key = "Value"):
        super().__init__(key + " already exists")
