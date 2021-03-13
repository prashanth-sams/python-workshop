from collections import Counter

k = ['A', 'A', 'C', 'B', 'C', 'A', 'B', 'A', 'C', 'B']

print(Counter(k))
# Counter({'A': 4, 'C': 3, 'B': 3})

print(dict(Counter(k)))
# {'A': 4, 'C': 3, 'B': 3}

print(Counter(A=3, B=2, C=1))
# Counter({'A': 4, 'C': 3, 'B': 3})