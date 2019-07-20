'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
# Tested 19-7-19 -> not entirely happy with how it actually works!
my_string = input("Please input a list of words separated by spaces: ")
my_list = my_string.split()
print(set(my_list))
print("Word with most occurences is: ", (max(set(my_list), key=my_list.count)))


