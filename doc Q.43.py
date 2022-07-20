def colors_dict(l):
    a={}
    for k, v in l:
         a.setdefault(k,[]).append(v)
    return a
b=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print(colors_dict(b))





