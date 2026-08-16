class User:
    def __init__(self,name,email,password,phone,dob,address):
        self.name = name
        self.__email = email
        self.__password = password
        self.__phone = phone
        self.__dob = dob
        self.__address = address
        
        
        def to_dict(self):
            # Parent returns a dictionary of its own properties
            return {
                "name": self.name,
                "email": self.__email,
                "password": self.__password,
                "phone": self.__phone,
                "dob": self.__dob,
                "address": self.__address,
            }
        
        
class Students(User):
    def __init__(self,student_id, name, email,password, phone, dob, address,major,semester):
        self.student_id = student_id
        super().__init__(name, email,password, phone, dob, address)
        self.major = major
        self.semester = semester
        
    def to_dict(self):
        # Start with parent dictionary fields
        data = super().to_dict()
        # Add or override child specific fields
        data.update({
            "id": self.student_id,
            "major": self.major,
            "semester": self.semester
        })
        return data
        
        
class Teachers(User):
    def __init__(self,employee_id, name, email,password, phone,dob,address,department,salary):
        self.employee_id = employee_id
        super().__init__(name, email,password, phone,dob,address)
        self.department = department
        self.__salary = salary 
        
    def to_dict(self):
        data = super().to_dict()
        data.update({
            "id": self.employee_id,
            "department": self.department,
            "salary": self.__salary
        })
        return data
        