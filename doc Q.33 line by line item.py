a={'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}
for i in a:
    print(i)
    for b in a[i]:
        print (b,':',a[i][b])
        