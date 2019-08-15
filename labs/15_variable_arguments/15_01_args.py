'''
Write a script with a function that demonstrates the use of *args.

'''
# Tested 15-08-19

def gardenimplements(*args):
    print("In my garden I have:")
    for tool in args:
        print(f"A {tool}")


gardenimplements('Rake', 'Spade', 'Lawnmower')
