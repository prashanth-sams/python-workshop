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

# type #3
k = "prashanth"
l = []

for i, j in enumerate(range(len(k), 0, -1)):
    if i%2==0:
        print(k[j-1])