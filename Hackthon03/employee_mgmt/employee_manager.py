import pickle
from employee import Employee
from storage import Storage

class EmployeeManager:
    def __init__(self):
        self.storage = Storage()
        self.employees = self.storage.load_data()

### Add new employee data ###
    def add_employee(self):
        name = input("Enter employee name: ")
        department = input("Enter department: ")
        designation = input("Enter designation: ")
        gross_salary = float(input("Enter gross salary: "))
        tax = float(input("Enter tax: "))
        bonus = float(input("Enter bonus: "))
        emp_id = max([e.emp_id for e in self.employees], default=0) + 1
        employee = Employee(emp_id, name, department, designation, gross_salary, tax, bonus)
        self.employees.append(employee)
        print(f"Employee {name} added successfully!")

### Viewing employee details ###
    def view_employees(self):
        for emp in self.employees:
            print(f"ID: {emp.emp_id}, Name: {emp.name}, Department: {emp.department}, "
                  f"Designation: {emp.designation}, Net Salary: {emp.net_salary}")


### Searching employee details with ID ###
    def search_employee(self):
        emp_id = int(input("Enter employee ID to search: "))
        for emp in self.employees:
            if emp.emp_id == emp_id:
                print(f"Found Employee: {emp.name}, Department: {emp.department}, "
                      f"Designation: {emp.designation}, Net Salary: {emp.net_salary}")
                return
        print("Employee not found.")

### Removing emoloyee data ###
    def delete_employee(self):
        emp_id = int(input("Enter employee ID to delete: "))
        self.employees = [emp for emp in self.employees if emp.emp_id != emp_id]
        print(f"Employee with ID {emp_id} deleted successfully!")

### Save the data ###
    def save_data(self):
        self.storage.save_data(self.employees)
        print("Employee data saved successfully.")