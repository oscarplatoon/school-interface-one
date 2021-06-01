#staff.py
# from classes.person import Person
import csv
import os

with open('../data/staff.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
    for row in csv_reader:
        print(row)
        # print(', '.join(row))

class Staff:
    def __init__(self, name, age, role, employee_id, password):
        self.name = name 
        self.age = age         
        self.role = role
        self.employee_id = employee_id
        self.password = password

Staff.all_staff()


# staff_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
# Staff(**staff_info)
