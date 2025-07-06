class myclass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self): # The function controls what should be returned when the class object is represented as a string
        return f'{self.name}{self.age}'# gives user friendly string output
    
    def __repr__(self):# gives developer friendly string output
        return f'{self.name}{self.age}'
    
    
obj = myclass('Jhone',36)

print(obj)
