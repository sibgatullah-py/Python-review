thisdict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year'  : 1964,
}
x = thisdict['model']
y = thisdict.get('year')# get() function also access values of a key

print(x)
print(y)

# The keys() method will return a list of keys in the dictionary 
z = thisdict.keys()
print(z)

# Changing the keys and values
thisdict['color'] = 'red'
a = thisdict
print(a)

# items() method will return each item in a dictionary, as a tuple in a list 
print(thisdict.items())

# The values() method will return a list of values in the dictionary
v = thisdict.values()
print(v)

# Checking if key is present in dictionary
if 'model' in thisdict:
    print("Present")