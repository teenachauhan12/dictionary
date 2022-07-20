def even(a):
    a={key: [idx for idx in val if not idx % 2]  
          for key, val in a.items()}   
    return a
b2={'V' : [1, 3, 5], 'VI' : [1, 5], 'VII' : [2, 7, 9]} 
print("even num")
print(even(b2))