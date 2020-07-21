k = ['a', 'b', 'c', 'd', 'e', 'f']

# print a list one by one
[print(i) for i in k]

# convert list to string
print(''.join([i for i in k]))
print(''.join(k))

k = [1, 2, 3, 4, 5, 6]
print([i for i in k if i >= 4])