import os, csv
from classes.person import Person
class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
        super(name, age, role, password)
        self.employee_id = employee_id
        
    @classmethod
    def all_staff(cls):
        #"Somehow" get the path
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/staff.csv")
    
        with open(path) as csvfile:
            #returns an array of student objects that represent each row in the students.csv file
            reader = csv.DictReader(csvfile)
            staff_list = []
            for line in reader:
                staff_list.append(line)
            return staff_list