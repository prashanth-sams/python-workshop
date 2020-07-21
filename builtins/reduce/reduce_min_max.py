from functools import reduce

print(reduce(lambda x, y: x if x > y else y, [1, 5, 3, 4]))
print(reduce(lambda x, y: x if x < y else y, [3, 5, 1, 4]))
