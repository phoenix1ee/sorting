#Shun Fai Lee Lab4
from sorter.qsort_helper import partitiion

def qsort1st(target: list, low, high):
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
    elif high-low == 1:
        if temp[low]<temp[high]:
            cpsum += 1
            return temp, cpsum, exsum
        else:
            cpsum+=1
            A = temp[low]
            temp[low] = temp[high]
            temp[high] = A
            exsum += 1
            return temp, cpsum, exsum
    else:
        new, temp_cp, temp_ex= partitiion(temp, low, high)
        cpsum+=temp_cp
        exsum+=temp_ex
        temp, temp_cp2, temp_ex2 = qsort1st(temp,low,new)
        cpsum+=temp_cp2
        exsum+=temp_ex2
        temp , temp_cp3, temp_ex3= qsort1st(target, new+1, high)
        cpsum+=temp_cp3
        exsum+=temp_ex3
        return temp, cpsum, exsum