class CustomIter:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        k = self.a
        self.a += 2
        return k


x = iter(CustomIter())
print(next(x))
print(next(x))
print(next(x))
