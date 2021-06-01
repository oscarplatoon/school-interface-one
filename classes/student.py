from classes.person import Person
import csv
import os.path

class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, role, password)
        self.school_id = school_id

    @classmethod
    def all_students():
        students = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        with open(path) as csvfile:
            csv_reader = csv.Dictreader(csvfile)
            for row in csv_reader:
                students.append(Student(**dict(row)))
                return students


# student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}

# s = Student(**student_info)
# #s.print_student
# s.all_students()
