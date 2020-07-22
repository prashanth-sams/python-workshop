print(type(0))
print(type(""))
print(type([]))
print(type(()))
print(type({}))
print(type({1, 2, 3}))
print(type(type('')))

print(type({1, 2, 3}) == set)

a = 0
print(a.__class__)


class Fruit:
    """
    fruits count
    """
    apple = 100


print(Fruit.__class__)
print(Fruit.__bases__)
print(Fruit.__dict__)
print(Fruit.__doc__)