from classes.student import Student
from classes.staff import Staff

class School:
    def __init__(self, name):
        self.name = name
        self.students = Student.all_students()
        self.staff = Staff.all_staff()
    
    def list_students(self):
        for k in self.students:
            print(f"1. {k.name} {k.school_id}")

    def find_student_by_id(self, id):
        for k in self.students:
            if k.school_id == id:
                return k