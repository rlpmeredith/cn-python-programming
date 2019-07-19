'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

str_input1 = input("Enter 10 numbers separated by a space:")
my_list = str_input1.split()
print("Biggest number is:", max(my_list))
product = 1
for num in my_list:
    product = product * int(num)
print("Product of Numbers is:", product)
