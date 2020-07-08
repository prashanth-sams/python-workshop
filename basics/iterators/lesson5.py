class CustomIter:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            k = self.a
            self.a += 1
            return k
        else:
            raise StopIteration


for i in iter(CustomIter()):
    print(i)