import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def test_net_salary(self):
        emp = Employee(5, "Prathap", "PY", "A1", 50000, 1500,4000)
        self.assertEqual(emp.net_salary, 52500)

if __name__ == '__main__':
    unittest.main()