print(range(5))
print(type(range(5)) == range)

import sys

a = (0, 1, 2, 3, 4, 5)
# size of 'a' in memory
print(sys.getsizeof(a))

b = [0, 1, 2, 3, 4, 5]
# size of 'b' in memory
print(sys.getsizeof(b))

print(sys.getsizeof(range(5)))
