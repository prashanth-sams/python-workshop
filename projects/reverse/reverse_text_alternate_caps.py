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
