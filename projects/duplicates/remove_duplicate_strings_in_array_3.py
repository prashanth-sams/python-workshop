k = ['apple', 'orange', 'orange', 'grapes', 'apple', 'apple', 'apple']
m = []


def remove_duplicates(k):
    for i in k:
        if i not in m:
            m.append(i)

    return m


print(remove_duplicates(k))
