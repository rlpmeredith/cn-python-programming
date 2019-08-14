'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''
#Tested 14-08-19

def my_sum(my_list):
    accum = 0
    for item in my_list:
        accum += item
    return(accum)

print(f"List is 1, 2, 3, 4")
accum = my_sum([1, 2, 3, 4])
print(f"Sum of list is: {accum}")