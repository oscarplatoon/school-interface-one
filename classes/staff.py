from .person import Person
import csv
import os.path

class Staff(Person):

    def __init__(self, name, age, role, password, employee_id):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id

    @classmethod
    def all_staff(cls):
        staff = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/staff.csv")

        with open(path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                staff.append(Staff(**row))
            return staff