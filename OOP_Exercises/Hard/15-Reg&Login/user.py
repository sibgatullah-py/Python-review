class User:
    def __init__(self,name,email,phone,dob,address):
        self.name = name
        self.email = email
        self.phone = phone
        self.dob = dob
        self.address = address
        
        
class Students(User):
    def __init__(self,student_id, name, email, phone, dob, address,major,semester):
        self.student_id = student_id
        super().__init__(name, email, phone, dob, address)
        self.major = major
        self.semester = semester
        
        
class Teachers(User):
    def __init__(self,employee_id, name, email, phone,dob,address,department,salary):
        self.employee_id = employee_id
        super().__init__(name, email, phone,dob,address)
        self.department = department
        self.salary = salary 
        