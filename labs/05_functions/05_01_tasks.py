'''

Write a script that completes the following tasks.

'''
#Tested 27-07-19

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
def div4or7(first_test):
    if first_test % 4 == 0 or first_test % 7 == 0:
        return True
    else:
        return False
# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean


def div4and7(second_test):
    if second_test % 4 == 0 and second_test % 7 == 0:
        return True
    else:
        return False

# take in a number from the user between 1 and 1,000,000,000


my_num = int(input("Please type in a number between 1 and a UK Billion! :"))

# call your functions, passing in the user input as the arguments, and set their output equal to new variables

isdiv4or7 = div4or7(my_num)
isdiv4and7 = div4and7(my_num)

# print your new variables to display the results

print(f"Divisible by 4 or 7, {isdiv4or7}")
print(f"Divisible by 4 and 7, {isdiv4and7}")
