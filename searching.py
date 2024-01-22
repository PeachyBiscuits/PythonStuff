def linear_search(l, item, issorted = False) :
    for i in range(len(l)) :
        if l[i] == item :
            return i
    return None 

def binary_search(l, item, issorted = False, ) :

    first = 0
    last = len(l) - 1

    if issorted == False :
        return(linear_search(l, item, issorted = False))

    while( first <= last ):
        mid = (first + last)//2
        if l[mid] == item :
            return mid
        elif item < l[mid] :
            last = mid - 1
        else :
            first = mid + 1	
    return None