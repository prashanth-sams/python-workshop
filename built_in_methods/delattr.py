class X:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return int(self.a) + int(self.b)


k = X('5', '10')

delattr(k, 'b')
print(hasattr(k, 'b'))
