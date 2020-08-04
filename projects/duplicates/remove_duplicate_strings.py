"""
through set you can opt out all the duplicates but it is unordered
"""

k = ['apple', 'orange', 'orange', 'grapes', 'apple', 'apple']
l = set(k)
k = list(l)
print(k)

"""
dict is ordered so it helps
"""
k = ['apple', 'orange', 'orange', 'grapes', 'apple', 'apple']
l = list(dict.fromkeys(k))
print(l)