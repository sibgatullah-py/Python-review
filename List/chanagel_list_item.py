thislist = ['a','b','c','d','e','f','g']
thislist[5] = 1
print(thislist)

# changing a serise of elements
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#if you insert more items then the list capacity , the new items will be added in the last
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) 