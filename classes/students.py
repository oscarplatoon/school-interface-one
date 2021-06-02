import os
import csv

class Student:
    def __init__(self, **student_info):
        self.name = name
        self.age = age
        self.password = password
        self.role = role
        self.school_id = school_id
    
    @classmethod
    def all_students(cls):
        student_list = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        with open(path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                student_list.append(line)
            return student_list


Student.all_students()