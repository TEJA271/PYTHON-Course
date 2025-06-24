# Exercise 15: Polymorphism with a Function
# Create a function describe_pet that takes an object of Animal and calls its speak method, demonstrating polymorphism.

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog says Woof!")

class Cat(Animal):
    def speak(self):
        print("Cat says Meow!")

def describe_pet(pet):
    pet.speak()

dog = Dog()
cat = Cat()

describe_pet(dog)
describe_pet(cat)
