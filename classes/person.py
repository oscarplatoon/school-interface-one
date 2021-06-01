class Person:    
    # def __init__(self, name, age, role, password):
    #     self.name = name
    #     self.age = age
    #     self.password = password
    #     self.role = role

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.password = kwargs['password']
        self.role = kwargs['role']