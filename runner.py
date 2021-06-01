from classes.school import School
from classes.person import Person
from classes.staff import Staff
from classes.student import Student

school = School('Ridgemont High')

#This output can be programmatically genereted with dict_reader/.csv files
student_info = {'name': 'Diana', 'password': 'password',
                'school_id': 12345, 'age': 17, 'role': 'Student'}
student = Student(**student_info)

print(student.school_id)
#print(staff_member.employee_id)
print(school.name)
