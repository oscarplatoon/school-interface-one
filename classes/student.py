from classes.person import Person
import csv
import os

class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, role, password)
        self.school_id = school_id

    @classmethod
    def all_students(cls):
        students = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        with open(path) as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                students.append(Student(**dict(row)))
        return students
    
    def __str__(self):
        return f"""{self.name.upper()} \n--------------\nage: {self.age}\nid: {self.school_id}
        """
