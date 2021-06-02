# student.py
import csv
import os
# with open('../data/students.csv') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for row in csv_reader:
#         print(row)


# my_path = os.path.abspath(os.path.dirname(__file__))
# path = os.path.join(my_path, "../data/students.csv")


class Student:
    @classmethod
    def all_students(cls):
        all_students_list = []
        with open('data/students.csv', 'r') as csv_file:
            student_reader = csv.Dictreader(csv_file)
            for row in student_reader:
                all_students_list.append(row)
            return all_students_list


    def __init__(self, name, age, role, school_id, password):
        self.name = name 
        self.age = age         
        self.role = role
        self.school_id = school_id
        self.password = password
        self.all_students = Student.all_students() 


student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
print(Student(**student_info))

Student.all_students()




# with open('students.csv', newline='') as csvfile:
#     studentreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in studentreader:
#         print(', '.join(row))


# print(isinstance(Student, Person))
# print(type(Student) == Person, type() == PhysicianRobot)