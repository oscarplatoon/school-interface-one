from classes.person import Person
import os


class Student(Person):
    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password, role)
        self.school_id = school_id

    @staticmethod
    def all_students():
        # absolute path goes back to home directory. also normalizes the path
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")

        with open(path) as csvfile:
            lines = csvfile.readlines()
            return lines
