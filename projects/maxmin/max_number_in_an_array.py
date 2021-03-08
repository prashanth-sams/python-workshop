k = [9, 4, 2, 44, 6, 23, 123, 33, 888, 34, 999, 9]

# method 1
print(max(k))

# method 2
for i in range(len(k)):
    for j in range(i, len(k)-1):
        if k[i] > k[j+1]:
            temp = k[i]
            k[i] = k[j+1]
            k[j+1] = temp

print(k[-1])

# method 3
k = [9, 4, 2, 44, 6, 23, 123, 33, 888, 34, 999, 9]
max = 0

for i in k:
    if i > max:
        max = i

print(max)
