import unittest
from unittest.mock import patch
from employee_manager import EmployeeManager
from employee import Employee


class TestEmployeeManager(unittest.TestCase):
    def setUp(self):
        self.manager = EmployeeManager()
        self.manager.employees = []  

    @patch('builtins.input', side_effect=['Mano', 'PY', "A1", '50000', '1500', '2000'])
    def test_add_search_delete_employee(self, mock_input):
      
        self.manager.add_employee()
        self.assertEqual(len(self.manager.employees), 1)
        emp = self.manager.employees[0]
        self.assertEqual(emp.name, 'Mano')

   
        with patch('builtins.input', return_value=str(emp.emp_id)):
            with patch('builtins.print') as mock_print:
                self.manager.search_employee()
                mock_print.assert_any_call(
                    f"Found Employee: {emp.name}, Department: {emp.department}, "
                    f"Designation: {emp.designation}, Net Salary: {emp.net_salary}"
                )

    
        with patch('builtins.input', return_value=str(emp.emp_id)):
            self.manager.delete_employee()
        self.assertEqual(len(self.manager.employees), 0)


if __name__ == '__main__':
    unittest.main()