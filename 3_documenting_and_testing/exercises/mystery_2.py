# def mystery_2(a, b):
#     c = []
#     while a:
#         if b in a[0]:
#             c.append(a[0])
#         a = a[1:]
#     return c


def filter_list(a, b):
    """
    This code filters a list of strings, returning only those that contain a specified substring.

    Args:
        a (list): A list of strings to be filtered.
        b (str): The substring to search for within each string in the list.

    Returns:
        c (list): A list of strings from the input list that contain the specified substring.

    Example:
    >>> filter_list(["apple", "banana", "cherry", "date"], "a")
    ['apple', 'banana', 'date']
    >>> filter_list(["apple", "banana", "cherry", "date"], "b")
    ['banana']
    >>> filter_list(["rice", "beans", "goat", "fish", "hot"], "o")
    ['goat', 'hot']
    
    """
    c = [] # an empty list to store the filter
    while a: # loop to remain in the list a
        if b in a[0]: # condition to check if set condition b is in first element in list a 
            c.append(a[0]) # store if the if condition is true
        a = a[1:]
    return c
