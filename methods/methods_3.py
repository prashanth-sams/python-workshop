class Fruits:
    def __init__(self, names, quantity):
        self.names = names
        self.quantity = quantity

    def buy(self):
        return self._price(self.quantity)

    @staticmethod
    def _price(p):
        return p * 12


print(Fruits('Banana', 5).buy())
print(Fruits._price(5))
