def convert(lst):
    a=[dict([a, int(x)] for a, x in b.items()) for b in lst]
    return a

def convert(lst):
    b=[dict([a, float(x)] for a, x in b.items()) for b in lst]
    return b

# num1=[{ 'x':'10' , 'y':'20' , 'z':'30' }, { 'p':'40', 'q':'50', 'r':'60'}]
# print(convert(num1))
num2=[{ 'x':'10.12', 'y':'20.23', 'z':'30'}, { 'p':'40.00', 'q':'50.19', 'r':'60.99'}]
print(convert(num2))







