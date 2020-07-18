# checks if the array object has append attribute
k = [1, 2, 3, 4]

print(hasattr(k, 'append'))

# checks if the tuple object has append attribute
k = (1, 2, 3, 4)

print(hasattr(k, 'append'))


# approach 3
class X:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b


k = X('5', '10')

print(hasattr(k, 'b'))
print(hasattr(k, 'sum'))
