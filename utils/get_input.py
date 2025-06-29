class Input:
    @staticmethod
    def __is_number_valid(num, begin, end, vals):
        return ((begin == end) or (begin <= num <= end)) and ((len(vals) == 0) or num in vals)
    
    @staticmethod
    def number(prompt = "", invalidmsg = "", errormsg = "", begin = 0, end = 0, vals = [], return_val = 0, maxiter = -1):
        num_inp = 0
        iterate = 0
        
        if begin > end:
            raise Exception("Begin value must be lower than End value")
        if len(vals) > 0 and min(vals) >= end and max(vals) <= begin and begin != end:
            raise Exception("Range of values is outside the range of begin and end")
        
        while True:
            iterate += 1
            if maxiter != -1 and maxiter <= iterate:
                break
            
            try:
                num_inp = int(input(prompt))
                if Input.__is_number_valid(num_inp, begin, end, vals):
                    return num_inp
                elif invalidmsg != "":
                    print(invalidmsg)
            except ValueError:
                if errormsg != "":
                    print(errormsg)
            
        return return_val
