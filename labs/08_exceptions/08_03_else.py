'''
Write a script that demonstrates a try/except/else.

'''

try:
    my_var = int(input("Enter an integer if you are good and a string if you are bad: "))
except ValueError:
    print("You really are bad")
else:
    print("At least you can follow instructions")

