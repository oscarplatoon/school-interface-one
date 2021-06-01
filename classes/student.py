from person import Person
import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/students.csv")
class Student(Person):

    @classmethod
    def all_students(cls):
        output_list = []
        with open(path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                output_list.append(row)


    def __init__(self, name, age, role, password, school_id):
        Person.__init__(self, name, age, role, password)
        self.school_id = school_id

# test_list = Student.all_students()
# print(test_list)