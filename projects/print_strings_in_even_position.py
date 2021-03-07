# method 1
k = 'Prashanth'
m = ''

for i in range(len(k)):
    if i % 2 != 0:
        m = m+k[i]

print(m)


# method 2
k = 'Prashanth'
val = ''

for i, j in enumerate(k):
    if (i % 2 != 0):
        val = val+j

print(val)