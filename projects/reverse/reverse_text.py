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
k = "prashanth"
l = ""

for i in k: l = i+l

print(l)


# method 6
k = "Hello world!"
l = []

length = len(k)-1

while(length != -1):
    l.append(k[length])
    length -= 1

print(''.join(l))


# method 7
k = 'Hello world!'

output = []

for i in range(len(k)-1, -1, -1):
    output.append(k[i])

print(''.join(output))


# method 8
k = 'Hello world!'
l = ''

for i in range(len(k)-1, -1, -1):
    l = l + k[i]

print(l)


# method 9
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

print("".join(list(reverse('abcdefg'))))