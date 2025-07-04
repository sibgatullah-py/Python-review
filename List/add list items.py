thislist = ['a','b','c','d','e','f','g']
thislist.append('h')# To add an item on the last of the list use append() method
print(thislist)

# INSERT 
thislist2 = ['a','b','c','d','e','f','g']
thislist2.insert(2,'apple')# to insert an item to designated index use insert() method
print(thislist2)

# EXTEND
# To append elements form another list use extend()
thislist3 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist3.extend(tropical)
print(thislist3)
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries)
anotherlist = ["apple", "banana", "cherry"]
thistuple = ('lichi','cherry')
anotherlist.extend(thistuple)
print(anotherlist)