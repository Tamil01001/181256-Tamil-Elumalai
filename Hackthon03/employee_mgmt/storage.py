import pickle

class Storage:
    def load_data(self):
        try:
            with open('employees.pkl', 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []

    def save_data(self, employees):
        with open('employees.pkl', 'wb') as file:
            pickle.dump(employees, file)