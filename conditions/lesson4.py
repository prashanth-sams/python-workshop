def myfunc(name, age):
    return {
        'Prashanth':
        {
            30: 'Prashanth',
            31: 'Not Prashanth'
        }.get(age, 'second skip'),

        'Sunil':
        {
            32: 'Sunil',
            31: 'Not Sunil'
        }.get(age, '')
    }.get(name, 'first skip')


print(myfunc('Sunil', 32))
