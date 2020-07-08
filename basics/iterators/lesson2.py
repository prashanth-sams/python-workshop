# tuple iterator #2
k = ('bike', 'car', 'cart', 'cycle')
l = len(k)
x = iter(k)

for i in range(l):
    print(next(x))