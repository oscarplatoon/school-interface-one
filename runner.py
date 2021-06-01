# from school import School 
from Student import Student

# school = School('Ridgemont High') 
student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
Student(**student_info)

# print(school.name)
print(student.info)