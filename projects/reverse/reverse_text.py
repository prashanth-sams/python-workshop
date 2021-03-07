# method 1
k = 'Hello world!'
name = ''

for i in k:
    name = f'{i}{name}'
    # name = i + name

print(name)


# method 2
k = 'Hello world!'[::-1]
print(k)


# method 3
k = 'Hello world!'
print(''.join(reversed(k)))


# method 4
def reverse(name):
    n = ''
    for i in name:
        n = f'{i}{n}'
    return n

print(reverse('Hello world!'))


# method 5
k = 'Hello world!'

output = []

length = len(k)-1

for i in range(len(k)):
    while(length != -1):
        output.append(k[length])
        length -= 1

print(''.join(output))


# method 6
k = 'Hello world!'

output = []

for i in range(len(k)-1, -1, -1):
    output.append(k[i])

print(''.join(output))
