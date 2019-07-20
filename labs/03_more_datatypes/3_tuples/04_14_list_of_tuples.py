'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
# Tested 19-07-19
my_string = input("Please type in a list of words with spaces in between: ")
my_list = my_string.split()
my_final_list = []
tuple_temp = ()
for i in my_list:
    tuple_temp = tuple(list(i))
    my_final_list.append(tuple_temp)
print(my_final_list)

