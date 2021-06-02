#staff.py
class Staff:
    @classmethod
    def all_staff(cls):
        
        staff_array = []
    
        with open(path) as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for line in dict_reader:
                staff_array.append(Staff(**line))
    
            return staff_array
    
    def __init__(self, **kwargs):
        self.name = kwargs['name'] 
        self.age = kwargs['age']        
        self.password = kwargs['password']
        self.role = kwargs['role']
        self.employee_id = kwargs['employee_id']
