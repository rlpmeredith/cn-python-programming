'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''
# Tested 19-17-19
str_input = input("Please enter your string input in lower case!: ")
vowel_list = ["a", "e", "i", "o", "u"]
vowel_count = 0
for i in vowel_list:
    vowel_count += (str_input.count(i))
print("Number of vowels is: " + str(vowel_count))

