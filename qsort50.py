#Shun Fai Lee Lab4
from sorter.insertionsort import insertionsort
from sorter.qsort_helper import partitiion

def qsort50(target: list, low, high):
    """
    sort the input list with quicksort using 1st element as pivot
    :param target: the list to be sorted
    :param low: the starting index of sorting
    :param high: the end index of sorting
    :return: the list, no. of comparisons and exchange make
    """
    temp = target
    cpsum = 0
    exsum = 0
    if low >= high:
        return temp, cpsum, exsum
    new, temp_cp, temp_ex = partitiion(temp, low, high)
    cpsum+=temp_cp
    exsum+=temp_ex
    if new - low < 50:
        temp[low:new+1], temp_cp2, temp_ex2 = insertionsort(temp[low:new+1])
    else:
        temp, temp_cp2, temp_ex2 = qsort50(temp,low,new)
    cpsum+=temp_cp2
    exsum+=temp_ex2
    if high - new < 50:
        temp[new + 1:high+1], temp_cp3, temp_ex3 = insertionsort(temp[new + 1:high+1])
    else:
        temp , temp_cp3, temp_ex3 = qsort50(temp, new + 1, high)
    cpsum+=temp_cp3
    exsum+=temp_ex3
    return temp, cpsum, exsum