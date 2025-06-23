# Exercise 4: Design a class SeriesCalculator that calculates the sum of an arithmetic series.

class SeriesCalculator:
    def __init__(self, first_term, common_difference, number_of_terms):
        self.first_term = first_term
        self.common_difference = common_difference
        self.number_of_terms = number_of_terms

    def calculate_sum(self):
        n = self.number_of_terms
        a = self.first_term
        d = self.common_difference
        return n * (2 * a + (n - 1) * d) / 2

calculator = SeriesCalculator(1, 2, 5)
print(calculator.calculate_sum())
