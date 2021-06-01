# student.py
import csv
import os

# from classes.person import Person

with open('../data/students.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
    for row in csv_reader:
        print(row)
        # print(', '.join(row))


# my_path = os.path.abspath(os.path.dirname(__file__))
# path = os.path.join(my_path, "../data/students.csv")


class Student:
    def __init__(self, name, age, role, school_id, password):
        self.name = name 
        self.age = age         
        self.role = role
        self.school_id = school_id
        self.password = password

Student.all_students()


# student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
# print(Student(**csv_reader))

# print(isinstance(x, PhysicianRobot))
# print(isinstance(y, PhysicianRobot))

# with open('students.csv', newline='') as csvfile:
#     studentreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in studentreader:
#         print(', '.join(row))


# print(isinstance(Student, Person))
# print(type(Student) == Person, type() == PhysicianRobot)