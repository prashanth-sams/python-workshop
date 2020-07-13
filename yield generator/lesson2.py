k = ['cars', 'bikes', 'motors', 'cycle']


# type #1
def yield_func():
    for i in k:
        yield i


result = yield_func()
print(next(result))
print(next(result))
print(next(result))
print(next(result))


# type #2
def yield_func2():
    for i in k:
        yield i


result = yield_func2()
for i in result:
    print(i)
