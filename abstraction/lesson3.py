from abc import ABC, abstractmethod


class Food(ABC):

    def __init__(self, order):
        self.order = order

    @abstractmethod
    def snacks(self):
        pass

    @abstractmethod
    def zomato(self):
        pass


class Shops(Food):

    def snacks(self):
        print('snacks: {}'.format(self.order))


class Delivery(Shops):

    def zomato(self):
        print('zomato: {}'.format(self.order))


obj = Delivery(5)
obj.snacks()
obj.zomato()
