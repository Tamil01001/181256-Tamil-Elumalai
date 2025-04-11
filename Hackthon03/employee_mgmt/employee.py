class Employee:
    def __init__(self, emp_id, name, department, designation, gross_salary, tax, bonus):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.designation = designation
        self.gross_salary = gross_salary
        self.tax = tax
        self.bonus = bonus
        self.net_salary = self.calculate_net_salary()

    def calculate_net_salary(self):
        return self.gross_salary - self.tax + self.bonus