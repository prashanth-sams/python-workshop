def switch(option):
    return {
        'a': 'cars',
        'b': 'bikes',
        'c': 'motor'
    }.get(option, 'Not found')


print(switch('b'))
