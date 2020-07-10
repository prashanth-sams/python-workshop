def switch(option):
    return {
        'a': 'cars',
        'b': 'bikes',
        'c': 'motor'
    }[option]


print(switch('c'))
