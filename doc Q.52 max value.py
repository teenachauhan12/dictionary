def max(a,n):
    k=sorted(a,key=a.get,reverse=True)[:n]
    return k
b={'a':5, 'b':14, 'c': 32, 'd':35, 'e':24, 'f': 100, 'g':57, 'h':8, 'i': 100}
n= 1
print(n,"maximum value")
print(max(b,n))
n = 2
print(n,"maximum value")
print(max(b,n))
n= 5
print(n,"maximum value")
print(max(b,n))





