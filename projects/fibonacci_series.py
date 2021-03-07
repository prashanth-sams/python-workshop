# method 1
num = input()
value = []
a, b = 0, 1

value.append(a)
value.append(b)

for i in range(int(num)-2):
    c = a + b
    a = b
    b = c
    # a, b = b, c
    value.append(c)

print(value)


# method 2
val = 10
fib = []
a, b = 0, 1

fib.append(a)
fib.append(b)

for i in range(val):
    if((i != 0) and (i != 1)):
        fib.append(fib[i-1]+fib[i-2])

print(fib)