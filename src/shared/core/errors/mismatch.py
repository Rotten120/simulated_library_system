from shared.core.lib_sys_error import LibSysError

class MisMatchError(LibSysError):
    def __init__(self, msg = "Value is incorrect"):
        super().__init__(msg)

class IncorrectPasswordError(MisMatchError):
    def __init__(self, msg = "Password is incorrect"):            
        super().__init__(msg)
