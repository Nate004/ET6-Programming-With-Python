def max_min(a, b):
    """"This function finds the minimum and maximum value between 2 inputs a & b
    where both inputs are equal, the final if condition returns the sum of a & b
    
    >>> max_min(10,7)
    7
    >>> max_min(3,10)
    3
    >>> max_min(2,2)
    4
    """
    if a < b: # test for minimum
        return a
    elif a > b: # test for maximum
        return b
    else:
        return a + b


result1 = max_min(3, 5)
result2 = max_min(10, 2)
result3 = max_min(4, 4)

# Print the results
print(result1)
print(result2)
print(result3)
