"""
0% for < 20000 AED
20% for >= 20000 AED
30% for >= 40000 AED
50% for >= 60000 AED
"""


def salary(value):
    if value < 20000:
        return value
    elif value >= 20000 and value < 40000:
        return value - (value * 20 / 100)
    elif value >= 40000 and value < 60000:
        return value - (value * 30 / 100)
    elif value >= 60000:
        return value - (value * 50 / 100)
    else:
        raise Exception('invalid amount')


print(salary(22000))
