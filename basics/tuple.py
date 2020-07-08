k = ("a", "b", "c", "d", "e")
print(k[2])

k = ("a", "b", "c", "d", "e")
print(k[2:4])

# Negative indexing means starting from the end of the tuple.
k = ("a", "b", "c", "d", "e")
print(k[-4:-1])

# convert tuple to list
k = ("a", "b", "c", "d", "e")
m = list(k)
m[1] = 'p'
k = tuple(m)
print(k)

# merge two tuples
k = ("a", "b", "c", "d", "e")
l = (1, 2, 3, 4, 5, 6)
print(k + l)

