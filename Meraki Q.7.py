
# dic1={1:10, 2:20}
# dic2={3:30, 2:40}
# dic3={5:50, 6:60}
# d={}
# for i in dic2:
#     if i  in dic1:
#         dic1[i]+=dic2[i]
#         dic1.update(dic3)
#     else:
#         dic1[i]=dic2[i]
# print(dic1)
#     d.update(i)
# for i in d:
#     if i in dic1:
#         if i in dic2:
#             d.update({i:(dic1,[i]+dic2[i])})
#         print(d)






a=[1,2,[3,4,[5,6],2,3]]
d=[]
i=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if type(a[i][j])==list:
                k=0
                while k<len(a[i][j]):
                    d.append(a[i][j][k])
                    k+=1
            else:
                d.append(a[i][j])
            j+=1
    else:
        d.append(a[i])
        i+=1
print(d)





