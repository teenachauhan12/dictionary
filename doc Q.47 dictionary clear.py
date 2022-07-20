def dict(a):
    for key in a:
        a[key].clear()
    return a
b={ 
    'C1' : [10,20,30], 
    'C2' : [20,30,40],
    'C3' : [12,34]
}
print(dict(b))





