from core.errors import OptionError

class FilterValue:
    def val_in_range(val, lo, hi):
        if not(lo <= val <= hi):
            raise OptionError(lo, hi)
