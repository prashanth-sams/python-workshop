# method 1
k = 32
m = []
for j in range(2, k+1):
    for i in range(2, j):
        if j % i == 0:
            break
    else:
        m.append(j)
print(list(dict.fromkeys(m)))



# method 2
k = 32

flag = False

m = []

for j in range(2, k+1):
    for i in range(2, j):
        if j % i == 0:
            flag = False
            break
        else:
            flag = True

    if flag == True:
        m.append(j)
        flag == False

print(m)
