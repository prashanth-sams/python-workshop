print(any([""]))
print(any(["", False, 0]))
print(any(["", False, 0, 1]))
print(any(("", False, 0, 1)))

print(any(["", False, 0, "Hey"]))

names = ["Prashanth", "Sams", "Christal"]
print(any([i == "Sams" for i in names]))

print(any(""))
print(any({}))
print(any([]))
print(any(()))