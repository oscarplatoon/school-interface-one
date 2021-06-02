from classes.person import Person
import os.path
import csv

class Student(Person):

    def __init__(self,name,age,role,school_id,password):
        super().__init__(name, age, role, password)
        self.school_id = school_id

    
    @classmethod
    def all_students(cls):
        students =[]
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path,"../data/students.csv")
        with open(path) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                students.append(Student(**dict(row)))
        return students

