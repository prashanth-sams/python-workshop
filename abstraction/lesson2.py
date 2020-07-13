from abc import ABC, abstractmethod


class Food(ABC):

    @abstractmethod
    def snacks(self):
        pass

    @abstractmethod
    def zomato(self):
        pass


class Shops(Food):

    def snacks(self):
        print('snacks')


class Delivery(Shops):

    def zomato(self):
        print('zomato')


obj = Delivery()
obj.snacks()
obj.zomato()
