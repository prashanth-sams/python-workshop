class CustomIter:

    def __init__(self, increment):
        self.increment = increment
        self.a = 1

    def __next__(self):
        k = self.a
        self.a += self.increment
        return k


x = CustomIter(4)
print(next(x))
print(next(x))
print(next(x))