'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
of numbers from the lower bound to the upper bound.

For example, if a user enters 1 and 100, the output should be:
The sum is: 5050
'''
# Tested 23-7-19
my_sum = 0
upper_bnd = int(input("Please enter upper bound: "))
lower_bnd = int(input("Please enter lower bound: "))

for i in range(lower_bnd, upper_bnd + 1):
    my_sum += i

print("The sum is: ", my_sum)


