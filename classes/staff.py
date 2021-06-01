from classes.person import Person

class Staff(Person):    
    def __init__(self, **kwargs):
        self.employee_id = kwargs['employee_id']
        Person.__init__(**kwargs)



 