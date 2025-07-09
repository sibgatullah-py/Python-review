class Person:
 counter = 0 # to keep track of the class instances
 def __init__(self,name,age):
  self.name= name 
  self.age = age
  counter +=1

  def greet(self):
   return f"hello {self.name}"

  @classmethod
  def create_anonymous(cls):
   return Person('Anonymous',22)
  
anonymous = Person.create_anonymous()
print(anonymous.name)