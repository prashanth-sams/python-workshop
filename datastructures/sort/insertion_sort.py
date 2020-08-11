def sort(k):
    for i in range(1, len(k)):
        while k[i-1] > k[i] and i > 0:
            temp = k[i-1]
            k[i-1] = k[i]
            k[i] = temp
            i -= 1
    return k


k = [5, 1, 5, 3, 44, 4, 7, 2, 4, 234]
sort(k)
print(k)