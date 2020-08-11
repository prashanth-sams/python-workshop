k = [5, 3, 1, 8, 6, 1, 2]

for i in range(len(k)):
    for j in range(i, len(k)-1):
        if k[j+1] > k[i]:
            temp = k[i]
            k[i] = k[j+1]
            k[j+1] = temp

k = k[-1:]
print("".join(map(str, k)))