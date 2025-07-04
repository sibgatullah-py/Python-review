thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)

thislist2 = ["banana", "Orange", "Kiwi", "cherry"]
thislist2.sort(key= str.lower)
print(thislist2)