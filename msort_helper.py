#Shun Fai Lee Lab4
def merge0(L1: list, L2: list):
    """
    this is the merge function for a merge sort.
    it will take 2 supposedly sorted list and output a combined sorted list. Priority will be given to items in list L1,
    when equal
    :param L1: the 1st input array to be merged
    :param L2: the 2nd input array to be merged
    :return: a combined array, no. of comparisons and exchange make
    """
    cpnos = 0
    exnos = 0
    L1size = len(L1)
    L2size = len(L2)
    output = []
    while len(L1)>0 and len(L2)>0:
        cpnos += 1
        if L1[0] <= L2[0]:
            output.append(L1.pop(0))
        else:
            output.append(L2.pop(0))
    if len(L1) == 0:
        output = output + L2
        L2.clear()
    elif len(L2) == 0:
        output = output + L1
        L1.clear()
    if len(output) != L1size+L2size:
        raise Exception()
    return output, cpnos, exnos