# Exercise 20: Dynamic Attribute Addition
# Demonstrate dynamic attribute addition where a class Vehicle starts without defined attributes and properties are added later.

class Vehicle:
    pass

v = Vehicle()
v.make = "Honda"
v.model = "Civic"
v.year = 2021

print("Make:", v.make)
print("Model:", v.model)
print("Year:", v.year)
