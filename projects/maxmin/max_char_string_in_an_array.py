# method 1
k = ['cat', 'zebra', 'girrafe', 'dog', 'tiger']

for i in range(len(k)-1):
    if len(k[i]) > len(k[i+1]):
        temp = k[i]
        k[i] = k[i+1]
        k[i+1] = temp

print(k[-1])

# method 2
k = ['cat', 'zebra', 'girrafe', 'dog', 'tiger']

count = 0
for i in range(len(k)-1):
    if len(k[i]) > count:
        count = len(k[i])
        long = i

print(k[long])
