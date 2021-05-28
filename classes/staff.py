from classes.person import Person
import os


class Staff(Person):
    def __init__(self, name, age, password, role, employee_id):
        super().__init__(name, age, password, role)
        self.employee_id = employee_id

    @staticmethod
    def all_staff():
        # absolute path goes back to home directory. also normalizes the path
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/staff.csv")

        with open(path) as csvfile:
            lines = csvfile.readlines()
            return lines
