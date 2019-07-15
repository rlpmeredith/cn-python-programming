'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

x = 7
y = float(x)
print(y)

a = 2.3
b = int(a)
print(b)

print(a // x)

num1 = int(input("First Number "))
num2 = int(input("Second Number "))
print("Result of multiplcation is ", num1 * num2)
