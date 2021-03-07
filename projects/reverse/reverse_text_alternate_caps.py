# method 1
def isodd(integer):
    if integer % 2 == 0:
        return True
    else:
        return False

k = 'Prashanth'
name = ''

for i, val in enumerate(k):
    if isodd(i) is True: val = val.upper()
    name = f'{val}{name}'

print(name)


# method 2
k = 'prashanth'
val = ''

for i in range(len(k)-1, -1, -1):
    if(i % 2 != 0):
        val = val + k[i].upper()
    else:
        val = val + k[i]

print(val)
