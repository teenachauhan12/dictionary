def len(a):
    k={}
    for val in a.values(): 
        k[val] = len(val) 
    return k   

b={1 : 'red', 2 : 'green', 3 : 'black', 4 : 'white', 5 : 'black'}
print(b)
print(len(b))
