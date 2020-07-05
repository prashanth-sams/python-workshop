# define, overriding, adding, reverse array, count of value in array,
# insert value in an array, copy array, index of array, clear array, extend another array's value
y = ['sdf', 'asdf']
y[0] = 'cars'
y[1] = 'bikes'
y.append('motor')
y.append('cycle')
y.append('travel')
y.pop(2)
y.remove('cars')
y.reverse()
y.insert(0, 'sams')
print(y)
print(y.index('sams'))
print(y.count('cycle'))
k = y.copy()
print(y.clear())
y.append('new')
print(k)
y.extend(k)
print(y)