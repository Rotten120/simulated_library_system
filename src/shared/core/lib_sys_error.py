class LibSysError(Exception):
    def __init__(self, msg = "Error occured!"):
        super().__init__(msg)
