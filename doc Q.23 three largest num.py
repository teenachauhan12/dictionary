from heapq import nlargest
a={'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
three_largest = nlargest(3, a, key=a.get)
print(three_largest)












 
