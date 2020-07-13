from abc import ABC, abstractmethod


class Food(ABC):

    @abstractmethod
    def snacks(self):
        pass

    @abstractmethod
    def noodles(self):
        pass


class Shops(Food):

    def snacks(self):
        print('snacks')

    def noodles(self):
        print('noodles')


obj = Shops()
obj.snacks()
obj.noodles()
