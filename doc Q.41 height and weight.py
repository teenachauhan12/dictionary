def filter_data(students):
    result = dict(filter(lambda x: (x[1][0], x[1][1]) > (6.0, 70), students.items()))
    return result  
students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
print("Original Dictionary:")
print(students)
print("\nHeight> 6ft and Weight> 70kg:")
print(filter_data(students))




# def value_check(students, n):
#     a=all(x == n for x in students.values()) 
#     return a
  
# b={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# print("Original Dictionary")
# print(b)
# n = 12
# print("\nCheck all are ",n,"in the dictionary")
# print(value_check(b,n))
# n = 10
# print("\nCheck all are ",n,"in the dictionary")
#print(value_check(b,n))

