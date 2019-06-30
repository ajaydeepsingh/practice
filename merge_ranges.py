class Range(object):
    def __init__(self):
        self.lower_bound = -1
        self.upper_bound = -1
    
    def __init__(self,lower_bound,upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
 
    def __str__(self):
        return "["+str(self.lower_bound)+","+str(self.upper_bound)+"]"


def merge_ranges(input_range_list):
    out = []
    initialRange = Range(input_range_list[0].lower_bound,input_range_list[0].upper_bound)
    out.append(initialRange)

    for x in input_range_list:
        for y in range(0,len(out)):
            if (out[y].upper_bound >= x.lower_bound and x.lower_bound >= out[y].lower_bound):
                if out[y].lower_bound > x.lower_bound:
                    out[y].lower_bound  = x.lower_bound
                if out[y].upper_bound < x.upper_bound:
                    out[y].upper_bound = x.upper_bound
            elif len(out) != y+1:
                pass
            else:
                new = Range(x.lower_bound,x.upper_bound)
                out.append(new)

    return out
# Driver Code

print(merge_ranges([[1,10], [5,8], [8,15]]))

