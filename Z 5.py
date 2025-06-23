# Exercise 5: Create a class MaxFinder that identifies the largest number in a list.

class MaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_max(self):
        if not self.numbers:
            return None
        max_num = self.numbers[0]
        for num in self.numbers:
            if num > max_num:
                max_num = num
        return max_num

finder = MaxFinder([3, 5, 1, 9, 2])
print(finder.find_max())
