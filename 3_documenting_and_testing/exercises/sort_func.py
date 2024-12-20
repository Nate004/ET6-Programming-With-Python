def sort_func(a, b=None):
    """This function sorts a list of numbers in ascending order
    returns a list b
    
    
    """
    if b is None:
        b = []
    while a:
        c = min(a)
        a.remove(c)
        b.append(c)
    return b
