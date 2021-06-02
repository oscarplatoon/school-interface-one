import os
import csv
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/students.csv")


class Student:   

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.password = kwargs['password']
        self.role = kwargs['role']
        self.school_id = kwargs['school_id']

        
    @classmethod
    def all_students(cls):

        student_array = []

        with open(path) as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                student_array.append(Student(**row))

        return student_array

    def __str__(self):
        return f"My name is {self.name} and my age is {self.age}. I am a {self.role} and my ID is {self.school_id}."

