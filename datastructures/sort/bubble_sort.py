def sort(k):
    for i in range(len(k)):
        for j in range(i, len(k)-1):
            if k[i] > k[j+1]:
                temp = k[i]
                k[i] = k[j+1]
                k[j+1] = temp
    return k


k = [1, 5, 3, 7, 2, 4]
sort(k)
print(k)