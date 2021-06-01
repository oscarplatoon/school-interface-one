"""
- run everything from runner.py
- running other classes individually may not work
"""

from classes.staff import Staff
from classes.school import School
from classes.student import Student

school = School('Ridgemont High')
student_info = {'name': 'Diana', 'password': 'password',
                'school_id': 12345, 'age': 17, 'role': 'Student'}
# using kwargs which "spreads" the dict without the need for order
diana = Student(**student_info)

print(school.staff)
print(school.students)
