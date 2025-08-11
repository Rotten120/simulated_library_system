from shared.core.lib_sys_error import LibSysError

class ValueNotFoundError(LibSysError):
    def __init__(self, msg = "Value not found"):
        super().__init__(msg)

class UsernameNotFoundError(ValueNotFoundError):
    def __init__(self, msg = "Username not found"):
        super().__init__(msg)

class CatalogNotFoundError(ValueNotFoundError):
    def __init__(self, msg = "Catalog not found"):
        super().__init__(msg)

class TransactNotFoundError(ValueNotFoundError):
    def __init__(self, msg = "Transaction not found"):
        super().__init__(msg)
