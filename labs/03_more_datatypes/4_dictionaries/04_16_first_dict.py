'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''
# tested 19-07-19
result = {}
for i in range(1, 10):
    my_value = i**2
    result[i] = my_value
print(result)
