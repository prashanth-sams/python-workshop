"""
vars()
vars(str)
vars(int)
vars(dict)
locals()
dir(Fruit())

------same-----
vars(Fruit())
Fruit.__dict__
"""

global k


class Fruit:

    def __init__(self, k=[]):
        self.k = k

        for i in range(10):
            print(i)
            self.k.append(i)


obj = Fruit()
print(vars(obj))