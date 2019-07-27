'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.
.
'''
# Tested 23-07-19
my_num = float(input("Type in a number between 1 and 1,000,000: "))

if (my_num % 3) == 0:
    print("Your number is divisible by 3")
else:
    print("Your number is not divisible by 3")
