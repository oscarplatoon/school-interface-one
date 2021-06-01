
import os
import csv

from classes.person import Person

class Student(Person):    
    def __init__(self, **kwargs):
        self.school_id = kwargs['school_id']
        Person.__init__(**kwargs)
        

    def all_students():

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        student_array = []

        with open(path) as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                student_array.append(row)
            print(student_array)
        return student_array
    
    
