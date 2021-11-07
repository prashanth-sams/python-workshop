name ="Prashanth"

def getLocation(value):
    for i in range(len(value)):
        for j in range(i, len(value)-1):
            if value[i] == value[j+1]:
                yield j+1

def removeDuplicates(value):
    k = list(getLocation(value))
    print(k)
    for i in range(len(value)-1, -1, -1):
        if i in k:
            value = value[:i] + '' + value[i + 1:]
    return value
print(removeDuplicates("Prashanth"))