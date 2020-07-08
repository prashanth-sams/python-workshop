x = 30

def age():
    global x
    x = 31
    print(f'my age is {x}')


age()
print(f'my age is {x}')
