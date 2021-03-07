from operator import itemgetter;

k = [
    {'name': 'Prashanth', 'age': 32, 'sex': 'male', 'color': 'black'},
    {'name': 'Sunil', 'age': 34, 'sex': 'male'},
    {'name': 'Lolita', 'age': 35, 'sex': 'female', 'color': 'white'},
    {'name': 'Pravin', 'age': 36, 'sex': 'male'},
]

result = sorted(k, key=itemgetter('age'))

print(result)