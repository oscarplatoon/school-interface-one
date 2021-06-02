from .person import Person
import csv
import os


class Student(Person):

    def __init__(self, name, age, role, password, school_id):
        super().__init__(name, age, role, password)
        self.school_id = school_id

    @classmethod
    def all_students(cls):
        students = []

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        with open(path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                students.append(Student(**row))
        return students
