from classes.person import Person

class Student(Person):

    def __init__(self, name, age, role, password, school_id):
        Person.__init__(self, name, age, role, password)
        self.school_id = school_id
