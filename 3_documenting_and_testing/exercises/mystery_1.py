def mystery_1(a):
    """" This sorts a list of elements in ascending order
    
    Parameters:
        a: is the input parameter of List type data
        b: an integer that stores the length of the list a; this determines the number of iterations for sorting
        c: an integer and a loop variable which runs from 0 to b-1 (range)
        d: an integer  which runs from 0 to b-c-1 to compare adjacent elements and swap in case of wrong order
    """
    b = len(a)
    for c in range(b):
        for d in range(0, b - c - 1):
            if a[d] > a[d + 1]:
                a[d], a[d + 1] = a[d + 1], a[d]
    return a
