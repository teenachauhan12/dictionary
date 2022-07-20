a= ['red', 'green', 'blue']
b= ['#FF0000','#008000', '#0000FF']
i=0
v={}
while i<len(a):
    v.update({a[i]:b[i]})
    i=i+1
print(v)



