"""
A module for filtering lists of strings.

Module contents:
    - mystery_7: filters a list of strings, returning only those that contain a given substring.

Created on 13 01 25
@author: Taiwo Babatunde
"""
# --- before documenting and testing ---

# def mystery_7(a, b):
#     c = []
#     for d in a:
#         if b in d:
#             c.append(d)
#     return c

# --- after documenting and testing ---

def list_filter(a: list[str], b: str) -> list[str]:
    """Filters a list of strings, returning only those that contain a given substring.

    Parameters:
        a: list[str], the list of strings to filter
        b: str, the substring to search for

    Returns -> list[str] with the strings that contain the substring

    Raises:
        AssertionError: if a is not a list of strings
        AssertionError: if b is not a string

    >>> list_filter(["apple", "banana", "cherry"], "a")
    ['apple', 'banana']

    >>> list_filter(["dog", "cat", "mouse"], "o")
    ['dog', 'mouse']

    >>> list_filter(["hello", "world"], "z")
    []
    """

    # ensure a is a list of strings and b is a string
    assert isinstance(a, list)
    assert all(isinstance(item, str) for item in a), "a is not a list of strings"
    assert isinstance(b, str), "b is not a string"

    # filter the list of strings
    result = []
    for d in a:
        if b in d:
            result.append(d)

    return result
