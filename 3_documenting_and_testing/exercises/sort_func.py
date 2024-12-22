def sort_func(a, b=None):
    """This function sorts a list of numbers in ascending order
    returns a list b
    Examples:
    >>> sort_func([1, 2, 4, 3])
    [1, 2, 3, 4]
    
    >>> sort_func([1.0, 3.2, 1.5, 2.9, 0.5])
    [0.5, 1.0, 1.5, 2.9, 3.2]
    
    """
    if b is None:
        b = []
    while a:
        c = min(a)
        a.remove(c)
        b.append(c)
    return b
