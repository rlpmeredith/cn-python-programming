'''
Write a script that generates an exception. Handle this exception with a try/except.
For example:

list_ = ["hello world!"]
print(list_[1])

This raises and exception that needs to be handled.

'''
#Tested 10-08-2019

try:
    my_int = int("Hello world")
    print(my_int)
except:
    print("Well that didn't work!")