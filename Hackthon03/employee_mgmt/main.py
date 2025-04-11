from employee_manager import EmployeeManager

def main():
    manager = EmployeeManager()
    while True:
        print("\nWelcome to Employee Management CLI")
        print("1. Add Employee data")
        print("2. View All Employees details")
        print("3. Search Employee detail with ID")
        print("4. Delete Employee")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            manager.add_employee()
        elif choice == '2':
            manager.view_employees()
        elif choice == '3':
            manager.search_employee()
        elif choice == '4':
            manager.delete_employee()
        elif choice == '5':
            manager.save_data()
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()