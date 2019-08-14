'''
Using list comprehension, create a list "positive" from the list
"numbers" that contains only the positive numbers from the list "numbers".

'''
# Tested 14-08-19

positive = []
numbers = [5, -8, 3, 10, -19, -22, 44, 2, -1, 4, 42]

positive = [mynum for mynum in numbers if mynum > 0]

print(positive)
