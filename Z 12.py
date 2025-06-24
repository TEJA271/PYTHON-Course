# Exercise 12: Calculating Student Results: Develop a class to accept a student's name and marks in three subjects, then calculate and display the total and average marks.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    def display_result(self):
        total = self.calculate_total()
        average = self.calculate_average()
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Total Marks: {total}")
        print(f"Average Marks: {average:.2f}")

name = input("Enter student's name: ")
marks = []

for i in range(3):
    mark = float(input(f"Enter mark for subject {i+1}: "))
    marks.append(mark)

student = Student(name, marks)
student.display_result()
