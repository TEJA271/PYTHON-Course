class Employee:
    def __init__(self, name, id, department="General"):
        self.name = name
        self.id = id
        self.department = department

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, id, department=None):
        if department is None:
            employee = Employee(name, id)
        else:
            employee = Employee(name, id, department)
        self.employees.append(employee)

    def display_employees(self):
        for emp in self.employees:
            print(emp.name, emp.id, emp.department)

manager = EmployeeManager()
manager.add_employee("Alice", 101)
manager.add_employee("Bob", 102, "HR")
manager.add_employee("Charlie", 103, "Finance")
manager.display_employees()
