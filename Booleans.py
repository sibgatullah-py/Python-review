a = 20 
b = 30
if a>b:
    print("a is greater then b")
else:
    print(" b is greater then a")
    
# The bool() function allows you to evaluate any value, and give you true or false
# if the variable is empty then it's false or it's true
x=None # None keyword indicates the variable is empty
y=20
z = 0 # also any number is true except 0
print(bool(x))
print(bool(y))
print(bool(z))

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False: 
class thisclass():
    def __len__(self):
        return 0
    
thisObject = thisclass()
print(bool(thisObject))

# Functions can return boolean 
def thisfun():
    return True

if thisfun():
    print("YES!")
else:
    print("NO!")


# Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x,int))