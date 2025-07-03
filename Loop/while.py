i = 1
while i < 10:
    print(i)
    if i == 5:
        break
    i+=1

j = 0   
while j < 8:
    j+=1
    if j == 4:
        continue
    
    print(j) # if the print was given before continue then the j will become 4 and j == 4 will be true so loop will keep printing 4 
    
    
k = 1 
while k < 6:
    print(k)
    k += 1
else:
    print("k is no longet less then 6")