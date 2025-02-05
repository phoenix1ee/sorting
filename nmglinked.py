from sorter.sorterhelper import nmnode

def merge1(n1: nmnode, n2: nmnode):
    """
    this is the merge function for a merge sort.
    it will take 2 supposedly sorted list and output a combined sorted list. Priority will be given to items in list L1,
    when equal
    :param n1: the 1st node to be merged
    :param n2: the 2nd node array to be merged
    :return: a combined array
    """
    cp = 0
    ex = 0
    if not n1 or not n2:
        raise Exception()
    else:
        c1 = n1
        c2 = n2
        if c1.v <= c2.v:
            temp = c1
            c1 = c1.next
        else:
            temp = c2
            c2 = c2.next
        cp += 1
        temp.next = None
        tail = temp
        while c1 and c2:
            if c1.v <= c2.v:
                tail.next = c1
                c1 = c1.next
            else:
                tail.next = c2
                c2 = c2.next
            cp += 1
            ex += 1
            tail = tail.next
            tail.next = None
        if c1:
            tail.next = c1
            ex += 1
        else:
            tail.next = c2
            ex += 1
        return temp, cp, ex

def nmglinked(inputlist: list):
    if len(inputlist) == 1:
        temp = inputlist[0]
        return temp, 0, 0
    else:
        mid = (len(inputlist) - 1) // 2
        leftnode,temp_cp1,temp_ex1 = nmglinked(inputlist[:mid+1])
        rightnode,temp_cp2,temp_ex2 = nmglinked(inputlist[mid+1:])
    outnode, temp_cp3,temp_ex3 = merge1(leftnode,rightnode)
    return outnode, temp_cp1+temp_cp2+temp_cp3, temp_ex1+temp_ex2+temp_ex3