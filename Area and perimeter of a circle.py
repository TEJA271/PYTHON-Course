class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

circle = Circle(5)  # radius = 5

print("Area:", circle.area())
print("Perimeter:", circle.perimeter())
