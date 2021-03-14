# method 1
k = 32

flag = False

for i in range(2, k):
    if k % i == 0:
        flag = False
        break
    else:
        flag = True

if flag == False:
    print(str(k) + ' is not a prime number')
else:
    print(str(k) + ' is a prime number')


# method 2
num = 29

flag = False

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")