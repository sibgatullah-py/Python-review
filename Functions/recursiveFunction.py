def myfun(x):
    if(x > 0):
        result = x + myfun(x-1)
        print(result)
    else:
        result = 0
    return result
myfun(6)
        