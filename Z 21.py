# Exercise 21: Interface Implementation
# Create an interface Shape with methods area() and perimeter(). Implement this interface in Rectangle and Circle classes.

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

r = Rectangle(5, 3)
print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())

c = Circle(4)
print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())
