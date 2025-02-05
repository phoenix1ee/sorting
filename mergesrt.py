#Shun Fai Lee Lab4
from sorter.msort_helper import merge0

def mergesrt(inputlist: list):
    """
    this is the recursive function for a straight merge function.
    User should provide an input list of items to be sorted. This function adapt the basic divided at the middle approach
    :param inputlist: the input array to be merged
    :return: the inputlist with the part [start:end] sorted, no. of comparisons and exchange make
    """
    cpsum = 0
    exsum = 0
    if len(inputlist) == 1:
        return inputlist, cpsum, exsum
    else:
        mid = (len(inputlist) - 1) // 2
        inputlist[0:mid + 1], temp_cp, temp_ex = mergesrt(inputlist[0:mid + 1])
        cpsum += temp_cp
        exsum += temp_ex
        inputlist[mid + 1:len(inputlist)], temp_cp2, temp_ex2  = mergesrt(inputlist[mid + 1:len(inputlist)])
        cpsum += temp_cp2
        exsum += temp_ex2
        inputlist, temp_cp3, temp_ex3 = merge0(inputlist[0:mid + 1],inputlist[mid + 1:len(inputlist)])
        cpsum += temp_cp3
        exsum += temp_ex3
        return inputlist, cpsum, exsum