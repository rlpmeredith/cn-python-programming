'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

my_string = input("Please type in a list of words with spaces in between:")
#my_list = my_string.split()
my_tuple = tuple(list(my_string))
print(my_tuple)

#stuck