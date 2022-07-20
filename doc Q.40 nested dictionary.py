def nested_dict(l1, l2, l3):
     a=[{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return a

b=["S001", "S002", "S003", "S004"] 
c=["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
k=[85, 98, 89, 92]
print(nested_dict(b,c,k))
