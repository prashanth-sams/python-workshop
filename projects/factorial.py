# method 1
k = 5
fac = 1

for i in range(k, 1, -1):
    fac = i*fac

print(fac)


# method 2
k = 7
fac = 1

while(k != 0):
    fac = fac * k
    k -= 1

print(fac)