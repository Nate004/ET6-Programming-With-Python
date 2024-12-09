# def mystery_1(a):
#     b = len(a)
#     for c in range(b):
#         for d in range(0, b-c-1):
#             if a[d] > a[d+1]:
#                 a[d], a[d+1] = a[d+1], a[d]
#     return a

def sort_bubble(a: list) -> list:
    """" This sorts a list of elements in ascending order
    
    Parameters:
        a: is the input parameter of List type data
        b: an integer that stores the length of the list a; this determines the number of iterations for sorting
        c: an integer and a loop variable which runs from 0 to b-1 (range)
        d: an integer  which runs from 0 to b-c-1 to compare adjacent elements and swap in case of wrong order
    the function returns a sorted list in ascending order
    >>> sort_bubble([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    >>> sort_bubble([3, 4, 1, 2])
    [1, 2, 3, 4]
    >>> sort_bubble([0, 2, 4, 5, 6, 1])
    [0, 1, 2, 4, 5, 6]
    >>> sort_bubble([])
    []
    """
    b = len(a)
    for c in range(b):
        for d in range(0, b - c - 1):
            if a[d] > a[d + 1]:
                a[d], a[d + 1] = a[d + 1], a[d]
    return a
