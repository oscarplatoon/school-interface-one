import os
import csv

class Staff:
    def __init__(self, name, age, password, role, employee_id):
        self.name = name
        self.age = age
        self.password = password
        self.role = role
        self.employee_id = employee_id
    
    @classmethod
    def all_staff(cls):
        staff_list = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/staff.csv")
        with open(path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                staff_list.append(Staff(line['name'], line['age'], line['password'], line['role'], line['employee_id']))
            return staff_list
