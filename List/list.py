# List are used to store multiple items in a sigle variable
# From python's prospective, list are defined as objects with the data type list
mylist = ["apple","banana","cherry"]
print(mylist)
print(type(mylist))

# ORDERED
# When we say that the list is ordered, it means that the items have a defined order, and that order will not change
# If we add new items in the list, the new item will be placed at the end of the list

# CHANGABLE
# The list is changable, that means that we can change, add, remove items in a list after it has been created 

# ALLOW DUPLICATES
# Since list are indexed, list can have items with the same value duplicates
thislist = ["apple","banana","cherry","apple","cherry"]
print(thislist)
print(len(thislist))# the length of the list

# A list can contain different data types
list1 = ['abc',1,True,40.5,'male']
print(list1)

#the list constructor acts like a type caster for tuple and set converting them to list
listcast = list(('apple','banana','lichi'))