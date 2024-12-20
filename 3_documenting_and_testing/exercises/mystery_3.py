def mystery_3(a, b):
    """"This function finds the minimum and maximum value between 2 inputs a & b
    where both inputs are equal, the final if condition returns the sum of a & b
    """
    if a < b: # test for minimum
        return a
    elif a > b: # test for maximum
        return b
    else:
        return a + b


result1 = mystery_3(3, 5)
result2 = mystery_3(10, 2)
result3 = mystery_3(4, 4)

# Print the results
print(result1)
print(result2)
print(result3)
