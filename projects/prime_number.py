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


# method 3
def checkPrimeNumber(value):
    if(value == 1): return False
    for i in range(2, value):
        if(value % i == 0):
            return False
            break
    
    return True


l = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

for i in l:
    print(checkPrimeNumber(i))