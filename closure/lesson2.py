
def calculation(x):

    def add(y):
        print(x+y)
    return add


result = calculation(100)
result(50)
result(150)
result(200)

calculation(100)(500)