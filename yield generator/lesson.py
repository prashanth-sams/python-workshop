# k = ['cars', 'bikes', 'motors', 'cycle']
# l = []
#
# def return_func():
#     for i in k:
#         l.append(i)
#
#     return l
#
# print(return_func())

k = ['cars', 'bikes', 'motors', 'cycle']

def yield_func():
    for i in k:
        yield i


print(list(yield_func()))