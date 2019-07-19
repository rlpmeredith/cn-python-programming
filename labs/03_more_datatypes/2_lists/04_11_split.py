'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''


my_string = input("Please input a list of words separated by spaces: ")
my_list = my_string.split()
print(max(set(my_list), key=my_list.count))


