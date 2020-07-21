# Example
def greater_than_4(i):
    return i > 4


# generic way
k = [1, 2, 3, 4, 5, 6]
print([i for i in k if greater_than_4(i)])


# using filter
print(list(filter(greater_than_4, k)))
