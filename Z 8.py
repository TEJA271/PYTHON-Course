# Exercise 8: Student Grade Calculator: Implement a Student class with attributes for name and a list of marks. Include a method to calculate the average and determine the grade.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

student = Student("Alice", [85, 92, 78])
print(student.name)
print("Average:", student.average())
print("Grade:", student.grade())
