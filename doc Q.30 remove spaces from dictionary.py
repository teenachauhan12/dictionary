a={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
b= {x.translate({32: None}):
y for x, y in a.items()}
print(b)




 