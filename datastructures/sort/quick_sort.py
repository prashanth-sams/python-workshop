def quick_sort(k):
    if len(k) <= 1:
        return k
    else:
        pivot = k.pop()

    l = []
    m = []

    for item in k:
        if item > pivot:
            l.append(item)
        else:
            m.append(item)

    return quick_sort(m) + [pivot] + quick_sort(l)


print(quick_sort([5, 1, 4, 3, 7, 4, 2]))
