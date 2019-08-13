'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''
#Tested 12-08-19

def subtract_divide(dividend, x, y):
        z = x - y
        return dividend / z


assert subtract_divide(10, 4, 2) == 5

assert subtract_divide(99, 6, 3) == 33

assert subtract_divide(100, 20, 10) == 5, "Doesn't work....."



