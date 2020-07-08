
a = b = "bike"
c = d = "cars"

if a is "bike" and b is "bike":
    print(True)

if a == "bike" and c != "bike":
    print(True)

if a == "bike" or c == "bike":
    print(True)

print(True) if a is not "cars" else print(False)

k = ['bike', 'cars', 'cycle', 'motor']

if 'cards' not in k:
    print(True)