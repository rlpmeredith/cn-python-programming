'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''
# Tested 19-17-19
str_input1 = input("Please enter your first string input: ")
str_input2 = input("Please enter your second string input: ")
str_input3 = input("Please enter your third string input: ")
print(max(str_input1, str_input2, str_input3, key=len))
