import math
import statistics

def total(values : list) -> float:
    total=sum(values)
    #print(total)
    return total

def average(values : list) -> float:
    if values == []:
        #print(math.nan)
        return math.nan
    else:
        average=sum(values)/len(values)
        #print(average)
        return average

def median(values : list) -> float:
    if values == []:
        raise ValueError("empty list")
    else:
        median=statistics.median(values)
        #print(median)
        return median

#total ([4,2,5])
#average ([4,2,5])
#median ([4,2,5,10])