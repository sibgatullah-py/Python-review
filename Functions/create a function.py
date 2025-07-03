def myfun():
    print("Hello Wolrd")
myfun()
print("\n")

# Pushing data in function
def thisfun(fname):
    print(fname+" refsnes")

thisfun("Email")
thisfun("Tobias")
thisfun("Linus")
print("\n")

# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def myFunction(*kids):# Arbitrary Arguments, *args
    print("the youngest child is "+ kids[2])
    
myFunction("email",'tobias','linus')
print("\n")

