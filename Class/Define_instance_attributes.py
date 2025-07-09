class Person:
   counter = 0
   def __init__(self, name , age):
      self.name = name 
      self.age = age
      Person.counter+=1

   def greet(self):
      return f"Hi, it's {self.name}."

person = Person('jhon',25)
p2 = Person('doe',19)

print(person.greet())
print(person.counter)