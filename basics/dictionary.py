k = {"a": "cars", "b": "bikes", "c": "cycle"}
print(k)

# dict keys, values, and items
print(k.keys())
print(k.values())
print(k.items())

# dict keys and values as list
print(list(k.keys()))
print(list(k.values()))

# pick value with key name
print(k['b'])
print(k.get('b'))

# update value of a key
k['b'] = 'tractor'
print(k)

# iterate through dictionary keys
for i in k:
    print(i)

# iterate through dictionary values
for i in k:
    print(k[i])
for i in k.values():
    print(i)

for a, b in k.items():
    print(a, b)

if "cycle" in k.values():
    print(True)

print((len(k)))

# append values in existing dict
k['d'] = 'motor'
print(k)

# remove key-pair from the dict
# del k['d']
k.pop('d')
print(k)

# remove the last key-pair from dict
k.popitem()
print(k)

# take copy of the existing dict
m = k.copy()
n = dict(k)
print(m)
print(n)

# removes all the key-pair from the dict
k.clear()
print(k)

# nested dictionaries
x = {0: {'a': 'love', 'b': 'peace'}, 1: {'c': 'pasta', 'd': 'noodles'}, 2: {'e': 'tea'}}
print(x)

# call from outside
d1 = {'a': 'love', 'b': 'peace'}
d2 = {'c': 'pasta', 'd': 'noodles'}
d3 = {'e': 'tea'}
d = {
    0: d1,
    1: d2,
    2: d3
}
print(d)

# dict constructor to make a new dictionary
test = dict(a='bible', b='prayer', c='worship')
print(test)