import random


# method 1
k = random.sample(range(0,8), 5)
k.sort()
print(k)


# method 2
l = []

for i in range(5):
    k = random.randint(4000,4999)
    l.append(k)

print(l)