# method #1
def value():
    print("am in a function")

value()

# method #2
def value2(name):
    print(f'name: {name}')

value2('Prashanth')
value2('Sams')
value2('David')

# arbitrary arguments - method #1
def test_func(*args):
    print(f'{args[0]}: {args[1]}, age: {args[2]}')

test_func('name', 'Prashanth', 30)

# arbitrary arguments - method #2
def test_func(args):
    print(f'{args[0]}: {args[1]}, age: {args[2]}')

test_func(('name', 'Prashanth', 30))

# arbitrary keyword arguments
def keywords(**args):
    print(f'{args["name"]}, {args["age"]}, {args["sex"]}')

keywords(name='Prashanth', age='30', sex='male')

# list as an argument
def list(arr):
    for i in arr:
        print(i)

list(['Prashanth', '30', 'male'])