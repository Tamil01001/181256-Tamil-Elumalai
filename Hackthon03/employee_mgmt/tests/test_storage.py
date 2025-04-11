import unittest
import os
from storage import Storage
from employee import Employee

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.storage = Storage()
        self.test_file = 'employees.pkl'
    
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
    
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_load(self):
      
        employee = Employee(4, "Mano", "PY", "A1", 50000, 1500, 2000)
        employees = [employee]

        self.storage.save_data(employees)

        loaded = self.storage.load_data()

        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].name, "Mano")
        self.assertEqual(loaded[0].net_salary, 50500)

if __name__ == '__main__':
    unittest.main()
