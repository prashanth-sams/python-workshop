# type #1
def isodd(i):
    if i % 2 == 0:
        return False
    else:
        return True

k = 'Prashanth'
name = ''

for i, val in enumerate(k):
    if isodd(i) is True: val = ''
    name = '{}{}'.format(val, name)

print(name)

# type #2
x = 'Prashanth'[::-2]
print(x)