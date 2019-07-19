'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

str_input = input("Please enter your string input: ")
letter_input = input("Please enter your letter: ")
print(str_input.index(letter_input))