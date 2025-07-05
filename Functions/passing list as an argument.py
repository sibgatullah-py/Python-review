def myfun(food):
    for x in food:
        print(x)
        
fruits = ['apple','orange','banana','cherry']
myfun(fruits)

# To let a function return a value use return statement 
def thisfun(x,y):
    return x * y

x = int(input())
y = int(input())
print(thisfun(x,y))

#if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.
def empty():
    pass