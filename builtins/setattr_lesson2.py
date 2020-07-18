class X:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return int(self.a) + int(self.b)


k = X('5', '10')

setattr(k, 'c', '20')
print(hasattr(k, 'c'))
print(getattr(k, 'c'))