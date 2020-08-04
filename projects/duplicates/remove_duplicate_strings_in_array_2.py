k = ['apple', 'orange', 'orange', 'grapes', 'apple', 'apple', 'apple']
m = []


def remove_duplicates(k):
    for i in range(len(k)):
        for j in range(i, len(k)-1):
            if k[i] == k[j+1]:
                m.append(j+1)

    l = list(dict.fromkeys(m))
    l.sort(reverse=True)

    for i in l:
        k.pop(i)

    return k


print(remove_duplicates(k))
