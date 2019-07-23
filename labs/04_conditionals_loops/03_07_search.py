'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
# Tested 23-07-19
my_count = 0
my_num = int(input("Please type in a number between 0 and a billion: "))

while my_count < my_num:
    my_count += 1
print("Number is ", my_count)