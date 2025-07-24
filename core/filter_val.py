from errors import *

class Filter:
    log_msg = ""

    def update_log():
        print(Filter.log_msg)
        Filter.log_msg = ""
    
    @staticmethod
    def valid_option(val, lo, hi):
        option = val
        if not(lo <= option <= hi):
            raise OptionError(lo, hi)
        return option
