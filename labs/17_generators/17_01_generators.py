'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''
#Tested 14-08-19

gen = (x for x in range(1, 11))

for my_num in gen:
    print(my_num)
