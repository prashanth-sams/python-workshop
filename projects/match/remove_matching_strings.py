k = ['apple', 'orange', 'orange', 'grapes', 'apple']

for i, j in enumerate(k):
    if j == 'grapes':
        k.pop(i)

print(k)