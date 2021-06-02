# runner.py 
from classes.school import School
import csv
import os

with open('data/students.csv', mode='a') as csv_file:
    paramNames = ['name', 'age','role','school_id','password']
    student_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)



school = School('Ridgemont High') 

print(school.staff) 

print(school.students)
