import os
import csv

from classes.students import Student
from classes.staff import Staff
class School:
    def __init__(self, name):
        self.name = name
        self.students = Student.all_students()
        self.staff = Staff.all_staff()

    def list_students(self):
        count = 0
        for student in self.students:
            count += 1
            print(f'{count}. {student.name} {student.school_id}')
    
    def find_student_by_id(self, id):
        for student in self.students:
            if student.school_id == id:
                return student