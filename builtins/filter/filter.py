# Example
k = [1, 2, 3, 4, 5, 6]
print([i for i in k if i >= 4])

# same in filter
print(list(filter(lambda i: i >= 4, k)))
