def sequence_gen(a):
    """This function generates a list of integers stored in b
    the list is to start from c=0, and while the length of b<a, 
    the function continues to generate all elements in the list
    with incremental value of 1
    For example:
    >>> sequence_gen(3)
    [0, 1, 2]
    >>> sequence_gen(7)
    [0, 1, 2, 3, 4, 5, 6]
    """
    assert isinstance(a, int)
    b = []

    c = 0
    while len(b) < a:
        b.append(c)
        c = c + 1 # increase next element in list by 1

    return b
