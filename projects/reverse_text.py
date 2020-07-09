# type 1
k = 'Prashanth'
name = ''

for i in k:
    name = f'{i}{name}'

print(name)

# type #2
x = 'Prashanth'[::-1]
print(x)

# type #3 - as a method
def reverse(name):
    n = ''
    for i in name:
        n = f'{i}{n}'
    return n


print(reverse('Prashanth'))