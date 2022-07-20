from itertools import product
def dict(a):
    k=[dict(zip(a, sub)) for sub in product(*a.values())]
    return k

b={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
#print(b)
#print("A key-value list pairings of the said dictionary")
print(dict(b))


