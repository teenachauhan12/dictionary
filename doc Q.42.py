def value_check(students, n):
    a=all(x == n for x in students.values()) 
    return a
  
b={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
print(b)
n = 12
print("Check all are ",n,"in the dict")
print(value_check(b,n))
n = 10
print("Check all are ",n,"in the dict")
print(value_check(b,n))









