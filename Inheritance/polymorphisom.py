#The word "polymorphism" means "many forms", 
#and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
        
    def move(self): # Method of same name is polymorphisom
        print(f'{self.brand} in {self.year}')
        print("Drive!")
        
class Boat:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    
    def move(self): # Method of same name is polymorphisom
        print(f'{self.brand} in {self.year}')
        print("Sail")
        
class Plane:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    
    def move(self): # Method of same name is polymorphisom
        print(f'{self.brand} in {self.year}')
        print("Fly!")
        
car1 = Car("Ford",1998)
boat1 = Boat("Ibiza",2019)
plane1 = Plane("Boeing",747)

for x in (car1,boat1,plane1):
    x.move()