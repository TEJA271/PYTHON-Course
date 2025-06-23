# Exercise 10: Last Digit in Words: Write a class with a method that takes an integer and prints the last digit of that number in words.

class LastDigitInWords:
    def __init__(self):
        self.digit_words = {
            0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
            5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
        }

    def print_last_digit_word(self, number):
        last_digit = abs(number) % 10
        print(self.digit_words[last_digit])

obj = LastDigitInWords()
obj.print_last_digit_word(123)    # three
obj.print_last_digit_word(-4567)  # seven
