from employee_data import Person, Employee, Department, save_to_json, load_from_json

### employee data ###
data_strings = [
    "John,35,Male,E101,HR,45000",
    "Jane,28,Female,E102,IT,55000",
    "Bob,40,Male,E103,HR,60000",
    "Alice,30,Female,E104,Finance,48000",
    "Charlie,45,Male,E105,IT,47000"
]

### Creating Person objects (name, age, and gender) ###
people = []
for data_string in data_strings:
    name, age, gender, *_ = data_string.split(',')  # Ignore employee-specific info
    person = Person(name, int(age), gender)  # Use Person class for basic info
    people.append(person)

### Print details of Person objects ###
print("=== Person Details ===")
for person in people:
    print(person.get_details())

### Creating Employee objects (including emp_id, department, salary) ###
employees = []
for data_string in data_strings:
    name, age, gender, emp_id, department, salary = data_string.split(',')
    employee = Employee(name, int(age), gender, emp_id, department, float(salary))  # Use Employee class
    employees.append(employee)

### Print Employee data and bonus eligibility ###
print("\n=== Employee Details ===")
for emp in employees:
    print(emp.get_details())
    print(f"Eligible for Bonus: {emp.is_eligible_for_bonus()}")

### Save to JSON ###
save_to_json(employees)
print("\nEmployees saved to JSON.")

### Load from .JSON ###
employees = load_from_json()
print("\nEmployees loaded from JSON:")

### sorted data by departments ###
hr_dept = Department("HR")
it_dept = Department("IT")
finance_dept = Department("Finance")

for emp in employees:
    if emp.department == "HR":
        hr_dept.add_employee(emp)
    elif emp.department == "IT":
        it_dept.add_employee(emp)
    elif emp.department == "Finance":
        finance_dept.add_employee(emp)
        
print("\n=== HR Department Employees ===")
for emp in hr_dept.get_all_employees():
    print(emp.get_details())

print("\n=== IT Department Employees ===")
for emp in it_dept.get_all_employees():
    print(emp.get_details())

print("\n=== Finance Department Employees ===")
for emp in finance_dept.get_all_employees():
    print(emp.get_details())
