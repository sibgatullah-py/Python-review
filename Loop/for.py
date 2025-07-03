#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# Loopint on a list
fruits = ['banana','apple','cherry']
for i in fruits:
    print(i)
print("\n")   

# Looping on a string
fruit = "Banana"
for c in fruit:
    print(c)
print("\n")
       
# Exiting the loop
thislist = ['apple','banana','lichi','cherry']
for x in thislist:
    print(x)
    if x == "lichi":
        break    
print("\n")

# Continueing the loop
anotherlist = ['apple','banana','lichi','cherry']
for y in anotherlist:
    if y == "banana":
        continue
    print(y)
print("\n")

# Looping with the range() function
for i in range(5):
    print(i)
print("\n")

# starting and ending of a range
for g in range(1,6):# will print until 5
    print(g)
print("\n")

# Increment the sequence by 2
for j in range(1,10,2):
    print(j)
print("\n")

# Nested loop
adj = ['red','yellow','green']
fruitl = ['banana','apple','cherry']
for x in adj:
    for y in fruitl:
        print(x,y)
print("\n")