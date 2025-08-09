from core.lib_sys_error import LibSysError

class UnreturnedCatalogError(LibSysError):
    def __init__(self, msg = "Return borrowed catalogs first"):
        super().__init__(msg)
