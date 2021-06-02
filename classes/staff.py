from classes.person import Person
import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "..data/students.csv")

class Staff(Person):
  def __init__(self, name, age, role, employee_id, password):
    Person.__init__(name, age, role, password)
    self.employee_id = employee_id

  @classmethod
  def all_staff(cls):
    with open(path) as staff_file:
      staff_reader = csv.DictReader(staff_file)
      staff_arr = []
      for row in staff_reader:
        # print(row)
        staff = Staff(row['name'], row['age'], row['role'], row['employee_id'], row['password'])
        # print(student.name)
        staff_arr.append(staff)
      return staff_arr