import os
import csv
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/staff.csv")

class Staff:  

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.password = kwargs['password']
        self.role = kwargs['role']
        self.employee_id = kwargs['employee_id']

    @classmethod
    def all_staff(cls):

        staff_array = []

        with open(path) as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                staff_array.append(Staff(**row))

            return staff_array

    def __str__(self):
        return f"My name is {self.name} and my age is {self.age}. I work as a {self.role} and my ID is {self.employee_id}."

 