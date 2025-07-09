class Person:
 def __init__(self,name,age):
  self.name = name
  self.age = age
p1 = Person('jhon',22)
p2 = Person('jene',22)

print(hash(p1))
print(hash(p2))