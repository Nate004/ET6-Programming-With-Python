def mystery_3(a, b):
    if a < b:
        return a
    elif a > b:
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
