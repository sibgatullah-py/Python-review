a = 50
b = 60
if a>b:
    print("a is greater then b")
elif b==a:
    print("a is equal to b")
else:
    print("b is greater then a")
    
    
x = 10
y = 20
print('A') if a>b else print('B')


# Nested if else
j = 40
if j>10:
    print("Above 10")
    if j>20:
        print("Also above 20")
    else:
        print("Not above 20")
else:
    print("Not above 10")