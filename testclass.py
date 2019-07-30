class Car:
    """Returns argument a is squared."""
    
    def __init__(self, model, year, speed=0):
        """Returns argument a is squared."""
        self.model = model
        self.year = year
        self.speed = speed
    
    def accelerate(self):
        """Returns argument a is squared."""
        self.speed += 5
    
    def brake(self):
        """Returns argument a is squared."""
        if self.speed > 0:
            self.speed -= 5
    
    def honk_horn(self):
        """Returns argument a is squared."""
        print(f"{self.model} goes 'beep beep'")


my_car = Car("Toyota", 1975)
print(my_car.speed)
