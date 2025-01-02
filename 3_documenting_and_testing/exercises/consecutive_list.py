"""
A module for generating lists of consecutive integers.

Module contents:
    - consecutive_list: generates a list of n consecutive integers starting from a given number.

Created on 02 01 25
"""

# --- before documenting and testing ---

# def mystery_6(a, b):
#     if a == 0:
#         return []
#
#     c = []
#     while len(c) < a:
#         c.append(b)
#         b = b + 1
#
#     return c

# --- after documenting and testing ---


def consecutive_list(a: int, b: int) -> list[int]:
    """Generates a list of consecutive integers starting from a given number.

    Parameters:
        a ==length: int, the number of integers to generate
        b ==start: int, the starting integer

    Returns -> list[int] with the generated consecutive integers

    Raises:
        AssertionError: if length is not an integer
        AssertionError: if start is not an integer
        AssertionError: if length is less than 0

    >>> consecutive_list(0, 5)
    []

    >>> consecutive_list(4, 5)
    [5, 6, 7, 8]

    >>> consecutive_list(3, 10)
    [10, 11, 12]
    """
    
    # the length should be an integer greater than or equal to 0
    assert isinstance(a, int), "a is not an integer"
    assert isinstance(b, int), "b is not an integer"
    assert a >= 0, "a is less than 0"
    
    
    if a == 0: # If list a is 0, function to return an empty list
        return []

    c = [] # final result is stored in c, a list
    while len(c) < a:
        c.append(b)
        b = b + 1

    return c
