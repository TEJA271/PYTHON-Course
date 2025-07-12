from abc import ABC , abstractmethod

class Abcclass (ABC):
    def print(self , x):
        print(" passed value  ;", x)

    def task(self):
        print("we are inside Absclass task ")

class test_class (Abcclass) :
    def task(self):
        print(" we are in test_class task")

test_obj = test_class()
test_obj.task()
test_obj.print(100)