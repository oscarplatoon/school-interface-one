from classes.person import Person

class Staff(Person):

    def __init__(self, name, age, role, password, employee_id):
        Person.__init__(self, name, age, role, password)
        self.employee_id = employee_id
