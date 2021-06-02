import csv
import os.path
from classes.person import Person

class Staff(Person):

    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id

    def __str__(self):
        print(f'{self.role}: {self.name}')

    @classmethod
    def objects(cls):
        staff = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/staff.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                staff.append(Staff(**dict(row)))

        return staff