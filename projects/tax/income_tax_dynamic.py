
def salary(value, tax_slab):

    sum = [*tax_slab.values()]
    tax = [*tax_slab.keys()]

    if value < sum[0]:
        return value - (value * tax[0] / 100)
    elif value < sum[1]:
        return value - (value * tax[1] / 100)
    elif value < sum[2]:
        return value - (value * tax[2] / 100)
    else:
        return value - (value * 50 / 100)


print(salary(82000, {1: 20000, 20: 40000, 30: 60000}))
