from .person import Person
import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/staff.csv")

class Staff(Person):

    @classmethod
    def all_staff(cls):
        output_list = []
        with open(path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                output_list.append(Staff(**row))
            return output_list


    def __init__(self, name, age, role, password, employee_id):
        Person.__init__(self, name, age, role, password)
        self.employee_id = employee_id