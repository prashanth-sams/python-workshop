def calculation(z):
    def new(x, y):
        def newx(x,y,z):
            return x+y+z
        return x+y
    return z


print(calculation(5))
print(calculation(5+5))
print(calculation(5+5+5))