# Exercise 6: Design a Rectangle class with default attributes for length and width set to 1. Include methods to set these attributes and calculate the area.

class Rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle()
print(rect.area())  
rect.set_length(5)
rect.set_width(3)
print(rect.area())  
