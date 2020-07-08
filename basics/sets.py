# add, remove, check if available, update, length, discard, pop, union set, delete set, clean set
x = {"cars", "bikes", "cycle"}
x.add("travel")
x.remove("travel")
print(x)
print('cars' in x)
x.update(["sams", "david", "cycle"])
print(len(x))
x.discard('cycle')
x.pop()
x.clear()
# del x
print(x)
a = {1, 2, 3}
b = {4, 5, 6}
c = a.union(b)
a.update(b)
print(c)
print(a)