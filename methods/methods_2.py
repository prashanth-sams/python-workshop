class Fruits:
    def __init__(self, names):
        self.names = names

    def __repr__(self):
        return f'{self.names}'


print(Fruits('Banana'))