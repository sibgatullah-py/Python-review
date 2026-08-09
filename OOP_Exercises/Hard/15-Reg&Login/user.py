class User:
    def __init__(self,name,email,password,phone,dob,address):
        self.name = name
        self.__email = email
        self.__password = password
        self.__phone = phone
        self.__dob = dob
        self.__address = address
        
        
class Students(User):
    def __init__(self,student_id, name, email,password, phone, dob, address,major,semester):
        self.student_id = student_id
        super().__init__(name, email,password, phone, dob, address)
        self.major = major
        self.semester = semester
        
        
class Teachers(User):
    def __init__(self,employee_id, name, email,password, phone,dob,address,department,salary):
        self.employee_id = employee_id
        super().__init__(name, email,password, phone,dob,address)
        self.department = department
        self.__salary = salary 
        