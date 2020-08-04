"""
split and combine
"""


def sort(k):
    if len(k) > 1:
        mid = len(k) // 2
        left = k[:mid]
        right = k[mid:]

        sort(left)
        sort(right)

        i, j, p = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                k[p] = left[i]
                i = i + 1
            else:
                k[p] = right[j]
                j = j + 1
            p = p + 1

        while i < len(left):
            k[p] = left[i]
            i = i + 1
            p = p + 1

        while j < len(right):
            k[p] = right[j]
            j = j + 1
            p = p + 1


k = [5, 2, 6, 4, 1, 3]
sort(k)
print(k)
