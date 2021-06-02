from classes.person import Person
import os.path
import csv

class Staff(Person):

    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name,age,role,password)
        self.employee_id = employee_id

    @classmethod
    def all_staff(cls):
        staff =[]
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path,"../data/staff.csv")
        with open(path) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                staff.append(Staff(**dict(row)))
        return staff


