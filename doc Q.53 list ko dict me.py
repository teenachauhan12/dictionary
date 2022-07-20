def dict(list):
    a={item[0]: item[1:] for item in list}
    return a

b=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
print(dict(b))