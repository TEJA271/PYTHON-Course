# Exercise 11: Object Count Tracker: Design a class that tracks how many objects have been created from it and has a method to display this count.

class ObjectCounter:
    count = 0

    def __init__(self):
        ObjectCounter.count += 1

    def display_count(self):
        print("Number of objects created:", ObjectCounter.count)

obj1 = ObjectCounter()
obj2 = ObjectCounter()
obj3 = ObjectCounter()

obj3.display_count()
