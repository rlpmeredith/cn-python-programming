'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
#Tested 31-7-19

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return f"Area is {self.length * self.width}"


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"Area is {self.radius ** 2 * 3.14}"


my_rect = Rectangle(3, 4)
my_circle = Circle(2)
print(my_rect.area())
print(my_circle.area())


