'''
Write a script with a function that demonstrates the use of **kwargs.

'''
# Tested 15-08-19

def my_function(**kwargs):
    print("Attendance in each year of University was:")
    for year, percent in kwargs.items():
        print(f"In year {year} attendance was {percent} percent")


my_function(one=85, two=99, three=90)

