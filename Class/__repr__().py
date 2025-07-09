class myclass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __repr__(self):# gives a string representation of an object 
        return f'{self.name}{self.age}'
    
    
obj = myclass('Jhone',36)

print(repr(obj))