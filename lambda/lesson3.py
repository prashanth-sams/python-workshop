result = {
  'a': {
    'name': lambda x: x * 5,
    'age': lambda x: x + 5
  }['name'](1),
  'b': {
    'name': lambda x: x + 7,
    'age': lambda x: x + 7
  }['age'](1)
}['a']

print(result)
