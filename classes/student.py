from classes.person import Person
import csv
import os 
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "..data/students.csv")

class Student(Person):
  def __init__(self, name, age, role, school_id, password):
    super().__init__(name, age, role, password)
    self.school_id = school_id

  @classmethod
  def all_students(cls):
    with open(path) as student_file:
      student_reader = csv.DictReader(student_file)
      student_arr = []
      for row in student_reader:
        # print(row)
        student = Student(row['name'], row['age'], row['role'], row['school_id'], row['password'])
        # print(student.name)
        student_arr.append(student)
      return student_arr

