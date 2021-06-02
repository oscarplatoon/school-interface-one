import os
import csv

class Student:
    def __init__(self, name, age, password, role, school_id):
        self.name = name
        self.age = age
        self.password = password
        self.role = role
        self.school_id = school_id
    
    def __str__(self):
        return f'{self.name}\n----------\n{self.age}\n{self.school_id}'
    
    @classmethod
    def all_students(cls):
        student_list = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        with open(path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                student_list.append(Student(line['name'], line['age'], line['password'], line['role'], line['school_id']))
            return(student_list)


Student.all_students()