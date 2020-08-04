k = [5, 3, 1, 8, 2]


def sort(k):
    for i in range(4):
        min_pos = i
        for j in range(i, 5):
            if k[j] < k[min_pos]:
                min_pos = j

            temp = k[i]
            k[i] = k[min_pos]
            k[min_pos] = temp
    return k


print(sort(k))