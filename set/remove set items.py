thisset = {"apple", "banana", "cherry","orange",'mango'}

thisset.remove("banana")

print(thisset) 

thisset.discard("cherry")# works same as remove() method , the set sequence will start after from the discarded item
print(thisset) 

thisset.pop()# remove the last item
print(thisset)

thisset.clear()#clearing all the items of the set
print(thisset)

del thisset# deleting the set