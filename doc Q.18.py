a={'x':500, 'y':5874, 'z': 560}
key_max = max(a.keys(), key=(lambda k:a[k]))
key_min = min(a.keys(), key=(lambda k:a[k]))
print('Maximum Value: ',a[key_max])
print('Minimum Value: ',a[key_min])






