 
k = [
    {'name': 'Prashanth', 'age': 32, 'sex': 'male', 'color': 'black'},
    {'name': 'Sunil', 'age': 34, 'sex': 'male'},
    {'name': 'Lolita', 'age': 35, 'sex': 'female', 'color': 'white'},
    {'name': 'Pravin', 'age': 36, 'sex': 'male'},
]

result = []

for i in k:
    if 'color' in i:
        result.append(i)

print(result)

output = []

for j in result:
    if j['sex'] == 'male':
        output.append(j)

print(output)

