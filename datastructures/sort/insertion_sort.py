def sort(k):
    for i in range(0, len(k)-1):
        while k[i] > k[i+1]:
            temp = k[i+1]
            k[i+1] = k[i]
            k[i] = temp
            i -= 1
    return k


k = [1, 5, 3, 44, 4, 7, 2, 4, 234]
sort(k)
print(k)