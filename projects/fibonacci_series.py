num = input()
value = []
a, b = 0, 1

value.append(a)
value.append(b)

for i in range(int(num)-2):
    a, b = a, b
    c = a + b
    a, b = b, c
    value.append(c)

print(value)