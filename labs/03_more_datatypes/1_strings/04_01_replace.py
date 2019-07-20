'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''
# Tested 19-17-19
str_input = input("Please enter your string input: ")
sym_input = input("Please enter your symbol input: ")
print(str_input.replace(str_input[0], sym_input))
