print([*map(chr, [66, 53, 0, 94])])
print(map(str, [66, 53, 0, 94]))
[print(i) for i in map(chr, [66, 53, 0, 94])]


# convert to upper case
def value(k):
    return k.upper()


print([*map(value, ['mango', 'jack fruit', 'pine apple', 'grapes'])])


# income tax calculator
def income_tax(sum, percent):
    return round(sum - (sum * percent / 100))


print([*map(income_tax, [20000, 30000, 40000, 50000], [20, 30, 40, 50])])
