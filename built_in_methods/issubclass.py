class X:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return int(self.a) + int(self.b)


class Y(X):

    def sum(self):
        return int(self.a) - int(self.b)


print(issubclass(Y, X))
print(issubclass(X, Y))
