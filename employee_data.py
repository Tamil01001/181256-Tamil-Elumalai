import json

### Person ###
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

### Employee ###
class Employee(Person):
    def __init__(self, name, age, gender, emp_id, department, salary):
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.department = department
        self.salary = salary
    
    def get_details(self):
        return f"{super().get_details()}, Employee ID: {self.emp_id}, Department: {self.department}, Salary: ₹{self.salary:.2f}"

    def is_eligible_for_bonus(self):
        return self.salary < 50000


    @classmethod
    def from_string(cls, data_string):
        name, age, gender, emp_id, department, salary = data_string.split(',')
        return cls(name, int(age), gender, emp_id, department, float(salary))

### Department ###
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
    
    def get_all_employees(self):
        return self.employees

### Save employee data in .JSON file ###
def save_to_json(employees, filename='MicroProject02\employees.json'):
    with open(filename, 'w') as f:
        json.dump([emp.__dict__ for emp in employees], f, indent=4)

### Load employee data from .JSON file ###
def load_from_json(filename='MicroProject02\employees.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
        return [Employee(**emp_data) for emp_data in data]
