'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''
Tested 31-07-2019

class Car:

    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def inc_max_speed(self):
        self.max_speed += 5

    def __str__(self):
        return f"The car model name is {self.model}, the car year is {self.year} and the max speed is {self.max_speed}"


my_car = Car("VW", 2017, 155)
my_car.inc_max_speed()
my_car.year = 2015
print(my_car)
