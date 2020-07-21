from functools import reduce

# generic method #1
print([1, 2] + [3, 4] + [5, 6])

# generic method #2
a = [[1, 2], [3, 4], [5, 6]]
print([k for i in a for k in i])

"""
reduce - method #1 
"""
print(reduce(lambda x, y: x + y, a))

"""
reduce - method #2
"""
def addition(x, y):
    return x + y


print(reduce(addition, a))
