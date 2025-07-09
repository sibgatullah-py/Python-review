class Person: 
 def __init__(self,name,age):
   self.name = name
   self.age= age

 def greet(self):
   return f"hello {self.name}"

class Employee(Person):
  
  def __init__(self, name, age,job):
      super().__init__(name, age)
      self.job = job
  
  def greet(self) :
    return super().greet() + f" i am a {self.job}"
  
employee = Employee('jhon',25,'python developer')
print(employee.greet())