# student.py
import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/students.csv")

class Student:
   
    @classmethod
    def all_students(cls):
        
        student_array = []
    
        with open(path) as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for line in dict_reader:
                student_array.append(Student(**line))
    
            return student_array
       
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']         
        self.password = kwargs['password']
        self.role = kwargs['role']
        self.school_id = kwargs['school_id']

    def __str__(self):
        return f"My name is {self.name} and my age is {self.age}. I am a {self.role} and my ID is {self.school_id}."

    

# students = Student.all_students()
# for x in students:
#     print(x)