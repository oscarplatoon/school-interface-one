from .staff import Staff
from .student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.students = Student.all_students() 
        self.staff = Staff.all_staff()

    def display_school(self):
        print (f"Welcome to {self.name}!\nOur staff members:")
        for mem in self.staff:
            print(mem)
        print("And our students:")
        for mem in self.students:
            print(mem)