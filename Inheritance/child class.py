class Parent:
    def __init__(self,fsname,lsname):
        self.firstname = fsname 
        self.lastname = lsname
        
    def printname(self):# Method
        print(self.firstname,self.lastname)
        

class Child(Parent):
    def __init__(self, fsname, lsname,year):
        Parent.__init__(self,fsname,lsname) # This line prevents the child class __init__ to overlap with the parent class
        super().__init__(fsname, lsname)# This line does the same as super() function indicates the parent class
        self.year = year
        
    def welcome(self):
        print(f"Welcome {self.firstname} {self.lastname} to the class of {self.year}")


x = Child("Jhon","Doe",2020)
x.welcome()
