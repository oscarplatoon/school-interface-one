import os, csv
from classes.person import Person
class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        super(name, age, role, password)
        self.school_id = school_id
        
    @classmethod
    def all_students(cls):
        #"Somehow" get the path
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
    
        with open(path) as csvfile:
            #returns an array of student objects that represent each row in the students.csv file
            reader = csv.DictReader(csvfile)
            student_list = []
            for line in reader:
                student_list.append(line)
            return student_list