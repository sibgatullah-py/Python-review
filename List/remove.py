thislist = ['a','b','c','d','e','f','g']
thislist.remove('a')# use remove() to remove an specific item form the list
print(thislist)
# if there are more then one item int the list then remove() method removes the first item

# The pop() method removes the specific indexed item
thislist.pop(1)# c will get removed
print(thislist)# If you do not specify the index, the pop() method removes the last item.

# the del keyword can also delete the designated item in the list
del thislist[0]
print(thislist)
# the del keyword can also delete the list completely del thislist

# The clear() method removes all items from the list 
thislist.clear()
print(thislist)