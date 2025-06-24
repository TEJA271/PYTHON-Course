# Exercise 19: Using Property Decorators
# Implement a class Circle with a private attribute radius and use property decorators to get and set its value with checks.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            print("Radius cannot be negative.")
        else:
            self._radius = value

c = Circle(5)
print("Radius:", c.radius)

c.radius = 10
print("Updated Radius:", c.radius)

c.radius = -3  