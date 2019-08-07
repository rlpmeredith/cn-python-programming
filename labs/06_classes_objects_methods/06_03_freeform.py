'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...

'''
# Tested 01-08-19

class Pet:

    def __init__(self, species, cuteness, size="Small"):
        self.species = species
        self.cuteness = cuteness
        self.size = size

    def __str__(self):
        return f"{self.species, self.cuteness, self.size}"

    def __add__(self, o):
        return self.species + o.species


class LibraryItem:

    def __init__(self, lib_id, location, status = "in_stock"):
        self.lib_id = lib_id
        self.location = location
        self.status = status

    def __str__(self):
        return f"{self.lib_id, self.location, self.status}"


class Tree:
    def __init__(self, species, max_height, evergreen="True"):
        self.species = species
        self.max_height = max_height
        self.evergreen = evergreen

    def __str__(self):
        return f"{self.species, self.max_height, self.evergreen}"


pet1 = Pet("Cat", "Very Cute")
pet2 = Pet("Dog", "Ugly", "Large")
pet3 = pet1 + pet2
print(pet3)

my_book = LibraryItem(1234, "B1H2")
print(my_book)
my_book.status = "out"
print(my_book)

my_tree = Tree("oak", 10)
my_tree.evergreen = "False"
print(my_tree)
