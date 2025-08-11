from core.lib_sys_error import LibSysError

class OptionError(LibSysError):
    def __init__(self, lo = None, hi= None):
        msg: str = "Option not in choices."
        if lo != None and hi != None:
            msg += f" Must be between {lo} and {hi}."
        super().__init__(msg)
