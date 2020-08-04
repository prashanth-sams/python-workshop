k = 'Prashanth'


def remove_duplicates(k):
    for i in range(len(k)):
        for j in range(i, len(k)-1):
            if k[i] == k[j+1]:
                l = k.replace(k[j+1], '')

    return l


print(remove_duplicates(k))