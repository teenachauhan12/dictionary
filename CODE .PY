#import random

# rooms=[401,402,403]
# a=["tanu","teena","rani","swati","teena","rani","tanu","monu","meena","pooja","manju","suman","sapna","tanuja","sona","sonu","mona","neetu","pyal"]
# n=int(input("enter the num"))
# if n<=len(a)//len(rooms):
#     i=0
#     b=[]
#     l=[]
#     while i<len(a):
#         b.append(a[i:i+n])
#         i+=n
#     my_dict={}
#     i=0
#     while i<len(rooms):
#         my_dict[rooms[i]]=b[i]
#         i+=1
#     print(my_dict)
# else:
#     print("please enter correct num.of girls i.e,<=",len(a)//len(rooms))




# a=int(input("enter the num"))
# b=[]
# for i in range(a+1):
#     b.append(i)
# print(b)
# k={}
# for i in range(len(b)):
#     if b[i]%2==0:
#         k.update({b[i]:"true"})
#     else:
#         k.update({b[i]:"false"})
# print(k)




# n=int(input("enter the num"))
# a={}
# for i in range(1,n):
#     a[i]=i*i
# print(a)




# n=int(input("enter the num"))
# i=0
# a={}
# while i<=n:
#     n1=input("enter the name:-")
#     n2=int(input("enter the marks:-"))
#     a.update({n1:n2})
#     i+=1
# print(a)



# a={1:1,2:2,3:3,4:4,5:5}
# n=int(input("enter the key"))
# if n in a:
#     a.pop(n)
#     print(a)
# else:
#     n1=int(input("enter the value"))
#     a[n]=n1
#     print(a)








# a={1:{2:30,3:40,4:50,5:60}}
# sum=0
# for i in a.values():
#     print(i)





# a=input("enter the num")
# if a=="{}":
#     print("empty")
# else:
#     print("not empty")



    


# a={"name":"teena","age":20,"city":"jaipur"}

# if a["age"]>30:
#     a.pop("age")
# print(a)  





# my={"a":34,"b":56,"c":89,"d":37,"e":100,"f":233}
# a=[]
# for i in my.values():
#     a.append(i)
# b=[]
# for i in range(3):
#     b.append(max(a))
#     a.remove(max(a))
# print(b)






# dict={"s":["tina","pooja","piya"]}
# for i in dict:
#     for j in dict[i]:
#         print(j)



# a={"s":3,"a":{"t":["tina","pooja","piya"]}}
# for item in a:
#     if type(a[item])==dict:
#         for item2 in a[item]:
#             if type(a[item][item2])==list:
#                 print(a[item][item2])






# n=int(input("enter the num of data you need in"))
# i=0
# dict={}
# while i<n:
#     name=input("enter the name")
#     dict2=[]
#     num=int(input("enter no of sub"))
#     j=0
#     while j<num:
#         sub=input("enter the sub name")
#         marks=int(input("enter the marks of sub"))
#         dict[sub]=dict2
#         i+=1
# print(dict)





# a="MISSISSIPPI"
# b={}
# for i in a:
#     if i not in b:
#         b[i]=1
#     else:
#         b[i]=b[i]+1


a={1:2,3:4,4:3,2:1,0:0}
l=[]
for i in a:
    l.append(a[i])
print(l)
for i in range(a[i]):
    for j in range(len(a)):
        if a[j]>a[j+1]:
            c=a[j]
            a[j]=a[j+1]
            a[j+1]=c
print(a)
dict={}
for i in range(len(a)):
    for j in a:
        if a[i]==a[j]:
            dict.update({j:a[i]})
print(dict)








































 


