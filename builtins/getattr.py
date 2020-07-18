class X:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b


k = X('5', '10')

print(getattr(k, 'b'))
print(getattr(k, 'sum'))
