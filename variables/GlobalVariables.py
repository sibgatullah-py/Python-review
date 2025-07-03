x = "Python "
def myfun():
    global y # Though variables in functions are local but using the global keyword makes the variables global
    y = "is Fantastic"
    
myfun()

print(x+y)