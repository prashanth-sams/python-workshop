k = [
    {'name': 'Prashanth', 'age': 32, 'sex': 'male'},
    {'name': 'XXX', 'age': 43, 'sex': None},
    {'name': 'Christal', 'age': 26, 'sex': 'female', 'salary': 2000},
    {'name': 'YYY', 'age': 44, 'sex': None}
]

value = []
for i in k:
    if i['sex'] != None : value.append(i)
print(value)


key = []
for j in k:
    if 'salary' not in j: key.append(j)
print(key)