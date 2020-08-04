k = [5, 6, 6, 2, 3, 5, 1, 6, 7]
m = []

for i in range(len(k)):
    for j in range(i, len(k)-1):
        if k[i] == k[j+1]:
            m.append(j+1)

m = list(dict.fromkeys(m))
m.sort(reverse=True)

for i in m:
    k.pop(i)

print(k)