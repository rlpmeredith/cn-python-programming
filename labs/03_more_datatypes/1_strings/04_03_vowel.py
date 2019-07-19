'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''

str_input = input("Please enter your string input in lower case!: ")
num_a = (str_input.count("a"))
num_e = (str_input.count("e"))
num_i = (str_input.count("i"))
num_o = (str_input.count("o"))
num_u = (str_input.count("u"))
print("Number of vowels is:")
print(num_a + num_e + num_i + num_o + num_u)

