
''' Write a script that sorts a list of tuples based on the number value in the tuple.
For example: unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''
# Tested 22-07-19 will only work with one fo each item as using tuple delete!
# Not great using a max number either?
unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []
lowest_value = 999
my_tuple = ()
for i in range(0, len(unsorted_list)):
    for j in unsorted_list:
        if j[1] < lowest_value:
            my_tuple = j
            lowest_value = j[1]
    sorted_list.append(my_tuple)
    unsorted_list.remove(my_tuple)
    lowest_value = 999
print(sorted_list)



