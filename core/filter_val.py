from errors import *

class Filter:
    log_msg = ""

    def update_log():
        print(Filter.log_msg)
        Filter.log_msg = ""
    
    @staticmethod
    def valid_option(val, lo, hi):
        try:
            option = int(val) - 1
            if not(lo <= option <= hi):
                raise OptionError(lo, hi)
        except ValueError:
            Filter.log_msg = "Invalid Input"
        except OptionError as o:
            Filter.log_msg = o
        else:
            return option
        return -1

    

    
    
