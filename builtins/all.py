print(all(""))
print(all({}))
print(all([]))
print(all(()))

print(all([True, False]))
print(all([True, True]))
print(all([True, 0]))
print(all([True, 1]))

print(all([10, 1]))

names = ["Prashanth", "Sams", "Christal"]
print(all([i == 'Sams' for i in names]))
